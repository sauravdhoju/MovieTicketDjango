from django.db import models
from datetime import datetime
class MovieSchedule(models.Model):
    def __str__(self):
        return self.name+' at '+ str(self.schedule_date )
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE)
    schedule_date= models.DateTimeField()

    class Movie(models.Model):
        def __str__(self):
            return self.name+' at '+ str(self.event_date )
    name  = models.CharField(max_length=255)
    description = models.TextField()
    added_date  = models.DateTimeField()
    average_rating = models.FloatField(default=0)  # Average rating

class MovieToGenre(models.Model):
    Movie_id = models.ForeignKey('Movie', on_delete = models.CASCADE)
    Genre_id = models.ForeignKey('Genre', on_delete = models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=40)

class Hall(models.Model):
    title = models.CharField(max_length=40)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    seats_count = models.PositiveIntegerField()

class MovieUserRating(models.Model):
    user     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    Movie_id = models.ForeignKey('Movie', on_delete = models.CASCADE)
    rating = models.FloatField(default=0)  # Average rating

class Comment:
    Movie_id = models.ForeignKey('Movie', on_delete = models.CASCADE)
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
    movie_schedule_id = models.ForeignKey('Movie', on_delete = models.CASCADE)
    creation_date = models.DateTimeField()
