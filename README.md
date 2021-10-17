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

app_01 = Blueprint('app_01', __name__)
logger = logging.getLogger()


@app_01.route('/app', methods=['POST'])
def app():
    try:
        param = request.get_json()
        logger.info(f'##########################')
        logger.info(f'app01')
        logger.info(f'##########################')
        logger.info(f'[REQ] {param}')

        return jsonify(status='OK')
    except Exception as e:
        logger.fatal(f'【システムエラー】{str(e)}：{str(request.get_json())}')
        return jsonify(status='NG', error_code=500, message='【システムエラー】処理に失敗しました。\n{}'.format(str(e)))
```

##### BluePrint api_02 작성
```python
import logging
from flask import Blueprint, request, jsonify

app_02 = Blueprint('app_02', __name__)
logger = logging.getLogger()


@app_02.route('/app', methods=['POST'])
def app():
    try:
        param = request.get_json()
        logger.info(f'##########################')
        logger.info(f'app02')
        logger.info(f'##########################')
        logger.info(f'[REQ] {param}')

        return jsonify(status='OK')
    except Exception as e:
        logger.fatal(f'【システムエラー】{str(e)}：{str(request.get_json())}')
        return jsonify(status='NG', error_code=500, message='【システムエラー】処理に失敗しました。\n{}'.format(str(e)))
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

app.register_blueprint(app_01, url_prefix='/app_01')
app.register_blueprint(app_02, url_prefix='/app_02')

if __name__ == '__main__':
    
    import sys
    args = sys.argv
    app.run(host=args[1], port=args[2])
    # app.run(host='0.0.0.0', port=4000)
```

#### Rest Api 확인 방법
##### Postman을 다운로드후에 api를 실행하면 된다. 




