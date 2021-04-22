from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    products= Product.objects.all()
    #return HttpResponse("this is the beginning")
    return render(request,'index.html',
                  {'products':products})

def new(request):
    return HttpResponse("this is a new page")

