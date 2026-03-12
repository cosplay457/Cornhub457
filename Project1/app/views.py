from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from app.models import *
import json
import math
# Create your views here.
class AllEmployees(View):
    def get(self, request):
        name = request.GET.get('name')
        type = request.GET.get('type')
        info = {}
        if name:
            info['name'] = name
        if type:
            info['type'] = type
        data = Employee.objects.filter(**info).values()
        num = 2
        page_max = math.ceil(len(data)/num)
        page_range = list(range(1, page_max+1))
        page_current = int(request.GET.get('page', 1))
        sta_idx = (page_current - 1)* num
        end_idx = page_current * num
        page_prev = page_current - 1
        page_next = page_current + 1
        return JsonResponse({
            'data': list(data[sta_idx:end_idx]),
            'page': {
                'cur': page_current,
                'prev': page_prev,
                'next': page_next,
                'range': page_range,
                'max': page_max
            }
        })

    def post(self, request):
        data = json.loads(request.body)
        Employee.objects.create(
            name=data['name'],
            age=data['age'],
            in_time=data['in_time'],
            type=data['type'],
        )
        return JsonResponse({
            'code': 200,
            'msg': "success"
        })

    def patch(self, request):
        id = request.GET.get('id', None)
        data = json.loads(request.body)
        Employee.objects.filter(id=id).update(**data)
        return JsonResponse({
            'code': 200,
            'msg': "success"
        })

    def delete(self, request):
        id = request.GET.get('id', None)
        Employee.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': "success"
        })


class Huixian(View):
    def get(self, request):
        id = request.GET.get('id', '')
        data = Employee.objects.filter(id=id).values().first()
        return JsonResponse({
            'code': 200,
            'data': data,
        })
