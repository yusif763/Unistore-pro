from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from account.forms import RegistrationForm, LoginForm , ChangePasswordForm
from account.tasks import send_confirmation_mail
from account.tools.tokens import account_activation_token
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView
)

User = get_user_model()


# class Register(CreateView):
#     form_class = RegistrationForm
    
# def register(request):
#     form = RegistrationForm()
#     print("dadsd")
#     if request.method == 'POST':
#         form = RegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             # http://example.com
#             site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
#             send_confirmation_mail(user_id=user.id, site_address=site_address)
#             messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
#             return redirect(reverse_lazy('common:home'))
#             print("aha")
#     context = {
#         'form': form
#     }
#     print("yoxa")
#     return render(request, 'index.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('common:home'))
    elif user:
        messages.error(request, 'Email is not activated. May be is already activated')
        return redirect(reverse_lazy('account:register'))
    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('account:register'))




def login(request):
    next_page = request.GET.get('next')  # /admin/stories/recipe/1/change/1
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user:
                django_login(request, user)
                messages.success(request, 'Siz ugurla daxil oldunuz')
                if next_page:
                    return redirect(next_page)
                return redirect(reverse_lazy('product:product_list'))
            else:
                messages.success(request, 'Daxil etdiyiniz melumatlar yalnisdir')
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


@login_required
def logout(request):
    django_logout(request)
    messages.success(request, 'Siz cixis etdiniz')
    return redirect(reverse_lazy('product:product_list'))


@login_required
def change_password(request):
    print("dadda")
    next_page = request.GET.get('next')
    form = ChangePasswordForm()
    if request.method == "POST":
        print("adadad")
        form = ChangePasswordForm(data=request.POST)
        if form.is_valid():
            print("qwert")
            oldpassword = form.cleaned_data.get("oldpassword")
            if not request.user.check_password(oldpassword):
                messages.error(request,'Old password is not True')
                return redirect('account:change_password')
            newpassword = form.cleaned_data.get("newpassword2")
            print(newpassword)
            request.user.set_password(newpassword)
            
            request.user.save()
            if next_page:
                return redirect(next_page)
            return redirect(reverse_lazy('product:product_list'))
    context = {
        "form":form,
    }
    return render(request, 'index.html', context)





@login_required
def forgot_password(request):
    print("dadda")
    next_page = request.GET.get('next')
    form = ChangePasswordForm()
    if request.method == "POST":
        print("adadad")
        form = ChangePasswordForm(data=request.POST)
        if form.is_valid():
            print("qwert")
            oldpassword = form.cleaned_data.get("oldpassword")
            if not request.user.check_password(oldpassword):
                messages.error(request,'Old password is not True')
                return redirect('account:change_password')
            newpassword = form.cleaned_data.get("newpassword2")
            print(newpassword)
            request.user.set_password(newpassword)
            
            request.user.save()
            if next_page:
                return redirect(next_page)
            return redirect(reverse_lazy('product:product_list'))
    context = {
        "form":form,
    }
    return render(request, 'index.html', context)