from django.db import models


class PokemonType(models.Model):
    pokemonType = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.pokemonType

class Pokemon(models.Model):
    pokeMonName = models.CharField(max_length=20)
    breed = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to="pokemonImages")
    
    pokemontype = models.ForeignKey(PokemonType, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pokeMonName