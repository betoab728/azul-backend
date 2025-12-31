import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config.settings import settings

class GmailEmailService:

    async def enviar_email(self, to_email: str, subject: str, html_content: str):

        if not settings.SMTP_USER or not settings.SMTP_PASSWORD:
            print("credenciales SMTP no configurado")
            return
        
        if not all([
            settings.SMTP_HOST,
            settings.SMTP_PORT,
            settings.SMTP_USER,
            settings.SMTP_PASSWORD
        ]):
            print("SMTP incompleto, no se envía email")
            return


        msg = MIMEMultipart("alternative")
        msg["From"] = f"{settings.MAIL_FROM_NAME} <{settings.MAIL_FROM}>"
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(html_content, "html"))

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                server.sendmail(
                    settings.MAIL_FROM,
                    to_email,
                    msg.as_string()
                )
        except Exception as e:
            print("Error enviando email:", e)
