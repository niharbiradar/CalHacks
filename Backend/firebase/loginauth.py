#login using python and firebase to auth user login
from getpass import getpass
import pyrebase

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

email = input("Please enter your email address: \n")
password = getpass("Please enter your password \n")

#user = auth.create_user_with_email_and_password(email, password)

login = auth.sign_in_with_email_and_password(email, password)

#auth.send_password_reset_email(email)

#auth.send_email_verification_email(login['idToken'])
print("Success...")





