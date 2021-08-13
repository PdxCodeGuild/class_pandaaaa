from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, PostForm, CommentForm
from .models import CustomUser, Post, Comment
from django.views.generic.list import ListView
from django.utils.translation import ugettext as _
from django.views.generic.list import ListView
from django.core.files.storage import FileSystemStorage



#login view. This view displays a username and password field with a submit button.
class LoginView(LoginView):
    template_name= 'registration/login.html'



#logout view. This view is used to log the user out. -it displays a logout success message.
class LogoutView(LogoutView):
    template_name= 'registration/logout.html'



#registration view. This view loads a form for user creation. The form includes username, password, and email.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    def get_success_url(self):
        return reverse_lazy('login')



#profile view. This view displays a users profile which lists the user's posts.
class ProfileView(ListView):
    template_name = 'chirp_app/profile.html'
    def get_queryset(self, *args, **kwargs):
        return  Post.objects.filter(author_id=self.kwargs ['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['data'] = CustomUser.objects.get(id=self.kwargs['slug'])
        return context

#home view. This view displays a list of all posts filtered by post time.
class HomeView(ListView):
    template_name ='chirp_app/home.html'
    context_object_name = 'home'
    model = Post

    #this function gets the context data -- returns a context that contains a dictionary of the posts, comments, and post form.
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = PostForm()
        context['data'] = Post.objects.order_by('-posttime')
        context['comments'] = Comment.objects.all()
        return context

    #this function is called when a POST request is made. The request is made through a text input and submit button in the view.
    def post(self, request):
        # newpost = PostForm(request.POST,request.FILES)
        newpost = Post.objects.create(text=request.POST['text'],media=request.FILES['media'],author=request.user)
        newpost.save()
        return redirect('home')



#This view is used to display a detailed view of a particular(slug/id) post. It also displays all comments for that post.
class PostDetailView(ListView):
    template_name ='chirp_app/post_detail.html'
    my_post = None
    def get_queryset(self, *args, **kwargs):
        self.my_post = Post.objects.filter(id=self.kwargs['slug'])
        return self.my_post


    #this function gets the context for the comments and post.
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['slug'])
        return context


    #this function is called a post request is made. This post request comes from the comment input box.
    def post(self, request, slug, *args, **kwargs):
        self.get_queryset()
        newpost = Comment.objects.create(text=request.POST['text'],author=request.user,post=self.my_post[0])
        newpost.save()
        my_post = Post.objects.get(id=slug)
        my_post.comment_count += 1
        my_post.save()
        return redirect('home')