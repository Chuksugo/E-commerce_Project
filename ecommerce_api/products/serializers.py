from rest_framework import serializers
from .models import Category, Product, Review, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'uploaded_at']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested category serializer
    images = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if data.get('price') <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        if data.get('stock_quantity') < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return data

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'review_text', 'created_at']
        read_only_fields = ['user', 'created_at']
