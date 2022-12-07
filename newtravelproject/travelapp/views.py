# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team


def demo(request):
    # return HttpResponse("Hello World?")
    obj=Place.objects.all()
    team_obj= Team.objects.all()
    return render(request, "index.html",{'result':obj,'team_result': team_obj})
