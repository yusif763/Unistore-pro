from django.urls import path, re_path,include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from account.views import activate, login, logout, change_password

app_name = 'account'

urlpatterns = [
    # path('register/', register, name='register'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
    #         activate, name='activate'),
    # path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('reset-password/', 
        auth_views.PasswordResetView.as_view(
        template_name="reset/password_reset.html",
        email_template_name = 'reset/password_reset_email.html',
        success_url = reverse_lazy('account:password_reset_done')),
        name='reset_password'),
    path('reset-password-done/', 
        auth_views.PasswordResetDoneView.as_view(template_name="reset/password_reset_done.html"), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="reset/password_reset_confirm.html",
        success_url = reverse_lazy('account:password_reset_complete')),
        name='password_reset_confirm'),
    path('reset-password-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="reset/password_reset_complete.html"),
        name='password_reset_complete'),
]