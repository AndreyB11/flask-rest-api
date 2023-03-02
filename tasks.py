from dotenv import load_dotenv
from services import EmailService

load_dotenv()


def send_user_registration_email(email, username):
    return EmailService.send_email(
        email,
        "Welcome to Flask REST API",
        f"Hi! {username}, you have successfully signed up to the Flask Stores API!"
    )
