from django.conf.urls import url
from . import views
from django.urls import path
app_name="first_app"
urlpatterns=[
    path('',views.home,name="home"),
    path('register',views.app,name="app"),
    path('login/',views.login,name="login"),
    
    
    path('about/',views.about,name="about"),
    path('gallery/',views.gallery,name="gallery"),
    path('contact/',views.contact,name="contact"),
]

