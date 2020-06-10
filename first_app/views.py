from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Register

def app(request):
    a=Register.objects.all()
    b=request.POST.get("save")
    if b=="Submit":
        d=Register()
        c=request.POST.get("user")
        e=request.POST.get("pass")
        d.username=c
        d.password=e
        d.save()
        return redirect('/')
    else:
        return render(request,'ab.html',{"a":a})    

def login(request):
    r=Register.objects.all()
    a=request.POST.get('user')
    b=request.POST.get('pass')
    try:
        c=Register.objects.filter(username=a,password=b)
        if c:
            return render(request,'test1.html',{"c":c})
        else:
            return render(request,'login.html',{'r':r})
    except:
        return render(request,'login.html',{'r':r}) 
    return render(request,'login.html',{'r':r})               
def home(request):
    return render(request,'a.html')
def about(request):
    return render(request,'b.html')
def gallery(request):
    return render(request,'c.html')
def contact(request):
    return render(request,'d.html')