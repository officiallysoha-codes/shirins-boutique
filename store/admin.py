from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Wishlist, WishlistItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)