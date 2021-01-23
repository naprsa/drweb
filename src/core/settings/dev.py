from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "3d(o%sj=_s2u_ak&(z)l8rik9i6z+n@=$hcbmutup03f8)&b*2"

INSTALLED_APPS += []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
