from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {
        'page_title': 'Головна'
    })


def about(request):
    return render(request, 'home/about.html', {
        'page_title': 'Про сайт'
    })


def contacts(request):
    return render(request, 'home/contacts.html', {
        'page_title': 'Контакти'
    })


def news(request):
    return render(request, 'home/news.html', {
        'page_title': 'Новини'
    })
