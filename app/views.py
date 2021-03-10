# coding:utf8
from app import app
from flask import Flask, url_for, request, render_template, flash, redirect, flash, send_from_directory, send_file
from .forms import UploadForm, AdminLoginForm
from .pictureEntry import EntryMetadataLoader, EntryMetadata
from subprocess import call
from flask_uploads import configure_uploads, IMAGES, UploadSet
from werkzeug.utils import secure_filename
from markupsafe import escape
from .customisationLoader import CustomisationLoader


from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import secrets

# file extensions
VIDEOS = ("AVCHD", "AVI", "FLV", "MKV", "MOV", "MP4", "WEBM", "WMV")
allowedUploads = UploadSet('images', IMAGES + VIDEOS)
configure_uploads(app, allowedUploads)

# login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin"

settings = CustomisationLoader().conf


class User(UserMixin):
    def __init__(self):
        self.id = 1
        self.name = app.config['ADMIN_USERNAME']
        self.password = app.config['ADMIN_PASSWORD']


# upload site
@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()


    filename = ""  # zeigt filename nach upload an
    prevErg = False  # zeigt erfolgsbanner an

    if form.validate_on_submit():
        print(form.image.data)

        entry = EntryMetadata(str(form.email.data), str(form.name.data), str(
            form.aufnahmedatum.data), str(form.beschreibung.data), form.image.data)
        entry.save()

        filename = secure_filename(form.image.data.filename)
        prevErg = True  # f'Filename: {filename}' + ''
    return render_template('upload.html', form=form, filename=filename, prevErg=prevErg, title=settings.title)


# administration
@app.route('/admin', methods=['GET', 'POST'])
def listAllFiles():

    form = AdminLoginForm()
    loginFail = False
    if form.validate_on_submit():

        if request.method == "POST":
            username = form.username.data
            password = form.password.data

            # sicheres vergleichen
            if secrets.compare_digest(username, app.config['ADMIN_USERNAME']) \
                    and secrets.compare_digest(password, app.config['ADMIN_PASSWORD']):
                user = User()
                login_user(user)

                loader = EntryMetadataLoader()
                data = loader.loadeAll()
                return render_template('allUploads.html', data=data)
            else:
                loginFail = True

    return render_template('login.html', form=form, loginFail=loginFail)


@app.route('/img/<path:filename>')
def download_file(filename):
    # get upload directory without "app" in the begining
    path = app.config['UPLOADED_IMAGES_DEST'].split("/", 1)[1]
    return send_file(path + filename)


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User()

# somewhere to logout


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return  redirect("/admin")
