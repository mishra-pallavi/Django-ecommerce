from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context = {
        'products' : products,
    }
    return render(request, 'home.html',context)