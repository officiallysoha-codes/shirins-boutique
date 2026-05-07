from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('category/<path:name>/', views.category_page, name='category'),

    path('wishlist/', views.wishlist, name='wishlist'),

    path('cart/', views.cart, name='cart'),

    path('search/', views.search, name='search'),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]