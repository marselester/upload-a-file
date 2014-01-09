# coding: utf-8
import os

from flask import (
    request, render_template, send_from_directory, redirect, url_for,
    flash,
)
from werkzeug import secure_filename
from flask.ext import uploads as flask_uploads

from . import app
from .utils import is_file_allowed


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/uploads/<filename>')
def show_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route('/self-contained-uploading', methods=['GET', 'POST'])
def upload_file_using_nothing_third_party():
    if request.method == 'POST':
        file_ = request.files['uploading_file']
        if file_ and is_file_allowed(file_.filename):
            filename = secure_filename(file_.filename)
            file_path = os.path.join(app.config['UPLOAD_PATH'], filename)
            file_.save(file_path)
            return redirect(url_for('show_file', filename=filename))
    return render_template('upload.html', menu_basic='active')


photos = flask_uploads.UploadSet('photos', flask_uploads.IMAGES)
flask_uploads.configure_uploads(app, photos)


@app.route('/extension-based-uploading', methods=['GET', 'POST'])
def upload_file_using_extension():
    if request.method == 'POST':
        file_ = request.files['uploading_file']
        if file_:
            try:
                filename = photos.save(file_)
            except flask_uploads.UploadNotAllowed:
                flash('Upload is not allowed.', 'danger')
            else:
                return redirect(url_for('show_file', filename=filename))
    return render_template('upload.html', menu_extension='active')
