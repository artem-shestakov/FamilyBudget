from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index, name='index'),
    
    # Incomes
    path('incomes/', views.incomes_list, name='incomes_list'),
    path('income/add', views.add_income, name='add_income'),
    path('income/<int:id>/edit', views.edit_income, name='edit_income'),
    path('income/<int:id>/delete', views.delete_income, name='delete_income'),

    # Savings
    path('savings/', views.savings_list, name='savings_list'),
    path('saving/add', views.add_saving, name='add_saving'),
    path('saving/<int:id>/edit', views.edit_saving, name='edit_saving'),
    path('saving/<int:id>/delete', views.delete_saving, name='delete_saving')
]