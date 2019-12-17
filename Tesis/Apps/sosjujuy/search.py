# -*- coding: utf-8 -*-
import json

from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.views import View

from .models import Pais


class Search(View):
    def get(self, request):
        # <view logic>
        # return HttpResponse('result')
        obj = {
          'data': "texto", 
        } 
        return JsonResponse(obj, status=200)

    def post(self, request):
        # <view logic>
        # return HttpResponse('result')
        url = request.POST["url"]
        data = Pais.objects.all()
        qs_json = serializers.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')