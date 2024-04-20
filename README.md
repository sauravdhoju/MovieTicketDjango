# AKRS Movie Ticket Booking System

AKRS Movie Booking System is a Django-based web application designed to streamline the process of booking movie tickets. With this system, users can browse available movies, view their details including descriptions, directors, actors, schedules, and book tickets for their desired showtimes.

## About

The AKRS Movie Booking System provides users with a user-friendly interface to explore a wide range of movies, access their details, and conveniently book tickets online. It offers features such as:

- Browse movies: Users can browse through a collection of movies available in the system.
- Movie details: Detailed information about each movie, including its description, directors, actors, writers, languages, and genres.
- Schedule management: Users can view available schedules for each movie and book tickets for specific showtimes.
- User authentication: Secure user authentication system allowing users to create accounts, log in, and log out.
- Ticket booking: Users can book tickets for their preferred movies and showtimes.

## Installation

To run the AKRS Movie Booking System locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/sauravdhoju/MovieTicketDjango.git
    ```

2. Navigate to the project directory
    ```bash
    cd MovieTicket
    ```
3. Create Virtual Environment
    ```bash
    python3 -m venv env
    ```
4. Activate Virtual Environment
    1. Linux
    ```bash
    source env/bin/activate
    ```
    2. Windows
    ```bash
    env/Scripts/activate
    ```
5. Install requrements 
    ```bash
    pip install -r requrements.txt
    ```
6. Setup PostgreSQL
    1. Install PostgreSQL and configure it on your system
    2. Create a new database for the project 

7. Update the database in the settings.py
    ```bash
    DATABASES = {
    'default': {
        'ENGINE': 'postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
        }
    }
    ```
8. Navigate to main directory
    ```bash
    cd MovieTicket
    ```
9. Run the project
    ```bash
    python manage.py runserver
    ```















TODO: 
======
- [x] load Movies model object / db with IMDB api
- [x] make login/ register form work
- [x] create specific movie page with url pattern /movie-id/
- [ ] create admin dashboard for editing and selecting homepage movies
- [x] create admin dashboard for editing hall, movie_schedule
- [x] create search, that supports filtering with name, genre, actors, language, director
- [x] create dynaimc ticket booking system
- [x] add movies through json

optional:
- [x] add functional comment section and user review page for specific movie
- [ ] add movies through api


        ux:
        home page ──► login/signup ──►  specific movie page   ──┐
         │ │                  ▲                                 ▼
         │ └─► select movie ──┘                       select movie schedule 
         ▼              ▲                                       │          
         search movie ──┘  your-tickets ◄─── select seat/book ◄─┘


        admin dashboard
        select 6 movies for home page sidescroller:
        select 12 other movies for display.
        rule for premium/ non premium seat
