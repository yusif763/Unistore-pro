from django.contrib import admin
from django.urls import path,include
from contact.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name =  "contact"

urlpatterns = [
    path('about-contact/', AboutContactView.as_view() , name = 'about'),
    path('contact/', ContactView.as_view() , name = 'contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



