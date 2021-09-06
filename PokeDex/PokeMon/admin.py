from django.contrib import admin
from PokeMon.models import *


@admin.register(PokemonType)
class PokemonTypeAdmin(admin.ModelAdmin):
    list_display = ['pokemonType']

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['pokeMonName', 'breed', 'pokemontype']