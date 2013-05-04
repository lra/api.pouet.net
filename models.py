from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Prod(db.Model):
    __tablename__ = 'prods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    download = db.Column(db.String(255))
    date = db.Column(db.Date())
    views = db.Column(db.Integer)
    added = db.Column(db.Integer)
    type = db.Column(db.String(255))
    party_year = db.Column(db.Integer)
    party_place  = db.Column(db.Integer)
    quand = db.Column(db.DateTime())
    latestip = db.Column(db.String(255))
    party = db.Column(db.Integer)
    group1 = db.Column(db.Integer)
    group2 = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    downloads = db.Column(db.Integer)
    downloads_ip = db.Column(db.String(255))
    video = db.Column(db.String(255))
    csdb = db.Column(db.Integer)
    zxdemo = db.Column(db.Integer)
    voteup = db.Column(db.Integer)
    votepig = db.Column(db.Integer)
    votedown = db.Column(db.Integer)
    voteavg = db.Column(db.Float)
    source = db.Column(db.String(255))
    partycompo = db.Column(db.Enum())
    group3 = db.Column(db.Integer)
    invitation = db.Column(db.Integer)
    invitationyear = db.Column(db.Integer)
    boardID = db.Column(db.Integer)
    sceneorg = db.Column(db.Integer)

    def __init__(self, name, download):
        self.name = name
        self.download = download

    def __repr__(self):
        return '<Prod %r>' % self.name
