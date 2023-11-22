from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register_user, name='register'),
    path('login',views.login_user, name='login'),
    path('about', views.about, name='about'),
    path('trainers', views.trainers, name='trainers'),
    path('events', views.events, name='events'),
    path('pricing', views.pricing, name='pricing'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('coursedetails', views.coursedetails, name='coursedetails'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('index1', views.index1, name='index1'),
]
