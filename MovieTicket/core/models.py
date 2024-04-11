from django.db import models
from datetime import datetime

class Movie(models.Model):
    def __str__(self):
        return self.name+' at '+ str(self.event_date )
    # user        = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    name  = models.CharField(max_length=80)
    # event_date  = models.DateTimeField()
    description = models.TextField()
    added_date  = models.DateTimeField()

class MovieSchedule(models.Model):
    def __str__(self):
        return self.name+' at '+ str(self.schedule_date )
    Movie = models.ForeignKey('.models.Movie', on_delete = models.CASCADE)
    schedule_date= models.DateTimeField()
