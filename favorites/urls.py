from django.contrib import admin
from django.urls import path,include
from favorites.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name =  "favorites"

urlpatterns = [
    path('favorites/' , fav_page , name  = 'favorites'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



