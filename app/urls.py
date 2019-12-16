from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# django.urls expects an app as an argument

# logoutf, loginf - to avoid name conflicts

urlpatterns = [
    path("", views.index, name='index'),
    path(r"register", views.register, name='register'),
    path(r"omega", views.omega, name='omega'),
    path(r"omega/<int:pk>", views.SinglePost, name='SinglePost'),
    path(r"loginf", auth_views.LoginView.as_view(
        template_name='app/login.html'), name='login'),
    path(r"logoutf", views.logoutf, name='logout'),
    path(r"registerStudent", views.registerStudent, name='registerStudent'),
    path(r"registerMentor", views.registerMentor, name='registerMentor'),
    path(r"MentorPost", views.MentorPost, name='MentorPost'),
    path(r"alpha", views.alpha, name='alpha'),
    path(r"AlphaAdd", views.AlphaAdd, name='AlphaAdd'),
    path(r"beta", views.beta, name='beta')
]
