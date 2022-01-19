from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from Todo.models import Todo
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


# Create your views here.

@login_required(login_url='login')
def home(request):

    tasks = Todo.objects.all().order_by('-date_added')
    return(render(request,'Todo/base.html',{'todo_items':tasks}))

@login_required(login_url='login')
def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']

    if content:
        # new_item = TodoItem(content=content,currentUser = request.user)
        #saving each new task created
        Todo.objects.create(date_added = current_date, task= content ,currenUser = request.user )
       
    return HttpResponseRedirect('/')

@login_required(login_url='login')
def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/') 


class ItemListView(ListView):
    model = Todo
    template_name = "Todo/base.html" 
    context_object_name = "todo_items"

    def get_queryset(self):
        return Todo.objects.filter(currentUser=self.request.user)       