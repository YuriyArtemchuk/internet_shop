from django.shortcuts import render
from django.http import JsonResponse
from .models import CartItem


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


def ajax_cart_display(request):
    uid = request.GET['uid']
    user_items = CartItem.objects.filter(user_id=uid)
    amount = 0.0
    for item in user_items:
        amount += item.product.price
    return JsonResponse({
        'count': len(user_items),
        'amount': amount
    })


def ajax_del_cart(request):
    del_id = request.GET['del_id']
    del_item = CartItem.objects.get(id=del_id)
    del_item_name = del_item.product.name
    del_item.delete()
    return JsonResponse({
        'report': f"Товар {del_item_name} успішно видален!"
    })
