from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_view(request):
    return HttpResponse("<img src='here'>HOLA</img>")