from django.shortcuts import render


def skating(request):
    context = {
        "title": 'Skating sahifasi'
    }
    return render(request, 'skating.html', context)
