from django.urls import path
from django.conf.urls import url, include
from pizzas.views import PizzaList, IncreasePrice, AddPizzaView, CoreTemplateView, EditOrderView, ShippingFormView 
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page


urlpatterns = [
    url(r'^pizza_list/$', PizzaList.as_view(), name='pizza-list'),
    url(r'^increase_price/$', IncreasePrice.as_view(), name='increase_price'),
    url(r'^pizzas/$', cache_page(60*30)(CoreTemplateView.as_view())),
    url(r'^add_pizza/$', AddPizzaView.as_view(), name='add-pizza'),
    url(r'^add_pizza/int:pk>/edit/', EditOrderView.as_view()),
    url(r'^shipping_form/$', ShippingFormView.as_view(), name='shipping-form'),
]
