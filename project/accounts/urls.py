from django.urls import path
from . import views



urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('about',views.about, name="about"),
    path('details',views.details, name="details"),
    path('help',views.help, name="help"),
    path('anouncement',views.anouncement, name="anouncement"),
    path('wherehouse',views.wherehouse, name="wherehouse"),
    path('add',views.add, name="add"),


]


