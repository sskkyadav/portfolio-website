from django.shortcuts import render
from .models import FAQ

def faq(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'faq.html', {
        'faqs': faqs
    })
