"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import imp 

try: 
	import secret_settings
except ImportError:
	pass

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_DIR = os.path.dirname(__file__)

PROJECT_PATH =  os.path.realpath(os.path.dirname(__file__))


MEDIA_URL = '/media/'

#Static Files
STATIC_ROOT = os.path.join(PROJECT_PATH, '../../staticfiles')
STATIC_URL = '/staticfiles/'

STATICFILES_DIRS = (
	os.path.join(PROJECT_PATH, '../../static'),
	os.path.join(PROJECT_PATH, '../../static/bootstrap'),
	os.path.join(PROJECT_PATH, '../../static/jquery'),
	os.path.join(PROJECT_PATH, '../../media')
	)

STATICFILE_FINDERS = (
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",

)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
	SECRET_KEY = secret_settings.SECRET_KEY
except (NameError, AttributeError) as e:
	SECRET_KEY = os.environ['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SITE_ID = 1
TEMPLATE_DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1','127.0.0.1:8000', 'localhost']
try:
	ALLOWED_HOSTS = secret_settings.ALLOWED_HOSTS
except (NameError, AttributeError) as e:
	ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sites',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'registration_authentication',
	'portfolio_listing',
	'south',
	'django_nose',
	'ordered_model',
	'stdimage',
	'contact_form'
)

MIDDLEWARE_CLASSES = (
	'django.middleware.gzip.GZipMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'htmlmin.middleware.HtmlMinifyMiddleware',
	'htmlmin.middleware.MarkRequestMiddleware',
	
)
HTML_MINIFY = True

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

dbconfig = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

DATABASES = {
	'default': { 
		'ENGINE': 'django.db.backends.postgresql_psycopg2', 
		'NAME': 'rain_db',                     
		
	}
}
 
try:
	DATABASES['default']['USER'] = secret_settings.DATABASE_USERNAME
	DATABASES['default']['PASSWORD'] = secret_settings.DATABASE_PASSWORD
except (NameError, AttributeError) as e:
	DATABASES['default']['USER'] = os.environ['DATABASE_USERNAME']
	DATABASES['default']['PASSWORD'] = os.environ['DATABASE_PASSWORD']
	


if dbconfig: 
	DATABASES['default'] = dbconfig


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True






# Template Directory

TEMPLATE_DIRS = (
	os.path.join(PROJECT_PATH, '../../templates'),
	os.path.join(PROJECT_PATH, '../mysite/portfolio_listing/templates'),
	os.path.join(PROJECT_PATH, '../mysite/registration_authentication/templates'),
	os.path.join(PROJECT_PATH, '../mysite/contact_form/templates'),
)




#Secure cookies
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SESSION_EXPIRE_AT_BROWSER_CLOSE=False

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages"
)
AUTH_USER_MODEL = 'registration_authentication.UserProfile'
ACCOUNT_ACTIVATION_DAYS = 2

MANAGERS = (('robert','rmwdeveloper@gmail.com'),)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
try: 
	EMAIL_HOST = secret_settings.EMAIL_HOST
	EMAIL_PORT = secret_settings.EMAIL_PORT
	EMAIL_HOST_USER = secret_settings.EMAIL_HOST_USER
	EMAIL_HOST_PASSWORD = secret_settings.EMAIL_HOST_PASSWORD
except (NameError, AttributeError) as e:
	EMAIL_HOST = os.environ['EMAIL_PORT']
	EMAIL_PORT = os.environ['EMAIL_HOST']
	EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
	EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

DEFAULT_FROM_EMAIL = 'rmwdeveloper@gmail.com'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'



TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
	'--with-coverage', 
	'--cover-package=portfolio_listing, registration_authentication',
]

##LOGGING
# LOGGING = {
# 	'version': 1,
# 	'disable_existing_loggers': False,
# 	'filters': {
# 		'require_debug_false': {
# 			'()': 'django.utils.log.RequireDebugFalse'
# 		}
# 	},
# 	'handlers': {
# 		'mail_admins': {
# 			'level': 'ERROR',
# 			'filters': ['require_debug_false'],
# 			'class': 'django.utils.log.AdminEmailHandler'
# 		},
# 		'logfile': {
# 			'class': 'logging.handlers.WatchedFileHandler',
# 			'filename':  os.path.join(PROJECT_PATH, '../../../var/log/django/error.log')
# 		},
# 	},
# 	'loggers': {
# 		'django.request': {
# 			'handlers': ['mail_admins'],
# 			'level': 'ERROR',
# 			'propagate': True,
# 		},
# 		'django': {
# 			'handlers': ['logfile'],
# 			'level': 'ERROR',
# 			'propagate': False,
# 		},
# 	}
# }