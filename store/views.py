from django.shortcuts import render
from django.http import Http404, HttpResponse
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

INFO_PAGES = {
    'sell-with-us': {
        'title': 'Sell with us',
        'body': ['Partner with Shirin\'s Boutique to showcase quality ethnic and occasion wear to our customers. Share your product details with our team and we will review the fit for our store.'],
    },
    'become-a-member': {
        'title': 'Become a member',
        'body': ['Join our customer community for boutique updates, new arrivals, and special shopping support. Contact us to register your interest.'],
    },
    'company-profile': {
        'title': 'Company Profile',
        'body': ['Shirin\'s Boutique is a Kolkata-based clothing brand focused on elegant ethnic wear, curated collections, and personal customer service.'],
    },
    'about-us': {
        'title': 'About us',
        'body': ['Shirin\'s Boutique brings together tradition, occasion styling, and contemporary elegance for customers looking for carefully selected clothing.'],
    },
    'how-do-i-shop': {
        'title': 'How do I shop',
        'body': ['Browse the collections, open the product you like, and use Add to Cart to begin your order. For help choosing a product, contact our team directly.'],
    },
    'how-do-i-pay': {
        'title': 'How do I pay',
        'body': ['Payment options are confirmed during order processing. Our team can guide you through available payment methods before final confirmation.'],
    },
    'refer-a-friend': {
        'title': 'Refer a friend',
        'body': ['You can share Shirin\'s Boutique with friends and family. For referral offers or active promotions, please contact customer care.'],
    },
    'cancellation-and-returns': {
        'title': 'Cancellation & Returns',
        'body': ['Cancellation and return requests are reviewed according to the order status, product condition, and applicable boutique policy. Please contact us as soon as possible for support.'],
    },
    'terms-of-use': {
        'title': 'Terms of Use',
        'body': ['By using this website, customers agree to use the service responsibly and provide accurate details for orders, delivery, and communication.'],
    },
    'privacy-policy': {
        'title': 'Privacy Policy',
        'body': ['Customer contact and order details are used only to support browsing, ordering, delivery, and customer-care communication.'],
    },
    'shipping-policy': {
        'title': 'Shipping Policy',
        'body': ['Shipping timelines and charges may vary by location and product availability. Our team will confirm delivery details when your order is processed.'],
    },
    'bulk-trade': {
        'title': 'Bulk Trade',
        'body': ['For bulk orders, boutique sourcing, or trade enquiries, please contact us with your requirement, quantity, and timeline.'],
    },
    'help-and-faq': {
        'title': 'Help & FAQ',
        'body': ['For product, payment, delivery, or order-related questions, reach out to our customer-care team by phone or email.'],
    },
    'career': {
        'title': 'Career',
        'body': ['For career enquiries, please email us with your details, area of interest, and experience.'],
    },
}


def info_page(request, slug):

    page = INFO_PAGES.get(slug)

    if page is None:
        raise Http404('Page not found')

    return render(request, 'store/info_page.html', page)