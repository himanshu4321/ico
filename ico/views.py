from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from . models import NsUsers, NsBlog
from django.contrib import messages
from django import template
from time import gmtime, strftime
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class Login(View):
	template_name="login.html"
	def get(self,request):
		if request.session.has_key('user_id'):
			return redirect("/test/")
		else:
			return render(request, self.template_name, {})

	def post(self, request):
		try:
			x = NsUsers.objects.get(user_email=request.POST['email'], user_password=request.POST['password'])
			if x.user_status == 1:
				request.session['user_id'] = x.user_id
				return redirect("/test/")
			else:
				return HttpResponse("Invalid login")
		except:
			return HttpResponse("incorrect login or password")

def logout(request):
	template_name="login.html"
	try:
		del request.session['user_id']
	except:
		pass
	return render(request, "login.html", {})


	     



class Fet(View):
	test="blog-list.html"
	def get(self,request):
		blog = NsBlog.objects.all()
		return render(request, self.test, {"blog_deatils": blog})


class SignUp(View):
	template_name="signup.html"

	def get(self, request):
		return render(request, self.template_name, {})

	def post(self, request):
		if request.method == 'POST':
			user=NsUsers()
			import datetime
			user.user_email = request.POST['email']
			user.user_firstname = request.POST['first_name']
			user.user_lastname = request.POST['last_name']
			user.user_password = request.POST['password']
			user.created_date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			user.user_status = 1
			NsUsers.save(user)
			return HttpResponse("Saved")
				##return render(request, self.template_name, {"err": err})
			
		


