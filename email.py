#from itsdangerous import URLSafeTimedSerializer
#from src import app, mail
#from flask_mail import Message, Mail
#from flask import Flask, app, request, url_for

#https://www.freecodecamp.org/news/setup-email-verification-in-flask-app/
#https://www.youtube.com/watch?app=desktop&v=vF9n248M1yk


#SALT = jdsak
#SEC = config("SALT", default="very-important")

'''def make_token(email):
    serial = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    return serial.dumps(email, salt="email-login")'''

'''def confirm(token, expiration=3600):
    serial = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    try:
        email = serial.loads(token, salt=app.config["SEC"], max_age=expiration)
        return email
    except Exception:
        return False'''
    

'''def confirm_email(user_email, given_email):
    if user_email == given_email:
        return True
    else:
        return False
    
def send_email(to, subject, template, token):
    msg = Message(subject, recipients=[to], html=template, sender=app.config["noreply@flask.com"])
    link = url_for(subject, token=token, _external=True)
    msg.body = "Click on the link: {}".format(link)
    return
    #mail.send(msg)'''

'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>email_confirmation</title>
</head>
<body>
    <div>
        <h1>Email Confirmation</h1>
        <form method="POST" action="/emailing">
            <label for="email">Enter Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <input type="submit" value="Submit">
        </form>
        <form action="/">
            <input type="submit" value="Main Menu">
        </form>
    </div>
</body>
</html>'''
