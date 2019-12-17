# coding=utf-8

from .views import *
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^core', TemplateView.as_view(template_name="core.html")),
    url(r'^my_order', TemplateView.as_view(template_name="my_order.html")),
]