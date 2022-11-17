import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure--4l=l!(shlqi8(fwqe24rvmwewej%sqfi2uk=krbu6'



DEBUG = False


ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}




STATIC_DIR = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS = [STATIC_DIR]

STATIC_ROOT= [os.path.join(BASE_DIR, 'static')]