from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category


# HOME PAGE

def home(request):

    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'store/home.html', {
        'categories': categories,
        'products': products
    })


# CATEGORY PAGE

def category_page(request, name):

    category = Category.objects.get(name=name)

    products = Product.objects.filter(category=category)


    return render(request, 'store/category.html', {
        'category': category,
        'products': products
    })


# WISHLIST PAGE

def wishlist(request):

    return HttpResponse("Wishlist Page Coming Soon")


# CART PAGE

def cart(request):

    return HttpResponse("Cart Page Coming Soon")


# SEARCH PAGE

def search(request):

    return HttpResponse("Search Page Coming Soon")


# ADD TO CART

def add_to_cart(request, product_id):

    return HttpResponse(f"Product {product_id} added to cart")