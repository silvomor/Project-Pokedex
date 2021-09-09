from django.urls import path
from PokeMon import views

urlpatterns = [
    path('', views.pokemonGallery, name="PokemonList" ),
    path('details/<int:pk>/', views.detailsPokemon, name="PokemonDetails" ),
    path('add-pokemon/', views.addPokemon, name="AddPokemon" ),
    path('delete/<int:pk>/', views.deletePokemon, name="deletePokemon" ),
] 