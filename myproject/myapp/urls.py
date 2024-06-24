from django.urls import path
from myapp.views import home,about,contact

urlpatterns =[
    path('home/',home,name="home"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact")
]