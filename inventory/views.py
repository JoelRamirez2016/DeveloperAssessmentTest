from rest_framework import viewsets
from inventory.models import *
from inventory.serializers import *
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        if ',' in pk:
            pk = [int(x.strip()) for x in pk.split(',') if x]
            orders = self.get_queryset().filter(pk__in = pk)        
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        if '-' in pk:
            pk = pk.split(' - ')            
            orders = self.get_queryset().filter(date__range=pk)      
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        return super().retrieve(request, pk)        

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShipppingViewSet(viewsets.ModelViewSet):
    queryset = Shippping.objects.all()
    serializer_class = ShipppingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
