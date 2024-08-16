from django.shortcuts import render
from .models import Product


def product(request):
    products = Product.objects.all()
    context = {
        "title": 'Product sahifasi Qo\'shimcha',
        'products': products,
        'count': len(products),
    }
    return render(request, 'product.html', context)
