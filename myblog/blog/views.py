from django.shortcuts import render, HttpResponse
from blog.models import Blog

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'bloghome.html', context)

def post(request, slug):
    blog = Blog.objects.get(slug=slug)
    print(blog)
    context = {'blog': blog}
    return render(request, 'blogpost.html', context)

