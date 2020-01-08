from django.views.generic.base import View 
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import User


class UsersApiView(View):

	def get(self, request):
		print("Get API Users")
		serialized_users = []
		for user in User.objects.all():
			serialized_users.append(user.get_serialize_data())
		return JsonResponse({'users_list': serialized_users})


class CreateUserApiView(View):

	def get(self, request):
		return JsonResponse({'message': 'Method GET is not supported.'})

	def post(self, request, *args, **kwargs):
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.create(email=email, username=email)
		user.set_password(password)
		user.save()
		return JsonResponse({
			'message': 'User created',
			'user': user.get_serialize_data(),
		})
