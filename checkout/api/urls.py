from django.urls import path
from checkout.api.views import OrderItemListAPIView, OrderItemDetail
app_name =  "checkapis"

urlpatterns = [
    # path('', api_views.payment_list_create_api_view , name = 'checkout-api'),
    # path('<int:pk>', api_views.payment_detail_api_view , name = 'check-apidetail'),
    path('orders/', OrderItemListAPIView.as_view() , name = 'order-api'),
    path('orders/<int:pk>/', OrderItemDetail.as_view() , name = 'order-api'),
    # path('payment', PaymentListCreateAPIView.as_view() , name = 'payment-api'),
    # path('checkout', CheckOutListCreateAPIView.as_view() , name = 'checkout-api'),
    # path('checkout/<int:pk>', CheckOutDetailAPIView.as_view() , name = 'check-apidetail'),
] 