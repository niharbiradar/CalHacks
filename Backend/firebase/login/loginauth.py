#login using python and firebase to auth user login
from getpass import getpass
from flask import config
import loginconf
import pyrebase


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

email = input("Please enter your email address: \n")
password = getpass("Please enter your password \n")

#user = auth.create_user_with_email_and_password(email, password)

login = auth.sign_in_with_email_and_password(email, password)

#auth.send_password_reset_email(email)

#auth.send_email_verification_email(login['idToken'])
print("Success...")





