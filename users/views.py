from django.shortcuts import render


def index(request):
    return render(request, 'users/index.html', {'title': 'template title'})
