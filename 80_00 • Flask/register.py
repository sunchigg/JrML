# -*- coding: utf-8 -*-
"""
http://127.0.0.1:5000/register
"""
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)
app.config["SECRET_KEY"] = "register_key"  # 避免 RuntimeError: A secret key is required to use CSRF.


class RegisterForm(FlaskForm):
    """自定義註冊表單類型
    """
    # {{ form.user_name.label }} @register.html
    user_name = StringField(label=u"用戶名", \
        validators=[DataRequired(u"用戶名不可為空")])
    """ in validators:
    {% for msg in form.user_name.errors %}
    <p>{{ msg }}</p>
    {% endfor %}
    @register.html
    """
    password = PasswordField(label=u"密碼", validators=[DataRequired(u"密碼不能為空")])
    password2 = PasswordField(label=u"確認密碼", validators=[DataRequired(u"確認密碼不能為空"), EqualTo("password", u"再次密碼不一致")])


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    """
    context = {
        'developer': {
            'name': 'Francislin'
        }
    }  # 這是demo用字典收變量
    form = RegisterForm()
    if form.validate_on_submit():
        uname = form.user_name.data
    return render_template("register.html", form=form, context=context)


@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
