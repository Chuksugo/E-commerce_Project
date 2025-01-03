from rest_framework import serializers
from .models import Order
from products.models import Product

class OrderCreateSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)
    status = serializers.ChoiceField(choices=Order.STATUS_CHOICES, default='reserved')

    class Meta:
        model = Order
        fields = ['product_id', 'quantity', 'status']

    def validate_product_id(self, value):
        try:
            # Validate if the product exists
            product = Product.objects.get(id=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found.")
        return value

    def create(self, validated_data):
        # Retrieve the product based on validated product_id
        product = Product.objects.get(id=validated_data['product_id'])

        # Create the order with the product and other data
        order = Order.objects.create(
            product=product,
            quantity=validated_data['quantity'],
            status=validated_data['status']
        )
        return order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'status', 'created_at'] 