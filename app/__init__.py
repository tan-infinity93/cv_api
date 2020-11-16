'''
'''

# Import Modules:

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from config import get_config

# Create Flask App Factory:

def create_app(config_name):
	app = Flask(__name__, template_folder='../templates/',  static_folder='../static')
	CORS(app)
	app.config.update(get_config(config_name))

	# App Binding:

	# from bindings.flask_mongo import FlaskMongo
	# from bindings.flask_logger import FlaskLogger
	from bindings.flask_sqlalchemy import FlaskSqlAlchemy

	# mongo_app = FlaskMongo()
	# mongo_app.init_app(app)

	# log_app = FlaskLogger()
	# log_app.init_app(app)

	# sqlalchemy_app = FlaskSqlAlchemy()
	# sqlalchemy_app.init_app(app)

	api = Api(app, catch_all_404s=True)

	# print(app.config.keys())

	# Add API Routes:

	from routes.welcome import Welcome
	from routes.cv import CV
	from routes.system import System
	from routes.auth import Auth
	from routes.url import UrlShortener

	# api.add_resource(ReportsCreator, '/edu/v1/utils/pdfs/create', methods=['POST'], endpoint='g_pdf')

	api.add_resource(Welcome, '/cv/v1/welcome', methods=['GET'], endpoint='welcome_api')
	api.add_resource(CV, '/cv/v1/cv-info', methods=['GET'], endpoint='cv_info')
	api.add_resource(System, '/cv/v1/system-info', methods=['GET'], endpoint='sys_info')
	api.add_resource(Auth, '/cv/v1/token-create', methods=['POST'], endpoint='create_token')
	api.add_resource(UrlShortener, '/cv/v1/shorten-url', methods=['POST'], endpoint='create_short_url')
	api.add_resource(UrlShortener, '/cv/v1/redirect-url', methods=['GET'], endpoint='redirect_url')

	return app
