# -*- coding: utf-8 -*-
import json

from django.http import JsonResponse
from django.views.generic import TemplateView

from models import Movi
from forms import AddMoviForm

class IndexView(TemplateView):
	template_name = "index.html"
	get_services = ('get_movi_data', )

	def get_context_data(self, *args, **kwargs):
		ctx = super(IndexView, self).get_context_data(*args, **kwargs)

		ctx['form'] = AddMoviForm()
		ctx['movi_data'] = Movi.objects.all()

		return ctx

	def post(self, request, *args, **kwargs):
		ctx = self.get_context_data()

		form = AddMoviForm(self.request.POST)
		form.save()

		return super(TemplateView, self).render_to_response(ctx)

	def get(self, *args, **kwargs):
		ctx = self.get_context_data()
		cmd = self.request.GET.get('cmd')

		if cmd and cmd in self.get_services:
			return getattr(self, '_%s' % cmd)()

		return super(IndexView, self).get(*args, **kwargs)


	def _get_movi_data(self):
		objects = Movi.objects.all()
		movi_data = []

		for o in objects:
			movi_data.append(o.to_json())

		return JsonResponse(movi_data, safe=False)
