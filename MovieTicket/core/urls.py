from django.urls import path            
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', views.sign_up, name = 'signup'),
    path('login/',  views.log_in, name = 'login'),
    path('logout/', views.log_out, name='logout'),
    # path("movie/<int>", views.login_signup, name="loginSignup"),
]
