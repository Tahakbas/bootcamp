from rest_framework import serializers
from baskets.serializers import BasketSerializer
from customers.serializers import CustomerSerializer,CitySerializer
from orders.models import Order, OrderItem, BillingAddress, ShippingAddress, OrderBankAccount


class BillingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingAddress
        fields = ("id", "full_name", "line_1", "line_2","phone","district", "zipcode", "city")


class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ("id", "full_name", "line_1", "line_2","phone","district", "zipcode", "city")


class OrderBankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderBankAccount
        fields = ("id", "name", "iban", "bank_name", "order")

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "customer", "basket", "status", "total_price")


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id", "product", "price", "order", )


class BillingAddressDetailedSerializer(BillingAddressSerializer):
    city = CitySerializer()


class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    city = CitySerializer()


class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    order = OrderSerializer()


class OrderDetailedSerializer(OrderSerializer):
    basket = BasketSerializer()
    customers = CustomerSerializer()


class OrderItemDetailedSerializer(OrderItemSerializer):
    order = OrderSerializer()

