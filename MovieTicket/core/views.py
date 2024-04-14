from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required


# from django.render import render redirect/
# Create your views here.
def index(request):
    return render(request, 'home.html')

def login_signup(request):
    return render(request, 'login_signup.html') 
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse("Your password and confirm password are not same.")
        else:
            my_user = User.objects.create_user(username,email,password1)
            my_user.save()
            # return redirect('login') 
    return render(request, 'login_signup.html') 
    if request.method=='POST':
        username=request.POST.get('username')
        passsword=request.POST.get('password')  
        user=authenticate(request, username=username,password=passsword)
        if user is not None:
            login(request,user)
            bmi_user=user.username
            return redirect("calculate")
        else:
            return redirect('signup') 

    return render(request, 'login.html')
