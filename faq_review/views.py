from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from faq_review.models import reviewUser,FrequentlyAskedQuestion
from faq_review.forms import reviewForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/main/login')
def show_faq_review(request):
    form = reviewForm()
    faq = FrequentlyAskedQuestion.objects.all()

    context = {
        'form': form,
        'faq': faq
    }
    return render(request, 'faq.html', context)

@csrf_exempt
# @login_required(login_url="/main/login/")
def add_review(request):
    if request.method == "POST":
        print("hi")
        user = request.user
        title = request.POST.get("title")
        review = request.POST.get("review")
        reviewUser.objects.create(
            title = title, review = review, user = user
        )
        return JsonResponse({
            "title": title,
            "review": review,
        }, status=200)

def show_json_faq(request):
    data = FrequentlyAskedQuestion.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json") 

def show_json_review(request):
    data = reviewUser.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")  