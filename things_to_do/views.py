from recommendation.models import Province
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import Food, Event
from recommendation.models import Province

# Create your views here.
def show_general(request):
    context = {}
    return render(request, "main_page.html", context)

def show_food_event(request, prov_id):
    province = Province.objects.get(pk=prov_id)
    if request.user.is_superuser:
        role = 'admin'
    else:
        role = 'user'
    context = {
        "prov_id": prov_id,
        "province": province.title,
        "role":role,
    }
    return render(request, "things.html", context)

@login_required(login_url='main:login')
def add_food(request):
    if request.method == 'POST':
        prov_id = request.POST.get("prov_id")
        province = Province.objects.get(pk=prov_id)
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.POST.get("image")
        food = Food.objects.create(
            province = province,
            name=name,
            description=description,
            image=image
        )
        return JsonResponse(
            {
                "pk": food.id, 
                "fields": {
                    "province": province.title,
                    "name": food.name, 
                    "description": food.description, 
                    "image": food.image}
            }, 
            status=200)

@login_required(login_url='main:login')
def update_food(request, food_id):
    if request.method == "POST":
        food = Food.objects.get(pk=food_id)
        province = request.POST.get("prov_id")
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.POST.get("image")

        # update food information
        if province:
            food.province = province
        if name:
            food.name = name
        if description:
            food.description = description
        if image:
            food.image = image

        food.save()        
        return JsonResponse(
            {
                "pk": food.id, 
                "fields": {
                    "province": food.province,
                    "name": food.name, 
                    "description": food.description, 
                    "image": food.image}
            }, 
            status=200)

@login_required(login_url='main:login')
def delete_food(request, food_id):
    food = Food.objects.filter(pk=food_id).first()
    food.delete()
    return JsonResponse(
            {
                "pk": food.id, 
                "fields": {
                    "name": food.name, 
                    "description": food.description, 
                    "image": food.image}
            }, 
            status=200)

def json_food(request, prov_id):
    food = Food.objects.filter(province=prov_id)
    return HttpResponse(serializers.serialize("json", food), content_type="application/json")

@login_required(login_url='main:login')
def add_event(request):
    if request.method == 'POST':
        prov_id = request.POST.get("prov_id")
        province = Province.objects.get(pk=prov_id)
        name = request.POST.get("name")
        date = request.POST.get("date")
        description = request.POST.get("description")
        image = request.POST.get("image")
        event = Event.objects.create(
            province = province,
            name=name,
            date=date,
            description=description,
            image=image
        )
        return JsonResponse(
            {
                "pk": event.id, 
                "fields": {
                    "province": province.title,
                    "name": event.name, 
                    "date": event.date, 
                    "description": event.description, 
                    "image": event.image}
            }, 
            status=200)

@login_required(login_url='main:login')
def update_event(request, event_id):
    if request.method == "POST":
        event = Event.objects.get(pk=event_id)
        province = request.POST.get("prov_id")
        name = request.POST.get("name")
        date = request.POST.get("date")
        description = request.POST.get("description")
        image = request.POST.get("image")

        # update event information
        if province:
            event.province = province
        if name:
            event.name = name
        if date:
            event.date = date
        if description:
            event.description = description
        if image:
            event.image = image

        event.save()        
        return JsonResponse(
            {
                "pk": event.id, 
                "fields": {
                    "province": event.province,
                    "name": event.name, 
                    "date": event.date, 
                    "description": event.description, 
                    "image": event.image}
            }, 
            status=200)

@login_required(login_url='main:login')
def delete_event(request, event_id):
    event = Event.objects.filter(pk=event_id).first()
    event.delete()
    return JsonResponse(
            {
                "pk": event_id, 
                "fields": {
                    "name": event.name, 
                    "date": event.date, 
                    "description": event.description, 
                    "image": event.image}
            }, 
            status=200)

def json_event(request, prov_id):
    event = Event.objects.filter(province=prov_id)
    return HttpResponse(serializers.serialize("json", event), content_type="application/json")

def json_province(request):
    province = Province.objects.all()
    return HttpResponse(serializers.serialize("json", province), content_type="application/json")