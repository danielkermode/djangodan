from django.conf.urls import patterns, include, url
from django.contrib import admin
from danapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dansproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

     url(r'^register/', views.register),
    url(r'^login/', views.loginpage),
     url(r'^home/', views.home),
     url(r'^$', views.home),
     url(r'^loggedin/', views.loggedin),
     url(r'^logoutview/', views.logoutview),
    
)