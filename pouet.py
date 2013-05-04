import os

from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse

import resources
from models import db


# Instantiate the application
app = Flask(__name__)

# Configure and instantiate the database connection
# On dev:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db.init_app(app)

# Instantiate the API extension
api = restful.Api(app)

# Add the resources handled by the API
api.add_resource(resources.ProdResource, '/prod/<int:prod_id>')

# Run the main app when not imported
if __name__ == '__main__':
    app.run(debug=True)
