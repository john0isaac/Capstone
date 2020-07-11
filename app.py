import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import Person, Industries
from auth.auth import AuthError, requires_auth

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
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # CORS Headers

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, PATCH,OPTIONS')
        return response

    @app.route('/')
    def landing_page():
        return 'Home'

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
    @requires_auth('get:industries')
    def retrive_industries(jwt):
        selection = Industries.query.order_by(Industries.id).all()

        if len(selection) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'persons': selection,
            'total_persons': len(selection)
            }), 200

    @app.route('/persons', methods=['POST'])
    @requires_auth('post:persons')
    def add_person(jwt):
        body = request.get_json()
        try:
            person = Person()
            person.name = body.get('name', None)
            person.address = body.get('address', None)
            person.city = body.get('city', None)
            person.phone = body.get('phone', None)
            person.website = body.get('website', None)
            person.facebook_link = body.get('facebook_link', None)
            person.seeking_job = body.get('seeking_job', None)
            person.profile_image = body.get('profile_image', None)
            person.industry_id = int(body.get('industry_id', None))

            person.insert()

            return jsonify({
                'success': True,
                'person': person
            }), 200
        except:
            abort(422)

    @app.route('/industries', methods=['POST'])
    @requires_auth('post:industries')
    def add_industry(jwt):
        body = request.get_json()
        try:
            industry = Industry()
            industry.industry = body.get('industry', None)

            industry.insert()

            return jsonify({
                'success': True,
                'person': industry
            }), 200
        except:
            abort(422)

    @app.route('/persons/<int:id>', methods=['PATCH'])
    @requires_auth('patch:persons')
    def edit_inforamtion(jwt, id):
        body = request.get_json()
        person = Person.query.filter(Person.id == id).one_or_none()

        if not person:
            abort(404)
        try:
            new_address = body.get('address', None)
            new_city = body.get('city', None)
            new_phone = body.get('phone', None)
            new_website = body.get('website', None)
            new_facebook_link = body.get('facebook_link', None)
            new_status = body.get('seeking_job', None)
            new_profile_image = body.get('profile_image', None)

            person.address = new_address
            person.city = new_city
            person.phone = new_phone
            person.website = new_website
            person.facebook_link = new_facebook_link
            person.seeking_job = new_status
            person.profile_image = new_profile_image
            person.update()

            return jsonify({
                'success': True,
                'persons': Person.query.all()
            }), 200
        except:
            abort(422)

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
        industry = industry.query.get(id)
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

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unauthorized '
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'forbidden'
        }), 403

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
