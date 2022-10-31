
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from PlanYourTrip.models import PlanProperties
from .forms import InputForm

# Create your views here.
# request handler
def say_helo(request):
    return render(request, 'helo.html', {'name': 'Tarreq'})

def say_plan(request):
    data_destinasi = PlanProperties.objects.all()
    context = {
        'name':'Tarreq',
        'list_destinasi': data_destinasi,
    }
    return render(request, "helo.html", context)

def say_form(request):
    context = {}
    context['form'] = InputForm()

    content = None
    form = InputForm()
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.post = post
            






    return render(request, 'form.html', context)
    # if request.method == 'POST':
    #     form = InputForm(request.POST)
    #     if form.is_valid():
    #         report = PlanProperties(
    #             user_submit = request.user,
    #             destinasi = form.cleaned_data['destinasi'],
    #             aktivitas = form.cleaned_data['aktivitas'],
    #             lokasi = form.cleaned_data['lokasi'],
    #         )
    #         report.save()
            
            #return render(request, 'form.html', context)

