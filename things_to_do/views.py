from recommendation.models import Province
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, csrf_exempt
from .forms import EventForm, FoodForm

from .models import Food, Event
from recommendation.models import Province

# Create your views here.
def show_general(request):
    context = {}
    return render(request, "main_page.html", context)

def show_food_event(request, prov_id):
    province = Province.objects.get(pk=prov_id)
    food_form = FoodForm()
    event_form = EventForm()
    if request.user.is_superuser:
        role = 'admin'
    else:
        role = 'user'
    context = {
        "food_form":food_form,
        "event_form":event_form,
        "prov_id": prov_id,
        "province": province.title,
        "role":role,
    }
    return render(request, "things.html", context)

@login_required(login_url='main:login')
@csrf_exempt
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
@csrf_exempt
def add_event(request):
    # months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Des"]
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

        # first_dash = str(event.date).index("-")
        # second_dash = str(event.date).index("-", first_dash + 1)
        # third_dash = str(event.date).index("-", second_dash + 1)

        return JsonResponse(
            {
                "pk": event.id, 
                "fields": {
                    "province": province.title,
                    "name": event.name, 
                    "date":event.date,
                    # "day": str(event.date)[second_dash+1:third_dash], 
                    # "month": months[int(str(event.date)[first_dash+1:second_dash]) - 1],
                    "description": event.description, 
                    "image": event.image
                    }
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
    event = Event.objects.filter(province=prov_id).order_by('date')
    return HttpResponse(serializers.serialize("json", event), content_type="application/json")

def json_province(request):
    province = Province.objects.all()
    return HttpResponse(serializers.serialize("json", province), content_type="application/json")