from django.shortcuts import render


def about(request):
    context = {
        "title": 'About sahifasi'
    }
    return render(request, 'about.html', context)

