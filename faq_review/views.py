from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from faq_review.models import reviewUser,FrequentlyAskedQuestion
from faq_review.forms import reviewForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
@login_required(login_url='/main/login')
def show_review(request):
    form = reviewForm()
    faq = FrequentlyAskedQuestion.objects.all()

    context = {
        'form': form,
        'faq': faq,
        # 'username': request.user

    }
    return render(request, 'review.html', context)

def show_faq(request):
    form = reviewForm()
    faq = FrequentlyAskedQuestion.objects.all()

    context = {
        'form': form,
        'faq': faq,
    }
    return render(request, 'faq.html', context)

@csrf_exempt
# @login_required(login_url="/main/login/")
def add_review(request):
    if request.method == "POST":
        print("hello")
        user = request.user
        username = request.user.username
        date = timezone.localdate()
        title = request.POST.get("title")
        review = request.POST.get("review")
        reviewUser.objects.create(
            title = title, review = review, user = user, username = username
        )
        # pk_id = reviewUser.objects.last("pk")
        return JsonResponse({
            "title": title,
            "review": review,
            "username": username,
            "date": date,
            # "pk": pk_id
        }, status=201)

def delete_review(request, pk):
    print("tes")
    data = reviewUser.objects.filter(pk=pk)
    print(data)
    data.delete()
    response = HttpResponseRedirect('/faq-review/review/')
    return response

def show_json_faq(request):
    data = FrequentlyAskedQuestion.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json") 


# @csrf_exempt
def show_json_review(request):
    data = reviewUser.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")  