from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-gmmh0i1z9v0i01vwno44jl^6bur1721ewv#vz%9dn!f9$t97kd"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',                      
        'USER': 'postgres',
        'PASSWORD': 'babe',
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": os.environ.get("POSTGRES_DB"),
#             "USER": os.environ.get("POSTGRES_USER"),
#             "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
#             "HOST": "db",
#             "PORT": "5432",
#         }
#     }