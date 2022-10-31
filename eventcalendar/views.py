from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.shortcuts import render, redirect
from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from .models import Event
# Create your views here.

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'all_events.html', {
        'event_list': event_list,
    })

def show_html(request, year, month):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    return render(request, 'calendar.html', {
                  'year': year,
                  'month': month,
                  'month_number' : month_number,
                  'cal' : cal,
                  'current_year' : current_year})


@allowed_users(allowed_roles=['Admin'])
#Ajax form
def create_event(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        event_date = request.POST.get('event_date')
        event = Event(title=title, description=description, location=location, 
                      event_date=event_date)
        event.save()
        return redirect('event-calendar:all_events')
    
    return HttpResponse("")
