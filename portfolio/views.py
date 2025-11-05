from django.shortcuts import render
from .models import Project, Category

def portfolio(request):
    category_filter = request.GET.get('category', 'all')
    if category_filter == 'all':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category__slug=category_filter)
    categories = Category.objects.all()
    return render(request, 'portfolio.html', {
        'projects': projects,
        'categories': categories,
        'current_category': category_filter
    })
