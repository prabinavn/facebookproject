from django.urls import path
from . import views
app_name='facebookapp'

urlpatterns =[
    path('home/',views.fn_home),
    path('facebook/',views.fn_facebook),
    path('login/',views.fn_login),
    path('password/',views.fn_home,name='password'),
    path('profile/',views.fn_userProfile, name='profile'),
    

]