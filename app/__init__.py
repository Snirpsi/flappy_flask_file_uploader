#coding:utf8
from flask import Flask
app = Flask(__name__)
app.config['ADMIN_USERNAME'] = "admin"
app.config['ADMIN_PASSWORD'] = "changePassword!!!"     #change this!
app.config['SECRET_KEY'] = 'insertSuperRandomSecretString' #change this!
app.config['UPLOADED_IMAGES_DEST'] = 'app/static/uploads/images/' #uploade location
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024 #max uploade file size


from app import views