from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from product.models import Product , Category , Review
from django.http import JsonResponse
from product.api.serializers import (
    ProductSerializer,
    ProductCreateSerializer,
    CategorySerializer,
    CategoryCreateSerializer,
    ReviewSerializer,
    ReviewCreateSerializer,
)




class Categories(APIView):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        # permission_classes = [IsAuthenticated]
        category_data = request.data
        serializer = CategoryCreateSerializer(data=category_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetail(APIView):
    def get_object(self, pk):
        if self.request.method == "GET":
            try:
                return Category.objects.get(pk=pk)
            except Category.DoesNotExist:
                raise Http404
        # else:
        #     try:
        #         return Recipe.objects.get(pk=pk, author=self.request.user)
        #     except Recipe.DoesNotExist:
        #         raise Http404

    
    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategoryCreateSerializer(instance=category, data=request.data , context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class Products(APIView):
    def get(self,request,*args,**kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        # permission_classes = [IsAuthenticated]
        product_data = request.data
        serializer = ProductCreateSerializer(data=product_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get_object(self, pk):
        if self.request.method == "GET":
            try:
                return Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                raise Http404
        # else:
        #     try:
        #         return Recipe.objects.get(pk=pk, author=self.request.user)
        #     except Recipe.DoesNotExist:
        #         raise Http404

    
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductCreateSerializer(instance=product, data=request.data , context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







class Reviews(APIView):
    def get(self,request,*args,**kwargs):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        permission_classes = [IsAuthenticated]
        review_data = request.data
        serializer = ReviewCreateSerializer(data=review_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewDetail(APIView):
    def get_object(self, pk):
        if self.request.method == "GET":
            try:
                return Review.objects.get(pk=pk)
            except Review.DoesNotExist:
                raise Http404
        # else:
        #     try:
        #         return Recipe.objects.get(pk=pk, author=self.request.user)
        #     except Recipe.DoesNotExist:
        #         raise Http404

    
    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewCreateSerializer(instance=review, data=request.data , context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET','POST'])
# def product(request):
#     if request.method == 'POST':
#         product_data = request.data
#         serializer = ProductCreateSerializer(data=product_data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     products = Product.objects.filter()
#     serializer = ProductSerializer(products, many=True, context={'request': request})
#     return Response(serializer.data)



# @api_view(['GET','PUT','DELETE'])
# def product_detail(request,pk):
#     product_instance = Product.objects.get(pk=pk)
#     if request.method == "GET":
#         serializer = ProductSerializer(product_instance)
#         return Response(serializer.data)


#     elif request.method == "PUT":
#         serializer = ProductCreateSerializer(product_instance, data = request.data,partial=True , context = {'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status= status.HTTP_201_CREATED)

#     elif request.method == "DELETE":
#         product_instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET','POST'])
# def category_list(request):
#     if request.method == 'POST':
#         category_data = request.data
#         serializer = CategoryCreateSerializer(data=category_data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     categories = Category.objects.filter()
#     serializer = CategorySerializer(categories, many=True, context={'request': request})
#     return Response(serializer.data)



# @api_view(['GET','PUT','DELETE'])
# def category(request,pk):
#     category_instance = Category.objects.get(pk=pk)
#     if request.method == "GET":
#         serializer = CategorySerializer(category_instance)
#         return Response(serializer.data)


#     elif request.method == "PUT":
#         serializer = CategoryCreateSerializer(category_instance, data = request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status= status.HTTP_201_CREATED)

#     elif request.method == "DELETE":
#         category_instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



