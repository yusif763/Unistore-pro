from django.contrib import admin
from django.urls import path,include
from checkout.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name =  "checkout"

urlpatterns = [
    path('checkout/', checkoutpage, name = 'checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



