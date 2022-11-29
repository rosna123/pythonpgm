# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    name="Mathematics"
    return render(request,"home.html", {'obj': name})
def about(request):
    return render(request,"about.html")
def contact(request):
   return HttpResponse("rosnamajeed@gmail.com")
def details(request):
    return render(request,"details.html")
def thanks(request):
    return HttpResponse("Thank you")
def operations(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return render(request,"result.html",{'add':add,'sub':sub,'mul':mul,'div':div,'num1':x,'num2':y})
