import keyring as kr
from flask import request, jsonify
import json
import os

def create_account(username, password, password2, email, finger):

    if password != password2:
        return False
    fin = open("UserInfo.txt", "a+")
    fin.seek(0, os.SEEK_END)
    if fin.tell != 0:
        fin.seek(os.SEEK_END, 0)
        for line in fin:
            #print(line)
            user = line.split(" ", 1)
            print(user)
            if user[0] == username:
                return "username"
    kr.set_password("ProjectForClass", username, password)
    new = json.dumps(finger)
    fin.write("%s %s\n" %(username, email))
    fin.close()
    return True

def delete_account(username, password):
    actual_password = kr.get_password("ProjectForClass", username)

    if password == actual_password:
        kr.delete_password("ProjectForClass", username)
        fout = open("UserInfo.txt", "r")
        fin = open("holder.txt", "w")
        for line in fout:
            user = line.split(" ", 1)
            if user[0] != username:
                fin.write(line)
        fout.close()
        fin.close()
        fout = open("UserInfo.txt", "w")
        fin = open("holder.txt", "r")
        for line in fin:
            fout.write(line)
    else:
        return False
    return True

def login(username, password):
    actual_password = kr.get_password("ProjectForClass", username)

    if password == actual_password:
        return True
    return "Error"

