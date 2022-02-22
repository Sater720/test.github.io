import os
"""
Django settings for Collor_Battle project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1wyi8gk7ag#ouf(^(!g6qnlru#y6!%3m=qo^*9xd2)3s(vfqro'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = []

DEBUG = True  # False

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_markdown2',

    'registration',
    'accounts',
    'avatar',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django_comments_xtd',
    'django_comments',
    'rest_framework',

    'payments',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.reddit',
]

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale/'), )

LANGUAGES = (
    ('en-us', _('English')),
    ('ru', _('Russian')),
)

# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Collor_Battle.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'Collor_Battle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# PAYMENT_HOST = 'localhost:8000'
# PAYMENT_USES_SSL = False
# PAYMENT_MODEL = 'registration.Payment'
# PAYMENT_VARIANTS = {'default': ('payments.dummy.DummyProvider', {})}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ACCOUNT_EMAIL_REQUIRED = True  # указвать или не указывать почту при регистрации
ACCOUNT_EMAIL_VERIFICATION = "none"  # "mandatory"


AVATAR_AUTO_GENERATE_SIZES = [250, 100]
AVATAR_MAX_SIZE = 1024 * 1024
AVATAR_MIN_SIZE = 100 * 100
AVATAR_CLEANUP_DELETED = True
AVATAR_EXPOSE_USERNAMES = True
AVATAR_THUMB_FORMAT = 'PNG'
AVATAR_MAX_AVATARS_PER_USER = 3
AVATAR_GRAVATAR_DEFAULT = 'https://i.ibb.co/ZXFWd4k/defoult.jpg'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "color.battle.confir@gmail.com"
EMAIL_HOST_PASSWORD = "tiger22scrol20GD18"
EMAIL_PORT = 587

# ACCOUNT_ADAPTER = "registration.adapter.MyAccountAdapter"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# MAX_USERNAME_LENGTH = 10
ACCOUNT_ADAPTER = 'registration.models.UsernameMaxAdapter'

'''
Для входа по email
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
'''


LOGIN_URL = ' '
LOGIN_REDIRECT_URL = "/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# COMMENTS_XTD_MODEL = 'mycomments.models.MyComment'

COMMENTS_APP = 'django_comments_xtd'

COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                     b"Aequam memento rebus in arduis servare mentem.")

COMMENTS_XTD_FROM_EMAIL = "color.scrooge3000admen@gmail.com"
COMMENTS_XTD_CONTACT_EMAIL = "color.scrooge3000admen@gmail.com"

COMMENTS_XTD_CONFIRM_EMAIL = False


COMMENTS_XTD_MAX_THREAD_LEVEL = 1
COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order')

COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'registration.comment': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': True,
    }
}

MEDIA_URL = '/IMG/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/IMG')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATETIME_FORMAT = 'N j, Y, H:i'

TIME_FORMAT = 'H:i'

SITE_ID = 1