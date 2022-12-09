from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse


def reg(request):
    admin_email = "admin@gmail.com"
    if request.method == 'GET':
        return render(request, 'account/reg.html')
    elif request.method == "POST":
        # 1. Зчитуємо із форми реєстраційні дані
        _login = request.POST.get('login')
        _pass1 = request.POST.get('pass1')
        _pass2 = request.POST.get('pass2')
        _email = request.POST.get('email')

        # 2. Сценарій реєстрації
        report = dict()
        new_user = User.objects.create_user(_login, _email, _pass1)
        if new_user is None:
            report['mess'] = 'У реєстрації відмовлено!'
        else:
            report['mess'] = 'Ви успішно зареєстровані!'
            # 3.1 Готуємо поштове повідомлення для підтвердження реєстрації
            url = f'http://localhost:8000/account/confirm?email={_email}'
            subject = 'Підтвердження реєстрації на сайті InternetShop'
            body = f"""
                <hr />
                <h3>Для підтвердження реєстрації перейдіть за посиланням</h3>
                <h4>
                    <a href="{url}">{url}</a>
                </h4>
                <hr />
            """
            # subject_admin = 'Реєстрація нового клієнта!'
            # body_admin = f"""
            #     <hr />
            #     <h3>Гарна новина!</h3>
            #     <h3>Реєстрація нового клієнта прошла успішно!</h3>
            #     <h4>
            #         Логін: {_login}
            #         E-mail: {_email}
            #     </h4>
            #     <hr />
            # """
            # 4.Відправляємо поштове повідомлення
            success = send_mail(subject, '', 'InternetShop', [_email], fail_silently=False, html_message=body)
            # feedback = send_mail(subject_admin, '', 'Нова реєстрація', [admin_email], fail_silently=False, html_message=body_admin)
            if not success:
                report['info'] = 'Ваша пошта не дійсна!'
            else:
                report['info'] = f"""
                На вказаний Вами при реєстрації E-mail {_email}
                відправлено повідомлення!
            """
        # !. Завантажуємо звіт на сторінку результатів
        return render(request, 'account/reg_res.html', context=report)


def entry(request):
    if request.method == 'GET':
        return render(request, 'account/entry.html')
    elif request.method == "POST":
        # 1. Зчитуємо із форми авторізаційні дані
        _login = request.POST.get('login')
        _pass1 = request.POST.get('pass1')
        # 2. Сценарій авторизації
        report = dict()
        check_user = authenticate(request, username=_login, password=_pass1)
        if check_user is None:
            report['mess'] = 'Користувач не знайдений!'
        else:
            report['mess'] = 'Ви успішно авторизовані!'
            login(request, check_user)
            
        return render(request, 'account/entry_res.html', context=report)


def confirm(request):
    # # Считуємо Email від якого прийшло підтверждення (з get параметра в def reg(request)
    # email = request.GET.get('email')

    # user = User.objects.filter(email=email)
    # group = User.groups.filter(name="New-Users")
    # User.groups.add(group)
    # # Треба створити в адмінці таку групу
    return render(request, 'account/confirm.html')


def exit(request):
    logout(request)
    return redirect('/home')


def profile(request):
    return render(request, 'account/profile.html')


def reset(request):
    return render(request, 'account/reset.html')


def reg_res(request):
    return render(request, 'account/reg_res.html')


def entry_res(request):
    return render(request, 'account/entry_res.html')


def ajax_signup(request):
    response = dict()
    login = request.GET['login']
    response['message_login'] = login
    #
    # user_check = User.objects.get(username=login)
    # if user_check:
    #     user_name = user_check.username
    #     response['user_name1'] = user_name
    #     response['ajax_message1'] = "Ok"
    # else:
    #     response['user_name2'] = "Немає такого логіну"
    #     response['ajax_message2'] = "not Ok"
    # #    
    # if user_check.DoesNotExist:
    #     response['ajax_message3'] = "Немає такого логіну"
    # elif user_check:
    #     user_name = user_check.username
    #     response['user_name1'] = user_name
    #     response['ajax_message1'] = "Ok"
    #
    users_check = User.objects.filter(username=login)
    if len(users_check) >= 1:
        response['ajax_message'] = "Ok"
        response['quntity'] = len(users_check)
    else:
        response['ajax_message'] = "not Ok"
        response['quntity'] = len(users_check)
    return JsonResponse(response)

"""
    Якщо user_name != login, то дана функція не працює (не повертає нічого, навіть response['message_login'] = login)
"""

def ajax_email(request):
    response = dict()
    user_email = request.GET['email']
    response['message_email'] = user_email
    #
    email_check = User.objects.filter(email=user_email)
    if len(email_check) >= 1:
        response['ajax_email'] = "Ok"
        response['quntity'] = len(email_check)
    else:
        response['ajax_email'] = "not Ok"
        response['quntity'] = len(email_check)
    return JsonResponse(response)
