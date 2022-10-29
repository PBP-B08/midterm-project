from recommendation.models import Province
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Food, Event
from recommendation.models import Province

# Create your views here.
def show_general(request):
    context = {}
    return render(request, "main_page.html", context)

def show_food_event(request, prov_id):
    province = Province.objects.get(pk=prov_id)
    context = {
        "prov_id": prov_id,
        "province":province.title,
    }
    return render(request, "things.html", context)

def add_food(request):
    pass

def update_food(request, food_id):
    pass

def delete_food(request, food_id):
    pass

def json_food(request, prov_id):
    food = Food.objects.filter(province=prov_id)
    return HttpResponse(serializers.serialize("json", food), content_type="application/json")

def add_event(request):
    pass

def update_event(request, event_id):
    pass

def delete_event(request, event_id):
    pass

def json_event(request, prov_id):
    event = Event.objects.filter(province=prov_id)
    return HttpResponse(serializers.serialize("json", event), content_type="application/json")

def json_province(request):
    province = Province.objects.all()
    return HttpResponse(serializers.serialize("json", province), content_type="application/json")