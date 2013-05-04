from flask.ext import restful

import models


class ProdResource(restful.Resource):
    def get(self, prod_id):
        p = models.Prod.query.filter_by(id=prod_id).first()

        resp = {'name': p.name,
                'download': p.download}

        return resp
