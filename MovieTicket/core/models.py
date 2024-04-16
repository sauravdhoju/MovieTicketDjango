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
    schedule_date= models.DateTimeField()
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE)

class MovieToGenre(models.Model):
    movie  = models.CharField(max_length=255)
    genre  = models.CharField(max_length=255)

class Genre(models.Model):
    name = models.CharField(max_length=255)

class MovieToActor(models.Model):
    movie  = models.CharField(max_length=255)
    actor  = models.CharField(max_length=255)
class Actor(models.Model):
    name = models.CharField(max_length=255)

class MovieToWriter(models.Model):
    movie  = models.CharField(max_length=255)
    writer  = models.CharField(max_length=255)
class Writer(models.Model):
    name = models.CharField(max_length=255)

class MovieToDirector(models.Model):
    movie  = models.CharField(max_length=255)
    director  = models.CharField(max_length=255)
class Director(models.Model):
    name = models.CharField(max_length=200)

class MovieToLanguage(models.Model):
    movie  = models.CharField(max_length=255)
    language  = models.CharField(max_length=255)
class Language(models.Model):
    name = models.CharField(max_length=255)

class Hall(models.Model):
    title = models.CharField(max_length=40)
    location = models.CharField(max_length=255)
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
