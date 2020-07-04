import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from auth.auth import AuthError, requires_auth

RESULT_PER_PAGE = 10

def paginate_results(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * RESULT_PER_PAGE
  end = start + RESULT_PER_PAGE

  results = [result.format() for result in selection]
  current_results = results[start:end]

  return current_results


def create_app(test_config=None):
    #Create and configure the app
    app = Flask(__name__)
    CORS(app)
    #CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @app.route('/')
    def landing():
        return 'Home'


    return app

app = create_app()

if __name__ == '__main__':
    app.run()