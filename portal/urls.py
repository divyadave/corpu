from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import TaskList, CustomLogin, CustomRegister, main, sessionalProfile, unit_page, apply_view

urlpatterns = [
    path('', main, name="home"),
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegister.as_view(), name='register'),
    path('detail/', TaskList, name='detail'),
    path('unit/', unit_page, name='unit_page'),
    path('apply/', apply_view, name='apply'),
    path('detail/', TaskList , name='detail'),
     path('profile/', sessionalProfile , name='profile')
]
