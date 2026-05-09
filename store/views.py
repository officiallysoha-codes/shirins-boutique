from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Category


CONTACT_PHONE = '919836380078'


def _cart(request):
    return request.session.setdefault('cart', {})


def _wishlist(request):
    return request.session.setdefault('wishlist', [])


def _cart_items(cart):
    product_ids = [int(product_id) for product_id in cart.keys()]
    products = Product.objects.filter(id__in=product_ids)
    items = []
    total = 0

    for product in products:
        quantity = int(cart.get(str(product.id), 0))
        subtotal = product.price * quantity
        total += subtotal
        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return items, total


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

    category = get_object_or_404(Category, name=name)

    products = Product.objects.filter(category=category)

    return render(request, 'store/category.html', {
        'category': category,
        'products': products
    })


# WISHLIST PAGE

def wishlist(request):

    product_ids = [int(product_id) for product_id in _wishlist(request)]
    products = Product.objects.filter(id__in=product_ids)

    return render(request, 'store/wishlist.html', {
        'products': products,
    })


# CART PAGE

def cart(request):

    items, total = _cart_items(_cart(request))
    whatsapp_text = 'Hello Shirin\'s Boutique, I would like to place an order.'

    return render(request, 'store/cart.html', {
        'items': items,
        'total': total,
        'whatsapp_phone': CONTACT_PHONE,
        'whatsapp_text': whatsapp_text,
    })


# SEARCH PAGE

def search(request):

    query = request.GET.get('q', '').strip()
    products = Product.objects.none()

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(category__name__icontains=query)
        ).distinct()

    return render(request, 'store/search.html', {
        'query': query,
        'products': products,
    })


# CART ACTIONS

def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart = _cart(request)
    product_key = str(product.id)
    cart[product_key] = int(cart.get(product_key, 0)) + 1
    request.session.modified = True

    return redirect('cart')


def remove_from_cart(request, product_id):

    cart = _cart(request)
    cart.pop(str(product_id), None)
    request.session.modified = True

    return redirect('cart')


# WISHLIST ACTIONS

def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    wishlist_items = _wishlist(request)
    product_key = str(product.id)

    if product_key not in wishlist_items:
        wishlist_items.append(product_key)
        request.session.modified = True

    return redirect('wishlist')


def remove_from_wishlist(request, product_id):

    wishlist_items = _wishlist(request)
    product_key = str(product_id)

    if product_key in wishlist_items:
        wishlist_items.remove(product_key)
        request.session.modified = True

    return redirect('wishlist')


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