from email import message
from django.shortcuts import render,redirect
from .forms import Registrationform
from django.contrib import  messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def register(request):
    form = Registrationform()
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            
            username = form.cleaned_data.get('username')
         
            messages.success(request,f'account created for {username}')
            return redirect('login')
        else :
            print(form.error_messages)
            messages.error(request,'error creating account')    
        

    context = {'form':form}        
    return(render(request,'Users/register.html',context,))

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request,username = username,password= password)   

        if user is not None:
            login(request,user)
            return redirect('Home')
        
        else:
            messages.info(request,'username or password is incorrect')


    context = {}

    return (render(request,'Users/login.html',context))

def logoutUser(request):
    logout(request)
    return redirect('login')
