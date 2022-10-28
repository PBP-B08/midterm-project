from multiprocessing import context
from django.shortcuts import redirect, render
from recommendation.forms import AreaForm, ProvinceForm, RecommendationForm
from recommendation.models import Recommendation

# Create your views here.


def index(request):
    recommendationList = Recommendation.objects.all()
    context = {'recommendationList': recommendationList}
    return render(request, 'recommendation.html', context)


def addProvince(request):
    context = {}
    if request.method == 'POST':
        form = ProvinceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/recommendation/')
    else:
        form = ProvinceForm()
    context['form'] = form
    return render(request, 'addProvince.html', context)


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
