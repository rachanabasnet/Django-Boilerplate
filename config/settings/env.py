from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3343434-5opl61#npm54t579gw&j^@*x23io_tdh_+%)n=rfdz889jq1qq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}
