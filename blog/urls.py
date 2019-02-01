from django.urls import path
from . import views
urlpatterns = [
path('', views.homepage, name='homepage'),
path('gallerry', views.gallery, name="gallery"),
path('registration', views.registration, name="registration"),
path('calculator', views.calculator, name="calculator"),
]
