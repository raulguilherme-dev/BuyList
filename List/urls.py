from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),


    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('edit_product/', views.edit_product, name='edit_product'),

    path('add_list/', views.add_list, name='add_list'),
    path('delete_list/<int:pk>/', views.delete_list, name='delete_list'),
    path('edit_list/', views.edit_list, name='edit_list'),

    path('add_product_to_list/', views.add_product_to_list, name='add_product_to_list'),
    path('delete_product_from_list/<int:li>/<int:pi>/', views.delete_product_from_list, name='delete_product_from_list' )
]