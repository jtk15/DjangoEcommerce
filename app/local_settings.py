#coding=utf-8

import os

DEBUG  = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASABES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}