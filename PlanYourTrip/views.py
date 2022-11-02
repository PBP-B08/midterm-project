
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from PlanYourTrip.models import PlanProperties
from .forms import InputForm
from django.contrib.auth.models import User

# Create your views here.
# request handler
def say_helo(request):
    return render(request, 'welcome.html', {'nama': User.get_username})

def say_plan(request):
    data_destinasi = PlanProperties.objects.all()
    context = {
        'name':'Tarreq',
        'list_destinasi': data_destinasi,
    }
    return render(request, "helo.html", context)

def say_form(request):
    items = PlanProperties.objects.filter(user=request.user)

    context = {}
    context['items'] = items
    context['form'] = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.user = request.user
            content.save()
            return JsonResponse({'judul': content.judul, 'destinasi':content.destinasi, 'aktivitas': content.aktivitas, 'hari': content.hari, 'orang':content.orang, 'deskripsi':content.deskripsi})


    return render(request, 'helo.html', context)


def delete_form(request, id):
    user = request.user
    temp = PlanProperties.objects.get(pk=id)
    if user.id == temp.user_id and request.method == 'DELETE':
        temp.delete()
    

    return HttpResponse('')

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

#content = None
    # form = InputForm()
    # if request.method == "POST":
    #     form = InputForm(request.POST)
    #     if form.is_valid():
    #         content = form.save(commit=False)
    #         content.post = post