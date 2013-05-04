from flask.ext import restful

import models


class ProdResource(restful.Resource):
    def get(self, prod_id):
        prod = models.Prod.query.get(prod_id)

        resp = prod.json

        return resp


class GroupResource(restful.Resource):
    def get(self, group_id):
        group = models.Group.query.get(group_id)

        resp = group.json

        return resp
