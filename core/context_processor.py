# coding=utf-8
from django.conf import settings
from pizzas.models import Pizza, Order


def contex_core(request):
    return {'site_url': settings.SITE_URL,
            'site_name': settings.SITE_NAME,
            'pizzas': Pizza.objects.all(),
            #'order': Order.objects.filter(user=request.user).first(),
            'support_email_address': settings.SUPPORT_EMAIL_ADDRESS,}
