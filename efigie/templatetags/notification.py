import datetime

from django import template
from django.contrib.auth.models import User
from django.utils import formats
from django.utils.translation import ugettext_lazy as _

from efigie.models import Key, Notification

register = template.Library()

@register.simple_tag
def notificationsBar(user):
  notifs = Notification.objects.filter(user=user, read=False)
  result = []
  for n in notifs:
    r = '<li> <a href="/notifications/#notif%s">' % (n.id)

    if n.category == Notification.Category.FRIEND_I_ACCEPT:
      message = n.message() % {'user': n.send_by()}
    elif n.category == Notification.Category.KEY:
      message = n.message() % {'key':'RSA'}
    else:
      message = n.message()


    r += '<i class="fa %(icon)s text-yellow"></i>' % {'icon': n.icon()}
    r += '%(user)s ' % {'user': n.send_by()} if n.category != Notification.Category.FRIEND_I_ACCEPT else (' ')
    r += '%(message)s </a></li>' % {'message': message}

    result.append(r)

  return result

@register.assignment_tag
def timeline(user):
  notifs = Notification.objects.filter(user=user)
  result = []
  date = None
  for n in notifs:
    created_at = n.created_at - datetime.timedelta(hours=3)

    if date != created_at.date() or date == None:
      date = created_at.date()
      result.append('<li class="time-label"><span class="bg-purple">%s</span></li>' % (date).strftime(formats.get_format('DATE_FORMAT')))

    r = '<li id="notif%s"> ' % (n.id)

    if n.category == Notification.Category.FRIEND_I_ACCEPT:
      message = n.message() % {'user': '<a href="/friend/%s">%s</a>' % (n.send_by().id, n.send_by())}
    elif n.category == Notification.Category.KEY:
      key = Key.objects.get(id=n.notification_id)
      message = n.message() % {'key': '<a href="/key/%s/friend">%s</a>' % (key.id, key)}
    else:
      message = n.message()

    r += '''
      <i class="fa %(icon)s bg-yellow"></i>
      <div class="timeline-item">
        <span class="time"><i class="fa fa-clock-o"></i> %(hour)s</span>
        <h3 class="timeline-header">
      ''' % {
        'icon': n.icon(),
        'hour': created_at.strftime(formats.get_format('TIME_FORMAT')),
      }

    r += '<a href="/friend/%(user_id)s">%(user)s</a> ' % {'user_id': n.send_by().id, 'user': n.send_by()} if n.category != Notification.Category.FRIEND_I_ACCEPT else (' ')
    r += '%(message)s</h3>' % {'message': message}

    if n.category == Notification.Category.FRIEND_ADD:
      r += '''
        <div class="timeline-footer">
          <a class="btn btn-primary btn-sm" href="/friend/%(user_id)s/add/confirm"><i class="fa fa-plus"></i> %(button_accept)s</a>
          <a class="btn btn-danger btn-sm" href="/friend/%(user_id)s/cancel"><i class="fa fa-ban"></i> %(button_delete)s</a>
        </div>
      '''  % {
      'user_id': n.send_by().id,
      'button_accept': _('Accept'),
      'button_delete': _('Delete')}

    r += '</div></li>'

    result.append(r)

  return result
