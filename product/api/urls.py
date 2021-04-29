from django.urls import path
from product.api.views import ProductDetail , Products,CategoryDetail,Categories,Reviews,ReviewDetail
app_name =  "productapis"

urlpatterns = [
    path('product/', Products.as_view(), name='product_api'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail_api'),
    path('category/', Categories.as_view(), name='category_api'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail_api'),
    path('reviews/', Reviews.as_view(), name='review_api'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review_detail_api'),
]