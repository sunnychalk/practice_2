from pizzas.models import Order

def orders_made(request):
	return {
	    'supersecret_code': "GYUFUTFUDTDFY",
	    'orders': Order.objects.all(),
	    
	}