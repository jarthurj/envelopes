from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="budgets"),
    path('create_budget/', views.create_budget, name="create_budget"),
]
