from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings
# import ssl
# import smtplib
# from decouple import config

def detectUser(user):
    if user.role == 1:
        redirectUril = 'vendorDashboard'
        return redirectUril
    elif user.role == 2:
        redirectUril = 'custDashboard'
        return redirectUril
    elif user.role == None and user.is_superadmin:
        redirectUril = '/admin'
        return redirectUril

# email_sender = 'chiiinonsky0009@gmail.com'
# email_password = config('EMAIL_HOST_PASSWORD')

def send_verification_email(request, user, mail_subject, email_template):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    
    message = render_to_string(email_template, {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])

    # context = ssl.create_default_context()

    # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #     smtp.login(email_sender, email_password)
    #     smtp.sendmail(email_sender, to_email, mail)
        
    
    mail.send()

