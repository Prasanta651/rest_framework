from rest_framework import serializers
from .models import Order, OrderItem, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock'
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0."
            )
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    '''
    When using a nested serializer, ensure the field name matches the `related_name` 
    used in the model for the ForeignKey relationship.
    '''
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = (
            'order_id', 
            'created_at', 
            'user', 
            'status',
            'items'
            )

# class ProductInfoSerializer(serializers.Serializer):
#     products = ProductSerializer(many=True)
#     count = serializers.ImageField()
#     max_price = serializers.FloatField()
    