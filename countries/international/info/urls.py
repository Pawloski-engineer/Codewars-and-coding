from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anthem', views.anthem, name='anthem'),
]