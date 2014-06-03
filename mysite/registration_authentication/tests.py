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
	def create_invalid_user(self):
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
	def create_valid_user(self,num = 0):
		"""
		Return valid registration vals
		"""
		if num == 0:
			return self.valid_registration_vals
		return self.valid_registration_vals_2


	
class RegisterViewTestCase(TestCase):
	def test_page(self):
		resp = self.client.get('/register/')
		self.assertEqual(resp.status_code, 200)

#Models Tests
class TestUserCreateForm(TestCase):
	def setUp(self):
		self.invalid_user = HelperFunctions().create_invalid_user()
		self.valid_user = HelperFunctions().create_valid_user()
	def test_form_should_validate_correctly(self):
		self.assertFalse(UserCreateForm(self.invalid_user).is_valid())
		self.assertTrue(UserCreateForm(self.valid_user).is_valid())

#Views Tests
class TestRegister(TestCase):
	def setUp(self):
		self.valid_user_form = HelperFunctions().create_valid_user()
		self.invalid_user_form = HelperFunctions().create_invalid_user()
		self.test_user_form = UserCreateForm(self.valid_user_form)
		if self.test_user_form.is_valid():
			self.test_user = self.test_user_form.save()
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
		valid_user = HelperFunctions().create_valid_user(1)
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
		self.valid_user_form = HelperFunctions().create_valid_user()
		self.invalid_user_form = HelperFunctions().create_invalid_user()
		self.test_user_form = UserCreateForm(self.valid_user_form)
		if self.test_user_form.is_valid():
			self.test_user = self.test_user_form.save()
	def test_login_required(self):
		self.client.login(username = self.valid_user_form['username'], password = self.valid_user_form['password1'])
		response = self.client.get('/logout/')
		self.assertRedirects(response, '/')
		response = self.client.get('/logout/')
		self.assertEqual(response.status_code , 302 )

class TestUserLogin(TestCase):
	def setUp(self):
		pass
