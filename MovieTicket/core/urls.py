from django.urls import path            
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loginSignup", views.login_signup, name="loginSignup"),
    # path("loginSignup", views.login_signup, name="loginSignup"),
]