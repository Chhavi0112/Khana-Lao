from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def detectUser(user):
    if user.role == 1:
        redirectUrl = 'restDashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'custDashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl


# def send_verification_email(request, user):
#     current_site = get_current_site(request)
#     sub = "Activate Your Account"
#     message = render_to_string('accounts/email/email_verification.html', {
#         'user': user,
#         'domain': current_site,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': default_token_generator.make_token(user)
#     })
#     to_email = user.email
#     mail = EmailMessage(sub, message, to=[to_email])
#     mail.send()
