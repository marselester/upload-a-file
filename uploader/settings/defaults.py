# coding: utf-8
import os

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'blah'

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

UPLOAD_PATH = os.path.join(PROJECT_PATH, 'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

UPLOADED_PHOTOS_DEST = UPLOAD_PATH
