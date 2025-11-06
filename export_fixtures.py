import os
import sys
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suresh_portfolio.settings')
django.setup()

from django.core import serializers
from blog.models import BlogPost
from faq.models import FAQ
from portfolio.models import Project
from services.models import Service
from testimonials.models import Testimonial
from contact.models import ContactMessage  # Fixed model name

def export_model(model, filename):
    if not os.path.exists('fixtures'):
        os.makedirs('fixtures')
    
    data = serializers.serialize('json', model.objects.all(), indent=4)
    with open(f'fixtures/{filename}', 'w', encoding='utf-8') as f:
        f.write(data)
    print(f'Exported {filename}')

# Export each model
export_model(BlogPost, 'blog.json')
export_model(FAQ, 'faq.json')
export_model(Project, 'portfolio.json')
export_model(Service, 'services.json')
export_model(Testimonial, 'testimonials.json')
export_model(ContactMessage, 'contact.json')

print('All fixtures exported successfully!')