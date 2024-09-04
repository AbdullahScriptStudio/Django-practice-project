from django.shortcuts import render
from django.http import HttpResponse
from norasite.models import Product
# Create your views here.



def contact(request):
    products = Product.objects.order_by('price')
    product_list = {'records': products}
    return render(request, 'norasite\index.html', context=product_list)
