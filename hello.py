import os

from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy

# Instantiate the application
app = Flask(__name__)

# Configure and instantiate the database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

# Instantiate the API extension
api = restful.Api(app)


class Prod(db.Model):
    __tablename__ = 'prods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    download = db.Column(db.String(255))

    def __init__(self, name, download):
        self.name = name
        self.download = download

    def __repr__(self):
        return '<Prod %r>' % self.name


class HelloWorld(restful.Resource):
    def get(self):
        p = Prod.query.filter_by(id=1).first()

        resp = {'name': p.name,
                'download': p.download}

        return resp


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
