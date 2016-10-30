from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from pet_search.models import Pet


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets
    })
