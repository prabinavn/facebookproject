from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def fn_home(request):
    return HttpResponse('hello')

def fn_facebook(request):
    
    if request.method == 'POST':
        first_name    = request.POST['firstname']
        last_name     = request.POST['lastname']
        user_dob      = request.POST['dob']
        gender        = request.POST['gender']

        user_name     = request.POST['username']
        password      = request.POST['password']
        
        login_obj     = Login(username=user_name,password=password)
        login_obj.save()
        if login_obj.id > 0:
            register_obj  = Register(firstname=first_name,lastname=last_name,dob=user_dob,gender=gender,loginForm=login_obj)
            register_obj.save()
            if register_obj.id > 0:
                return render(request,'facebook.html',{"message": "You have successfully registered"})  
            else:
                return HttpResponse('failed') 
    return render(request,'facebook.html')  

def fn_login(request):
    if request.method == 'POST':
        user_name     = request.POST.get('username')
        user_psw      = request.POST.get('password')
        check      = Login.objects.filter(username=user_name).exists()
        if check:
            login = Login.objects.get(username=user_name)
            if user_name == login.username and user_psw == login.password:
                request.session['userId'] = login.id
                return render(request,'home.html')  
            else:
                return HttpResponse('login failed')


def fn_home(request):
    if request.method == 'POST':
        currentpassword = request.POST['mypassword']
        newpass     = request.POST['newpassword']
        user_obj = Login.objects.get(id=request.session['userId'])
        if user_obj.password == currentpassword:
            user_obj.password = newpass
            user_obj.save()
            return HttpResponse( 'password changed')
        return HttpResponse('old password does not match')
    return render(request,'password.html')                    
           

def fn_userProfile(request):
    id = request.session['userId']
    log_obj = Login.objects.get(id=id)
    user = Register.objects.get(loginForm=id)
    new_image = ''
    try:
        
        if request.method == 'POST':
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            updation = 0
           
            if user.firstname != fname:
                user.firstname = fname
                updation += 1
            if user.lastname != lname:
                user.lastname = lname
                updation += 1
            if updation > 0:
                user.save()
            
            if request.FILES:
                new_image = request.FILES['profilepic']
                user_image_obj = Profile_Pic.objects.get(fk_login=id)
                user_image_obj.image.delete()
                user_image_obj.image = new_image
                user_image_obj.save()
                user.image = user_image_obj.image
            
        # user_image_obj = Profile_Pic.objects.get(fk_login=id)
        # user.image = user_image_obj.image

    except Profile_Pic.DoesNotExist:
        if request.method == 'POST':
            image_obj = Profile_Pic(image=new_image,fk_login=log_obj)
            image_obj.save()
            user.image = image_obj.image
            return render(request,'profile.html', {'data':user})      
        return render(request,'profile.html', {'data':user})
    return render(request,'profile.html', {'data':user})








