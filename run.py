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



