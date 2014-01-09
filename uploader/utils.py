# coding: utf-8
from flask import current_app


def is_file_allowed(filename):
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']
    )
