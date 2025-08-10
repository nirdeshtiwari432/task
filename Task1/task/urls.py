from django.contrib import admin
from django.urls import include, path
from task import views

urlpatterns = [
    path("",views.index),
    path('task/', views.task, name='task')
]