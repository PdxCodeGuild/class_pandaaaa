from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.base import View
# from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Cheep
from .forms import CheepForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = CheepForm
        cheeps = Cheep.objects.all()
        return render(request, 'index.html',{'cheeps':cheeps,'form':form})

    def post(self, request, *args, **kwargs):
        form = CheepForm(request.POST)
        form.instance.user = self.request.user
        if form.is_valid():
            form.save()
            return redirect('index')


class NewCheep(LoginRequiredMixin,CreateView):
    model = Cheep
    template_name = 'cheep.html'
    form_class = CheepForm

    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)