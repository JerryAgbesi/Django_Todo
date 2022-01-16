from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from Todo.models import Todo
# from django import 

# Create your views here.

def home(request):

    tasks = Todo.objects.all().order_by('-date_added')


    return(render(request,'Todo/base.html',{'todo_items':tasks}))

def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']

    Todo.objects.create(date_added = current_date, task= content )

    return HttpResponseRedirect('/')

def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')    