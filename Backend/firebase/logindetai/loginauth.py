#login using python and firebase to auth user login

import pyrebase
from getpass import getpass
from flask import config

config = { 
  "apiKey": "AIzaSyB3fiImMBNpCXyezj9aFoSEcvs9kRQrFgo",
  "authDomain": "ai-security-login.firebaseapp.com",
  "projectId": "ai-security-login",
  "storageBucket": "ai-security-login.appspot.com",
  "messagingSenderId": "152297271877",
  "appId": "1:152297271877:web:0ee1a22a410746efd8e92c",
  "measurementId": "G-D7QY4KJQPZ",
  "databaseURL": "https://ai-security-login-default-rtdb.firebaseio.com"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def RegisterNewUser():
    email = input("Please enter your email address: \n")
    password = getpass("Please enter your password \n")

    try:
        user = auth.create_user_with_email_and_password(email, password)
        login = auth.send_email_verification_email(login['idToken'])
        print("Success...")
    except:
        print("An account with the provided email address already exists. Please use a different email.")




def Login(email, password):
    login_attempts = 0
    max_attempts = 10
    reset_threshold = 3

    while login_attempts < max_attempts:
        try:
            login = auth.sign_in_with_email_and_password(email, password)
            auth.send_password_reset_email(email)
            print("Success...")
            return
        except:
            login_attempts += 1
            if login_attempts == reset_threshold:
                choice = input("You have reached the maximum login attempts. Do you want to reset your password? (yes/no) \n")
                if choice.lower() == "yes":
                    auth.send_password_reset_email(email)
                    print("A password reset email has been sent to your email address.")
                else:
                    print("Login failed. Please contact support for further assistance.")
                    return
            elif login_attempts == max_attempts:
                print("You have reached the maximum number of login attempts. Please contact support for further assistance.")
                return
            else:
                print("Invalid credentials. Please try again.")
                password = getpass("Please enter your password \n")






