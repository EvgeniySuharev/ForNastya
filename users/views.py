from django.shortcuts import render


def index(request):
    return render(request, 'myapp/test.html', {'title': 'template title'})
