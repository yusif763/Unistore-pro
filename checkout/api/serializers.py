from rest_framework import serializers
from checkout.models import Payment , CheckOut , OrderItem
from datetime import datetime
from django.utils.timesince import timesince
from product.api.serializers import ProductSerializer

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
            'gender',

        ]



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    # product = serializers.SerializerMethodField()
    author = UserSerializer()
    # order_count = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'count',
            'product',
            'author',

        ]
    # def get_product(self, obj):
    #     product = obj.product.all()
    #     return ProductSerializer(product, many=True).data

    # def get_order_count(self, obj):
    #     return obj.count()

    



class OrderItemCreateSerializer(serializers.ModelSerializer):
    # product = serializers.SerializerMethodField()
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'count',
            'product',
            'author',
        ]
    # def get_product(self, obj):
    #     product = obj.product.all()
    #     return ProductSerializer(product, many=True).data

    def validate(self, data):
        request = self.context.get('request')
        print(request)
        data['author'] = request.user
        attrs = super().validate(data)
        return attrs




class CheckOutSerializer(serializers.ModelSerializer):
    # payment = PaymentSerializer()
    # author = serializers.StringRelatedField()
    class Meta:
        model = CheckOut
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at' ]

class PaymentSerializer(serializers.ModelSerializer):
    # payments = CheckOutSerializer(read_only=True, many=True)
    payments = serializers.HyperlinkedRelatedField(
        many = True,
        read_only=True,
        view_name = 'checkapis:check-apidetail',
    )
    # time_since_pub = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = '__all__'
        # exclude = ['updated_at' ,]





# class PaymentDefaultSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     payment = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
    


#     def create(self, validated_data):
#         print(validated_data)
#         return Payment.objects.create(**validated_data)

#     def update(self , instance , validated_data):
#         instance.payment = validated_data('payment', instance.payment)
#         instance.created_at = validated_data('created_at', instance.created_at)
#         instance.updated_at = validated_data('updated_at', instance.updated_at)
#         return instance


