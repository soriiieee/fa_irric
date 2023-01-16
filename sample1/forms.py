from wtforms.form import Form
from wtforms.fields import (
    StringField,PasswordField, SubmitField
)
from wtforms.validators import DataRequired, Email,EqualTo
from wtforms import ValidationError

# from sample1.models import User

class LoginForm(Form):
    email = StringField("email:",validators = [DataRequired() , Email("メールアドレスが誤っています")])
    password = StringField("password:",validators = [DataRequired()])
    submit = SubmitField("ログイン")


class RegisterForm(Form):
    email = StringField("email:",validators = [DataRequired() , Email("メールアドレスが誤っています")])
    username = StringField("name:",validators = [DataRequired()])
    password = PasswordField("パスワード:",validators = [
        DataRequired() , EqualTo("confirm_password" ,message = "パスワードが違います")])
    confirm_password = PasswordField("確認用(再度入力をしてください)",validators = [DataRequired()])
    submit = SubmitField("登録")
