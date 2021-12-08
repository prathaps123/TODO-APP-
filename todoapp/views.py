from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
# Create your views here.

def base(request):
    if request.method == "POST":
        x=request.POST['todo']
        Data= Todata(data=x)
        print(Data)
        Data.save()
    todata=Todata.objects.all()
    return render(request,'home.html',{'todata':todata})

def remove(request,i):
    x=Todata.objects.get(id=i)
    x.delete()
    todata=Todata.objects.all()
    return redirect('/')

def update(request,i):
    t=Todata.objects.get(id=i)# it will fetch id and data
    if request.method=="POST":
        x1=request.POST['u1']
        yy=Todata(data=x1)
        yy.save()
        return redirect('/')
    return render(request,'update.html',{'t':t})
        
