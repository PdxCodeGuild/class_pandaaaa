from django.http.response import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BlogPost
from .forms import CreateForm
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    # print(request.user.userprofile.avatar.url)
    return render(request, 'blog_app/home.html')



class CreatePost(CreateView):
    model = BlogPost
    form_class = CreateForm
    success_url = reverse_lazy('blog_app:home')
    template_name = 'blog_app/create.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CreatePost,self).form_valid(form)



class ListView(ListView):
    model = BlogPost
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class PostDetailView(DetailView):
    model = BlogPost
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def get_queryset(self) -> models.query.QuerySet[T]:
    #     return super().get_queryset()a
      # context['authorpost_list'] = BlogPost.objects.filter(author = self.request.user)
    # paginate_by = 2
# template_name = 'blog_app/detail.html'
    # template_name = 'blog_app/list.html'
        # my_todos = TodoModel.objects.filter(startdate__lte=timezone.now()).order_by('duedate')