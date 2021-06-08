from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
import template_app

app_name = 'template_app'

urlpatterns = [
    path('', views.homepage, name='homepage')
]
