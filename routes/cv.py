'''
'''

# Import Modules:

import json
from datetime import datetime
from flask import Flask, request, current_app as c_app, send_file
from flask_restful import Resource
from middleware.decorators import is_valid_token

# Class Definitions:

class CV(Resource):
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
			cv_data = {}
			file = './docs/tan_cv.json'
			with open(file, 'r') as f:
				cv_data = json.loads(f.read())
			# send_file(BytesIO(resp.content), mimetype="image/jpeg", attachment_filename="img2.jpg", as_attachment=True)
			response = {
				"meta": self.meta,
				"cv_data": cv_data
			}
			return response, self.success_code, self.headers

		except Exception as e:
			raise e
			response = {
				"meta": self.meta,
				"message": "unable to process request"
			}
			return response, self.exception_code, self.headers