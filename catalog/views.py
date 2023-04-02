from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from django.views.generic import ListView 
from django.core.paginator import Paginator
from .models import Category, Producer, Product
from django.contrib.auth.models import User
from cart.models import CartItem
from orders.models import Order, Delivery


class CatalogHome(ListView):
    paginate_by = 1
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "all_products"
    extra_context = {"page_title": _('PageTitle')}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['all_producers'] = Producer.objects.all()
        context['category_selected'] = 0
        return context
    
# def index(request):
    
#     if request.method == "GET":
#         page_size = 5
#         all_products = Product.objects.all()
#         #
#         paginator = Paginator(all_products, page_size)
#         page_number = request.GET.get('page')
#         paginate_products = paginator.get_page(page_number)

#         return render(request, 'catalog/index.html', {
#             "page_title": _('PageTitle'),
#             "all_products": all_products,
#             "paginate_products": paginate_products,
#             "all_categories": Category.objects.all(),
#             "all_producers": Producer.objects.all()
#         })
    
class CategoriesHome(ListView):
    paginate_by = 1
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "all_products"
    extra_context = {"page_title": _('PageTitle')}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['all_producers'] = Producer.objects.all()
        context['category_selected'] = context['all_products'][0].pk
        return context

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs['cat_id'])

# def categories(request, cat_id):
#     page_size = 1
#     all_products = Product.objects.filter(category=cat_id)
#     paginator = Paginator(all_products, page_size)
#     page_number = request.GET.get('page')
#     paginate_products = paginator.get_page(page_number)
#     return render(request, "catalog/index.html", {
#         "page_title": _('PageTitle'),
#         "all_products": paginate_products,                         # !!! all_products": paginate_products
#         "paginate_products": paginate_products,
#         "all_categories": Category.objects.all(),
#         "all_producers": Producer.objects.all(),
#         "category_selected": cat_id,
#     })

class ProducersHome(ListView):
    paginate_by = 1
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "all_products"
    extra_context = {"page_title": _('PageTitle')}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['all_producers'] = Producer.objects.all()
        context['category_selected'] = context['all_products'][0].pk
        return context

    def get_queryset(self):
        return Product.objects.filter(producer__pk=self.kwargs['prod_id'])


# def producers(request, prod_id):
#     page_size = 1
#     all_products = Product.objects.filter(producer=prod_id)
#     paginator = Paginator(all_products, page_size)
#     page_number = request.GET.get('page')
#     paginate_products = paginator.get_page(page_number)
#     return render(request, "catalog/index.html", {
#         "page_title": _('PageTitle'),
#         "all_products": paginate_products,                         # !!! all_products": paginate_products
#         "paginate_products": paginate_products,
#         "all_categories": Category.objects.all(),
#         "all_producers": Producer.objects.all(),
#         "category_selected": prod_id,
#     })

def pageNotFound(request, exception):                                     # не працює !!! + див url.py
    return HttpResponseNotFound('Страница не найдена - 404')


def product_detail(request, prod_id):
    product = Product.objects.get(pk=prod_id)
    return render(request, "catalog/product.html", {
        "page_title": _('PageTitle'),
        'product': product,
        # 'product_pk': product.pk,
        
    })


def ajax_cart_product_page(request):
    response = dict()
    uid = request.GET['uid']
    pid = request.GET['pid']
    response['uid'] = uid
    response['pid'] = pid
    #
    CartItem.objects.create(
        user_id=uid,
        product_id=pid,
        status='Очікування обробки замовлення'
    )
    response['report'] = "Товар успішно збережений у кошику"
    user_items = CartItem.objects.filter(user_id=uid)
    amount = 0.0
    for item in user_items:
        amount += item.product.price
    #
    response['count'] = len(user_items)
    response['amount'] = amount
    return JsonResponse(response)


