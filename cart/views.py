from django.shortcuts import render
from django.http import JsonResponse
from .models import CartItem
from catalog.models import Product





def index(request):
    return render(request, 'cart/index.html', {
        'page_title': 'Управління кошиком',
        'user_items': CartItem.objects.filter(user_id=request.user.id),
        'k': 0
    })


def ajax_cart(request):
    response = dict()
    uid = request.GET['uid']
    pid1 = request.GET['pid1']
    pid2 = request.GET['pid2']
    response['uid'] = uid
    response['pid1'] = pid1
    response['pid2'] = pid2
    #
    if pid1:
        pid = pid1
    else:
        pid = pid2
    #
    current_product, created = CartItem.objects.update_or_create(
        user_id=uid,
        product_id=pid,
        status='Очікування обробки замовлення',
    )
    if not created:
        current_product.qty_in_cart += 1
        current_product.save()
    #    
    response['report'] = "Товар успішно збережений у кошику"
    #
    response = count_and_amount(request, response)
    return JsonResponse(response)


def ajax_cart_display(request):
    response = dict()
    response = count_and_amount(request, response)
    return JsonResponse(response)


def count_and_amount(request, response):
    uid = request.GET['uid']
    user_items = CartItem.objects.filter(user_id=uid)
    amount = 0.0
    count = 0
    for item in user_items:
        amount += item.product.price
        count += item.qty_in_cart
    response['count'] = count                                
    response['amount'] = amount
    return response

def ajax_del_cart(request):
    del_id = request.GET['del_id']
    del_item = CartItem.objects.get(id=del_id)
    del_item_name = del_item.product.name
    del_item.delete()
    return JsonResponse({
        'report': f"Товар {del_item_name} успішно видален!"
    })

def ajax_change_qty(request):
    response = dict()
    change_product_id = request.GET['prod_id']
    new_qty = request.GET['current_qty']
    update_product = CartItem.objects.get(pk=change_product_id)
    update_product.qty_in_cart = int(new_qty)
    update_product.save()
    response['changed_qty'] = update_product.qty_in_cart
    # 
    return JsonResponse(response)