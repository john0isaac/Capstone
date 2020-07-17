import os
from flask import Flask, render_template, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from auth.auth import AuthError, requires_auth
from models import setup_db, Person, Industries

RESULT_PER_PAGE = 10


def paginate_results(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * RESULT_PER_PAGE
    end = start + RESULT_PER_PAGE

    results = [result.format() for result in selection]
    current_results = results[start:end]

    return current_results


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # CORS Headers

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, PATCH,OPTIONS')
        return response

    @app.route('/')
    def landing_page():
        return render_template('pages/home.html')

    @app.route('/persons')
    @requires_auth('get:persons')
    def retrive_persons(jwt):
        selection = Person.query.order_by(Person.id).all()
        current_persons = paginate_results(request, selection)

        if len(current_persons) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'persons': current_persons,
            'total_persons': len(Person.query.all())
            }), 200

    @app.route('/industries')
    @requires_auth('get:industries ')
    def retrive_industries(jwt):
        selection = Industries.query.order_by(Industries.id).all()
        current_industries = paginate_results(request, selection)

        if len(selection) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'industries': current_industries,
            'total_industries': len(selection)
            }), 200

    @app.route('/persons', methods=['POST'])
    @requires_auth('post:persons')
    def add_person(jwt):
        body = request.get_json()
        try:    
            new_name = body.get('name', None)
            new_info = body.get('info', None)
            new_city = body.get('city', None)
            new_phone = body.get('phone', None)
            new_website = body.get('website', None)
            new_facebook_link = body.get('facebook_link', None)
            new_seeking_job = body.get('seeking_job', None)
            new_industry_id = int(body.get('industry_id', None))
            
            person = Person(name=new_name, info=new_info, city=new_city, phone=new_phone, website=new_website, facebook_link=new_facebook_link, seeking_job=new_seeking_job, industry_id=new_industry_id)
            person.insert()

            return jsonify({
                'success': True,
                'person': person.format()
            }), 200
        except:
            abort(422)

    @app.route('/industries', methods=['POST'])
    @requires_auth('post:industries')
    def add_industry(jwt):
        try:
            body = request.get_json()
            new_industry = body.get('industry', None)
            
            industry = Industries(industry=new_industry) 
            industry.insert()

            return jsonify({
                'success': True,
                'industry': industry.format()
            }), 200
        except:
            abort(422)

    @app.route('/persons/search', methods=['POST'])
    @requires_auth('post:persons')
    def search_persons(jwt):
        body = request.get_json()
        search_term = body.get('search', None)
        current_industry = []
        try:
            search = '%{}%'.format(search_term)
            selection = Person.query.order_by(Person.industry_id).filter(Person.info.ilike(search)).all()
            persons = paginate_results(request, selection)

            industries = Person.query.with_entities(Person.industry_id).order_by(Person.industry_id).filter(Person.info.ilike(search)).all()
            for industry in industries:
                for innerlist in industry:
                    current_industry.append(innerlist)

            return jsonify({
                'success': True,
                'persons': persons,
                'current_industry': current_industry,
                'total_persons': len(selection)
                })
        except:
            abort(422)

    @app.route('/persons/<int:id>', methods=['PATCH'])
    @requires_auth('patch:persons')
    def edit_inforamtion(jwt, id):
        body = request.get_json()
        person = Person.query.get(id)

        if not person:
            abort(404)
        try:
            new_name = body.get('name', None)
            new_info = body.get('info', None)
            new_city = body.get('city', None)
            new_phone = body.get('phone', None)
            new_website = body.get('website', None)
            new_facebook_link = body.get('facebook_link', None)
            new_seeking_job = body.get('seeking_job', None)

            person.name = new_name
            person.info = new_info
            person.city = new_city
            person.phone = new_phone
            person.website = new_website
            person.facebook_link = new_facebook_link
            person.seeking_job = new_seeking_job
            person.update()

            return jsonify({
                'success': True,
                'persons': person.id
            }), 200
        except:
            abort(404)

    @app.route('/persons/<int:id>', methods=['DELETE'])
    @requires_auth('delete:persons')
    def delete_person(jwt, id):
        person = Person.query.get(id)
        if person:
            person.delete()

            return jsonify({
                'success': True,
                'delete': id
            }), 200
        else:
            abort(404)

    @app.route('/industries/<int:id>', methods=['DELETE'])
    @requires_auth('delete:industries')
    def delete_industry(jwt, id):
        industry = Industries.query.get(id)
        if industry:
            industry.delete()

            return jsonify({
                'success': True,
                'delete': id
            }), 200
        else:
            abort(404)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resourse not found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server errors'
        }), 500

    @app.errorhandler(AuthError)
    def Auth_Error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
