from django.urls import path
from users import views
#SH
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.conf.urls import url
from django.contrib import admin

from .views import group_check, logout_view, register_teacher, register_student

#  Url paths of the website with naming
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    #SH
    path('', LoginView.as_view(template_name='index.html'), name="home"),
    path('group/', views.group_check, name='group'),
    path('register_teacher/', views.register_teacher.as_view(), name='register_teacher'),
    path('register_student/', views.register_student.as_view(), name='register_student'),



    ]


