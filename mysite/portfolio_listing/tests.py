from django.test import TestCase , LiveServerTestCase
from models import Project
import datetime
import random
from selenium import webdriver
from mysite import settings
from registration_authentication.tests import HelperFunctions

# Create your tests here.
class TestViewConnections(TestCase):
	"""
	Tests all view connections in portfolio_listing
	"""
	def run_connection_test(self, url_string , auth = False):
		"""
		Tests the response to a particular url. 

		Auth is a bool depending on whether the user should connect if they are not authorized. False means
		no authorization is required. 
		"""
		response = self.client.get(url_string)
		if auth == True:
			self.assertEqual(response.status_code, 404)

		self.assertEqual(response.status_code, 200 , url_string + ' is not connecting properly')

		if auth == True:
			my_admin = HelperFunctions().create_superuser()
			
			self.client.login(my_admin.user , my_admin.password)

	def test_views_connections_noauth(self):
		"""
		Test all connections that do not require a login 
		"""
		url_string_list = ["/portfolio/", ]
		for url in url_string_list:
			self.run_connection_test(url)

class TestPortfolioListingPage(LiveServerTestCase):

	def test
	driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX.copy())
	driver.get('http://www.google.com')
