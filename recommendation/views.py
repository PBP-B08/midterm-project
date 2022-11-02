from email.mime import image
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from recommendation.forms import AreaForm, ProvinceForm
from recommendation.models import Area, Province
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    provinceForm = ProvinceForm()
    if request.user.is_superuser:
        role = 'admin'
    else:
        role = 'user'
    context = {
        'provinceForm': provinceForm,
        'role': role
    }
    return render(request, 'recommendation.html', context)


@login_required(login_url='main:login')
def addProvince(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        header = request.POST.get('header')
        summary = request.POST.get('summary')
        image = request.POST.get('image')
        province = Province.objects.create(
            title=title,
            header=header,
            summary=summary,
            image=image
        )
        return JsonResponse(
            {
                "pk": province.id,
                "fields": {
                    "title": province.title,
                    "header": province.header,
                    "summary": province.summary,
                    "image": province.image
                }
            },
            status=200)


@login_required(login_url='main:login')
def delete_province(request, pk):
    province = Province.objects.get(pk=pk)
    province.delete()
    return JsonResponse(
        {
            "pk": province.id,
            "fields": {
                "title": province.title,
                "header": province.header,
                "summary": province.summary,
            }
        },
        status=200)


@login_required(login_url='main:login')
def addArea(request, pk):
    if request.method == 'POST':
        title = request.POST.get('title')
        province = Province.objects.get(id=pk)
        summary = request.POST.get('summary')
        description = request.POST.get('description')
        image = request.POST.get('image')
        area = Area.objects.create(
            title=title,
            province=province,
            summary=summary,
            description=description,
            image=image
        )
        # return HttpResponse(serializers.serialize("json", [area, ]), content_type="application/json")
        return JsonResponse(
            {
                "pk": area.id,
                "fields": {
                    "title": area.title,
                    # "province": area.province,
                    "summary": area.summary,
                    "description": area.description,
                    "image": area.image
                }
            },
            status=200)


@login_required(login_url='main:login')
def delete_area(request, pk, area_pk):
    province = Province.objects.get(id=pk)
    area = Area.objects.get(pk=area_pk)
    area.delete()
    return JsonResponse(
        {
            "pk": area.id,
            "fields": {
                "title": area.title,
                # "province": area.province,
                "summary": area.summary,
                "description": area.description
            }
        },
        status=200)


def detail(request, pk):
    province = Province.objects.get(id=pk)
    areaForm = AreaForm
    context = {'province': province,
               'areaForm': areaForm
               }
    return render(request, 'detail.html', context)


def detail_area(request, pk, area_pk):
    area = Area.objects.get(id=area_pk)
    context = {'area': area}
    return render(request, 'detail_area.html', context)


def show_json(request):
    province = Province.objects.all()
    return HttpResponse(serializers.serialize("json", province), content_type="application/json")

# show json area based on province id


def show_area_json(request, pk):
    area = Area.objects.filter(province=pk)
    return HttpResponse(serializers.serialize("json", area), content_type="application/json")
