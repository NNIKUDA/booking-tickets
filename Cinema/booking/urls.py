from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    #path('users', users, name='users'),
    #path('user/<id:int>', user, name='user'),
    #path('cinemas', cinemas,name='cinema'),
    #path('cinema/<id:int>', cinema, name='cinema'),
    #path('cinema_halls', cinema_halls, name='cinema_halls'),
    #path('cinema_hall/<id:int', cinema_hall, name='cinema_hall'),
    #path('seats', seats, name='seats'),
    #path('seat/<id:int>', seat, name='seat'),
    #path('movies', movies, name='movies'),
    #path('movie/<id:int>', movie, name='movie'),
    #path('tickets', tickets, name='tickets'),
    #path('ticket/<id:int>', ticket, name='ticket'),
    #path('bookings', bookings, name='bookings'),
    #path('booking/<id:int>', booking, name='booking')
]