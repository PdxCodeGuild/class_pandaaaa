from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_view(request):
    form = PostForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, "blog/create_post.html", context)

def detail_view(request, id):
    context={}
    context["data"] = Post.objects.get(id=id)
    return render(request, "blog/detail_post.html", context)

def update_view(request, id):
    context={}
    # fetch the object related to passed id
    obj = get_object_or_404(Post, id = id)
    # pass the object as instance in form
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "blog/update_post.html", context)