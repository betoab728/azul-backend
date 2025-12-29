#import os
from app.config.settings import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from fastapi import HTTPException
from fastapi.concurrency import run_in_threadpool


class EmailService:

    def __init__(self):
        self.from_name = settings.MAIL_FROM_NAME
        self.api_key = settings.SENDGRID_API_KEY
        self.from_email = settings.MAIL_FROM
        

         # Verificar que la clave API esté configurada
        if not self.from_name:
            print("WARNING: MAIL_FROM_NAME no configurado, los emails no se enviarán.")
            #raise RuntimeError("MAIL_FROM_NAME no configurado")

        if not self.from_email:
            print("WARNING: MAIL_FROM no configurado, los emails no se enviarán.")
            #raise RuntimeError("MAIL_FROM no configurado")

        if not self.api_key:
            print("WARNING: SENDGRID_API_KEY no configurado, los emails no se enviarán 19.")
            #raise RuntimeError("SENDGRID_API_KEY no configurado")

    async def enviar_email(
        self,
        to_email: str,
        subject: str,
        html_content: str
    ):  
        if not self.api_key:
            print("SENDGRID_API_KEY no configurado, no se envía el email, regresando...")
            return

        message = Mail(
            from_email=(self.from_email, self.from_name),
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )

        try:
            sg = SendGridAPIClient(self.api_key)
            await run_in_threadpool(sg.send, message)
        except Exception as e:
            print("Error enviando email:", e)