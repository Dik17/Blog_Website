from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.modules import User



class RegistrationForm(FlaskForm):
    username = StringField('username',
                        validators=[DataRequired(),Length(min=2,max=20)])
    # DataRequired()-to ensure that username cant be empty,Length(min=2,max=20)- to ensur ethat username must be btn 2 and 20 chars
    email=StringField('Email',
                     validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('confirm password',
                                  validators=[DataRequired(),EqualTo('password')])
    Submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken already. please choose a different one')
    def validate_email(self,email):
        Euser=User.query.filter_by(email=email.data).first()
        if Euser:
            raise ValidationError('Account with same email id exists already .please choose differnt email id')









class LoginForm(FlaskForm):
    # DataRequired()-to ensure that username cant be empty,Length(min=2,max=20)- to ensur ethat username must be btn 2 and 20 chars
    email=StringField('Email',
                     validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    Submit=SubmitField('Login')   



class UpdateAccountForm(FlaskForm):
    username = StringField('username',
                        validators=[DataRequired(),Length(min=2,max=20)])
    # DataRequired()-to ensure that username cant be empty,Length(min=2,max=20)- to ensur ethat username must be btn 2 and 20 chars
    email=StringField('Email',
                     validators=[DataRequired(),Email()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])                 
    Submit=SubmitField('Update')

    def validate_username(self,username):
        if username.data!=current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken already. please choose a different one')
    def validate_email(self,email):
        if email.data!=current_user.email:
             Euser=User.query.filter_by(email=email.data).first()
             if Euser:
                raise ValidationError('Account with same email id exists already .please choose differnt email id')

class RequestResetForm(FlaskForm):
    email=StringField('Email',
                     validators=[DataRequired(),Email()])
    Submit=SubmitField('Request Password Reset')

    def validate_email(self,email):
        Euser=User.query.filter_by(email=email.data).first()
        if Euser is None:
            raise ValidationError('No account exist with that email.You must register first.')

class ResetPasswordForm(FlaskForm):
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('confirm password',
                                  validators=[DataRequired(),EqualTo('password')])    
    Submit=SubmitField(' Reset Password')                                      

