import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)


    @app.route('/')
    def landing():
        return 'جوسيان ام شخة'


    return app

app = create_app()

if __name__ == '__main__':
    app.run()