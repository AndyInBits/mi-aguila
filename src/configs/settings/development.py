"""
Django settings for {{ project_name }} project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Import default settings
from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

ALLOWED_HOSTS += ['*']

# Add development apps not required on production
INSTALLED_APPS += []
MIDDLEWARE += []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DB", None),
        'USER': os.environ.get("POSTGRES_USER", None),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", None),
        'HOST': os.environ.get("POSTGRES_HOST", None),
        'PORT': os.environ.get("POSTGRES_PORT", 5432),
    }
}