from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('category/<path:name>/', views.category_page, name='category'),

    path('wishlist/', views.wishlist, name='wishlist'),

    path('cart/', views.cart, name='cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('search/', views.search, name='search'),

    path('info/<slug:slug>/', views.info_page, name='info_page'),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

]
