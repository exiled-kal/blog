from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages


def index(request):
    if 'username' not in request.session:
        return redirect('./login')
    context = {
        'username': request.session['username'],
        'blogs': Blog.objects.all()
    }
    return render(request, 'all_blogs.html', context)


def login(request):
    return render(request, 'login.html')


def process_login(request):
    user = User.objects.filter(username=request.POST['username'])
    if not user.exists():
        user = User.objects.create(username=request.POST['username'])
    request.session['username'] = request.POST['username']

    return redirect('./')


def new(request):
    return render(request, 'new_blog.html')


def process_new(request):
    if 'username' not in request.session:
        return redirect('./login')
    
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f"./new")
    else:
        user = User.objects.filter(
            username=request.session['username']).first()
    Blog.objects.create(user=user, description=request.POST['description'])
    return redirect('./')


def create(request):
    return HttpResponse("create placeholder")


def blog(request, number):
    context = {
        'blog': Blog.objects.get(id=number)
    }
    return render(request, 'blog.html', context)


def process_new_entry(request, number):
    blog_entry = BlogEntry.objects.create(
        text=request.POST['text'], blog_id=number)
    return redirect(f"../{number}")


def edit(request, number):
    return HttpResponse(f"placeholder to edit blog number {number}")


def delete(request, number):
    return redirect('/blogs')
