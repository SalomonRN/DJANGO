from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_view(request):
    return HttpResponse("<h1>HOLA MUNDO!</h1>")
    
def gmail_view(request):
    return render(request, "index.html")
