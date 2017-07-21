from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def sendMailTemplate(subject, context, recipient_list,from_email=settings.DEFAULT_FROM_EMAIL, fail_silently=False):
  template_name = 'user_password_reset_mail.html'
  message_html = render_to_string(template_name, context)
  message_txt = striptags(message_html)
  email = EmailMultiAlternatives(
    subject=subject, body=message_txt, from_email=from_email,
    to=recipient_list
    )
  email.attach_alternative(message_html, "text/html")
  
  # Para evitar que de erro no servidor de teste remoto
  if not 'heroku' in context['confirmation_url']:
    email.send(fail_silently=fail_silently)