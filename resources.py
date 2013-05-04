from flask.ext import restful

import models


class ProdResource(restful.Resource):
    def get(self, prod_id):
        prod = models.Prod.query.get(prod_id)

        resp = {'name': prod.name,
                'download': prod.download}

        return resp
