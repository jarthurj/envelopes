from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="budgets"),
    path('create_budget/', views.create_budget, name="create_budget"),
    path('budget/', views.budget, name="budget"),
    path('transaction/', views.transaction_form, name="transaction_form"),
    path('create_transaction/', views.create_transaction, name="create_transaction"),
    path('budger_render/', views.budget_render, name="budget_render"),
]
