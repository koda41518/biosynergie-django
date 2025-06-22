from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     # autres paths...
    path('register/', views.register, name='register'),
    path('', views.welcome, name='welcome'),             # Accueil
    path('mode-emploi/', views.mode_emploi, name='mode_emploi'),  # Mode d'emploi
    path('home/', views.home, name='home'),              # Données en temps réel
    path('diagnostic/', views.diagnostic_view, name='diagnostic'),  # Diagnostic intelligent
    path('api/data/', views.sensor_data, name='sensor_data'),       # API capteurs
    path('donnees/', views.home, name='donnees'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]





