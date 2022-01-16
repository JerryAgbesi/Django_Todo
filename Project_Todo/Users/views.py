from email import message

from django.shortcuts import render
from .forms import Registrationform
from django.contrib.messages import constants as messages
# Create your views here.
def register(request):
    form = Registrationform
    if request == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.SUCCESS(request,f'account created for {username}')
        else :
            messages.ERROR(request,'error creating account')    
        

    context = {'form':form}        
    return(render(request,'Users/register.html',context,))

def login(request):
    return (render(request,'Users/login.html'))
