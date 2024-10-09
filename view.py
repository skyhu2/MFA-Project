from flask import Flask, Blueprint, render_template, request, jsonify, redirect, url_for
import username_password as up
import timebased as tb
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
        result = up.create_account(username, pwd, pwd2)
        return result
    return render_template("createAccount.html")

@view.route("/delete", methods=['POST', 'GET'])
def deletion():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['pwd']
        result = up.delete_account(username, pwd)
        return result
    return render_template("deleteAccount.html")

@view.route("/totp", methods=['POST', 'GET'])
def time():
    tb.generate_totp()
    if request.method == 'POST':
        code = request.form['code']
        result = tb.verify_totp(code)
        print("After verify")
        return result
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

