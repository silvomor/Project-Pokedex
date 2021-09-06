from django.urls import path
from PokeMon import views

urlpatterns = [
    path('', views.pokemonGallery, name="PokemonList" ),
    path('add-pokemon/', views.addPokemon, name="AddPokemon" ),
] 