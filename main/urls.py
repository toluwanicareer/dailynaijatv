from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='home' ),
	url(r'^category/(?P<slug>[-\w]+)/$', views.CatView.as_view(), name='category'),

]