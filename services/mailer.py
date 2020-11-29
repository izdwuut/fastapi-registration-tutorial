from smtplib import SMTP
from email.message import EmailMessage
from config.settings import Settings

settings = Settings()


class Mailer:
    @staticmethod
    def send_message(content: str, subject: str, mail_to: str):
        message = EmailMessage()
        message.set_content(content)
        message['Subject'] = subject
        message['From'] = settings.MAIL_SENDER
        message['To'] = mail_to
        SMTP(settings.SMTP_SERVER).send_message(message)

    @staticmethod
    def send_confirmation_message(token: str, mail_to: str):
        confirmation_url = '{}/verify/{}'.format(settings.BASE_URL, token)
        message = '''Hi!

Please confirm your registration: {}.'''.format(confirmation_url)
        Mailer.send_message(
            message,
            'Please confirm your registration',
            mail_to
        )
