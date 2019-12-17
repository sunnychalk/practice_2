from django.test import TestCase, Client
from django.urls import resolve, reverse

from pizzas.views import *
from pizzas.forms import *

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

class PizzaTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.pizza = Pizza.objects.create(name="Vegan", price=10)

	def test_home_page(self):
		response = self.client.get('/')
		self.assertContains(response, "Bootstrap starter template")

	def test_pizza_list_page(self):
		response = self.client.get('/pizza_list/')
		self.assertEqual(response.status_code, 404)
		print(response.context)
		self.assertContains(response, "Pizza")
		self.assertTrue('pizza_amount' in response.context)
		self.assertTrue(len(response.context['pizza_amount'])==1)
		self.assertTrue('more_than_40' in response.context)
		self.assertTrue(len(response.context['more_than_40'])==0)
		self.assertTrue('values_list' in response.context)
		self.assertTrue(len(response.context['values_list'])==1)

	def test_pizza_form_label(self):
		form = PizzaForm
		self.assertTrue(form.fields['pizza_id'].label == None or form.fields['pizza_id', 'count'].label == 'pizza_id')



