from rest_framework import serializers
from .models import Wishlist, WishlistItem
from products.serializers import ProductSerializer  # Assuming you have a ProductSerializer

class WishlistItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = WishlistItem
        fields = ['id', 'product', 'added_at']

class WishlistSerializer(serializers.ModelSerializer):
    items = WishlistItemSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'name', 'items']
