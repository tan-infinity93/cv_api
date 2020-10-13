'''
'''

# Import Modules:

import os
import sys
import json
import platform
import multiprocessing
from datetime import datetime
from flask import Flask, request, current_app as c_app, send_file
from flask_restful import Resource
from middleware.decorators import is_valid_token

# Class Definitions:

class System(Resource):
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

	@is_valid_token
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
				"python_version": sys.version.replace('\n',''),
				"backend": {
					"programming_language": "Python",
					"framework": "Flask",
					"database": "None",
					"wsgi_server": "Gunicorn",
					"web_server": "Heroku Vegur",
				},
				"frontend": {
					"programming_language": "Javascript",
					"ui_framework": "VueJS",
					"middleware": "Express"
				}
			}
			response = {
				"meta": self.meta,
				"system_data": system_data
			}
			return response, self.success_code, self.headers

		except Exception as e:
			raise e
			response = {
				"meta": self.meta,
				"message": "unable to process request"
			}
			return response, self.exception_code, self.headers