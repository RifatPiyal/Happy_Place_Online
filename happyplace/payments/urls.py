from django.urls import path

from . import views

# url paths for payments
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('charge/', views.charge, name='charge'),
]
