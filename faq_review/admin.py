from django.contrib import admin

from faq_review.models import FrequentlyAskedQuestion, reviewUser

# Register your models here.
admin.site.register(reviewUser)
admin.site.register(FrequentlyAskedQuestion)