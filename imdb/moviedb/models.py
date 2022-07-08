from django.db import models

# Create your models here.
class Actor(models.Model):
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)

class Movie(models.Model):
	movie_name = models.CharField(max_length=32)
 
class Role(models.Model):
	actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="roles")
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="roles")