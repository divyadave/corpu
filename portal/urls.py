from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import TaskList, CustomLogin, CustomRegister

urlpatterns  = [
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegister.as_view() , name='register'),
    path('detail/', TaskList , name='detail')
]