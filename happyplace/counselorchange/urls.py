from django.urls import path
from counselorchange import views

#  Url paths of the website with naming
urlpatterns = [
    path('', views.contact_us, name='ch-contactus'),

]
