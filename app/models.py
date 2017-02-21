# -*- coding: utf-8 -*-

from django.db import models

CATEGORIAS_MOVI = (
	('Contato', 'Contato'),
	('Movimento', 'Movimento'),
	('Pauta', 'Pauta'),
	('Midia', 'Evento'),
)

class Movi(models.Model):
	nome = models.CharField(
		max_length=150
	)
	cidade = models.CharField(
		max_length=150
	)
	bairro = models.CharField(
		max_length=150,
		blank=True
	)
	end = models.CharField(
		max_length=150,
		default=None,
		blank=True
	)
	categoria = models.CharField(
		max_length=150, 
		choices=CATEGORIAS_MOVI
	)
	
	tel = models.CharField(
		max_length=150,
		blank=True
	)

	def to_json(self):
		data = {
			"nome": self.nome,
			"cidade": self.cidade,
			"bairro": self.bairro,
			"end": self.end,
			"categoria": self.categoria,
			"tel": self.tel
		}

		return data

	def __unicode__(self):
		return self.nome
