from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product

# Create your views here.
def index(request):
    name = "dio brando"
    age = 500
    return render(request, "index.html", {"name":name, "age":age})

def db(request):
    all_products = Product.objects.all
    some_products = Product.objects.filter(price__gt=2500)
    return render(request, "db.html", {"all_products": all_products, "some_products": some_products})

def hello(request):
    return HttpResponse("<h1>Hello<h1>")