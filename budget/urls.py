from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index, name='index'),
    
    # Sources
    path('sources/', views.sources_list, name='sources_list'),
    path('source/add', views.add_source, name='add_source'),
    path('source/<int:id>/edit', views.edit_source, name='edit_source'),
    path('source/<int:id>/delete', views.delete_source, name='delete_source'),

    # Savings
    path('savings/', views.savings_list, name='savings_list'),
    path('saving/add', views.add_saving, name='add_saving'),
    path('saving/<int:id>/edit', views.edit_saving, name='edit_saving'),
    path('saving/<int:id>/delete', views.delete_saving, name='delete_saving')
]