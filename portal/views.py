from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
from .forms import RegistrationForm
from django.shortcuts import render, redirect 
from .forms import LoginForm
from .models import JobListing
from django.views import View 
from .models import CreateJob
from .forms import CreateJobForm


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# def joblisting(request):
#     return render(request, 'joblisting.html')

# def listofjobs(request):
#     return render(request, 'listofjobs.html')

def viewjob(request):
    return render(request, 'viewjob.html')

def listofapplications(request):
    return render(request, 'listofapplications.html')

def sessionalProfile(request):
    return render(request, 'sessionalprofile.html')

def sessionalapplicant(request):
    return render(request, 'sessionalapplicant.html')

def viewapplication(request):
    return render(request, 'viewapplication.html')

# def createjob(request):
#     return render(request, 'createjob.html')

def applicantjobdetail(request):
    return render(request, 'applicantjobdetail.html')

class CustomLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


class CustomRegister(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

    # def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        if user is not None:
            print(user)
            login(self.request, user)
        return response

    # def get(self, *args, **kwargs):
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(CustomRegister, self).get(*args, **kwargs)


def main(request):
    return render(request, 'home.html')

@login_required

# def apply_view(request):
#     if request.method == 'POST':
#         form = UnitForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'success.html')
#     else:
#         form = UnitForm()
#     return render(request, 'success.html', {'form': form})

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'portal/user_form.html', {'form': form})

def success(request):
    return render(request, 'portal/success.html')



def login(request): 
    if request.method == 'POST': 
        form = LoginForm(request.POST) 
        if form.is_valid(): 
            # Perform login logic 
            return redirect('home') # Replace 'home' with your desired URL 
        else: 
            form = LoginForm() 

        return render(request, 'login.html', {'form': form})

@login_required
def job_listing(request):
     table_data = JobListing.objects.all()
     context = {'table_data': table_data}
     return render(request, 'joblisting.html', context)


def createjob(request):
    if request.method == 'POST':
        unit_name = request.POST.get('unitName')
        course_description = request.POST.get('courseDescription')
        required_qualification = request.POST.get('requiredQualification')
        teaching_materials = request.POST.get('teachingMaterials')
        session_times = request.POST.get('sessionTimes')
        responsibilities = request.POST.get('responsibilities')
        benefits = request.POST.get('benefits')

        # Create a new JobListing object and save it to the database
        job_listing = JobListing(
            unit_name=unit_name,
            course_description=course_description,
            required_qualification=required_qualification,
            teaching_materials=teaching_materials,
            session_times=session_times,
            responsibilities=responsibilities,
            benefits=benefits
        )
        job_listing.save()

        return redirect('jobListing')  # Redirect to jobListing URL

    return render(request, 'createjob.html')
