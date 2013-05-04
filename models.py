from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


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
