from django.urls import path
from . import views

urlpatterns = [
path('', views.contract_list, name='contract_list'),
    path('create/', views.contract_create, name='contract_create'),
    path('update/<int:contract_id>/', views.contract_update, name='contract_update'),
    path('delete/<int:contract_id>/', views.contract_delete, name='contract_delete'),
]