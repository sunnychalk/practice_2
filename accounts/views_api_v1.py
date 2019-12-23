from django.views.generic.base import TemplateView, View 
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import User


class UsersApiView(View):

	def get(self, request):
		print("Get API Users")
		users = User.objects.all()
		serialized_users = []
		for user in users:
			serialized_users.append(user.get_serialize_data())
		return JsonResponse({'users_list': serialized_users})