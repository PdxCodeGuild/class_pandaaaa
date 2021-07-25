from django.http.response import HttpResponseRedirect
from django.shortcuts import render
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