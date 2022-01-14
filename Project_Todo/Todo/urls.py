from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='Home'),
    path('add/',views.add_todo,name='add_task'),
    path('delete_task/<int:todo_id>/',views.delete_todo,name='delete_task')
]
