import os, sys
import logging

# Dummy ``ugettext`` function
_ = ugettext = lambda s: s

# Get absolute path for current directory
DIRNAME = os.path.dirname(__file__)

INTERNAL_IPS = ('127.0.0.1',)

# Insert parent and lib dirs to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(DIRNAME, '..')))
sys.path.insert(0, os.path.abspath(os.path.join(DIRNAME, '../lib')))
sys.path.insert(0, os.path.abspath(DIRNAME))

# Accounts settings
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_URL = '/logout/'
LOGOUT_REDIRECT_URL = '/'

# Database settings
# Please, set up proper values in ``settings_local.py`` file
DATABASE_ENGINE = 'sqlite3'
DATABASE_HOST = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_NAME = ':memory:'
DATABASE_PORT = ''

# Debug settings
DEBUG = True
TEMPLATE_DEBUG = False

# Email settings
# Please, set up proper email settings in ``settings_local.py`` file
DEFAULT_FROM_EMAIL = 'mail@localhost'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = 'root@localhost'

import time
TIME_ZONE = time.tzname[0]

# Installed applications
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',

    'faststart.app',

)

# Locale settings
USE_I18N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
)

# Middleware settings
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)



# Template settings
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
)

# Other **Django** related settings
ROOT_URLCONF = 'faststart.urls'
SITE_ID = 1

# **Registration** settings
# The number of days activation keys will remain valid after an account is
# registered.
ACCOUNT_ACTIVATION_DAYS = 30
AUTH_PROFILE_MODULE = 'member.Profile'


# Trying to load settings located in ``settings_local.py`` file
try:
    from settings_local import *
except ImportError, e:
    logging.exception(e)
    pass