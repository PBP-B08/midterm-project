from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from recommendation.forms import AreaForm, ProvinceForm
from recommendation.models import Area, Province
from django.core import serializers

# Create your views here.

def highlights_index(request):
    return render(request, 'highlights.html')

def index(request):
    return render(request, 'recommendation.html')


def addProvince(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        header = request.POST.get('header')
        summary = request.POST.get('summary')
        province = Province.objects.create(
            title=title,
            header=header,
            summary=summary
        )
        # province.save()
        return JsonResponse(
            {
                "pk": province.id,
                "fields": {
                    "title": province.title,
                    "header": province.header,
                    "summary": province.summary
                }
            },
            status=200)


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


def addArea(request, pk):
    if request.method == 'POST':
        title = request.POST.get('title')
        province = Province.objects.get(id=pk)
        summary = request.POST.get('summary')
        description = request.POST.get('description')
        area = Area.objects.create(
            title=title,
            province=province,
            summary=summary,
            description=description
        )
        # return HttpResponse(serializers.serialize("json", [area, ]), content_type="application/json")
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


def delete_area(request, pk):
    area = Area.objects.get(pk=pk)
    area.delete()
    return JsonResponse(
        {
            "pk": area.id,
            "fields": {
                "title": area.title,
                "province": area.province,
                "summary": area.summary,
                "description": area.description
            }
        },
        status=200)

# def addArea(request):
#     context = {}
#     if request.method == 'POST':
#         form = AreaForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/recommendation/')
#     else:
#         form = AreaForm()
#     context['form'] = form
#     return render(request, 'addArea.html', context)


def detail(request, pk):
    province = Province.objects.get(id=pk)
    context = {'province': province}
    return render(request, 'detail.html', context)


def show_json(request):
    province = Province.objects.all()
    return HttpResponse(serializers.serialize("json", province), content_type="application/json")

# show json area based on province id


def show_area_json(request, pk):
    area = Area.objects.filter(province=pk)
    return HttpResponse(serializers.serialize("json", area), content_type="application/json")
