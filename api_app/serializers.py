from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')


class UserModelSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()

    # def validate_email(self, value):
    #     lower_email = value.lower()
    #     if get_user_model().objects.filter(email__iexact=lower_email).exists():
    #         raise serializers.ValidationError("Email Already Exists")
    #     return lower_email
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email"]
