from django.shortcuts import render

from models import *

def index(request):
    context = {
        ''
    }
    return render(request, 'booking/index.html', context)

