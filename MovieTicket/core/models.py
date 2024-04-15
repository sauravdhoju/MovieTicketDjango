from django.db import models
from datetime import datetime

class Movie(models.Model):
    def __str__(self):
        return self.name+' at '+ str(self.event_date )
    # user        = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    name  = models.CharField(max_length=255)

    # event_date  = models.DateTimeField()
    description = models.TextField()
    added_date  = models.DateTimeField()
    average_rating = models.FloatField(default=0)  # Average rating
    total_reviews = models.IntegerField(default=0) 

class MovieSchedule(models.Model):
    def __str__(self):
        return self.name+' at '+ str(self.schedule_date )
    Movie = models.ForeignKey('.models.Movie', on_delete = models.CASCADE)
    schedule_date= models.DateTimeField()

class MovieToGenre(models.Model):
    Movie_id = models.ForeignKey('Movie.id', on_delete = models.CASCADE)
    Genre_id = models.ForeignKey('Genre.id', on_delete = models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=40)

class Hall(models.Seat):
    title = models.CharField(max_length=40)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    seats_count = models.PositiveIntegerField()

class MovieUserRating(models.Model):
    user     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    rating = models.FloatField(default=0)  # Average rating

class Comment:
    Movie_id = models.ForeignKey('Movie.id', on_delete = models.CASCADE)
    user     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    comment = models.Textfield()
    added_date = models.DateTimeField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

class Reply:
    reply_to_a_comment = models.BoolanField(default=True) 
    parentComment_id = models.PositiveIntegerField()
    user     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    comment = models.Textfield()
    added_date = models.DateTimeField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

class Ticket:
    user     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    ticket_code = models.CharField(max_length=255)
    seat        = models.ForeignKey('Seat.id', on_delete = models.CASCADE)
    movie_schedule_id = models.ForeignKey('Movie.id', on_delete = models.CASCADE)
    creation_date = models.DateTimeField()
