import requests
import os


class EmailService():
    @staticmethod
    def send_email(to, subject: str, body: str, html):
        domain = os.getenv("MAILGUN_DOMAIN")

        return requests.post(
            f"https://api.mailgun.net/v3/{domain}/messages",
            auth=("api", os.getenv("MAILGUN_API_KEY")),
            data={"from": f"FlaskAPI Admin <mailgun@{domain}>",
                  "to": [to],
                  "subject": subject,
                  "text": body,
                  "html": html
                  })
