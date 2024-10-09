import pyotp
import time 
#python3 -m venv path/to/venv
#   source path/to/venv/bin/activate
#  python3 -m pip install xyz

totp = pyotp.TOTP(pyotp.random_base32())
def generate_totp():
    #totp = pyotp.TOTP(pyotp.random_base32())
    hold = totp.now()
    print("Code:")
    print(hold)
    #time.sleep(30)
    #code = input("Enter code: ")
    return #totp.verify(code)
    #print(totp.now())

def verify_totp(code):
    #totp = pyotp.TOTP(pyotp.random_base32())
    #print(totp.verify(code))
    return totp.verify(code)