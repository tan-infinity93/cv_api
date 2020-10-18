'''
'''

# Import Modules:

import os
import sys
import json
import string
import random
from datetime import datetime
from flask import Flask, request, current_app as c_app, redirect, make_response
from flask_restful import Resource
from middleware.decorators import is_valid_token

# Class Definitions:

class UrlShortener(Resource):
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
			short_url = {
				"DKZF3TYH": "https://www.youtube.com/watch?v=KR0g-1hnQPA"
			}

			args_data = request.args.to_dict()
			url = args_data.get('url', 'www.google.com')
			long_url = short_url.get(url)

			# response = {
			# 	"meta": self.meta,
			# 	"system_data": system_data
			# }
			response = make_response(redirect(long_url, code=302))
			response.headers['X-Parachutes'] = 'parachutes are cool'
			return response
			return redirect(long_url, code=302), self.success_code, self.headers

		except Exception as e:
			raise e
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
			url = post_data.get('url')
			length = post_data.get('length', 7)
			short_url = ''.join(
				random.choices(string.ascii_uppercase + string.digits, k = length)
			)
			url_data = {
				"url": url,
				"length": length,
				"short_url": short_url,
			}
			response = {
				"meta": self.meta,
				"url_data": url_data
			}
			return response, self.success_code, self.headers

		except Exception as e:
			raise e
			response = {
				"meta": self.meta,
				"message": "unable to process request"
			}
			return response, self.exception_code, self.headers