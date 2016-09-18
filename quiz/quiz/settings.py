"""
Django==1.7.0
mongoengine==0.8.4
pymongo==2.6.2

Django settings for quiz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from config import *

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = (os.path.join(BASE_DIR + "/quiz/",'static'))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '&5+h(wh0fl5vmfi%w13$8euz_^e(_nai-20s$9cdzy90@ro21_'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*'] 
# Application definition

SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'quizpage',
)
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
)


ROOT_URLCONF = 'quiz.urls'

WSGI_APPLICATION = 'quiz.wsgi.application'



#SESSION_ENGINE = 'mongoengine.django.sessions'
#mongoengine.connect('Quiz', alias='default')

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7sumlgl2ovmpg',
        'USER': 'gncunxinnnspnm',
        'PASSWORD': 'qt6f1RKkDS7U8L0sCeK3AqM4mW',
        'HOST': 'ec2-54-243-207-17.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

'''
#Old Sqlite Database
DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
        }

    }
'''
#import dj_database_url
#DATABASES['default'] = dj_database_url.config()


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/djsite'


SOCIAL_AUTH_FACEBOOK_KEY = '1265904420128016'
SOCIAL_AUTH_FACEBOOK_SECRET = '036034a21a718b32c60a4676af2d6d59'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '8507...kg6.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'gUzw...CD32-'

SOCIAL_AUTH_TWITTER_KEY = 'lNx...yQH8u'
SOCIAL_AUTH_TWITTER_SECRET = '8virx...Div4dwB'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
