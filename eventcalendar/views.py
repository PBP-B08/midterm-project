from django.shortcuts import render, redirect
from .models import EventCalendar
from django.http import HttpResponse
from django.core import serializers
from .forms import EventCalendarForm

def show_calendar(request):
    events = EventCalendar.objects.all()
    eventform = EventCalendarForm()
    context = {
        'eventform' : eventform,
        'events' : events,
    }
    return render(request, 'all_events.html', context)

def event_data_json(request):
    # mengembalikan semua data event dalam bentuk json
    data = EventCalendar.objects.get(event_date=request.event_date)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_event(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        event_date = request.POST.get('event_date')
        
        event = EventCalendar(title=title, description=description, location=location,
                      event_date=event_date)
        event.save()
        
        return redirect('eventcalendar:show_event')
    
    return HttpResponse("")