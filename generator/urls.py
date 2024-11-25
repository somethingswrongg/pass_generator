from django.contrib.auth.views import LoginView
from django.urls import path

from generator import views
from generator.views import AboutMeView, RegisterView, login_view

app_name = 'generator'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('test/', login_view, name='test'),
    path("password/", views.password, name='password'),
    path('about/', views.about, name='about'),
    path('passlist/', views.pass_list, name='passlist'),
    path('login/',
         LoginView.as_view(
             template_name='generator/login.html',
             redirect_authenticated_user=True,
         ),
         name='login'),
    path("logout/", views.logout_view, name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),
]
