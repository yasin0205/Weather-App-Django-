from django.urls import path
from . import views #call the view
urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
]
