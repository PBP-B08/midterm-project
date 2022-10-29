from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from recommendation.forms import AreaForm, ProvinceForm
from recommendation.models import Province
from django.core import serializers

# Create your views here.


def index(request):
    return render(request, 'recommendation.html')


def addProvince(request):
    # context = {}
    # if request.method == 'POST':
    #     form = ProvinceForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/recommendation/')
    # else:
    #     form = ProvinceForm()
    # context['form'] = form
    # return render(request, 'addProvince.html', context)
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
    context = {}
    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/recommendation/')
    else:
        form = AreaForm()
    context['form'] = form
    return render(request, 'addArea.html', context)


# def createRecommendation(request):
#     context = {}
#     if request.method == 'POST':
#         form = RecommendationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/recommendation/')
#     else:
#         form = RecommendationForm()
#     context['form'] = form
#     return render(request, 'createRecommendation.html', context)


def detail(request, pk):
    province = Province.objects.get(pk=pk)
    context = {'province': province}
    return render(request, 'detail.html', context)


def show_json(request):
    province = Province.objects.all()
    return HttpResponse(serializers.serialize("json", province), content_type="application/json")
