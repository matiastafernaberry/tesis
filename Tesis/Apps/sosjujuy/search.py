# -*- coding: utf-8 -*-
import json

from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.views import View

from .models import Pais, Provincia, Beneficiario, Prestador


class Search(View):
    def post(self, request):
        url = request.POST["url"]
        data = Pais.objects.all()
        qs_json = serializers.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')


class ProvinciaListado(View):
    def post(self, request):
        valueId = request.POST["value"]
        if valueId == 0: data = {}
        else: data = Provincia.objects.filter(pais__id=valueId)
        
        qs_json = serializers.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')


class BeneficiarioListado(View):
    def post(self, request):
        url = request.POST["url"]
        data = Beneficiario.objects.all()
        qs_json = serializers.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')


class PrestadorListado(View):
    def post(self, request):
        url = request.POST["url"]
        data = Prestador.objects.all()
        qs_json = serializers.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')