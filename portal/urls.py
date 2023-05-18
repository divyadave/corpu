from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLogin, CustomRegister, main, sessionalProfile, unit_page, apply_view, dashboard, sessionalapplicant,viewapplication,createjob,joblisting,viewapplication,listofapplications,viewjob,listofjobs, applicantjobdetail

urlpatterns = [
    path('', main, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegister.as_view(), name='register'),
    path('unit/', unit_page, name='unit_page'),
    path('apply/', apply_view, name='apply'),
    path('profile/', sessionalProfile , name='profile'),
    path('viewapplication/', viewapplication, name='viewapplication' ),
    path('createjob/', createjob, name='createjob' ),
    path('sessionalapplicant/', sessionalapplicant, name='sessionalapplicant' ),
    path('joblisting/', joblisting, name='joblisting' ),
    path('listofapplications/', listofapplications, name='listofapplications' ),
    path('viewjob/', viewjob, name='viewjob' ),
    path('listofjobs/', listofjobs, name='listofjobs' ),
         path('view/', applicantjobdetail, name='applicantjob' ),
]
