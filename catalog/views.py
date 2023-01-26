from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Category, Producer, Product
from django.contrib.auth.models import User
from cart.models import CartItem
from orders.models import Order, Delivery



def index(request):
    page_size = 3
    if request.method == "GET":
        
        all_products = Product.objects.all()
        #
        paginator = Paginator(all_products, page_size)
        page_number = request.GET.get('page')
        paginate_products = paginator.get_page(page_number)

        return render(request, 'catalog/index.html', {
            "page_title": _('PageTitle'),
            "all_products": all_products,
            "paginate_products": paginate_products,
            "all_categories": Category.objects.all(),
            "all_producers": Producer.objects.all()
        })
    elif request.method == "POST":
        product_by_category = request.POST['category']   
        # product_by_brand = request.POST['brand-name']
        #
        if product_by_category == 'Взуття для хлопчика':
            current_category = Category.objects.get(name=product_by_category)
            all_products = Product.objects.filter(category=current_category)
        elif product_by_category == 'Взуття для дівчинки':
            current_category = Category.objects.get(name=product_by_category)
            all_products = Product.objects.filter(category=current_category)
        elif product_by_category == 'Bartek':
            current_brand = Producer.objects.get(name=product_by_category)
            all_products = Product.objects.filter(producer=current_brand)
        elif product_by_category == 'Kangaroos':
            current_brand = Producer.objects.get(name=product_by_category)
            all_products = Product.objects.filter(producer=current_brand) 
        elif product_by_category == 'Shagovita':
            current_brand = Producer.objects.get(name=product_by_category)
            all_products = Product.objects.filter(producer=current_brand)
        elif product_by_category == 'reset':
            all_products = Product.objects.all() 
        elif product_by_category == 'all':
            all_products = Product.objects.all()           
        #
        paginator = Paginator(all_products, page_size)
        page_number = request.GET.get('page')
        paginate_products = paginator.get_page(page_number)

        return render(request, 'catalog/index.html', {
            "page_title": _('PageTitle'),
            "all_products": all_products,
            "paginate_products": paginate_products,
            "all_categories": Category.objects.all(),
            "all_producers": Producer.objects.all(),
        })

def ajax_sort_catalog(request):
    response = dict()
    product_by_category = request.GET['category_name']
    response['category'] = product_by_category
    #
    current_category = Category.objects.get(name=product_by_category)
    response['current_category'] = current_category.id
    all_products = Product.objects.filter(category=current_category)   # не передаються об'єкти через словник response
    
    # page_size = 2
    # paginator = Paginator(all_products, page_size)
    # page_number = request.GET.get('page')
    # paginate_products = paginator.get_page(page_number)
    #
    response['all_products'] = all_products
    # response['paginate_products'] = paginate_products
    # response['all_categories'] = Category.objects.all()
    # response['all_producers'] = Producer.objects.all()
    return JsonResponse(response)


