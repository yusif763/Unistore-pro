from django.contrib import admin
from django.urls import path,include
from common.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name =  "common"

urlpatterns = [
    path('blog/', BlogListView.as_view() , name = 'blog'),
    path('faq/', faq_page , name = 'faq'),
    path('', home_page , name = 'home'),
    path('item-photo/<int:pk>' , BlogDetailView.as_view() , name='blog_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



