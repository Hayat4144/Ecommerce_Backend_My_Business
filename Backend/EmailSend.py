from django.core.mail import send_mail
from .settings  import EMAIL_HOST_USER
def password_reset_email_send(ValidUser,url):
    subject = 'You are requested for password reset.'
    message = f""""<h2>Hello {ValidUser.values()[0]['full_name']} </h2>
                <p> Here is your password reset link <b> <a>{url}</a></b>"""
    email_from = EMAIL_HOST_USER
    recipient_list = [ValidUser.values()[0]['email'],]
    send_mail(subject, message, email_from, recipient_list)