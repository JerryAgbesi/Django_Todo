from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register,name='sign_up'),
    path('login/',views.login,name='login'),
  
]
