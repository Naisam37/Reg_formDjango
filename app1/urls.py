from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.SignUp,name='signup'),
    path('login/',views.Login,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout',views.LogOut,name='logout'),
    
]