from django.db import models
from accounts.models import User

# Create your models here.
class Pizza(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
	
	class Meta:
		verbose_name = "Пицца"
		verbose_name_plural = "Пиццы"

	def __str__(self):
		return self.name

	def create_instance_pizza(self, count):
		return InstancePizza.objects.create(
			name=self.name,
			price=self.price,
			pizza_template=self,
			count=count
		)


class InstancePizza(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
	pizza_template = models.ForeignKey(Pizza, related_name='pizza_template', null=True, on_delete=models.SET_NULL)
	count = models.PositiveIntegerField(default=1)

	class Meta:
		verbose_name = "Пицца в заказ"
		verbose_name_plural = "Пиццы в заказ"

	def __str__(self):
		return 'name: {}, price: {}, count: {}'.format(self.name, str(self.price), str(self.count))


class Order(models.Model):
	pizzas = models.ManyToManyField(InstancePizza, blank=True, null=True)
	full_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"

	def __str__(self):
		return 'Order: {}, price: {}'.format(self.id, str(self.full_price))

	def get_full_price(self):
		pizzas = self.pizzas.all()
		full_price = 0
		for pizza in pizzas:
			full_price += pizza.price * pizza.count
		return full_price


