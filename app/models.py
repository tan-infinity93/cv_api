'''
'''

# Import Modules:

import json
from datetime import datetime, date
from flask import current_app as c_app
from sqlalchemy import Column, Boolean, Integer, String, DateTime, JSON, ARRAY, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLAlchemy ORM Object:

Base = declarative_base()

# Tables:

class UrlShorten(Base):
	'''
	'''
	__tablename__ = 'url_shortener_details'
	id = Column(Integer, primary_key=True)
	url = Column(String, index=True)
	length =  Column(Integer)
	short_url =  Column(String, index=True)
	timestamp = Column(DateTime, index=True)

	def to_json(self):
		return {
			'id': self.id,
			'url': self.url,
			'length': self.length,
			'short_url': self.short_url,
			'timestamp': self.timestamp.isoformat(),
		}

	def find(self, kwargs={}, one=False):
		'''
		'''
		try:
			c_session = c_app.config.get('SESSION')
			url_data = c_session.query(self.__class__).filter_by(**kwargs).first()

			if url_data:
				return url_data.to_json()
			return {}

		except Exception as e:
			raise e

	def save(self):
		'''
		'''
		try:
			c_session = c_app.config.get('SESSION')
			self.timestamp = datetime.utcnow().isoformat()
			c_session.add(self)
			c_session.commit()

		except Exception as e:
			c_session.rollback()
			raise e