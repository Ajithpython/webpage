from django.shortcuts import render
from django.http import HttpResponse
from .models import product


# Create your views here.
def fun(request):
    obj = product()
    obj.name = "powerful theme"
    obj.price = 100
    obj = product.objects.all()

    return render(request, "index.html", {'results': obj})

def addition(request):
    nu1=int(request.POST["num1"])
    nu2=int(request.POST["num2"])
    num3=nu1+nu2
    return render(request,"result.html",{"add":num3})
