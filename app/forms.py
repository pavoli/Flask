# coding: utf-8
__author__ = 'polly'

'''

'''

from flask_wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, StringField, FileField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname


class FindVacancy(Form):
    search = StringField('search')
    submit = SubmitField('Find...')


class PictureList(Form):
    upload = FileField('...')
    save = SubmitField('Save')