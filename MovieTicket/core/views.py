from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from core.models import MovieSchedule
import requests, json
from . models import Movie, Genre, MovieToGenre
from django.contrib import messages
import re

def home(request):
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
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # print(email)
        # print(is_valid_email(email))
        if not username or not password1 or not email or not password2:
            messages.error(request, 'Please fill out all the fileds.')
            return render(request, 'signup.html')
        elif password1 != password2:
            messages.error(request, "Password didn't matched!")
            return render(request, 'signup.html')
        elif len(password1)<8:
            messages.error(request, "Your password must be at least 8 characters long")
            return render(request, 'signup.html')
        elif not is_valid_email(email):
            messages.error(request, "Invalid email address.")
            return render(request, 'signup.html')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists')
            return render(request, 'signup.html')
        else:
            user = User.objects.create_user(username,email,password1)
            user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def log_in(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')  
        print(username, password)
        user=authenticate(request, username=username,password=password)
        if not username or not password:
            messages.error(request, 'Please fill out all the fields.')
        if user is None:
            messages.error(request, 'Couldn\'t find your account!')
        else:
            login(request,user)
            return redirect("home")
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('login')

def addMovie(request):
    if request.method=='POST':
        name = request.POST.get('name')
        description = request.POST.get('description'),
        if Movie.objects.filter(name=movie_name).exists():
            messages.error(request, 'The movie is already added! add another movie.')
            return render(request, 'addMovie.html')
        elif not name or not description:
            messages.error(request, 'please fill all the forms!')
            return render(request, 'addMovie.html')
        else:
            movie = Movie(name = name, description  = description, added_date=timezone.now())
            movie.save()
            genre_string = dic['Genre']
            for g in genre_string.split(","):
                if not Genre.objects.filter(name=g).exists():
                    new_genre = Genre(name=genre)
                    print(f'{g} is new.')
                    # new_genre.save()
                else:
                    print(f'{g} is already present.')
                gen = Genre.objects.get(name=g)
                movie.genre_set.add(gen)
            # movie.save()
            print(genre_string, ' ? ', movie.genre_set.all())
            messages.success(request, movie_name+' was successfully added!.')
            return render(request, 'addMovie.html')
    return render(request, 'addMovie.html')

# def addMovie(request):
#     if request.method=='POST':
#         movie_name = request.POST.get('movie_name')
#         if Movie.objects.filter(name=movie_name).exists():
#             messages.error(request, 'The movie is already added! add another movie.')
#             return render(request, 'addMovie.html', {'created': True})
#         # dic = parse(movie_name) api not working at all + json is unparsable
#         # print(dic)
#         dic = {
#                 'Name':          movie_name,
#                 'Plot':          request.POST.get('Description'),
#                 'Genre':         request.POST.get('Genres'),
#                 }
#         if dic == None:
#             messages.error(request, 'couldnt find the movie through api! for it')
#             print(movie_name)
#             return render(request, 'addMovie.html')
#         else:
#             movie = Movie(name = dic['Name'],
#                           description  = dic['Plot'],
#                           added_date=timezone.now(),
#                           )
#             print([ dic['Name'], dic['Plot'], timezone.now()])
#             genre_string = dic['Genre']
#             for g in genre_string.split(","):
#                 if not Genre.objects.filter(name=g).exists():
#                     new_genre = Genre(name=genre)
#                     print(f'{g} is new.')
#                     # new_genre.save()
#                 else:
#                     print(f'{g} is already present.')
#                 gen = Genre.objects.get(name=g)
#                 movie.genre_set.add(gen)
#             # movie.save()
#             print(genre_string, ' ? ', movie.genre_set.all())
#             messages.success(request, movie_name+' was successfully added!.')
#             return render(request, 'addMovie.html')
#     return render(request, 'addMovie.html')



# def parse(movie_name):
#     '''returns Title, Plot, imdbRating, Actors,
#     Genre, Director, Runtime, Language, Writer'''
#     url = "http://www.omdbapi.com/"
#     api_key = "dfc1ebee"
#     response = requests.get(url, params={
#         "apikey": api_key,
#         "t": movie_name
#         })
#     if response.status_code == 200:
#         return json.loads(response.json())    
#     else:
#         api_key = "1b40d701"
#         response = requests.get(url, params={
#             "apikey": api_key,
#             "t": movie_name
#             })
#         if response.status_code == 200:
#             return json.loads(response.json())    
#         else:
#             return None

def ticket(request):
    return render(request, 'ticket.html')
