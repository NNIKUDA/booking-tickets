from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class User(User):
    birthday = models.DateField(verbose_name='День рождения')
    passport_number = models.CharField(max_length=9, verbose_name='Паспортный номер')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user', {'id': self.id})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Cinema(models.Model):
    name = models.TextField(verbose_name='Название')
    address = models.TextField(verbose_name='Адресс')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cinema', {'id': self.id})

    class Meta:
        db_table = 'cinema'
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'


class CinemaHall(models.Model):
    cinema_id = models.ForeignKey(Cinema.id, verbose_name='Кинотеатр')
    number = models.IntegerField(verbose_name='Номер кинозала')

    def __str__(self):
        return f'Кинозал №{self.number}'

    def get_absolute_url(self):
        return reverse('cinema_hall', {'id': self.id})

    class Meta:
        db_table = 'cinema_hall'
        verbose_name = 'Кинозал'
        verbose_name_plural = 'Кинозалы'


class Seat(models.Model):
    cinema_hall_id = models.ForeignKey(CinemaHall.id, verbose_name='Кинозал')
    number = models.IntegerField(verbose_name='Номер места')

    def __str__(self):
        return f'Место №{self.number}'

    def get_absolute_url(self):
        return reverse('seat', {'id': self.id})

    class Meta:
        db_table = 'seat'
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Movie(models.Model):
    movie_name = models.TextField(verbose_name='Название фильма')
    age_rating = models.IntegerField(verbose_name='Возростной рейтинг')
    poster = models.ImageField(verbose_name='Постер')

    def __str__(self):
        return self.movie_name

    def get_absolute_url(self):
        return reverse('movie', {'id': self.id})

    class Meta:
        db_table = 'movie'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class FilmSession(models.Model):
    movie_id = models.ForeignKey(Movie.id, verbose_name='Фильм')
    cinema_hall_id = models.ForeignKey(CinemaHall, verbose_name='Кинозал')
    date = models.DateTimeField(verbose_name='Дата сессии')

    def __str__(self):
        return f'Сессия {self.movie_id} Дата: {self.date}'

    def get_absolute_url(self):
        return reverse('film_session', {'id': self.id})

    class Meta:
        db_table = 'film_session'
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'


class Ticket(models.Model):
    seat_id = models.ForeignKey(Seat.id, verbose_name='Место')
    film_session_id = models.ForeignKey(FilmSession, verbose_name='Сессия')

    def __str__(self):
        return f'Билет на {self.film_session_id.movie_id} Место: {self.seat_id}'

    def get_absolute_url(self):
        return reverse('ticket', {'id': self.id})

    class Meta:
        db_table = 'ticket'
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'


class Booking(models.Model):
    user_id = models.ForeignKey(User.id)
    ticket_id = models.ForeignKey(Ticket.id, verbose_name='Билет')
    is_active = models.BooleanField(default=True, verbose_name='Действительность')

    def __str__(self):
        return f'{self.user_id} {self.ticket_id} '

    def get_absolute_url(self):
        return reverse('booking', {'id': self.id})

    class Meta:
        db_table = 'booking'
        verbose_name = 'Бронироване'
        verbose_name_plural = 'Бронирования'
