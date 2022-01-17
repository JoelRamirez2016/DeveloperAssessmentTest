from rest_framework import serializers
from inventory.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = User
        fields = ['id','password',  'username', 'email']

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['id', 'type', 'date', 'status', 'total']

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'company', 'gov_id']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'date', 'user', 'total', 'subtotal', 'taxes', 'paid']

class ShipppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shippping
        fields = ['id', 'order', 'address', 'city', 'state', 'country', 'cost']