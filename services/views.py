from django.shortcuts import render
from .models import Service, DemoProject

def services(request):
    services = Service.objects.all()
    demo_projects = DemoProject.objects.all()
    return render(request, 'services.html', {
        'services': services,
        'demo_projects': demo_projects
    })
