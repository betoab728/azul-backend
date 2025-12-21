import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from fastapi import HTTPException

class EmailService:

    def __init__(self):
        self.api_key = os.getenv("SENDGRID_API_KEY")
        self.from_email = os.getenv("MAIL_FROM")
        self.from_name = os.getenv("MAIL_FROM_NAME", "Azul Sostenible")

        if not self.api_key:
            raise RuntimeError("SENDGRID_API_KEY no configurado")

    async def enviar_email(
        self,
        to_email: str,
        subject: str,
        html_content: str
    ):
        message = Mail(
            from_email=(self.from_email, self.from_name),
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )

        try:
            sg = SendGridAPIClient(self.api_key)
            sg.send(message)
        except Exception as e:
             print("Error enviando email:", str(e))