"""
Contains settings for only production environment.
"""

import os
import warnings
from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: Allow hosts should not be left empty
ALLOWED_HOSTS += []

# Add production apps
INSTALLED_APPS += []
MIDDLEWARE += []

# HTTPS requests
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DB", None),
        'USER': os.environ.get("POSTGRES_USER", None),
        'PASSWORD': os.environ.get("POSTGRES_USER_PASSWORD", None),
        'HOST': os.environ.get("POSTGRES_HOST", None),
        'PORT': os.environ.get("POSTGRES_PORT", 5432),
    }
}

# NOTE: Password validation if required to change
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
#AUTH_PASSWORD_VALIDATORS = [ ]
