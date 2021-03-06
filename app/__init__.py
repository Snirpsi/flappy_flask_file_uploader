#coding:utf8
from flask import Flask
from .customisationLoader import CustomisationLoader

settings = CustomisationLoader().conf

app = Flask(__name__)

app.config['ADMIN_USERNAME'] = settings.username
app.config['ADMIN_PASSWORD'] = settings.password    #change this!
app.config['SECRET_KEY'] = settings.secret #change this!
app.config['UPLOADED_IMAGES_DEST'] = 'app/static/uploads/images/' #upload location
app.config['MAX_CONTENT_LENGTH'] = (settings.form.file.maxSize + 10)* 1024 * 1024 #max upload file size


from app import views