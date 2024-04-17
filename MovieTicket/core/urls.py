from django.urls import path            
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('signup/', views.sign_up, name = 'signup'),
    path('login/',  views.log_in, name = 'login'),
    path('logout/', views.log_out, name='logout'),
    path('movie/<int:movie_id>/', views.moviePage, name='moviepage'),
    path('booking/<int:movie_id>/<int:schedule_id>/', views.bookMoviePage, name='book'),
    path('search/', views.search, name='search'),
    path('addSchedule/<int:movie_id>/', views.addSchedule, name='addSchedule'),
    path('editMovie/<int:movie_id>/', views.editMovie, name='editMovie'),
    path('aboutus/', views.aboutUs, name= 'aboutUs'),
]
