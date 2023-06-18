import os
import base64
import mimetypes
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Email configuration
RECIPIENT_EMAIL = 'recipient@example.com'
SUBJECT = 'Automated No-Reply Email'
IMAGE_FILE = 'image.png'  # Replace with the path to your image file

# Gmail API configuration
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
TOKEN_FILE = 'token.json'  # Replace with the path to your token file
CREDENTIALS_FILE = 'credentials.json'  # Replace with the path to your credentials file

def create_message_with_attachment(sender, to, subject, message_text, file_path=None):
    message = MIMEMultipart()
    message['to'] = to
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    if file_path:
        content_type, encoding = mimetypes.guess_type(file_path)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        with open(file_path, 'rb') as file:
            data = file.read()
        attachment = MIMEImage(data, _subtype=sub_type)
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
        message.attach(attachment)

    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    credentials = flow.run_local_server()
    with open(TOKEN_FILE, 'w') as token:
        token.write(credentials.to_json())

    return build('gmail', 'v1', credentials=credentials)

def send_email(service, message):
    service.users().messages().send(userId='me', body=message).execute()

def main(send_image):
    service = get_authenticated_service()
    if send_image:
        message = create_message_with_attachment('me', RECIPIENT_EMAIL, SUBJECT, '', IMAGE_FILE)
    else:
        message = create_message_with_attachment('me', RECIPIENT_EMAIL, SUBJECT, '')
    send_email(service, message)
    print('Email sent successfully!')

if __name__ == '__main__':
    send_image = True  # Replace with the parameter value (True or False) from the other Python file
    main(send_image)
