import logging
from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields

logger = logging.getLogger()

app_01 = Blueprint('app_01', __name__)
api = Api(app_01, version="1.0", title="app01 API", description="app01 api description",)
ns = api.namespace("ns01_app", description="app01 api description")


@ns.route('/app01', methods=['POST'])
@api.doc(responses={404: "App not found"}, params={"APP_id": "The App ID"})
class app01(Resource):

    def post(self):
        return jsonify(status='POST OK')

