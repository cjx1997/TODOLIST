# -*- coding: UTF-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import UserSerializer

# Create your views here.

class index(APIView):
	renderer_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		if ('username' in request.session):
			return HttpResponseRedirect('/business/getlist')
		return Response(template_name='index.html')

class checkinfo(APIView):
	renderer_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		return HttpResponseRedirect('/')

	def post(self,request):
		user = authenticate(username=request.data['username'],password=request.data['password'])
		if user is not None:
			login(request,user)
			request.session['username']=request.POST['username']
			return HttpResponseRedirect('/business/getlist')
		else:
			info="The user name or password error, please enter again!"
			return Response({'info':info},template_name='index.html')

class register(APIView):
	renderer_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		if ('username' in request.session):
			return HttpResponseRedirect('/business/getlist')
		return Response(template_name='register.html')

	def post(self,request):
		username=request.data['username']
		password=request.data['password']
		users = User.objects.filter(username=username)
		if len(users)==0:
			User.objects.create_user(username=username,password=password)
			request.session['username']=username
			return HttpResponseRedirect('/business/getlist')
		else:
			return Response({'info':'User name already exists!'},template_name='register.html')

class userlogout(APIView):
	renderer_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		if 'username' in request.session:
			logout(request)
		return HttpResponseRedirect('/')

class show(APIView):
	renderer_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		try:
			username=request.session['username']
		except KeyError, e:
			username='empty'
		return Response({'username':username},template_name='show.html')