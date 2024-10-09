import keyring as kr
from flask import request, jsonify
import json

def create_account(username, password, password2):
    #username = input("Enter Username: ")
    #password = input("Enter Password: ")
    #password2 = input("Re-enter your password: ")

    if password != password2:
        #print("Error")
        return "Error"
    
    kr.set_password("ProjectForClass", username, password)
    return "Account Created"

def delete_account(username, password):
    #username = input("Enter Username: ")
    #password = input("Enter Password: ")

    actual_password = kr.get_password("ProjectForClass", username)

    if password == actual_password:
        kr.delete_password("ProjectForClass", username)
    else:
        return "Password is not correct"
    return "Deleted"

def login(username, password):
    #username = input("Enter Username: ")
    #password = input("Enter Password: ")

    actual_password = kr.get_password("ProjectForClass", username)

    if password == actual_password:
        return True
    return "Error"

