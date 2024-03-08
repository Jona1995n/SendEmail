import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = input("Enter your outlook email: ")
PASSWORD = getpass.getpass("Enter password: ")
TO_EMAIL = input("Enter receiving email: ")
SUBJECT = input("Enter the subject: ")

message = MIMEMultipart("alternative")
message['Subject'] = SUBJECT
message['From'] = FROM_EMAIL
message['To'] = TO_EMAIL
message['Cc'] = FROM_EMAIL
message['Bcc'] = FROM_EMAIL

body = input("Enter Body: ")

html_part = MIMEText(body, 'plain')
message.attach(html_part)

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
smtp.quit()