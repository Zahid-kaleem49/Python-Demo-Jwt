import pytest
from django.conf import settings

from tutorial.settings import BASE_DIR


def pytest_configure():
    settings.configure(DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'dbtest.sqlite3',
        }
    })
