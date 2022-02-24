from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('income/create', views.create_income, name='create_income')
]