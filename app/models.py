# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models


CATEGORIAS_MOVI = (
	('Contato', 'Contato'),
	('Movimento', 'Movimento'),
	('Pauta', 'Pauta'),
	('Midia', 'Evento'),
)

CATEGORIAS_NOTA = (
	('Nota', 'Nota'),
	('Tarefa', 'Tarefa'),
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
			"id": self.id,
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

class Nota(models.Model):
	titulo = models.CharField(
		max_length=150
	)
	texto = models.CharField(
		max_length=500
	)
	categoria = models.CharField(
		max_length=150, 
		choices=CATEGORIAS_NOTA,
		default='Nota'
	)
	data = models.DateTimeField(default=timezone.now())
	related_to = models.ForeignKey(Movi, null=True, blank=True)

	def to_json(self):
		data = {
			"id": self.id,
			"titulo": self.titulo,
			"texto": self.texto,
			"categoria": self.categoria,
			"data": self.data,
			"related_to": self.related_to.nome
		}

		return data

	def __unicode__(self):
		return self.titulo
