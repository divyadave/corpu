from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .forms import UnitForm


def TaskList(LoginRequiredMixin, request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render())

def sessionalProfile(request):
    template = loader.get_template('sessionalprofile.html')
    return HttpResponse(template.render())

class CustomLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('detail')


class CustomRegister(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy(True)

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('detail')
        return super(CustomRegister, self).get(*args, **kwargs)


def main(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def unit_page(request):

    form = UnitForm()
    return render(request, 'unit_page.html', {'form': form})


def apply_view(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = UnitForm()
    return render(request, 'apply.html', {'form': form})
