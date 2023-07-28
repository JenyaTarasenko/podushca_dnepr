from django.shortcuts import render, get_object_or_404
from .models import *

def product_list(request, category_slug=None):
    """отображения каталога списка товара """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)#булево значение в models получаем товары которые есть в наличии
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'magazin/home.html', {'category': category, 'categories': categories, 'products': products})




#def home(request):
#    post = Category.objects.all()
#    return render(request, 'magazin/home.html', {'post': post})


def product_detail(request, id, slug):
    """детальное отображение продукта"""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, '', {'product': product})