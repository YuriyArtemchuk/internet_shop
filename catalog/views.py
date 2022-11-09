from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Producer, Product


def index(request):
    page_size = 2
    all_products = Product.objects.all()

    paginator = Paginator(all_products, page_size)
    page_number = request.GET.get('page')
    paginate_products = paginator.get_page(page_number)

    return render(request, 'catalog/index.html', {
        "page_title": 'Каталог товарів',
        "all_products": all_products,
        "paginate_products": paginate_products,
        "all_categories": Category.objects.all(),
        "all_producers": Producer.objects.all()
    })


