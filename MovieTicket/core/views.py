from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from . models import Movie, MovieSchedule
# from fuzzywuzzy import process

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
            print('login:',username)
            user=authenticate(request, username=username,password=passsword)
            # if user is not None:
            #     login(request,user)
        elif 'signup' in request.POST:
            username = request.POST.get('Username')
            password = request.POST.get('Password')
            email    = request.POST.get('Email')
            print(username, email)
            my_user = User.objects.create_user(username,email)
    #         my_user.save()
            # return render(request, 'login.html')
    else:
        return render(request, 'login_signup.html') 

    @login_required(login_url = 'loginSignup')
    def movie(request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)  # pk stands for primary key
        except movie.DoesNotExist:
            return render(request, 'movie_not_found.html')
        if movie:
            print(movie)
            return render(request, 'movie.html', {'movie': movie})

    # @login_required(login_url = 'loginSignup')
    # def search(request):
    # if request.method == 'POST':
    #     tagList = request.POST.get('tagList')
    #     movie_name = request.POST.get('movie_name')
    #     # filteredMovies = Movie.objects.filter(genres__name__in=['Action', 'Adventure'])
    #     # movies_in_db = Movie.objects.all()
    #     filteredMovies = Movie.objects.filter(genres__name__in=tagList)
    #     matching_names = process.extract(target_movie_name, queryset.values_list('name', flat=True), limit=None)
    #     matching_movies = [name for name, score in matching_names if score >= threshold]
    #     search_result = queryset.filter(name__in=matching_movies)
    #     return render(request, 'search.html', { 'movie_list': search_result, 'movie_name': movie_name, 'tags': tags })
    # else:
    #     return render(request, 'search.html', {})
