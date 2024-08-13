from django.shortcuts import render


def shop(request):
    context = {
        "title": 'Shop sahifasi'
    }
    return render(request, 'shop.html', context)
