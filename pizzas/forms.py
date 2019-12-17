from django import forms
from django.forms import ModelForm
from pizzas.models import Pizza, Shipping 

class IncreasePriceForm(forms.Form):
	message = forms.CharField(max_length=100, initial = 'I want to increase price by 100')

	
class PizzaForm(forms.Form):
	pizza_id = forms.IntegerField()
	count = forms.IntegerField()

class ShippingForm(forms.ModelForm):
	class Meta:
		model = Shipping
		fields = ['email', 'first_name', 'last_name', 'street', 'city', 'postcode', 'region', 'country']


	