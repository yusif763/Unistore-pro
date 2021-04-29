from django.template import Library
from common.forms import SubscriberForm,CommentForm
from product.forms  import ReviewForm
from account.forms import RegistrationForm , LoginForm , ChangePasswordForm

register = Library()


@register.simple_tag
def get_comment():
    return ReviewForm()


@register.simple_tag
def get_subs():
    return SubscriberForm()



@register.simple_tag
def get_blog_comment():
    return CommentForm()

@register.simple_tag
def get_register():
    return RegistrationForm()

@register.simple_tag
def get_login():
    return LoginForm()


@register.simple_tag
def get_change():
    return ChangePasswordForm()