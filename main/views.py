from django.shortcuts import render


def index(request):
    context = {
        "title": 'Bosh sahifa'
    }
    return render(request, 'index.html', context)
