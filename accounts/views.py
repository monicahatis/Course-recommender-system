from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from .models import UserTable
from .form import (
    SignINForm,
    SignUpForm
)

# Create your views here.


def logout_user(request):
    if request.method=="POST":
        logout(request)
        return HTTPResponse("lOGGED OUT SUCCESSFULLY")
    # return redirect("homepage:homepage")


def signIn(request):

    login_form = SignINForm(request.POST,None)

    
    context = {
        'login' : login_form
    }
    if login_form.is_valid:
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(request,username = username, password = password )
        print("jjja",user)
        if user is not None:
        
            login(request,user)
            return redirect("homepage:homepage")
        else:
            pass
    
    return render(request,'sign-in.html',context)


def signUp(request):
    sign_up = SignUpForm(request.POST,None)

    context =  { 
        "form" :sign_up
    }
    if request.method == "POST":
        if sign_up.is_valid:
         
            first_name = request.POST.get("firstName")
            last_name =  request.POST.get("lastName")
            phone =  request.POST.get("phone")
            email = request.POST.get('email')
            password = request.POST.get("password")
            user = authenticate(request,username = email, password = password )
            if user is not None:
                print("user exists")
                return redirect("account:sign_in")
            else:
                    
                user = UserTable.objects.create_user(username = email , email = email , password = password)
                user.last_name = last_name
                user.first_name = first_name
        
                user.phone = phone
                
                user.save()
                user = authenticate(request,username = email, password = password )
                print("jjja",user)
                if user is not None:
                    
                    login(request,user)
                    return redirect("homepage:raisec")
                else:
                    pass
                # return redirect("homepage:raisec")
    return render(request,'sign-up.html',context)