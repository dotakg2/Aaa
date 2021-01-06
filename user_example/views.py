from django.shortcuts import render

from .models import Drink

def index(request):
    drinks = Drink.objects.all()
    return  render(request, 'user_example/index.html', context={'drinks': drinks})
