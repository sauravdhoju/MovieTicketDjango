from django.db import models
from datetime import datetime

class Movie(models.Model):
    def __str__(self):
        return self.name+' at '+ str(self.added_date )
    name  = models.CharField(max_length=255)
    description = models.TextField()
    added_date  = models.DateTimeField()
    # released_date  = models.DateField(default =None )
    average_rating = models.TextField(default=0) 
    length = models.TextField(default='0 min')
    poster = models.URLField(null=True, blank=True)  # Poster link

class MovieSchedule(models.Model):
    def __str__(self):
        return self.name+' at '+ str(self.schedule_date )
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE)
    schedule_date= models.DateTimeField()

class MovieToGenre(models.Model):
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete = models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=40)

class MovieToActor(models.Model):
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete = models.CASCADE)

class Actor(models.Model):
    name = models.CharField(max_length=200)

class MovieToWriter(models.Model):
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE)
    writer = models.ForeignKey('Writer', on_delete = models.CASCADE)

class Writer(models.Model):
    name = models.CharField(max_length=200)

class MovieToDirector(models.Model):
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE)
    director = models.ForeignKey('Director', on_delete = models.CASCADE)

class Director(models.Model):
    name = models.CharField(max_length=200)

class MovieToLanguage(models.Model):
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE)
    language = models.ForeignKey('Language', on_delete = models.CASCADE)

class Language(models.Model):
    name = models.CharField(max_length=200)

class Hall(models.Model):
    title = models.CharField(max_length=40)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    seats_count = models.PositiveIntegerField()

class MovieUserRating(models.Model):
    user     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    Movie = models.ForeignKey('Movie', on_delete = models.CASCADE)
    rating = models.FloatField(default=0)  # Average rating

class Comment:
    Movie = models.ForeignKey('Movie', on_delete = models.CASCADE)
    user     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    comment = models.TextField()
    added_date = models.DateTimeField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

class Reply:
    reply_to_a_comment = models.BooleanField(default=True) 
    parentComment_id = models.PositiveIntegerField()
    user     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    comment = models.TextField()
    added_date = models.DateTimeField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

class Ticket:
    user     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    ticket_code = models.CharField(max_length=255)
    seat        = models.ForeignKey('Seat', on_delete = models.CASCADE)
    movie_schedule = models.ForeignKey('Movie', on_delete = models.CASCADE)
    creation_date = models.DateTimeField()
