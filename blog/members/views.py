from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

def blog(request):
    return render(request, "blog.html", {})

def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')

        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, '')  
    return render(request, "register.html")

def blogs(request):
    return render(request,"blogs.html")



