from django.contrib import admin
from .models import *
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']

class OrderAdmin(admin.ModelAdmin):
	filter_horizontal = ['pizzas']

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(InstancePizza)
admin.site.register(Order, OrderAdmin)

