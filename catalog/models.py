from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a movie genre')
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    synopsis = models.TextField(max_length=1000, help_text='Enter a synopsis')
    actor = models.ManyToManyField('Actor')
    genre = models.ManyToManyField(Genre, help_text='Select a genre')
    year = models.PositiveSmallIntegerField()
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    director = models.ManyToManyField('Director')
    
    RATINGS = (
        ('G', 'General Audiences'),
        ('PG', 'Parental Guidance Suggested'),
        ('PG-13', 'Parents Strongly Cautioned'),
        ('R', 'Restricted'),
        ('NC-17', 'Adults Only'),
    )
  
    rating = models.CharField(
        max_length=5,
        choices=RATINGS,
        blank=True,
        help_text='MPAA Film Rating',
    )
    
    class Meta:
        ordering = ['title']
    
    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class MovieInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this movie copy')
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    due_date = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_date and date.today() > self.due_date:
            return True
        return False

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Movie availability',
    )

    class Meta:
        ordering = ['due_date']
        permissions = (("can_mark_returned", "Set book as returned"),)   


    def __str__(self):
        return f'{self.id} ({self.movie.title})'


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('actor-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.middle_name}'

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.middle_name}'

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

class Language(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the language')

    def __str__(self):
        return self.name