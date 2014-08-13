from django.test import TestCase
from models import Project, ProjectTypeValidation, ProjectType
import datetime
import random
from mysite import settings

# Create your tests here.
class TestViewConnections(TestCase):
	"""
	Tests all view connections in portfolio_listing
	"""
	def run_connection_test(self, url_string):
		"""
		Tests the response to a particular url
		"""
		response = self.client.get(url_string)
		self.assertEqual(response.status_code, 200 , url_string + ' is not connecting properly')

	def test_views_connections_noauth(self):
		"""
		Test all connections that do not require a login 
		"""
		url_string_list = ["/portfolio/",]
		for url in url_string_list:
			self.run_connection_test(url)

