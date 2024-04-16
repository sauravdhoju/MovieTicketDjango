from django.urls import path            
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('signup/', views.sign_up, name = 'signup'),
    path('login/',  views.log_in, name = 'login'),
    path('logout/', views.log_out, name='logout'),
    # path('add/', views.addMovie, name='addmovie'),
    # path("movie/<int>", views.login_signup, name="loginSignup"),
]
