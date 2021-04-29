from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from checkout.models import Payment,CheckOut , OrderItem
from product.models import Product
from checkout.api.serializers import PaymentSerializer,CheckOutSerializer , OrderItemCreateSerializer,OrderItemSerializer
from rest_framework.generics import get_object_or_404


# @api_view(['GET', 'POST'])
# def payment_list_create_api_view(request):
    
#     if request.method == 'GET':
#         payments = Payment.objects.all()   # obyektlerden yaradilmis queryset
#         serializer = PaymentSerializer(payments, many = True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PaymentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status= status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET', "PUT", "DELETE"])
# def payment_detail_api_view(request , pk):
#     try:
#         payment_instance = Payment.objects.get(pk=pk)
#     except Payment.DoesNotExist:
#         return Response(
#             {
#                 "errors":{
#                     "code":404,
#                     "message":"Bele bir Odenish novu yoxdur."
#                 }
#         },
#         status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = PaymentSerializer(payment_instance)
#         return Response(serializer.data)


#     elif request.method == 'PUT':
#         serializer = PaymentSerializer(payment_instance, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status= status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)



#     elif request.method == "DELETE":
#         payment_instance.delete()
#         return Response(
#             {
#                 "errors":{
#                     "code":204,
#                     "message":"Bu usulu sildiniz!"
#                 }
#         },
#             status= status.HTTP_204_NO_CONTENT
#         )



class OrderItemListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        orders = OrderItem.objects.filter(author = self.request.user , completed = False)
        serializer = OrderItemSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        order_data = request.data
        product_id = order_data['product'] 
        product = Product.objects.filter(id = product_id).first()
        basket = OrderItem.objects.filter(product = product, author = request.user,completed = False ).first()

        serializer = OrderItemCreateSerializer(data=order_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if basket:
            basket.count = order_data['count']
            basket.save()
        else:
            serializer.save(product=product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request , *args , **kwargs):
        print(request, 'patch')

   

class OrderItemDetail(APIView):
    def get_object(self, pk):
        if self.request.method == "GET":
            try:
                return OrderItem.objects.get(pk=pk)
            except OrderItem.DoesNotExist:
                raise Http404
        # else:
        #     try:
        #         return Recipe.objects.get(pk=pk, author=self.request.user)
        #     except Recipe.DoesNotExist:
        #         raise Http404

    
    def get(self, request, pk):
        order_item = self.get_object(pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)

    def put(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        serializer = OrderItemCreateSerializer(instance=order_item, data=request.data , context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentListCreateAPIView(APIView):
    
    def get(self,request):
        payments = Payment.objects.all()   # obyektlerden yaradilmis queryset
        serializer = PaymentSerializer(payments, many = True, context={'request': request})
        return Response(serializer.data)


    def post(self,request):
        serializer = PaymentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# class CheckOutListCreateAPIView(APIView):
#     def get(self,request):
#         checks = CheckOut.objects.all()   # obyektlerden yaradilmis queryset
#         serializer = CheckOutSerializer(checks, many = True)
#         return Response(serializer.data)


#     def post(self,request):
#         serializer = CheckOutSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status= status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# class CheckOutDetailAPIView(APIView):

#     def get_object(self,pk):
#         checkout_instance = get_object_or_404(CheckOut , pk = pk)
#         return checkout_instance

#     def get(self,request,pk):
#         checkout = self.get_object(pk = pk)
#         serializer = CheckOutSerializer(checkout)
#         return Response(serializer.data)
    

#     def put(self,request,pk):
#         checkout = self.get_object(pk =pk)
#         serializer = CheckOutSerializer(checkout,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,pk):
#         checkout = self.get_object(pk = pk)
#         checkout.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
