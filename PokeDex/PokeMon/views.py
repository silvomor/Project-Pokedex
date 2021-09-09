from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import PokemonForm
from PokeMon.models import *

def pokemonGallery(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'PokeMon/gallery.html', {'pokemons':pokemons})

def addPokemon(request):
    categories = PokemonType.objects.all()
    
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)
        print('lets try this')
        if form.is_valid():
            print('Got upto here')
            form.save()
            print('saved the data')
            pokemonName = form.cleaned_data.get('pokeMonName')
            messages.success(request, f'{pokemonName} was saved successfully!')
            return redirect('PokemonList')
        else:
            print('error')

    form = PokemonForm()
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'PokeMon/add_pokemon.html', context)


def detailsPokemon(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    context={'pokemon':pokemon}
    return render(request, 'PokeMon/showDetails.html', context)


def deletePokemon(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    pokemon.delete()
    return redirect('PokemonList')