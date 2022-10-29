from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from recommendation.forms import AreaForm, ProvinceForm, RecommendationForm
from recommendation.models import Province, Recommendation
from django.core import serializers

# Create your views here.


def index(request):
    recommendationList = Recommendation.objects.all()
    context = {'recommendationList': recommendationList}
    return render(request, 'recommendation.html', context)


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


def createRecommendation(request):
    context = {}
    if request.method == 'POST':
        form = RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/recommendation/')
    else:
        form = RecommendationForm()
    context['form'] = form
    return render(request, 'createRecommendation.html', context)


def detail(request, recommendation_id):
    recommendation = Recommendation.objects.get(id=recommendation_id)
    context = {'recommendation': recommendation}
    return render(request, 'detail.html', context)


def show_json(request):
    province = Province.objects.all()
    return HttpResponse(serializers.serialize("json", province), content_type="application/json")
