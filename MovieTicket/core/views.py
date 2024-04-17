from django.shortcuts import render, redirect, HttpResponse, get_object_or_404 
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
import requests, json
from . models import *
from django.contrib import messages
import re
from fuzzywuzzy import fuzz, process

class moviex():
    def __init__(self, movie_name):
        self.movie     = Movie.objects.get(name=movie_name)
        self.genres    = MovieToGenre.objects.filter(movie=movie_name)
        self.actors    = MovieToActor.objects.filter(movie=movie_name)
        self.writers   = MovieToWriter.objects.filter(movie=movie_name)
        self.directors = MovieToDirector.objects.filter(movie=movie_name)
        self.languages = MovieToLanguage.objects.filter(movie=movie_name)

def retriveMovieListObj(movieList):
    movies = []
    for m in movieList:
        movie = moviex(m)
        if len(movie.languages)>0:
            movies.append(movie)
    return movies

def home(request):
    addMovieData()
    return render(request, 'home.html', {
        'swipierMovieGenre': retriveMovieListObj([  "Spider-Man: No Way Home",
                                                    "Doctor Strange in the Multiverse of Madness",
                                                    "Black Panther: Wakanda Forever"]),
                  's1movies': retriveMovieListObj([ "Dune",
                                                    "Eternals",
                                                    "The Matrix Resurrections",
                                                    "Uncharted",
                                                    "Ambulance", ]),
                  's2movies': retriveMovieListObj([ "The Lost City",
                                                    "Morbius",
                                                    "Marry Me",
                                                    "Old",
                                                    "Free Guy", ]),
                  's3movies': retriveMovieListObj([ "The Night House",
                                                    "In the Heights",
                                                    "Queen Bees",
                                                    "Luca",
                                                    "No Sudden Move", ])
                  })
@login_required(login_url = 'login')
def moviePage(request, movie_id):
    if request.method=='POST':
        comment =request.POST.get('user_comment')
        c = Comment( movie = Movie.objects.get(pk=movie_id),
                    user = request.user,
                    comment = comment,
                    likes = 0,
                    dislikes = 0,
                    added_date = timezone.now()
                )
        c.save()
    if Movie.objects.filter(id=movie_id).exists():
        movie = Movie.objects.get(pk=movie_id)
        m=retriveMovieListObj([movie.name]),
        schedules = MovieSchedule.objects.filter(movie=movie_id)
        comments = Comment.objects.filter(movie=movie_id)
        return render(request, 'specific_movie.html', {
            'movie': m[0][0], 
            'schedules': schedules,
            'isSuperuser': request.user.is_superuser,
            'comments': comments
            })
    else:
        return render(request, 'page_not_found.html')

@login_required(login_url = 'login')
def ticket(request):
    t=Ticket.objects.filter(user=request.user)
    return render(request, 'yourticket.html', { 'yourTickets' : t})

@login_required(login_url = 'login')
def bookMoviePage(request, movie_id, schedule_id):
    if request.method=='POST':
        seatsSelected =request.POST.get('selectedSeats')
        seatsSelected  = parse_integers(seatsSelected)
        seats = Seat.objects.filter(schedule_id=schedule_id).order_by('id')
        firstIndex = seats[0].id
        print(firstIndex)
        for seat in seatsSelected:
            s=Seat.objects.get(pk=seat)
            s.isAvailable= False
            s.number = s.id-firstIndex+1
            # print('number', firstIndex)
            s.save()
            newTicket = Ticket(seat=s,
                               user = request.user,
                               schedule = MovieSchedule.objects.get(pk=schedule_id),
                               ticket_code = str(request.user)+str(schedule_id)+str(seat),
                               creation_date = timezone.now())
            newTicket.save()
        # print("seats:",seatsSelected)
        return redirect('yourTickets')
    else:
        if Movie.objects.filter(id=movie_id).exists():
            movie = Movie.objects.get(pk=movie_id)
            m=retriveMovieListObj([movie.name]),
            schedule = MovieSchedule.objects.get(pk=schedule_id)
            seats = Seat.objects.filter(schedule_id=schedule_id).order_by('id')
            tickets = Ticket.objects.filter(user=request.user)
            # print(tickets)
            userSeats = [ticket.seat.id for ticket in tickets]
            # print(userSeats)
            # print(len(seats))
            return render(request, 'book.html', {
                'movie': m[0][0],
                'schedule': schedule,
                'seats' : seats,
                'userSeats': userSeats
                })
        else:
            return render(request, 'page_not_found.html')


