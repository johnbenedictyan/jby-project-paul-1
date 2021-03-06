"""
Django settings for condo_fault_project project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
import dj_database_url
from django.contrib.messages import constants as messages
# import env

# Overrides the default django error for an invalid CSRF token with a custom view function.
CSRF_FAILURE_VIEW = 'fault_submission.views.csrf_failure'

# Changes the messages tag so that are displayed in Bootstrap
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# This line changes the default message storage to be a session based one.
# This allows messages to be rendered through a redirect.
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# This allows the cookies to persist sitewide.
SESSION_COOKIE_SECURE = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7fbi=-)egd*5at^k0k8plgst4h&a95*a_&)fy2pna8#o01u+ag'
# SECRET_KEY = os.urandom(24)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["condo-fault-project.herokuapp.com","e5deb49e1e1a4281a9286bda38916f5b.vfs.cloud9.ap-southeast-1.amazonaws.com"]

# Application definition

INSTALLED_APPS = [
    'pyuploadcare.dj',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_panel',
    'fault_submission',
    'crispy_forms'
]

# This changes the crispy forms to render the form in Bootstrap.
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'condo_fault_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'condo_fault_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {'default': dj_database_url.parse("postgres://nzsfffcppbiudw:47e11edd2c23e568d8b73b976f1348a22be1b6d0fd8c712a1fcdcaed93d55f3e@ec2-174-129-227-205.compute-1.amazonaws.com:5432/deh3dnjntrnora")}
    
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Commonly used url routes.
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/admin_panel/sign_in/'
LOGOUT_URL = '/admin_panel/sign_out/'
HOME_URL = '/'

UPLOADCARE = {
    'pub_key': os.environ.get("UPLOADCARE_PUBLIC_KEY"),
    'secret': os.environ.get("UPLOADCARE_SECRET_KEY"),
    'widget_version': '2.8.1',
    'widget_build': 'min',  ## without jQuery
}
