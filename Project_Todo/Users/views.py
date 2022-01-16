from django.shortcuts import render
from .forms import Registrationform

# Create your views here.
def register(request):
    form = Registrationform
    if request == 'POST':
        form = Registrationform
        if form.is_valid():
            form.save()
        

    context = {'form':form}        
    return(render(request,'Users/register.html',context))

def login(request):
    return (render(request,'Users/login.html'))
