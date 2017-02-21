# -*- coding: utf-8 -*-
from django.forms import ModelForm

from models import Movi

class AddMoviForm(ModelForm):
	class Meta:
		model = Movi
		fields = ['nome', 'cidade', 'bairro', 'end', 'categoria', 'tel']