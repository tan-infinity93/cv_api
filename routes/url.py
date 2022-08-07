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
from app.models import UrlShorten
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
			args_data = request.args.to_dict()
			url = args_data.get('url')

			url_obj = UrlShorten()
			url_data = url_obj.find({'short_url': url}, one=True)
			long_url = url_data.get('url')

			if url_data:
				response = make_response(redirect(long_url, code=302))
				response.headers['X-Parachutes'] = 'parachutes are cool'
				return response
			else:
				response = {
					"meta": self.meta,
					"message": "no long url is present for such short code"
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
			url = post_data.get('url')
			length = post_data.get('length', 7)
			short_url = ''.join(
				random.choices(string.ascii_uppercase + string.digits, k = length)
			)

			# Save Data in DB:

			db_obj = UrlShorten()
			db_obj.url = url
			db_obj.length = length
			db_obj.short_url = short_url
			db_obj.save()

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
			traceback.print_exc()
			response = {
				"meta": self.meta,
				"message": "unable to process request"
			}
			return response, self.exception_code, self.headers