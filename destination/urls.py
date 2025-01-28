from django.urls import path

from . import views

urlpatterns = [
  path('destination', views.destination, name='destination')
]