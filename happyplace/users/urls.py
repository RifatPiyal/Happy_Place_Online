from django.urls import path
from users import views

#  Url paths of the website with naming
urlpatterns = [
    path('profile/', views.profile, name='user-profile'),
    ]


