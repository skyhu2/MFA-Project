from flask import Flask, Blueprint, app, render_template, request, jsonify, redirect, url_for
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import username_password as up
import timebased as tb
import emailing as em
import fingerprint as finger
from flask_mail import Message, Mail
import json

view = Blueprint(__name__, "view")

@view.route("/")
def home():
    return render_template("menu.html")

@view.route("/create", methods=['POST', 'GET'])
def creation():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['pwd']
        pwd2 = request.form['pwd2']
        email = request.form['eme']
        fing = finger.createFingerprint(username)
        result = up.create_account(username, pwd, pwd2, email, fing)
        if result == True:
            return render_template("successful_login.html")
        elif result == "username":
            return "Username is already used"
    return render_template("createAccount.html")

@view.route("/delete", methods=['POST', 'GET'])
def deletion():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['pwd']
        result = up.delete_account(username, pwd)
        if result == True:
            return render_template("menu.html")
    return render_template("deleteAccount.html")

@view.route("/totp", methods=['POST', 'GET'])
def time():
    tb.generate_totp()
    if request.method == 'POST':
        code = request.form['code']
        result = tb.verify_totp(code)
        if result == True:
            return render_template("confirm_email.html")
        else:
            return "<p1>Wrong code</p1>"
    return render_template("code.html")

@view.route("/loggedIn", methods=['POST', 'GET'])
def logging_in():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['pwd']
        result = up.login(username, pwd)
        if result == True:
            return redirect(url_for("view.time"))
        return result
    return render_template("login.html")

@view.route("/emailing", methods=['POST', 'GET'])
def emailing():
    #form = RegisterForm(request.form)
    #if form.validate_on_submit():
        #user = User(email=form.email.data, password=form.password.data)
    if request.method == 'POST':
        #token = em.make_token()
        username = request.form['username']
        email = request.form['email']
        result = em.confirm_email(username, email)
        token = em.make_token(email)
        if result == True:
        #url = url_for("view.complete", token = token, _external=True)
        #html = render_template("send_email.html", confirm_url=url)
            em.send_email(email, token)
            return render_template("after_email.html")
        else:
            return render_template("confirm_email.html")
        #else:
            #return redirect(url_for("view.home"))
    return render_template("confirm_email.html")

@view.route("/after_email/<token>")
def after_email(token):
    serial = URLSafeTimedSerializer("hihhgftydsesvf")
    try:
        email = serial.loads(token, salt='email-login', max_age=360)
    except SignatureExpired:
        return '<h1> Token expired </h1>'
    return '<h1> Successfully completed email authorization </h1>'

@view.route("/fingerprint", methods=['POST', 'GET'])
def login_finger():
    if request.method == 'POST':
        user = request.form['username']
        fing = finger.createFingerprint(user)
        finger.verifyFingerprint(fing)
        return render_template("successful_login.html")
    return render_template("requestFingerprint.html")

@view.route("/complete")
def complete():
    return render_template("successful_login.html")
