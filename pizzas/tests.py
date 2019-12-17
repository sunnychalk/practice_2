from django.test import TestCase, Client
from django.urls import resolve, reverse

from pizzas.views import *
from pizzas.forms import *
from pizzas.models import *

# Create your tests here.
class TestUrls(TestCase):
	def test_resolution_for_increase_price(self):
		resolver = resolve('/increase_price/')
		self.assertEqual(resolver.view_name, 'increase_price')

	def test_resolution_for_pizza_list(self):
		resolver = resolve('/pizza_list/')
		self.assertEqual(resolver.view_name, 'pizza-list')

	def test_resolution_for_pizzas(self):
		resolver = resolve('/pizzas/')
		self.assertEqual(resolver.view_name, 'pizzas')

	def test_resolution_for_add_pizzas(self):
		resolver = resolve('/add_pizza/')
		self.assertEqual(resolver.view_name, 'add-pizza')

	def test_pizza_list(self):
		url = reverse('pizza-list')
		self.assertEqual(url, '/pizza_list/')

	def test_increase_price(self):
		url = reverse('increase_price')
		self.assertEqual(url, '/increase_price/')

	def test_pizzas(self):
		url = reverse('pizzas')
		self.assertEqual(url, '/pizzas/')

	def test_add_pizza(self):
		url = reverse('add-pizza')
		self.assertEqual(url, '/add_pizza/')

class PizzaModelTestCase(TestCase):
	@classmethod
	def setUp(self):
		Pizza.objects.create(name='New pizza', price=10.0, description="new pizza", photo="static/pizzas/no_photo.png")

	def test_pizza_name(self):
		pizza = Pizza.objects.get(name='New pizza')
		self.assertEqual(pizza.price, 10)


class ShippingFormTest(TestCase):
	def setUp(self):
		Shipping.objects.create(email="user@user.com", first_name="user", last_name="user2",
		street="street", city="Odessa", postcode="000000", region="Odessa region", country="Ukraine")

	def test_shipping_form_valid(self):
		form = ShippingForm(data={"email": "user@user.com", "first_name": "user", "last_name": "user2",
		"street": "street", "city": "Odessa", "postcode": "000000", "region": "Odessa region", "country": "Ukraine"})
		self.assertTrue(form.is_valid())

	def test_shipping_form_invalid(self):
		form = ShippingForm(data={"email": "ufgth.com", "first_name": "gh", "last_name": "h",
		"street": "s", "city": "ghj", "postcode": "87", "region": "egion", "country": "Ue"})
		self.assertFalse(form.is_valid())


		
		
