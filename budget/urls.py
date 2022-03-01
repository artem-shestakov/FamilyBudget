from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index, name='index'),
    
    # Incomes
    path('income/add', views.add_income, name='add_income')
]