from django.conf.urls import url
from django.contrib import admin
from blog import views

app_name = 'blog'
urlpatterns = [
 url(r'^$', views.home_page, name='home_page'),
]