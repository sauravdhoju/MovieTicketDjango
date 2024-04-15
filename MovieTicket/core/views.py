from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from . models import Movie, MovieSchedule


# from django.render import render redirect/
# Create your views here.
def index(request):
    return render(request, 'home.html')

def login_signup(request):
    # return render(request, 'login_signup.html') 
    if request.method == 'POST':
        if 'login' in request.POST:
            username=request.POST.get('username')
            passsword=request.POST.get('password')  
            user=authenticate(request, username=username,password=passsword)
            if user is not None:
                login(request,user)
                return redirect("calculate")

        elif 'signup' in request.POST:
            username = request.POST.get('Username')
            password = request.POST.get('Password')
            email    = request.POST.get('Email')
    else:
        return render(request, 'login_signup.html') 
    #         my_user = User.objects.create_user(username,email,password1)
    #         my_user.save()
    #         # return redirect('login') 
    # if request.method=='POST':
    #
    # return render(request, 'login.html')

    @login_required(login_url = 'loginSignup')
    def movie(request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)  # pk stands for primary key
        except movie.DoesNotExist:
            return render(request, 'movie_not_found.html')
        if movie:
            print(movie)
            return render(request, 'movie.html', {'movie': movie})

    def search(request, movie_name):
        movies_in_db = Movie.objects.all()
        movie_names = [movie.name for movie in movies_in_db]
        if movie_name in movie_names:
            return redirect(request, '')