def addSchedule(request, movie_id):
    movie =  Movie.objects.get(pk=movie_id)
    if request.method=='POST':
        dateTime=request.POST.get('Scheduled_DateTime')
        location=request.POST.get('location')  
        seat_count=request.POST.get('seat_count')  
        premiumSeats = request.POST.get('premiumSeats')
        # print(seat_count)
        if not dateTime or not location or not seat_count or not premiumSeats:
            messages.error(request, 'Please fill out all the fields.')
        # if not dateTime or not location or not seatCount:
        #     messages.error(request, 'Please fill out all the fiel
        else:
            print(premiumSeats)
            premiumSeats = parse_integers(premiumSeats)
            print(premiumSeats)
            schedule = MovieSchedule(movie=movie,
                          schedule_date=dateTime,
                          location = location,
                          seat_count= seat_count
                          ) 
            schedule.save()
            for i in range(1, int(seat_count)+1):
                if i not in premiumSeats:
                    create_seat = Seat( schedule_id = schedule,
                                       isPremium = False,
                                       isAvailable = True,
                                       number = i)
                else:
                    create_seat = Seat( schedule_id = schedule,
                                       isPremium = True,
                                       isAvailable = True,
                                       number = i)
                create_seat.save()
            messages.success(request, 'successfully added the schedule.')
    return render(request, 'addSchedule.html', {'movie':movie})

def parse_integers(string):
    integer_list = []
    for part in string.split(','):
        part = part.strip()
        if part.isdigit():  
            integer_list.append(int(part))
    return integer_list

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

# def addMovie(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description'),
#         if Movie.objects.filter(name=movie_name).exists():
#             messages.error(request, 'The movie is already added! add another movie.')
#             return render(request, 'addMovie.html')
#         elif not name or not description:
#             messages.error(request, 'please fill all the forms!')
#             return render(request, 'addMovie.html')
#         else:
#             movie = Movie(name = name, description  = description, added_date=timezone.now())
#             movie.save()
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

