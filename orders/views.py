from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import JsonResponse
from cart.models import CartItem
from orders.models import Order, Delivery


def order(request, sel_list: str):
    items_str = sel_list.split(',')
    items_int = [int(x) for x in items_str]
    id_items = items_int[0:-1]
    total_price= items_int[-1]
        #
    final_list = []
    for id in id_items:
        item = CartItem.objects.get(id=id)
        final_list.append({
            'product_name': item.product.name,
            'category_name': item.product.category.name,
            'product_price': item.product.price,
            'product_photo': item.product.photo,
        }) 
    user_id = request.user.id
    user_email = request.user.email
    #
    new_order = Order.objects.create(
        user = User.objects.get(id=user_id),
        amount=total_price,
    )    
    if request.method == "GET":        
        return render(request, 'orders/order.html', {
            'page_title': "Оформлення замовлення",
            'total_price': total_price,
            'final_list': final_list,
            'init_list': sel_list,
            'user_email': user_email,
            'order_id': new_order.id,
        })
    # elif request.method == "POST":
        
    #     user_id = request.user.id
    #     current_user = User.objects.get(id=user_id)
    #     #
    #     first_name = request.POST['first']
    #     last_name = request.POST['last']
    #     current_user.first_name = first_name
    #     current_user.last_name = last_name
    #     current_user.save()
      
        # phone_delivery = request.POST['phone']
        # company_delivery = request.POST['company']
        # city_delivery = request.POST['city']
        # depot_delivery = request.POST['depot']
        # address_delivery = request.POST['address']
        # info_delivery = request.POST['info']
        
        # new_delivery = Delivery.objects.create(
        #     user = User.objects.get(id=user_id),
        #     order = new_order,
        #     company = company_delivery,
        #     city = city_delivery,
        #     depot = depot_delivery,
        #     address = address_delivery,
        #     info = info_delivery
        # )
        # return render(request, 'orders/confirm/.html', {
            # 'new_order': new_order,
            # 'new_delivery': new_delivery,
            # 'first_name': first_name
            
        # })  


def confirm(request, init_list: list, order_id):

    current_order = Order.objects.get(id=order_id)
    current_delivery = Delivery.objects.get(order=current_order)
    #
    sel_list_str = init_list.split(',')  
    sel_list_num = [int(x) for x in sel_list_str]  
    id_list = sel_list_num[:-1]  
    total_price = sel_list_num[-1]  
    info_list = []
    #
    for id in id_list:
        item = CartItem.objects.get(id=id)
        info_list.append({
        'product_name': item.product.name,
        'category_name': item.product.category.name,      
        'product_price': item.product.price,
    }) 
    #
    if request.method == "GET":        
        return render(request, 'orders/confirm.html', {
            'page_title': 'Підтвердження замовлення',
            'order_id': order_id,
            'date_order': current_order.date_order,
            'info_list': info_list,
            "total": total_price,
            'init_list': init_list,
            'current_order': current_order,
            'current_delivery': current_delivery,
            'delivery_city': current_delivery.city,
            'delivery_phone': current_delivery.phone,
            'delivery_company': current_delivery.company,
        })
    elif request.method == 'POST':
        pay = request.POST['selector']
        #
        if pay == "1":
            return render(request, 'orders/payment.html', {
                'page_title': "Сторінка оплати",
        })
        elif pay == "2":
            user_email = request.user.email
            # email = request.POST['email']
            # user_email = 'uaa2uaa@gmail.com'
            #
            subject = f'Повідомлення про замовлення № {order_id} на сайті InternetShop "STEP"'
            body = f"""
                    <h1>Повідомлення про Ваше замовлення № {order_id} від {current_order.date_order} на сайті InternetShop "STEP"</h1>
                    <hr />
                    <h2 style="color: purple">Ви підтвердили замовлення наступних товарів</h2>
                    <h3>
                    <ol>
                """
            #
            for item in info_list:
                body += f"""
                    <li>
                        {item.get('product_name')} / 
                        {item.get('category_name')} -
                        {item.get('product_price')} грн
                    </li>
            """
            #
            body += f"""
                </ol>
                </h3>
                <hr />
                <h2 style="color: purple">Інформація про доставку:</h2>
                    <p>Ваше ім'я та фамілія: {request.user.first_name} {request.user.last_name}</p>
                    <p>Ваш Контактний номер телефону: {current_delivery.phone}</p>
                    <p>Транспортна компанія: {current_delivery.company}</p>
                    <p>Населенний пункт для відправки: {current_delivery.city}</p>
                <hr />
                <h2>
                        Загальна сума до сплати:
                        <span style="color: red">
                            {total_price} грн
                        </span>
                    </h2>
                """
            #
            success = send_mail(subject, '', 'InternetShop "STEP"', [user_email], fail_silently=False, html_message=body)
            if success:
                return render(request, 'orders/success.html', {
                    'page_title': "Подяка за замовлення",
                    'email': user_email
                })
            else:
                return render(request, 'orders/failed.html', {
                    'page_title': "Помилка поштового відправлення",
                })


def success(request):
    
    return render(request, 'orders/success.html', {
        'page_title': "Подяка за замовлення",
        
    })             

def ajax_delivery_info(request):
    response = dict()
    order_id = request.GET['order']
    init = request.GET['init']
    first = request.GET['first']
    last = request.GET['last']
    phone = request.GET['phone']
    company = request.GET['company']
    city = request.GET['city']
    # depot = request.GET['depot']
    # address = request.GET['address']
    # info = request.GET['info']
    #
    response['order'] = order_id
    response['init'] = init
    response['first'] = first
    response['last'] = last
    response['phone'] = phone
    response['company'] = company
    response['city'] = city
    # response['depot'] = depot
    # response['address'] = address
    # response['info'] = info
    #
    user_id = request.user.id
    current_user = User.objects.get(id=user_id)
    current_user.first_name = first
    current_user.last_name = last
    current_user.save()
    #
    new_delivery = Delivery.objects.create(
        user = User.objects.get(id=user_id),
        order = Order.objects.get(id=order_id),
        phone = phone,
        company = company,
        city = city,
    )
    delivery_id = new_delivery.id
    response['delivery_id'] = delivery_id
    if first and last and phone and company and city:
        response['result'] = "Ok"
    return JsonResponse(response)
