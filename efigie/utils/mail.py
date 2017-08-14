import requests

from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

import efigie.config as config

def sendMailTemplate(subject, context, recipient_list,from_email=settings.DEFAULT_FROM_EMAIL, fail_silently=False):
  template_name = 'user_password_reset_mail.html' #AGARD
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
  else:
    sendMailbyIFTTT(recipient_list, context['name'], context['confirmation_url'])



def sendMailbyIFTTT(emailList, name, link):

  # curl -X POST -H "Content-Type: application/json" -d
  #  '{"value1":"email@email.com","value2":"NameXX","value3":"http://url.com.br"}'
  # https://maker.ifttt.com/trigger/efigie_new/with/key/IFTTT_KEY

  url  = 'https://maker.ifttt.com/trigger/efigie_new/with/key/%s' % (config.IFTTT_KEY)
  date = {'value1': emailList,'value2': name, 'value3': link }
  headers = {}

  try:
    res = requests.post(url, data=date, headers=headers)
    if res.status_code == requests.codes.ok:
      return True
  except Exception as e:
    return False
  return False
