from django.urls import path

from Candidate import views
from Candidate.views import handleResume, personal, contact, con, canRegistration, CanLogin, CanLogout
from django.conf.urls.static import static

app_name='Candidate'
urlpatterns = [
    path('login', CanLogin, name='login'),
    path('registration', canRegistration, name='registration'),
    path('logout', CanLogout, name='logout'),
    path('', handleResume, name='submitCV'),
    path('personal/', personal, name='personal'),

    path('con/', con, name='con'),
    path('con/contact/', contact, name='contact'),
]
