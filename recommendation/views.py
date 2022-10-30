from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from recommendation.forms import AreaForm, ProvinceForm
from recommendation.models import Province, Area
from django.core import serializers

# Create your views here.


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
        province.save()
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


def addArea(request):
    if request.method == "POST":
        title = request.POST.get("title")
        summary = request.POST.get("summary")
        description = request.POST.get("description")
        area = Area.objects.create(
            title=title,
            province=Province.objects.get(pk=request.POST.get("province")),
            summary=summary,
            description=description,
        )

        context = {
            'pk': area.pk,
            'fields': {
                'title': area.title,
                'province': area.province.title,
                'summary': area.summary,
                'description': area.description,
            }
        }

        return JsonResponse(context)


def detail(request, pk):
    province = Province.objects.get(pk=pk)
    context = {'province': province}
    return render(request, 'detail.html', context)


def show_json(request):
    province = Province.objects.all()
    return HttpResponse(serializers.serialize("json", province), content_type="application/json")
