from django.forms import ModelForm
from .models import EventCalendar

class EventCalendarForm(ModelForm):
    class Meta:
        model = EventCalendar
        fields = '__all__'