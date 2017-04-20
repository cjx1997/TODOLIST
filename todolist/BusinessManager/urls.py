from django.conf.urls import url
from .views import businesscreate,businessdetail,businesssolve,businessdelete,getlistjson,getlist,getdetailjson,businessedit

urlpatterns = [
	url(r'^getlist$',getlist.as_view()),
	url(r'^create$',businesscreate.as_view()),
	url(r'^detail$',businessdetail.as_view()),
	url(r'^solve$',businesssolve.as_view()),
	url(r'^delete$',businessdelete.as_view()),
	url(r'^getlistjson$',getlistjson.as_view()),
	url(r'^getdetailjson$',getdetailjson.as_view()),
	url(r'^edit$',businessedit.as_view()),
]