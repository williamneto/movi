# -*- coding: utf-8 -*-
import json

from django.http import JsonResponse
from django.views.generic import TemplateView

from models import Movi, Nota
from forms import AddMoviForm, AddNotaForm

class IndexView(TemplateView):
	template_name = "index.html"
	get_services = ('get_movi_data', 'drop_movi', 'get_movi_cidade')

	def get_context_data(self, *args, **kwargs):
		ctx = super(IndexView, self).get_context_data(*args, **kwargs)

		ctx['form'] = AddMoviForm()
		ctx['nota_form'] = AddNotaForm()
		ctx['movi_data'] = Movi.objects.all()
		ctx['notas'] = Nota.objects.all()

		return ctx

	def post(self, request, *args, **kwargs):
		ctx = self.get_context_data()

		if self.request.POST.get('nome'):
			form = AddMoviForm(self.request.POST)
			form.save()
		else:
			form = AddNotaForm(self.request.POST)
			form.save()

		return super(TemplateView, self).render_to_response(ctx)

	def get(self, *args, **kwargs):
		ctx = self.get_context_data()
		cmd = self.request.GET.get('cmd')

		if cmd and cmd in self.get_services:
			return getattr(self, '_%s' % cmd)()

		return super(IndexView, self).get(*args, **kwargs)

	def _get_movi_cidade(self):
		cidade = self.request.GET['cidade']
		movi_data = Movi.objects.all().filter(cidade=cidade)

		json = []
		for m in movi_data:
			json.append(m.to_json())

		return JsonResponse(json, safe=False)

	def _get_movi_data(self):
		objects = Movi.objects.all()
		movi_data = []

		for o in objects:
			movi_data.append(o.to_json())

		return JsonResponse(movi_data, safe=False)

	def _drop_movi(self):
		ctx = self.get_context_data()

		movi = Movi.objects.get(id=self.request.GET.get('id'))
		movi.delete()

		return super(TemplateView, self).render_to_response(ctx)

