from django.contrib import admin
from django.urls import path,include
from product.views import ProductDetailView , ProductListView
from django.conf import settings
from django.conf.urls.static import static

app_name =  "product"

urlpatterns = [
    path('product-list/', ProductListView.as_view() , name = 'product_list'),
    path('product/<int:pk>/' , ProductDetailView.as_view(), name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



