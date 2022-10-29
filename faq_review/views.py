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
    form = reviewForm(request.POST)
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
        title = request.POST.get("title")
        review = request.POST.get("review")
        reviewUser.objects.create(
            title = title, review = review
        )
        JsonResponse({}, status=200)
    return redirect("faq_review:show_faq_review")

def show_json(request):
    data = FrequentlyAskedQuestion.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")