'''
'''

# Import Modules:

import jwt
import time
import traceback
import secrets
from datetime import datetime
from flask import Flask, request, current_app as c_app
from flask_restful import Resource

# Class Definitions:

class Auth(Resource):
	'''
	'''
	def __init__(self):
		'''
		'''
		self.meta = {
			"version": 1.0,
			"timestamp": datetime.now().isoformat()
		}
		self.headers = {"Content-Type": "application/json"}
		self.success_code = 200
		self.bad_code = 400
		self.exception_code = 500

	def get(self):
		'''
		'''
		try:
			system_data = {
				"platform": platform.system(),
				"release": platform.release(),
				"version": platform.version(),
				"architecture": ' '.join(platform.architecture()),
				"cpu_cores": multiprocessing.cpu_count(),
				"python_version": sys.version,
			}
			response = {
				"meta": self.meta,
				"system_data": system_data
			}
			return response, self.success_code, self.headers

		except Exception as e:
			traceback.print_exc()
			response = {
				"meta": self.meta,
				"message": "unable to process request"
			}
			return response, self.exception_code, self.headers

	def post(self):
		'''
		'''
		try:
			post_data = request.get_json()
			username = post_data.get('username')
			password = post_data.get('password')

			if username == 'tan-infinity93' and password == 'm@broSonu2002':
				key = c_app.config.get('SECRET_KEY')
				headers = {'kid': secrets.token_hex(10)}
				post_data.pop('password')
				post_data.update(
					{
						'exp': time.time() + 86400
					}
				)

				token = jwt.encode(post_data, key, algorithm='HS256', headers=headers)
				token_data = token.decode('UTF-8')

				response = {
					"meta": self.meta,
					"token": token_data
				}
				return response, self.success_code, self.headers

			else:
				response = {
					"meta": self.meta,
					"token_data": "Bad username or password"
				}
				return response, self.bad_code, self.headers

		except Exception as e:
			traceback.print_exc()
			response = {
				"meta": self.meta,
				"message": "unable to process request"
			}
			return response, self.exception_code, self.headers