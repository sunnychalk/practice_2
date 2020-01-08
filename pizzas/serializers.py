from rest_framework import serializers
from .models import *

class PizzaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pizza
		fields = ['name', 'price', 'description']


class InstancePizzaSerializer(serializers.ModelSerializer):
	pizza_template = PizzaSerializer()

	class Meta:
		model = InstancePizza
		fields = ['name', 'price', 'pizza_template', 'count']


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['email']


class OrderSerializer(serializers.ModelSerializer):
	pizzas = PizzaSerializer()
	user = UserSerializer()

	class Meta:
		model = Order
		fields = ['pizzas', 'full_price', 'user', 'date_created']
		
	