from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render


def good (request):
    return HttpResponse("<h1>ГУГУГАГА</h1>")


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')