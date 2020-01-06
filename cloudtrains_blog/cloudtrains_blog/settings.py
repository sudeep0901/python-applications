"""
Django settings for cloudtrains_blog project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd_a=g_^@5do(5fhgsd#j-8*h30wh$_(4@sj23l_w_t5ddas77i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'django_extensions',
    'taggit',
    # 'simple_pagination',
    # 'django_blog_it',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'bootstrap4',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cloudtrains_blog.urls'

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

WSGI_APPLICATION = 'cloudtrains_blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',  # the missing piece of the puzzle
        # 'PORT': '',  # optional, I don't need this since I'm using the standard port
    },

}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
print(BASE_DIR)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

EMAIL_HOST = 'localhost'
EMAIL_PORT = '8999'

# EMAIL_HOST_USER
# : Password for the SMTP server
# EMAIL_HOST_PASSWORD
# : Whether to use a TLS secure connection
# EMAIL_USE_TLS
# : Whether to use an implicit TLS secure

# in case SMTP server not available Django prints message to console

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# send_mail('Django Mail', 'This is a test email','sudeep.tech.patel@gmail.com', ['sudeep.tech.patel@gmail.com'], fail_silently=False)

# PACKAGE_DIRS = '/home/sudeep/.local/lib/python3.7/site-packages/'
# TEMPLATE_DIRS = (
#     os.path.join(PACKAGE_DIRS, 'django_blog_it/django_blog_it/templates/dashboard/'),
# )
# print(os.path.join(PACKAGE_DIRS, 'django_blog_it/django_blog_it/templates/dashboard/'))
