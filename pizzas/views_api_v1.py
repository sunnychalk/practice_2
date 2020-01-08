from django.views.generic.base import View 
from django.http import JsonResponse
from .models import Pizza, Order
from accounts.models import User

class PizzasApiView(View):

	def get(self, request):
		print("Get API Pizzas")
		pizzas = list(Pizza.objects.all().order_by('price'))
		serialized_pizzas = []
		for pizza in pizzas:
			serialized_pizzas.append(pizza.get_serialize_data())
		return JsonResponse({'pizzas_list': serialized_pizzas})


class OrdersApiView(View):

	def get(self, request):
		print("Get API Orders")
		serialized_orders = []
		for order in Order.objects.all():
			serialized_orders.append(order.get_serialize_data())
		return JsonResponse({'orders_list': serialized_orders})


class CreateOrderApiView(View):

	def get(self, request):
		return JsonResponse({'message': 'Method GET is not supported.'})

	def post(self, request, *args, **kwargs):
		pizzas = request.POST.get('pizzas')
		full_price = request.POST.get('full_price')
		user = request.POST.get('user')
		order = Order.objects.create(pizzas=pizzas, full_price=full_price, user=User)
		return JsonResponse({
			'Message': 'Order created',
			'Order': order.get_serialize_data(),
		})
