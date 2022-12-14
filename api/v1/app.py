#!/usr/bin/python3
""" Import a blueprint and runs Flask """

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['SWAGGER'] = {
    'swagger_version': '2.0',
    'title': 'Flasgger',
    'headers': [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
        ('Access-Control-Allow-Credentials', "true"),
    ],
    'specs':[
        {
            'version': '1.0.0',
            'title': 'HBNB API',
            'endpoint': 'v1_views',
            'description': 'HBNB REST API',
            'route':'/v1/views/',
        }
    ]
}

swagger = Swagger(app)

@ap.teardown_appcontext
def teardown_db(exception):
    """Closes storage session"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')

    host = '0.0.0.0' if not HBNB_API_HOST else HBNB_API_HOST
    port = '5000' if not HBNB_API_PORT else HBNB_API_PORT
    app.run(host=host, port=port, threaded=True)
