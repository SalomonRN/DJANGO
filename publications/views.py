from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def first_view(request):
    return HttpResponse("<h1>HOLA MUNDO!</h1>")
    
def gmail_view(request):
    return render(request, "index.html")

@login_required
def dashboard(request):
    return HttpResponse("Hola, mundo!")