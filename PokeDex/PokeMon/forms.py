from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Pokemon

class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'