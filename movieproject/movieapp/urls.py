from django.urls import path, include
from . import views

app_name= 'movieapp'
urlpatterns = [
    path('', views.index, name='index'),
    # path('details/', views.details, name='details'),
    path('details/<int:movie_id>/', views.details, name='details'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update_movie, name='update'),
    path('delete/<int:id>/', views.delete_movie, name='delete'),
]