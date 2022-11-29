from django.urls import path
from . import views
app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('classbvhome/', views.TaskListView.as_view(), name='classbvhome'),
    path('classbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='classbvdetail'),
    path('classbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='classbvupdate'),
    path('classbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='classbvdelete'),
]
