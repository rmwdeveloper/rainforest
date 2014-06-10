from django.test import TestCase , LiveServerTestCase
import datetime
import random
from mysite import settings
from registration_authentication import models , forms
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest

class HelperFunctions: 
	def __init__(self):
		self.invalid_registration_vals = {
		"username": "",
		"first_name": "",
		"middle_initial": "",
		"last_name": "",
		"email": "test",
		"birth_date": "June Twenty Second Two thousand and Three",
		"street_address": "",
		"city": "",
		"state": "Philadelphia",
		"zip_code":"three81",
		'password1': '1234',
		'password2': 'asadf'}

		self.valid_registration_vals = {
		"username": "test01",
		"first_name": "John",
		"middle_initial": "M",
		"last_name": "Doe",
		"email": "test01@test.com",
		"birth_date": datetime.date(2006,12,12) ,
		"street_address": "123 Fake Street",
		"city": "Rockaway",
		"state": "NJ",
		"zip_code":"07866",
		'password1': '123456',
		'password2': '123456'}
		self.valid_registration_vals_2 = {
		"username": "test02",
		"first_name": "John",
		"middle_initial": "M",
		"last_name": "Doe",
		"email": "test02@test.com",
		"birth_date": datetime.date(2006,12,12) ,
		"street_address": "123 Fake Street",
		"city": "Rockaway",
		"state": "NJ",
		"zip_code":"07866",
		'password1': '123456',
		'password2': '123456'}
	def create_invalid_user_vals(self):
		"""
		Randomly generates a dictionary of fields for a UserCreateForm that has one invalid value.
		"""
		invalid_registration_form = {}
		invalid_field = random.choice(self.invalid_registration_vals.keys())

		invalid_registration_form[invalid_field] = self.invalid_registration_vals[invalid_field]

		for key in self.valid_registration_vals:
			if key == invalid_field:
				pass
			else:
				invalid_registration_form[key] = self.valid_registration_vals[key]
		return invalid_registration_form
	def create_valid_user_vals(self,num = 0):
		"""
		Return valid registration vals
		"""
		if num == 0:
			return self.valid_registration_vals
		return self.valid_registration_vals_2
	def create_user(self, version = 0):
		"""
		Creates a UserProfile. Version is an integer that determines which userprofile to generate (one of two)
		"""
		registration_values = self.create_valid_user_vals(version)
		user_form = forms.UserCreateForm(registration_values)
		if user_form.is_valid():
			user_form.save()

class TestViewConnections(TestCase):
	"""
	Tests all view connections in registration_authentication
	"""
	def run_connection_test(self, url_string):
		"""
		Tests the response to a particular url
		"""
		response = self.client.get(url_string)
		self.assertEqual(response.status_code, 200 , url_string + ' is not connecting properly')

	def test_views_connections(self):

		url_string_list = []
		for url in url_string_list:
			self.run_connection_test(url)
	def test_login_required_view_connections(self):
		"""
		Test all connections that require a login
		"""
		test_user_vals = HelperFunctions().create_valid_user_vals()
		test_user = HelperFunctions().create_user()
		url_string_list = ['/storefront/']
		self.client.login(username = test_user_vals['username'], password = test_user_vals['password1'])
		for url in url_string_list:
			self.run_connection_test(url)

class TestMainPage(TestCase):
	def setUp(self):
		self.valid_user_form = HelperFunctions().create_valid_user_vals()
		self.invalid_user_form = HelperFunctions().create_invalid_user_vals()
		self.test_user = HelperFunctions().create_user()

	def test_connection(self):
		self.client.login(username=self.valid_user_form['username'], 
						  password=self.valid_user_form['password1'])

		response = self.client.get('/storefront/')
		self.assertEqual(response.status_code, 200)
	def test_unauthenticated_user_should_redirect(self):
		response = self.client.get('/storefront/')
		self.assertRedirects(response, '/login/')

class EnteringProductTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		self.browser.get('http://localhost:8000/')
		login_modal = self.browser.find_element_by_class_name('login-window')
		login_modal.click()
		username_input = self.browser.find_element_by_name('login_username')
		password_input = self.browser.find_element_by_name('login_password')
		username_input.send_keys('test01')
		password_input.send_keys('123456')
		password_input.send_keys(Keys.ENTER)

		header_username  = self.browser.find_element_by_id('header_username')
		self.assertEqual(
			 	'test01', header_username.text
			)
		self.browser.get('http://localhost:8000/storefront/')
		self.assertIn('Storefront', self.browser.title)

	def tearDown(self):
		self.browser.quit()
	def input_test(self, form_element_id, placeholder_text, input_value):
		"""
		Finds the element corresponding form_element_id, tests if it's input_value
		value is correct, then checks to see if input is inputted correctly.
		"""
		form_input = self.browser.find_element_by_id(form_element_id)
		self.assertEqual(
			form_input.get_attribute('placeholder'),
			placeholder_text
		)
		form_input.send_keys(input_value)
		self.assertEqual(
			form_input.get_attribute('value'),
			input_value
		)

	def test_user_should_be_able_to_enter_product_information(self):
		self.input_test('product_name', 'Enter product name', 'Toaster')
		self.input_test('product_price', 'Enter product price', '49.99')
		self.input_test('product_description','Enter product description', 'A stainless steel toaster')
		self.input_test('product_weight_value', 'Enter product weight', '5')

		weight_type_selection = self.browser.find_element_by_id('product_weight_type')
		for option in self.browser.find_elements_by_tag_name('option'):
			if option.text == 'Kilogram(s)':
				option.click()
		self.assertEqual(
			weight_type_selection.get_attribute('value'),
			'KG'
		)





	
