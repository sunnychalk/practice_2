from rest_framework import viewsets
from .serializers import *
from .models import *

class PizzaViewSet(viewsets.ModelViewSet):
	queryset = Pizza.objects.filter(price__lte='50')
	serializer_class = PizzaSerializer


class InstancePizzaViewSet(viewsets.ModelViewSet):
	queryset = InstancePizza.objects.all()
	serializer_class = InstancePizzaSerializer


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.order_by('date_created')
	serializer_class = OrderSerializer
