from celery import shared_task
from django.template.loader import render_to_string
from common.models import Subscriber
from product.models import Product
from django.db.models import Count
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

from django.conf import settings
from django.core.mail import EmailMessage

@shared_task
def send_subs_mail():
    user_email = Subscriber.objects.values_list('email', flat= True)
    recipes = Product.objects.annotate(Count('comment__content')).order_by('-comment__content__count')[:3]
    subject = ("Most popular recipes of month")
    context = {
        'recipes':recipes,
        "SITE_ADRESS":settings.SITE_ADRESS
    }
    body = render_to_string('emails/email-subscribers.html', context)
    mail = EmailMessage(subject, to=user_email, from_email=settings.EMAIL_HOST_USER, body=body)
    mail.content_subtype = 'html'
    mail.send()


@shared_task
def send_login_mail():
    time = datetime.now() - datetime.timedelta(days=1)
    print(time , "time delta")

    user = User.objects.filter(last_login__lt = time )
    user_email = user['email']
    recipes = Product.objects.annotate(Count('comment__content')).order_by('-comment__content__count')[:3]
    subject = ("Most popular recipes of month")
    context = {
        'recipes':recipes,
        "SITE_ADRESS":settings.SITE_ADRESS
    }
    body = render_to_string('emails/email-subscribers.html', context)
    mail = EmailMessage(subject, to=user_email, from_email=settings.EMAIL_HOST_USER, body=body)
    mail.content_subtype = 'html'
    mail.send()