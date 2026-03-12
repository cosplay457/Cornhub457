from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
import math
from .models import *
# Create your views here.
class Movies(View):
    def get(self,request):
        filters = {}
        if request.GET.get('id'):
            filters['id'] = request.GET.get('id')
        if request.GET.get('name'):
            filters['name__contains'] = request.GET.get('name')
        if request.GET.get('type'):
            filters['type'] = request.GET.get('type')
        data=Movie.objects.filter(**filters).values('id','name','actor','area','type__name','type')


        num=3
        page_max=math.ceil(len(data)/num)
        page_range=list(range(1,page_max+1))
        page_cur=int(request.GET.get('page',1))
        s_idx=(page_cur-1)*num
        e_idx=page_cur*num
        prev=page_cur-1
        next=page_cur+1

        return JsonResponse({
            'data':list(data)[s_idx:e_idx],
            'code':200,
            'page':{
                'prev':prev,
                'next':next,
                'cur':page_cur,
                'max':page_max,
                'range':page_range,

            }
        })

    def post(self,request):
        args=json.loads(request.body)
        Movie.objects.create(
            name=args['name'],
            actor=args['actor'],
            area=args['area'],
            type_id=args['type'],
        )

        return JsonResponse({
            'code':200,
            'msg':'添加成功'
        })


    def patch(self,request):
        data=json.loads(request.body)
        id=request.GET.get('id')
        Movie.objects.filter(id=id).update(**data)
        return JsonResponse({
            'code':200,
            'msg':'修改成功'
        })

    def delete(self,request):
        id=request.GET.get('id')
        Movie.objects.filter(id=id).delete()
        return JsonResponse({
            'code':200,
            'msg':'删除成功'
        })

class Types(View):
    def get(self,request):
        data=Type.objects.all().values()
        return JsonResponse({
            'code':200,
            'data':list(data)
        })

    def post(self,request):
        data=json.loads(request.body)

        Type.objects.create(
            name=data['name'],
        )
        return JsonResponse({
            'code':200,
            'msg':'添加类型成功'
        })
