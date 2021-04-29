from django.urls import path
from account.api import views as api_views
from account.api.views import CustomAuthToken , registration_view , ChangePasswordView

app_name =  "account-api"


urlpatterns = [
    path('login/',CustomAuthToken.as_view(), name='token'),
    path('register/', api_views.registration_view , name = 'register-api'),
    path('change/', ChangePasswordView.as_view() , name = 'change-api'),
] 