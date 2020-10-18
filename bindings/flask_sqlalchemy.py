'''
'''

# Import Modules:

try:
	from datetime import datetime
	from ast import literal_eval
	from flask import current_app as c_app
	from sqlalchemy import create_engine
	from sqlalchemy.ext.declarative import declarative_base
	from sqlalchemy.orm import sessionmaker, load_only
	from app.models import (
		Base, UrlShorten
	)

except ImportError as e:
	raise e

# Class Definition:

class FlaskSqlAlchemy:

	def __init__(self, app=None, config_prefix="SQLALCHEMY_CONNECTION", **kwargs):
		'''
		'''
		self.config_prefix = config_prefix

		if app is not None:
			self.init_app(app)

	def init_app(self, app, **kwargs):
		'''
		'''
		try:
			db_url = app.config.get('DB_URL')
			connection_string = f'{db_url}'
			engine = create_engine(connection_string)
			Session = sessionmaker(bind=engine)
			session = Session()
			app.config['BASE'] = Base
			app.config['ENGINE'] = engine
			app.config['SESSION'] = session
			Base.metadata.create_all(engine)

		except Exception as e:
			raise e
