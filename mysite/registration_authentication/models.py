from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
	)
from django.core.validators import MinLengthValidator

# Create your models here.
class MyUserManager(BaseUserManager):
	def create_user(self,username,first_name, middle_initial,
					last_name, email, birth_date,
					street_address, city, state, zip_code,
					password=None):
		if not email: 
			raise ValueError('Users must have an email address')
		user = self.model(
			username = username,
			first_name = first_name,
			middle_initial = middle_initial,
			last_name = last_name,
			email = MyUserManager.normalize_email(email),
			birth_date = birth_date,
			street_address = street_address,
			city = city,
			state = state,
			zip_code = zip_code,
		)
		user.is_active = True
		user.is_admin = False
		# user.is_staff = False
		user.set_password(password)
		user.save()
		return user
	
	def create_superuser(self, username, birth_date, password,
						first_name, middle_initial, last_name, email,
						street_address, city, state, zip_code):
		user = self.create_user(username=username,
							birth_date = birth_date,
							password=password,
							first_name=first_name,
							middle_initial=middle_initial, last_name=last_name,
							email=email,street_address=street_address,
							city=city, state=state, zip_code=zip_code)
		user.is_active = True
		user.is_admin = True
		user.save()
		return user

class UserProfile(AbstractBaseUser):
	username = models.CharField(max_length=20, unique = True, 
								validators = [MinLengthValidator(6)])
	middle_initial = models.CharField(max_length=1)
	birth_date = models.DateField()
	street_address = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=2)
	zip_code = models.CharField(max_length=5)
	email = models.EmailField(
						verbose_name='email address',
						max_length=255)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['birth_date','first_name','middle_initial',
						'last_name','email','street_address','city',
						'state','zip_code']

	

	def get_full_name(self):
    	# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True
	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin
# class MyUserManager(BaseUserManager):
# 	def create_user(self,username,first_name, middle_initial,
# 					last_name, email, birth_date,
# 					street_address, city, state, zip_code,
# 					password=None):
# 		if not email: 
# 			raise ValueError('Users must have an email address')
# 		user = self.model(
# 			username = username,
# 			first_name = first_name,
# 			middle_initial = middle_initial,
# 			last_name = last_name,
# 			email = MyUserManager.normalize_email(email),
# 			birth_date = birth_date,
# 			street_address = street_address,
# 			city = city,
# 			state = state,
# 			zip_code = zip_code,
# 		)
# 		user.is_active = True
# 		user.is_admin = False
# 		# user.is_staff = False
# 		user.set_password(password)
# 		user.save()
# 		return user
	
# 	def create_superuser(self, username, birth_date, password,
# 						first_name, middle_initial, last_name, email,
# 						street_address, city, state, zip_code):
# 		user = self.create_user(username=username,
# 							birth_date = birth_date,
# 							password=password,
# 							first_name=first_name,
# 							middle_initial=middle_initial, last_name=last_name,
# 							email=email,street_address=street_address,
# 							city=city, state=state, zip_code=zip_code)
# 		user.is_active = True
# 		user.is_admin = True
# 		user.save()
# 		return user

# class UserProfile(AbstractBaseUser):
# 	username = models.CharField(max_length=20, unique = True)
# 	middle_initial = models.CharField(max_length=1)
# 	birth_date = models.DateField()
# 	street_address = models.CharField(max_length=30)
# 	city = models.CharField(max_length=30)
# 	state = models.CharField(max_length=2)
# 	zip_code = models.CharField(max_length=5)
# 	email = models.EmailField(
# 						verbose_name='email address',
# 						max_length=255)
# 	first_name = models.CharField(max_length=50)
# 	last_name = models.CharField(max_length=50)
# 	is_active = models.BooleanField(default=True)
# 	is_admin = models.BooleanField(default=False)

# 	objects = MyUserManager()

# 	USERNAME_FIELD = 'username'
# 	REQUIRED_FIELDS = ['birth_date','first_name','middle_initial',
# 						'last_name','email','street_address','city',
# 						'state','zip_code']

	

# 	def get_full_name(self):
#     	# The user is identified by their email address
# 		return self.email

# 	def get_short_name(self):
# 		# The user is identified by their email address
# 		return self.email

# 	def __unicode__(self):
# 		return self.email

# 	def has_perm(self, perm, obj=None):
# 		"Does the user have a specific permission?"
# 		# Simplest possible answer: Yes, always
# 		return True

# 	def has_module_perms(self, app_label):
# 		"Does the user have permissions to view the app `app_label`?"
# 		# Simplest possible answer: Yes, always
# 		return True
# 	@property
# 	def is_staff(self):
# 		"Is the user a member of staff?"
# 		# Simplest possible answer: All admins are staff
# 		return self.is_admin