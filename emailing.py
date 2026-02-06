import smtplib
import imghdr
from email.message import EmailMessage
import os

PASSWORD = os.getenv("GOOGLE_WEBCAM_TOKEN")
SENDER = "pplctnproject@gmail.com"
RECEIVER = "pplctnproject@gmail.com"

if PASSWORD is None:
    raise RuntimeError("Environment variable GOOGLE_WEBCAM_TOKEN is missing. Please set the environment variable")
def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New object has been detected"
    email_message.set_content("The webcam just detected a new object")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/10.png")