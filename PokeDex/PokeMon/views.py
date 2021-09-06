from django.http import response
from django.shortcuts import render

from PokeMon.models import *

def pokemonGallery(request):
    return render(request, 'PokeMon/gallery.html')

def addPokemon(request):
    categories = PokemonType.objects.all()
    contex = {
        'categories': categories
    }
    return render(request, 'PokeMon/add_pokemon.html', contex)