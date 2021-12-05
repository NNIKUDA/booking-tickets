from django.contrib import admin

from models import *

admin.site.register(User)
admin.site.register(Cinema)
admin.site.register(CinemaHall)
admin.site.register(Seat)
admin.site.register(Movie)
admin.site.register(FilmSession)
admin.site.register(Ticket)
admin.site.register(Booking)