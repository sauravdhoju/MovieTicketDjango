from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from core.models import MovieSchedule


# from django.render import render redirect/
# Create your views here.
def index(request):
    return render(request, 'home.html')

    # @login_required(login_url = 'loginSignup')
    # def movie(request, movie_id):
    #     try:
    #         movie = Movie.objects.get(pk=movie_id)  # pk stands for primary key
    #     except movie.DoesNotExist:
    #         return render(request, 'movie_not_found.html')
    #     if movie:
    #         print(movie)
    #         return render(request, 'movie.html', {'movie': movie})
    #
    # def search(request, movie_name):
    #     movies_in_db = Movie.objects.all()
    #     movie_list
    #     for movie in movies_in_db:
    #         if movie.name == movie_name:
    #
    #
    #     return render(request, 'movie.html', )


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username, email, password1)
        if password1 != password2:
            return HttpResponse("Your password and confirm password are not same.")
        else:
            my_user = User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect('login') 
    return render(request, 'signup.html')    

def log_in(request):
    if request.method=='POST':
        username=request.POST.get('username')
        passsword=request.POST.get('password')  
        user=authenticate(request, username=username,password=passsword)
        if user is not None:
            login(request,user)
            return redirect("seat.html")
        else:
            return redirect('signup') 
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('login')