# -*- coding: utf-8 -*-
from django.forms import ModelForm

from models import Movi, Nota

class AddMoviForm(ModelForm):
	class Meta:
		model = Movi
		fields = ['nome', 'cidade', 'bairro', 'end', 'categoria', 'tel']

class AddNotaForm(ModelForm):
	class Meta:
		model = Nota
		fields = ['titulo', 'texto', 'categoria', 'related_to']