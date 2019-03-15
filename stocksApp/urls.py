"""Defines URL patterns for stocksApp."""
from django.urls import path
from django.conf.urls import include, url
from . import views
from stocksApp.views import IndexView
from django.views.generic import TemplateView

app_name = 'stocksApp'
urlpatterns = [
       # Home page
       url(r'^$', views.index, name='index'),
       path('graphs/', IndexView.as_view(), name='graphs'),
]
