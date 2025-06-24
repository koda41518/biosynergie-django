from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # Page d'accueil
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('mode-emploi/', views.mode_emploi, name='mode_emploi'),  # Mode d’emploi
    path('home/', views.home, name='home'),  # (tu peux renommer en /donnees/ si tu veux)
    path('donnees/', views.home, name='donnees'),
    path('diagnostic/', views.diagnostic_view, name='diagnostic'),  # Diagnostic intelligent
    path('api/data/', views.sensor_data, name='sensor_data'),  # API capteurs
]