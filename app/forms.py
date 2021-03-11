#coding:utf8
from app import app
from flask_wtf import FlaskForm, Form
from wtforms import StringField,PasswordField, SubmitField, BooleanField, DecimalField, IntegerField, FileField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional
from flask_uploads import UploadSet, IMAGES
from .customisationLoader import CustomisationLoader
from pprint import pprint

class UploadFormFactory():



    
    def getForm(self):
        class F(UploadForm):
            pass

        formData = CustomisationLoader().conf.form
        allowedUploads = UploadSet('images', tuple(formData.file.fileTypes))

        print(formData.__dict__.keys())

        for formFieldName in formData.__dict__.keys():
            formFieldData = formData.__dict__[formFieldName]
            formFieldObj = None
            if formFieldData.meta.type == "string":
                formFieldObj = StringField( formFieldData.label, [Length(min=0, max=50,message=formFieldData.errorLength),DataRequired(formFieldData.errorReqired)])
            elif formFieldData.meta.type == "email":
                formFieldObj = StringField(formFieldData.label,  [DataRequired(formFieldData.errorReqired), Email(formFieldData.errorValidation)]) 
            elif formFieldData.meta.type == "date":
                formFieldObj = DateField(formFieldData.label ,validators=[Optional()])
            elif formFieldData.meta.type == "text":
                formFieldObj = TextAreaField(formFieldData.label % {"maxLength":formFieldData.maxLength}, [Length(min=0, max=formFieldData.maxLength, message=formFieldData.errorLength)])
            elif formFieldData.meta.type == "file":
                formFieldObj = FileField(formFieldData.label  %  {"size":formFieldData.maxSize ,  "types":str(formFieldData.fileTypes) },validators=[\
                    FileRequired(formFieldData.errorReqired),\
                    FileAllowed(allowedUploads, formFieldData.errorType % {  "types":str(formFieldData.fileTypes) } )])
            elif formFieldData.meta.type == "check":
                formFieldObj = BooleanField( formFieldData.label ,validators=[DataRequired(formFieldData.errorReqired)])
            elif formFieldData.meta.type == "submit":
                formFieldObj = SubmitField(formFieldData.label)
            else:
                formFieldObj = StringField("err")

            setattr(F,formFieldName,formFieldObj)

        form = F()


        #form = UploadForm()
        #form.__setitem__(name="test", value= StringField( "test",validators=[DataRequired("reqired")]) )
        return form


class UploadForm(FlaskForm):

    class Meta:
       def render_field(self, field, render_kw):
            render_kw.setdefault('required', False)
            return super().render_field(field, render_kw)



class AdminLoginForm(FlaskForm):
    username = StringField('Username', [Length(min=0, max=50),DataRequired("Bitte feld ausfüllen!")])
    password = PasswordField('Password', [Length(min=0, max=50),DataRequired("Bitte feld ausfüllen!")])
    submit = SubmitField('Login')
