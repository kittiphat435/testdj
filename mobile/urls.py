from django.urls import path
from .views import Home, About ,Contact ,EMS, Ask_qa
urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('contact/', Contact, name='contact-page'),
    path('ems/', EMS, name='ems-page'),
    path('askqa/', Ask_qa, name='ask-page'),
]




