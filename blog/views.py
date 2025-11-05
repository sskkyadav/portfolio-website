from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost

def blog_list(request):
    search_query = request.GET.get('q', '')
    if search_query:
        posts = BlogPost.objects.filter(
            published=True,
            title__icontains=search_query
        ) | BlogPost.objects.filter(
            published=True,
            content__icontains=search_query
        )
    else:
        posts = BlogPost.objects.filter(published=True).order_by('-published_at')
    
    paginator = Paginator(posts, 6)  # 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'blog_detail.html', {'post': post})
