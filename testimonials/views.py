from django.shortcuts import render
from .models import Testimonial

def testimonials(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    # Get first 3 testimonials for carousel (or all if fewer than 3)
    carousel_testimonials = testimonials[:3] if testimonials.count() >= 3 else testimonials
    return render(request, 'testimonials.html', {
        'testimonials': testimonials,
        'carousel_testimonials': carousel_testimonials
    })
