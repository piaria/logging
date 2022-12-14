"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$y9d2h5qhe^&*ec1u9@ucsr9*x7ylx&tw_f@jmxt6(_3x&*5w3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mysite.logging.middleware.RequestLogMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Log file configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,    # Whether to disable the existing logger
    'formatters': {                      # The format of log information display
        'verbose': {'format': '[%(asctime)s %(levelname)s [%(module)s:%(lineno)d] [%(process)d:%(threadName)s] %(message)s'},
        'simple':  {'format': '%(asctime)s %(levelname)s [%(module)s:%(lineno)d] %(message)s'},
        'complex': {'format': '[%(hostname)s source_ip:%(source_ip)s] [UOW:%(uow)s] [%(asctime)s %(levelname)s [%(module)s:%(lineno)d] [%(process)d:%(threadName)s] %(message)s'},
        'clicOH': {'format': '[%(asctime)s] [%(hostname)s] [%(username)s] [%(uow)s] [%(request_id)s] [%(levelname)s] [%(module)s:%(lineno)d] %(message)s'},
    },
    'filters': {
        'new_add': {
            '()': 'mysite.logging.middleware.RequestLogFilter',
        },
    },
    'handlers': {         # Log processing method
        'console': {      # Output logs to the terminal
            'level': 'INFO',
            'filters': ['new_add'],
            'class': 'logging.StreamHandler',
            'formatter': 'clicOH'
        },
    },
    'loggers': {
        '': {                                     # Defines a default logger
            'handlers': ['console'],              # It can output log to terminal and file at the same time
            'level': 'INFO',                      # The lowest log level that the logger receives
            'propagate': False,                   # Whether to inherit the log Information ,0: no 1: yes
        },
    }
}