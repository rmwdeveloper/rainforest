from django.test import TestCase
from models import MyUserManager
from forms import UserCreateForm
import datetime
import random
from mysite import settings

# Create your tests here.
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
		user_form = UserCreateForm(registration_values)
		if user_form.is_valid():
			user_form.save()
	def create_superuser(self, version = 1):
		"""
		Creates a Superuser profile. 
		"""
		super_user = self.create_user(version = 1)
		super_user.is_admin = True
	


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
		"""
		Test all connections that do not require a login 
		"""
		url_string_list = ["/", "/tests/", "/register/","/placeholder/", "/error/", "/login/",]
		for url in url_string_list:
			self.run_connection_test(url)
	def test_login_required_view_connections(self):
		"""
		Test all connections that require a login
		"""
		test_user_vals = HelperFunctions().create_valid_user_vals()
		test_user = HelperFunctions().create_user()
		url_string_list = []
		self.client.login(username = test_user_vals['username'], password = test_user_vals['password1'])
		for url in url_string_list:
			self.run_connection_test(url)

#Models Tests
class TestUserCreateForm(TestCase):
	def setUp(self):
		self.invalid_user = HelperFunctions().create_invalid_user_vals()
		self.valid_user = HelperFunctions().create_valid_user_vals()
	def test_form_should_validate_correctly(self):
		self.assertFalse(UserCreateForm(self.invalid_user).is_valid())
		self.assertTrue(UserCreateForm(self.valid_user).is_valid())

#Views Tests
class TestRegister(TestCase):
	def setUp(self):
		self.valid_user_form = HelperFunctions().create_valid_user_vals()
		self.invalid_user_form = HelperFunctions().create_invalid_user_vals()
		self.test_user = HelperFunctions().create_user()

	def test_logged_in_user_should_redirect(self):
		self.client.login(username=self.valid_user_form['username'], password = self.valid_user_form['password1'])
		response = self.client.get('/register/')
		self.assertRedirects(response, '/')
	def test_invalid_form_should_return_form_errors(self):
		response = self.client.post('/register/', data = self.invalid_user_form, secure= True)
		self.assertTemplateUsed(response, template_name='register.html')
		self.assertTrue(response.context['errors'])
		self.assertTrue(response.context['form'])
	def test_valid_form_should_save_user(self):
		valid_user = HelperFunctions().create_valid_user_vals(1)
		response = self.client.post('/register/', data = valid_user, secure=True)
		test_user = self.client.login(username =  valid_user['username'], password = valid_user['password1'])
		self.assertTrue(test_user)
	def test_invalidate_in_use_username(self):
		response = self.client.get('/register/', data = {'username': self.valid_user_form['username']} )
		self.assertTrue(response.content == 'false')
	def test_validate_free_username(self):
		response = self.client.get('/register/', data = {'username': 'freeusername'} )
		self.assertTrue(response.content == 'true')
	def test_invalidate_in_use_email(self):
		response = self.client.get('/register/', data = {'email': self.valid_user_form['email']} )
		self.assertTrue(response.content == 'false')
	def test_validate_free_email(self):
		response = self.client.get('/register/', data = {'email': 'freeuseremail@test.com'} )
		self.assertTrue(response.content == 'true')
class TestUserLogout(TestCase):
	#refactor setUp method, does this need invalid_user_form? Also has alot in common with TestRegister.setup
	def setUp(self):
		self.valid_user_form = HelperFunctions().create_valid_user_vals()
		self.invalid_user_form = HelperFunctions().create_invalid_user_vals()
		test_user = HelperFunctions().create_user()
	def test_login_required(self):
		self.client.login(username = self.valid_user_form['username'], password = self.valid_user_form['password1'])
		response = self.client.get('/logout/')
		self.assertRedirects(response, '/')
		response = self.client.get('/logout/')
		self.assertEqual(response.status_code , 302 )

class TestUserLogin(TestCase):
	def setUp(self):
		pass
