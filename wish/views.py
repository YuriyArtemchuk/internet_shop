from django.shortcuts import render
from django.http import JsonResponse
from .models import WishItem


def ajax_wish(request):
    response = dict()
    uid = request.GET['uid']
    pid = request.GET['pid']
    response['uid'] = uid
    response['pid'] = pid
    #
    WishItem.objects.create(
        user_id=uid,
        product_id=pid
    )
    response['report'] = 'ТОвар успішно збережений в <ОБРАНИХ>'
    #
    user_wish = WishItem.objects.filter(user_id=uid)
    amount_wish = 0.0
    for wish in user_wish:
        amount_wish += wish.product.price
    #
    response['amount_wish'] = amount_wish
    response['count'] = len(user_wish)
    return JsonResponse(response)


def ajax_wish_display(request):
    uid = request.GET['uid']
    user_wish = WishItem.objects.filter(user_id=uid)
    amount_wish = 0.0
    for wish in user_wish:
        amount_wish += wish.product.price
    return JsonResponse({
        'amount_wish': amount_wish,
        'count': len(user_wish),
        'uid': uid,

    })

