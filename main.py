import username_password
import timebased
import emailing
from flask import Flask
from view import view

app = Flask(__name__)
app.register_blueprint(view, url_prefix="/")


#@app.route('/')
#def home():
    #return

#def main():
    #username_password.create_account()
    #print(username_password.login())
    #timebased.generate_totp()
    #return

if __name__ == "__main__":
    app.run(debug=True)
