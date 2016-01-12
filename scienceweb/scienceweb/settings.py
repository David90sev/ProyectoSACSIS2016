"""
Django settings for scienceweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import LOGIN_REDIRECT_URL, LOGOUT_URL
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%ch8ea)&_kf!xk(!p*3sb%b^_=smg#nm(z66bt*x1l_qx$&qrr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'scienceweb.urls'

WSGI_APPLICATION = 'scienceweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'scienceweb',
        'USER': 'scienceweb',
        'PASSWORD': 'scienceweb',
        #'HOST': 'db.local',
        'HOST': '',
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }


#LOGIN
from django.core.urlresolvers import reverse_lazy
LOGIN_URL=reverse_lazy('login')
LOGIN_REDIRECT_URL=reverse_lazy('login')
LOGOUT_URL=reverse_lazy('logout')

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = 'http://localhost:8888/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


ACCOUNT_ACTIVATION_DAYS=7

EMAIL_HOST = 'smtp.gmail.com'
#cambiar con nombre del dominio
EMAIL_HOST_USER = 'science.developers@gmail.com'
EMAIL_HOST_PASSWORD = 'QgO1mljMFpuvXltUozwJ'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Science <noreply@science.org>'


SITE_ID=1