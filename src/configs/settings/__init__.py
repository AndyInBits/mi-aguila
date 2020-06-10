import os

__django_env = os.environ.get('DJANGO_ENV', '').lower()

if __django_env == 'development':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'configs.settings.development'
elif (__django_env == 'production'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'configs.settings.production'
elif (__django_env == 'qa'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'configs.settings.qa'
else:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'configs.settings.common'
