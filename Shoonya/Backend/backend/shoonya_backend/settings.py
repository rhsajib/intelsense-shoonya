"""
Django settings for shoonya_backend project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import logging
import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
    from google.cloud import logging as gc_logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("ENV") == "dev"

if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0", "*"]
else:
    ALLOWED_HOSTS = [
        "shoonya.ai4bharat.org",
        "0.0.0.0",
        "backend.shoonya.ai4bharat.org",
    ]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "rest_framework",
    "djoser",
    "users",
    "organizations",
    "workspaces",
    "dataset",
    "projects",
    "tasks",
    "functions",
    "loging",
    "corsheaders",
    "import_export",
    "django_celery_results",
    "django_celery_beat",
    "django.contrib.postgres",
]

CSRF_COOKIE_SECURE = False

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

ROOT_URLCONF = "shoonya_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "shoonya_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "shoonya_backend.pagination.CustomPagination",
}


# Email Settings
EMAIL_BACKEND = "django_smtp_ssl.SSLEmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv("SMTP_USERNAME")
EMAIL_HOST_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

DOMAIN = "shoonya.ai4bharat.org"
SITE_NAME = "shoonya.ai4bharat.org"

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "#/forget-password/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "users/auth/users/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "users/auth/users/activation/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {},
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "BLACKLIST_AFTER_ROTATION": False,
    "REFRESH_TOKEN_LIFETIME": timedelta(days=20),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=100),
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 102400  # higher than the count of fields

# Logging Configuration

# # Get loglevel from env
LOGLEVEL = os.getenv("LOG_LEVEL", "INFO")

# Make a new directory for logs
Path(BASE_DIR / "logs").mkdir(exist_ok=True)

# Define the list of formatters
formatters = {
    "console": {
        "()": "shoonya_backend.logger.ConsoleFormatter",
        "format": "({server_time}) {console_msg}",
        "style": "{",
    },
    "file": {
        "format": "{levelname} ({asctime}) [{module}:{process}|{thread}] {message}",
        "style": "{",
    },
    "csvfile": {
        "format": "{levelname},{asctime},{module},{process},{thread},{message}",
        "style": "{",
    },
}

# Define the list of handlers
handlers = {
    "console": {
        "level": LOGLEVEL,
        "class": "logging.StreamHandler",
        "formatter": "console",
    }
}

# If logging is enabled, add file handlers
if os.getenv("LOGGING", "False").lower() in ("true", "1", "t", "yes", "y"):
    handlers["file"] = {
        "level": "WARNING",
        "class": "logging.FileHandler",
        "filename": os.path.join(BASE_DIR, "logs/default.log"),
        "formatter": "file",
    }

    handlers["csvfile"] = {
        "level": "WARNING",
        "class": "logging.FileHandler",
        "filename": os.path.join(BASE_DIR, "logs/logs.csv"),
        "formatter": "csvfile",
    }

# Setup the Cloud Logging Client
# if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
#    client = gc_logging.Client()
#    client.setup_logging(log_level=logging.WARNING)
#    handlers["gcloud-logging"] = {
#        "class": "google.cloud.logging.handlers.CloudLoggingHandler",
#        "client": client,
#    }

# Define logger configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": formatters,
    "handlers": handlers,
    "loggers": {
        "": {
            "level": LOGLEVEL,
            "handlers": handlers.keys(),
        },
        "django": {
            "handlers": [],
        },
        "django.server": {"propagate": True},
    },
}
CELERY_IMPORTS = ("users.tasks",)

# Celery settings
CELERY_TIMEZONE = "Asia/Kolkata"
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"


# Project lock TTL for task pulling(in seconds)
PROJECT_LOCK_TTL = 5
PROJECT_LOCK_RETRY_INTERVAL = 1
