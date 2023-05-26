from django.urls import path
from django.contrib.auth.views import LogoutView
<<<<<<< HEAD
from .views import CustomLogin, CustomRegister, main, sessionalProfile, unit_page, apply_view, dashboard, sessionalapplicant, viewapplication, createjob, joblisting, viewapplication, listofapplications, viewjob, listofjobs, applicantjobdetail, about, contact
from .views import CustomLogin, CustomRegister, main, sessionalProfile, unit_page, apply_view, dashboard, sessionalapplicant, viewapplication, createjob, joblisting, viewapplication, listofapplications, viewjob, listofjobs, applicantjobdetail
from .views import CustomLogin, CustomRegister, CreateJobView, about, contact, main, sessionalProfile, unit_page, apply_view, dashboard, sessionalapplicant, viewapplication, createjob, joblisting, viewapplication, listofapplications, viewjob, listofjobs, applicantjobdetail
=======
from .views import CustomLogin, CustomRegister, main, success, sessionalProfile, dashboard, sessionalapplicant,viewapplication,createjob,viewapplication,listofapplications,viewjob,job_listing, applicantjobdetail
>>>>>>> 334c92b0b1c94dcc2ffe6e56eab063f3e739840c

urlpatterns = [
    path('', main, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegister.as_view(), name='register'),
<<<<<<< HEAD
    path('unit/', unit_page, name='unit_page'),
    path('apply/', apply_view, name='apply'),
    path('profile/', sessionalProfile, name='profile'),
    path('viewapplication/', viewapplication, name='viewapplication'),
    # path('createjob/', createjob, name='createjob'),
    path('sessionalapplicant/', sessionalapplicant, name='sessionalapplicant'),
    # path('joblisting/', joblisting, name='joblisting'),
    # path('listofapplications/', listofapplications, name='listofapplications'),
    # path('viewjob/', viewjob, name='viewjob'),
    path('listofjobs/', listofjobs, name='listofjobs'),
    path('view/', applicantjobdetail, name='applicantjob'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('createjob/', createjob, name='createjob'),
    path('sessionalapplicant/', sessionalapplicant, name='sessionalapplicant'),
    path('joblisting/', joblisting, name='joblisting'),
    path('listofapplications/', listofapplications, name='listofapplications'),
    path('viewjob/', viewjob, name='viewjob'),
    path('listofjobs/', listofjobs, name='listofjobs'),
    path('view/', applicantjobdetail, name='applicantjob'),
    path('profile/', sessionalProfile, name='profile'),
    path('viewapplication/', viewapplication, name='viewapplication'),
    path('createjob/', CreateJobView.as_view(), name='createjob'),
    path('sessionalapplicant/', sessionalapplicant, name='sessionalapplicant'),
    path('joblisting/', joblisting, name='joblisting'),
    path('listofapplications/', listofapplications, name='listofapplications'),
    path('viewjob/<int:row_id>/', viewjob, name='viewjob'),
    path('listofjobs/', listofjobs, name='listofjobs'),
    path('view/', applicantjobdetail, name='applicantjob'),
=======
    path('profile/', sessionalProfile , name='profile'),
    path('viewapplication/', viewapplication, name='viewapplication' ),
    path('createjob/', createjob, name='createjob' ),
    path('sessionalapplicant/', sessionalapplicant, name='sessionalapplicant' ),
    path('joblisting/', job_listing, name='jobListing' ),
    path('listofapplications/', listofapplications, name='listofapplications' ),
    path('viewjob/', viewjob, name='viewjob' ),
    # path('listofjobs/', listofjobs, name='listofjobs' ),
    path('view/', applicantjobdetail, name='applicantjob' ),
    path('sucess', success , name="success")
>>>>>>> 334c92b0b1c94dcc2ffe6e56eab063f3e739840c
]
