# ❏ Flask REST API

## 

#### URL
```
http://localhost:5000/{blueprint}/{api}
```

#### Sample Source
##### BluePrint api_01 작성
```python
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
```

##### BluePrint api_02 작성
```python
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
```

##### Flask run.py 작성
```python
import logging.config
from flask import Flask

from application01.app01 import app_01
from application02.app02 import app_02

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(app_01, url_prefix='/a_01')
app.register_blueprint(app_02, url_prefix='/a_02')

if __name__ == '__main__':
    
    import sys
    args = sys.argv
    app.run(host=args[1], port=args[2])
    # app.run(host='0.0.0.0', port=4000)
```

#### Rest Api 확인 방법
##### Postman을 다운로드후에 api를 실행하면 된다. 




