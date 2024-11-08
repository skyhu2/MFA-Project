from itsdangerous import URLSafeTimedSerializer
#from src import app, mail
from flask_mail import Message, Mail
from flask import Flask, request, url_for
import main

#https://www.freecodecamp.org/news/setup-email-verification-in-flask-app/
#https://www.youtube.com/watch?app=desktop&v=vF9n248M1yk

#SALT = jdsak
#SEC = config("SALT", default="very-important")
#app = Flask(__name__)
mail = Mail(main.app)

main.app.config['MAIL_DEFAULT_SENDER'] = "noreply@flask.com"
main.app.config['MAIL_SERVER'] = "smtp.gmail.com"
main.app.config['MAIL_PORT'] = 465
main.app.config['MAIL_USE_TLS'] = False
main.app.config['MAIL_USE_SSL'] = True
#main.app.config['MAIL_DEBUG'] = False
main.app.config['MAIL_USERNAME'] = "noreply@flask.com"
main.app.config['MAIL_PASSWORD'] = "EMAIL_PASSWORD"

def make_token(email):
    serial = URLSafeTimedSerializer("hihhgftydsesvf")
    return serial.dumps(email, salt="email-login")

'''def confirm(token, expiration=3600):
    serial = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    try:
        email = serial.loads(token, salt=app.config["SEC"], max_age=expiration)
        return email
    except Exception:
        return False'''
    

def confirm_email(username, given_email):
    given_email = given_email.strip()
    fin = open("UserInfo.txt", "r")
    for line in fin:
        (user, user_email) = line.split(" ", 1)
        if user == username:  
            user_email = user_email.strip()
            if user_email == given_email:
                return True
    return False
    
def send_email(to, token):
    #msg = Message("Email", recipients=[to], html=template, sender="noreply@flask.com")
    msg = Message("Email", sender="noreply@flask.com", recipients=[to])
    link = url_for("view.complete", token=token, _external=True)
    msg.body = "Click on the link: {}".format(link)
    #mail.send(msg)
    return
