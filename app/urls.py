from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('template', views.Template.as_view(), name='template'),
]