from django.urls import path
from . import views

app_name='Account'
urlpatterns = [
    path('', views.userRole, name='roll'),
    path('candidatepage', views.candidate, name='candidate'),
    path('authoritypage', views.authority, name='authority'),
]