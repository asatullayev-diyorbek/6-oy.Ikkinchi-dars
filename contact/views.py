from django.shortcuts import render


def contact(request):
    context = {
        "title": 'Contact sahifasi'
    }
    return render(request, 'contact.html', context)
