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

    '''
    If we don't include the `items` property in the serializer, 
    it will not automatically serialize the related `OrderItem` objects. 
    Instead, only the primary key of the related `OrderItem` objects will be returned by default.
    '''

    total_price = serializers.SerializerMethodField(method_name='total')

    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    class Meta:
        model = Order
        fields = (
            'order_id', 
            'created_at', 
            'user', 
            'status',
            'total_price',
            'items'
            )

class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.ImageField()
    max_price = serializers.FloatField()
    