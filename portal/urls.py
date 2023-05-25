from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLogin, CustomRegister, main, success, sessionalProfile, dashboard, sessionalapplicant,viewapplication,createjob,viewapplication,listofapplications,viewjob,job_listing, applicantjobdetail

urlpatterns = [
    path('', main, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegister.as_view(), name='register'),
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
]
