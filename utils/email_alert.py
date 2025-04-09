import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

SENDER = os.getenv("ALERT_EMAIL")
PASSWORD = os.getenv("ALERT_EMAIL_PASSWORD")
TO = os.getenv("MANAGER_EMAIL")

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER
    msg['To'] = TO
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, TO, msg.as_string())
        server.quit()
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)
