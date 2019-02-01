from django.shortcuts import render

from .models import Post
from django.utils import timezone

# Create your views here.
def homepage(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/homepage.html', {'posts': posts})
def gallery(request):
    return render(request, 'blog/gallerydemo.html', {})
def registration(request):
    return render(request, 'blog/registration.html',{})
def calculator(request):
    return render(request, 'blog/calculator.html',{})
