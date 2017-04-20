# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Business
from .serializers import BusinessSerializer
from datetime import datetime
import time

# Create your views here.

class businesscreate(APIView):
	renderer_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		if ('username' not in request.session):
			return HttpResponseRedirect('/')
		return Response(template_name='create.html')
	def post(self,request):
		try:
			title = request.data['title']
			content = request.data['content']
			deadline = request.data['deadline']
			Business.objects.create(title=title,createdate=datetime.now(),content=content,deadline=deadline,owner=request.session['username'])
		except ValidationError, e:
			return Response({"warn":"illegal"},template_name="create.html")  
		return HttpResponseRedirect('/business/getlist')

class businessdetail(APIView):
	renderer_classes= [ TemplateHTMLRenderer ]

	def get(self,request):
		if ('username' not in request.session):
			return HttpResponseRedirect('/')
		business = get_object_or_404(Business,id=request.GET['id'])
		if business.owner==request.session['username']:
			d = business.deadline
			return Response({'id':business.id,'status':business.status,'year':d.year,'month':d.month,'day':d.day,'hour':d.hour,'minute':d.minute},template_name='detail.html')
		else:
			return Response(template_name='illegal.html',status=404)

class businesssolve(APIView):
	renderers_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		return Response(template_name='illegal.html',status=404)

	def post(self,request):
		business = get_object_or_404(Business,id=request.data['id'])
		if business.owner==request.session['username']:
			business.status=2
			business.save()
			return HttpResponseRedirect('/business/getlist')
		else:
			return Response(template_name='illegal.html',status=404)

class businessdelete(APIView):
	renderers_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		return Response(template_name='illegal.html',status=404)

	def post(self,request):
		business = get_object_or_404(Business,id=request.data['id'])
		if business.owner==request.session['username']:
			business.delete()
			return HttpResponseRedirect('/business/getlist')
		else:
			return Response(template_name='illegal.html',status=404)

class businessedit(APIView):
	renderers_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		return Response(template_name='illegal.html',status=404)

	def post(self,request):
		business = get_object_or_404(Business,id=request.data['id'])
		if business.owner==request.session['username']:
			business.content=str(request.data['content'])
			business.save()
			return HttpResponseRedirect('/business/detail?id='+request.data['id'])
		else:
			return Response(template_name='illegal.html',status=404)

class getlist(APIView):
	renderer_classes = [ TemplateHTMLRenderer ]

	def get(self,request):
		if ('username' not in request.session):
			return Response(template_name='illegal.html',status=404)
		return Response({'username':request.session['username']},template_name='list.html')

class getlistjson(APIView):

	def get(self,request,format=None):
		if ('username' not in request.session):
			return Response()
		name = request.session['username']
		queryset = Business.objects.filter(owner=name)
		nowtime = datetime.now()
		unfinished = queryset.filter(status=1)
		for x in unfinished:
			if time.mktime(x.deadline.timetuple())<time.mktime(nowtime.timetuple()):
				x.status=3
				x.save()
		queryset = Business.objects.filter(owner=name)
		serializer = BusinessSerializer(queryset,many=True)
		return Response(serializer.data)

class getdetailjson(APIView):

	def get(self,request,format=None):
		if ('username' not in request.session):
			return Response()
		business = get_object_or_404(Business,id=request.GET['id'])
		if business.owner==request.session['username']:
			serializer = BusinessSerializer(business)
			return Response(serializer.data)
		else:
			return Response()