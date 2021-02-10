#coding:utf8
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, DecimalField, IntegerField, FileField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional
from flask_uploads import UploadSet, IMAGES#, VIDEOS

VIDEOS = ("AVCHD","AVI","FLV","MKV", "MOV","MP4","WEBM","WMV")+("avchd","avi","flv","mkv", "mov","mp4","webm","wmv")
allowedUploades = UploadSet('images', IMAGES + VIDEOS)


class UploadeForm(FlaskForm):

    class Meta:
       def render_field(self, field, render_kw):
            render_kw.setdefault('required', False)
            return super().render_field(field, render_kw)

    
    name = StringField('Name/Spitzname des Fotografen: Wird veröffentlicht wenn das Foto verwendet wird. (Pflichtfeld)', [Length(min=0, max=50),DataRequired("Bitte Namen angeben!")])
    email = StringField('Email: (Pflichtfeld wird nicht veröffentlicht)',  [DataRequired("Bitte Email-Addresse angeben!"), Email("Für eine eventuelle Kontaktaufnahme wird eine gültige Email-Adresse benötigt.")])
    aufnahmedatum = DateField('Aufnahmedatum: (sofern bekannt)' ,validators=[Optional()])##validator not working
    beschreibung = TextAreaField('Beschreibung: des Fotos' , [Length(min=0, max=500)] )
    image = FileField('Foto/Video nicht größer als ' +  str( int(app.config['MAX_CONTENT_LENGTH']/1024/1024)) +  "MegaByte." + " Erlaubte Formate sind:"  + str(IMAGES +VIDEOS) ,validators=[FileRequired("Bitte wählen Sie ein Bild zum hochladen aus."),FileAllowed(allowedUploades, 'Es sint lediglich Bilder/Videos der folgenden Formate erlaubt:' + ' Bilder: ' +  str(IMAGES + VIDEOS) + ' Videos: ' )])
    legal = BooleanField( 'Ich besitze die Rechte an diesem Bild und gebe es hiermit zur Veröffentlichung und Bearbeitung frei. Des Weiteren habe ich die Datenschutzbestimmungen gelesen.*' ,validators=[DataRequired('Das Bild wird nur angenommen, wenn Sie der Erklärung zustimmen!')])
    submit = SubmitField('Speichern')

class AdminLoginForm(FlaskForm):
    username = StringField('Username', [Length(min=0, max=50),DataRequired("Bitte feld ausfüllen!")])
    password = PasswordField('Password', [Length(min=0, max=50),DataRequired("Bitte feld ausfüllen!")])
    submit = SubmitField('Login')
