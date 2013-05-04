import json

from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    website_url = db.Column('web', db.String(255))
    added = db.Column(db.Integer)
    views = db.Column(db.Integer)
    quand = db.Column(db.DateTime())
    csdb = db.Column(db.Integer)
    zxdemo = db.Column(db.Integer)
    acronym = db.Column(db.String(8))

    def __repr__(self):
        return '<Group %r>' % self.name

    @property
    def json(self):
        """
        Returns:
            dict: Dict representation of the group
        """
        data = {
            'id': self.id,
            'name': self.name,
            'website_url': self.website_url or None,
        }

        return data


class Prod(db.Model):
    __tablename__ = 'prods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    download_url = db.Column('download', db.String(255))
    release_date = db.Column('date', db.Date())
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

    def __repr__(self):
        return '<Prod %r>' % self.name

    @property
    def group_ids(self):
        """
        Returns:
            list: List of groups
        """
        group_ids = []
        if self.group1:
            group_ids.append(self.group1)
        if self.group2:
            group_ids.append(self.group2)
        if self.group3:
            group_ids.append(self.group3)
        return group_ids

    @property
    def groups_as_json(self):
        """
        Returns:
            list: List of json representation of groups
        """
        data = []

        for group_id in self.group_ids:
            group = Group.query.get(group_id)
            data.append(group.json)

        return data


    @property
    def json(self):
        """
        Returns:
            dict: Dict representation of the prod
        """
        data = {
            'id': self.id,
            'name': self.name,
            'download_url': self.download_url,
            'groups': self.groups_as_json
        }

        return data
