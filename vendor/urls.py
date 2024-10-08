from django.urls import path, include
from . import views
from accounts import views as AccountViews

urlpatterns = [
    path('', AccountViews.restDashboard, name='restaurant'),
    path('profile/', views.rprofile, name='rprofile'),
    path('menu-builder/', views.menu_builder, name='menu_builder'),
    path('menu-builder/category/<int:pk>/', views.foodItems_by_category, name='foodItems_by_category'),
    path('myorders/', views.myorders, name='rest_myorders'),
    path('order_detail/<int:order_number>/', views.order_detail, name='rest_order_detail'),

    # category urls
    path('menu-builder/category/add', views.add_category, name='add_category'),
    path('menu-builder/category/edit/<int:pk>', views.edit_category, name='edit_category'),
    path('menu-builder/category/delete/<int:pk>', views.delete_category, name='delete_category'),

    # food Item urls
    path('menu-builder/food/add', views.add_food, name='add_food'),
    path('menu-builder/food/edit<int:pk>/', views.edit_food, name='edit_food'),
    path('menu-builder/food/delete<int:pk>/', views.delete_food, name='delete_food'),

]
