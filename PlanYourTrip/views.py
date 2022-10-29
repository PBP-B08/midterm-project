from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler
def say_helo(request):
    return render(request, 'helo.html', {'name': 'Tarreq'})