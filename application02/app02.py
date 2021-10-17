import logging
from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields

logger = logging.getLogger()

app_02 = Blueprint('app_02', __name__)
api = Api(app_02, version="1.0", title="app02 API", description="app02 api description",)
ns = api.namespace("ns02_app", description="app02 api description")


@ns.route('/app02', methods=['POST'])
@api.doc(responses={404: "App not found"}, params={"APP_id": "The App ID"})
class app02(Resource):

    def post(self):
        return jsonify(status='POST OK')



