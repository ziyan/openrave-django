# -*- coding: utf-8 -*-

"""
Django settings for mujin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_ROOT = os.path.join(os.path.dirname(ROOT), 'data')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a8h37=3$dpg99twij+12-wr@^nkr*-^8hjq$&&5pi&n7_=qb!y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
APPEND_SLASH = False

# version derived from hostname
# because docker uses container id as docker name
# this version string is likely to change
import hashlib
VERSION = hashlib.sha1(os.environ.get('HOSTNAME', '')).hexdigest()

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'web',
    'user',
    'robot',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "web.context_processors.all",
)

TEMPLATE_DIRS = (
    os.path.join(ROOT, 'template'),
)

ROOT_URLCONF = 'mujin.urls'
WSGI_APPLICATION = 'mujin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT, 'db.sqlite3'),
        'ATOMIC_REQUESTS': True,
    }
}

# timezone and locale
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (
    os.path.join(ROOT, 'locale'),
)
LANGUAGE_CODE = 'en-us'
LANGUAGE_COOKIE_NAME = 'locale'
LANGUAGE_COOKIE_PATH = '/'
LANGUAGES = (
    ('en-us', u'English (US)'),
    ('zh-cn', u'简体中文'),
)

# static files
STATIC_URL = '/static/' + VERSION + '/'
STATIC_ROOT = os.path.join(DATA_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(ROOT, 'static'),
)

