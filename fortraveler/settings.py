"""
Django settings for fortraveler project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
<<<<<<< HEAD
from pathlib import Path
import my_settings
import os
=======

from pathlib import Path
import my_settings, os
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
=======

>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ekbgu4v_51u3y99f7j+r*ry9eqg($71g!n%cyu5kc$ce0xxco^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

<<<<<<< HEAD
=======

>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'post',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
<<<<<<< HEAD
    # 'django.middleware.csrf.CsrfViewMiddleware',
=======
    'django.middleware.csrf.CsrfViewMiddleware',
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fortraveler.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
=======
        'DIRS': [],
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
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

WSGI_APPLICATION = 'fortraveler.wsgi.application'

<<<<<<< HEAD
=======

>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databasespy

DATABASES = my_settings.DATABASES

<<<<<<< HEAD
=======

>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

<<<<<<< HEAD
=======

>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

<<<<<<< HEAD
USE_TZ = True
=======
USE_TZ = False

>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

<<<<<<< HEAD
STATIC_URL = 'static/'

=======


STATIC_URL = 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/') #사용자가 업로드한 파일 관리

>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
<<<<<<< HEAD

LOGIN_REDIRECT_URL = '/'
=======
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
