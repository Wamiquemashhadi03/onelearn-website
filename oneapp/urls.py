from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login',views.login, name='login'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('coursedetails', views.coursedetails, name='coursedetails'),
    path('logout', views.logout, name='logout')
]
