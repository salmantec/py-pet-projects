import smtplib
import os
from email.mime.text import MIMEText

def send_reminder(email, password, recipient, message):
    # Get email and password from env var
    email = os.environ.get("YOUR_EMAIL")
    password = os.environ.get("YOUR_PASSWORD")

    # Check email and password are provided
    if not email or not password:
        raise ValueError("Email and Password must be provided")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)

    msg = MIMEText(message)
    msg["Subject"] = "Reminder"
    msg["From"] = email
    msg["To"] = recipient

    server.sendmail(email, recipient, message.as_string())
    server.quit()

recipient = "receiver_mail@gmail.com"
message = "Remember to complete your tasks for today!"

# Ensure your email and password are set as env var
send_reminder(email=None, password=None, recipient=recipient, message=message)