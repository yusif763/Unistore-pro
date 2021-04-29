from rest_framework import serializers
from product.models import Product , Tag , ScreenSize , Category , Review , Image
from django.contrib.auth import  get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'image',
            'username',
            'email',
            'bio',
            'gender'
        ]

class ScreenSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenSize
        fields = [
            'id',
            'size'
        ]



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'tags'
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'image'
        ]

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.types')
    brand = serializers.CharField(source='brand.brand')
    screensize = ScreenSizeSerializer(many = True)
    taglar = TagSerializer(many=True)
    images = serializers.SerializerMethodField()
    endirim = serializers.ReadOnlyField()
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id',
            'short_title',
            'price',
            'faiz',
            'slug',
            'full_title',
            'description',
            'main_image',
            'created_at',
            'category',
            'brand',
            'screensize',
            'taglar',
            'endirim',
            'images',
            'comment'
        ]
    def get_images(self,obj):
        images = obj.productimages.all()
        # reply = Comment.objects.get_or_create(=obj)
        return ImageSerializer(images, many =True).data

    def get_comment(self,obj):
        # comment = obj.productsreview.all()
        # reply = Comment.objects.get_or_create(=obj)
        return ReviewSerializer(obj.productsreview.filter(parent_comment__isnull=True), many =True).data

class ProductCreateSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'short_title',
            'price',
            'faiz',
            'slug',
            'full_title',
            'description',
            'main_image',
            'created_at',
            'category',
            'brand',
            'screensize',
            'taglar',
        ]
    

    def get_comment(self,obj):
        images = obj.productimages.all()
        # reply = Comment.objects.get_or_create(=obj)
        return ImageSerializer(images, many =True).data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'types',
        ]


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'types',
        ]





# class ReplyReviewSerializer(serializers.ModelSerializer):
#     product = serializers.CharField(source='product.title')
#     author = UserSerializer()
#     # parent_comment = CommentSerializer(read_only= True)
#     class Meta:
#         model = Review
#         fields = [
#             'id',
#             'product',
#             'author',
#             'parent_comment',
#             'full_name',
#             'email',
#             'comment',    
#         ]

class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.short_title')
    author = UserSerializer()
    reply = serializers.SerializerMethodField()
    # parent_comment = CommentSerializer(many = True , read_only= True)
    class Meta:
        model = Review
        fields = [
            'id',
            'product',
            'author',
            'parent_comment',
            'full_name',
            'email',
            'comment',
            'reply',
        ]

    def get_reply(self,obj):
        reply = obj.sub_reviews.all()
        # reply = Comment.objects.get_or_create(=obj)
        return ReviewSerializer(reply , many =True).data




class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'product',
            'author',
            'parent_comment',
            'full_name',
            'email',
            'comment',
        ]