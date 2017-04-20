from .views import checkinfo,index,register,userlogout,show
from django.conf.urls import url

urlpatterns = [
    url(r'^$',index.as_view()),
    url(r'^login$',checkinfo.as_view()),
    url(r'^register$',register.as_view()),
    url(r'^logout$',userlogout.as_view()),
    url(r'^show$',show.as_view()),
]