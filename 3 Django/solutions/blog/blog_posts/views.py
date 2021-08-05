from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import BlogPost

def all_posts(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog_posts/all_posts.html', context)

@login_required
def details(request, id):
    blog = BlogPost.objects.get(id = id)

    # if blog.user == request.user:
    #     return render(request, 'blog_posts/detail.html', {"blog": blog})
    # return redirect('profile')
    return render(request, 'blog_posts/detail.html', {"blog": blog})



@login_required
def add_post(request):
    if request.method == 'GET':
        return render(request, 'blog_posts/create.html')
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        post = BlogPost.objects.create(
            title = title, 
            body = text, 
            user = request.user
        )
        return redirect('profile')

@login_required
def remove_post(request, id):
    post = BlogPost.objects.get(id = id)
    post.delete()
    return redirect('profile')

@login_required
def update(request, id):
    post = BlogPost.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'blog_posts/update.html', {'post': post})
    elif request.method == 'POST':
        post.title = request.POST['title']
        post.body = request.POST['text']
        post.save()
        return redirect('details', post.id)

def search_posts(request):
    if request.method == 'POST':
        tag = request.POST['search']
        # posts = BlogPost.objects.filter(tags = tag)
        # posts = BlogPost.objects.get(tags=tag)
        # posts =  BlogPost.objects.all()
        # my_model = MyModel.objects.get(another_model__name='Some name')
        # posts = BlogPost.objects.get(tags__tags=tag)
        posts = BlogPost.objects.filter(tags__title__contains=tag)
        # Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)

        context = {
            'blogs': posts,
            'search': tag
        }
        return render(request, 'blog_posts/all_posts.html', context)
