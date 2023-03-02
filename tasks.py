import jinja2
from dotenv import load_dotenv
from services import EmailService

load_dotenv()

template_loader = jinja2.FileSystemLoader('templates')
template_env = jinja2.Environment(loader=template_loader)


def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)


def send_user_registration_email(email, username):
    return EmailService.send_email(
        email,
        "Welcome to Flask REST API",
        f"Hi! {username}, you have successfully signed up to the Flask Stores API!",
        render_template("email/welcome.html", username=username)
    )