def addMovieData():
    with open('movies_data.json', 'r') as file:
        data = json.load(file)
    for movie_name, movie_data in data.items():
        if movie_data["Response"] == "False":
            print(f"Couldn't find the {movie_name} in JSON.")
            continue  

        if Movie.objects.filter(name=movie_name).exists():
            print(f"{movie_name} already exists in db.")
            return  
        movie = Movie(
            name=movie_data['Title'],
            description=movie_data['Plot'] + '\nAwards' + movie_data['Awards'],
            added_date=timezone.now(),  # Use datetime.now(timezone.utc)
            # released_date=datetime.strptime(movie_data['Released'], "%d %b %Y").date(),  # Parse date format
            average_rating=movie_data['imdbRating'],
            length=movie_data['Runtime'],
            poster=movie_data['Poster'],
        )
        movie.save() 

        genre_string = movie_data['Genre']
        genres_to_create = []  # List for bulk creation
        movietogenres_to_create = []  # List for bulk creation
        for genre_name in genre_string.split(","):
            genre_name = genre_name.strip()
            if not Genre.objects.filter(name=genre_name).exists():
                genres_to_create.append(Genre(name=genre_name))
                print(f'{genre_name} added')
            movietogenres_to_create.append(Genre(name=genre_name))
        Genre.objects.bulk_create(genres_to_create)
        for genre in Genre.objects.filter(name__in=[g.name for g in movietogenres_to_create]):
            MovieToGenre.objects.create(movie=movie.name, genre=genre.name)
            

        actor_string = movie_data['Actors']
        actors_to_create = []  # List for bulk creation
        mactors_to_create = []  # List for bulk creation
        for actor_name in actor_string.split(","):
            actor_name = actor_name.strip()
            if not Actor.objects.filter(name=actor_name).exists():
                actors_to_create.append(Actor(name=actor_name))
                print(f'{actor_name} added')
            mactors_to_create.append(Actor(name=actor_name))
        Actor.objects.bulk_create(actors_to_create)
        for actor in Actor.objects.filter(name__in=[g.name for g in mactors_to_create]):
            MovieToActor.objects.create(movie=movie.name, actor=actor.name)

        writer_string = movie_data['Writer']
        writers_to_create = []  # List for bulk creation
        mwriters_to_create = []  # List for bulk creation
        for writer_name in writer_string.split(","):
            writer_name = writer_name.strip()
            if not Writer.objects.filter(name=writer_name).exists():
                writers_to_create.append(Writer(name=writer_name))
                print(f'{writer_name} added')
            mwriters_to_create.append(Writer(name=writer_name))
        Writer.objects.bulk_create(writers_to_create)
        for writer in Writer.objects.filter(name__in=[g.name for g in mwriters_to_create]):
            MovieToWriter.objects.create(movie=movie.name, writer=writer.name)

        director_string = movie_data['Director']
        directors_to_create = []  # List for bulk creation
        mdirectors_to_create = []  # List for bulk creation
        for director_name in director_string.split(","):
            director_name = director_name.strip()
            if not Director.objects.filter(name=director_name).exists():
                directors_to_create.append(Director(name=director_name))
                print(f'{director_name} added')
            mdirectors_to_create.append(Director(name=director_name))
        Director.objects.bulk_create(directors_to_create)
        for director in Director.objects.filter(name__in=[g.name for g in mdirectors_to_create]):
            MovieToDirector.objects.create(movie=movie.name, director=director.name)
        print(f"{movie_name} added successfully!")
        language_string = movie_data['Language']
        languages_to_create = []  # List for bulk creation
        mlanguages_to_create = []  # List for bulk creation
        for language_name in language_string.split(","):
            language_name = language_name.strip()
            if not Language.objects.filter(name=language_name).exists():
                languages_to_create.append(Language(name=language_name))
                print(f'{language_name} added')
            mlanguages_to_create.append(Language(name=language_name))
        Language.objects.bulk_create(languages_to_create)
        for language in Language.objects.filter(name__in=[g.name for g in mlanguages_to_create]):
            MovieToLanguage.objects.create(movie=movie.name, language=language.name)
        print(f"{movie_name} added successfully!")

def search(request):
    movies = Movie.objects.all().order_by('name')
    movie_names = list(set([m.name for m in movies]))
    if request.method=='POST':
        query          = request.POST.get('query')
        if not query:
            return render(request, 'search.html', {'searchResult' :  retriveMovieListObj(movie_names), 'previousQuery': ""})
        results = process.extract(query, movie_names, scorer=fuzz.partial_ratio, limit=None)
        sortedL = sorted(results, key=lambda x: x[1], reverse=True)
        movie_names = [result[0] for result in sortedL]
        return render(request, 'search.html', {'searchResult' :  retriveMovieListObj(movie_names), 'previousQuery': query})
    return render(request, 'search.html', {'searchResult' :  retriveMovieListObj(movie_names), 'previousQuery': ""})


@login_required(login_url = 'login')
def editMovie(request, movie_id):
    if Movie.objects.filter(id=movie_id).exists():
        movie = Movie.objects.get(pk=movie_id)
        m=retriveMovieListObj([movie.name]),
        schedules = MovieSchedule.objects.get(movie=movie_id)
        return render(request, 'editMovie.html', {
            'movie': m[0][0], 
            'schedules': schedules,
            'isSuperuser': request.user.is_superuser,
            })
    else:
        return render(request, 'page_not_found.html')
    
def aboutUs(request):
    return render(request, 'aboutUs.html')
