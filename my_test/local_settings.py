from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-j=+l%s0!jox*rk46yo0dypqd41rogv=ducx2f$#az(c++!)zy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'ORA12PDB_2.uvt.nl',
        'USER': 'BEESEN',
        'PASSWORD': 'beesen',
        'HOST': 'bakphoon.uvt.nl',
        'PORT': '1521',
    },
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
