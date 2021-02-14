#coding:utf8
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, DecimalField, IntegerField, FileField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional
from flask_uploads import UploadSet, IMAGES
from .customisationLoader import CustomisationLoader
from pprint import pprint




class UploadForm(FlaskForm):

    class Meta:
       def render_field(self, field, render_kw):
            render_kw.setdefault('required', False)
            return super().render_field(field, render_kw)
    
    #magicly creates conf object
    texts = CustomisationLoader().conf.form
    allowedUploads = UploadSet('images', tuple(texts.file.fileTypes))
    
    name = StringField( texts.name.label, [Length(min=0, max=50,message=texts.name.errorLength),DataRequired(texts.name.errorReqired)])
    email = StringField(texts.email.label,  [DataRequired(texts.email.errorReqired), Email(texts.email.errorValidation)])
    aufnahmedatum = DateField(texts.recordingDate.label ,validators=[Optional()])##validator not working
    beschreibung = TextAreaField(texts.description.label % {"maxLength":texts.description.maxLength} , [Length(min=0, max=texts.description.maxLength , message=texts.description.errorLength )  ] )
    image = FileField(texts.file.label  %  {"size":texts.file.maxSize ,  "types":str(texts.file.fileTypes) },validators=[\
        FileRequired(texts.file.errorReqired),\
        FileAllowed(allowedUploads, texts.file.errorType % {  "types":str(texts.file.fileTypes) } )])
    legal = BooleanField( texts.legal.label ,validators=[DataRequired(texts.legal.errorReqired)])
    submit = SubmitField(texts.submit.label)

class AdminLoginForm(FlaskForm):
    username = StringField('Username', [Length(min=0, max=50),DataRequired("Bitte feld ausfüllen!")])
    password = PasswordField('Password', [Length(min=0, max=50),DataRequired("Bitte feld ausfüllen!")])
    submit = SubmitField('Login')
