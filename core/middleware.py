from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.contrib.auth import logout
import datetime
from datetime import timedelta, timezone
from django.http import HttpResponseRedirect
import project.settings


"""class AutoLogOutMiddleware(MiddlewareMixin):
	def process_request(self, request):
		print('process_request')

		if request.user.is_authenticated:
			current_datetime = datetime.datetime.now()
			if ('last_login' in request.session):
				last = (current_datetime - request.session['last_login']).seconds
				if last > settings.SESSION_IDLE_TIMEOUT:
					logout(request. core.html)
			else:
				request.session['last_login'] = current_datetime
		return None

	def process_response(self, request, response):
		print('process_response')
		return response"""




		


