# -*- coding: utf-8 -*-

from django.db import models

CATEGORIAS_MOVI = (
	('Contato', 'Contato'),
	('Movimento', 'Movimento'),
	('Pauta', 'Pauta'),
)

class Movi(models.Model):
	nome = models.CharField(
		max_length=150
	)
	cidade = models.CharField(
		max_length=150
	)
	bairro = models.CharField(
		max_length=150
	)
	categoria = models.CharField(
		max_length=150, 
		choices=CATEGORIAS_MOVI
	)
	
	tel = models.CharField(
		max_length=150,
		blank=True
	)
