from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from . forms import Movieform
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list': movie
    }
    return render(request,'index.html',context)
    # return render(request,'index.html')

# def details(request):
#     return render(request, 'details.html')
def details(request,movie_id):
        movie=Movie.objects.get(id=movie_id)
        return render(request,'details.html',{'movie':movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image = request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=image)
        movie.save()
        return redirect('/')
    return render(request,'add.html')

def update_movie(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
    # return render(request, 'edit.html')
def delete_movie(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')