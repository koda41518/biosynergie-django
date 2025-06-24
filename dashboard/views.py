from django.shortcuts import render
from django.http import JsonResponse
from .models import SensorData
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
import random

# Pour restreindre l'accès aux utilisateurs connectés
from django.contrib.auth.decorators import login_required

# === Page d'accueil ===
@login_required
def welcome(request):
    return render(request, 'dashboard/welcome.html')

# === Page Mode d'emploi ===
@login_required
def mode_emploi(request):
    return render(request, 'dashboard/mode_emploi.html')

# === Page Données en temps réel ===
@login_required
def home(request):
    last_data = SensorData.objects.order_by('-timestamp')[:10]
    return render(request, 'dashboard/home.html', {
        'history': list(reversed(last_data))
    })

# === API appelée toutes les 2 secondes par JavaScript dans home.html ===
@login_required
def sensor_data(request):
    temp = round(random.uniform(20.0, 40.0), 1)
    ph = round(random.uniform(6.0, 8.0), 2)
    pressure = random.randint(100000, 102000)
    sun = round(random.uniform(300, 1000), 1)
    methane = round(random.uniform(0.2, 1.0), 3)
    solar = round(random.uniform(10.0, 80.0), 1)
    algae = round(random.uniform(0.0, 1.0), 2)

    SensorData.objects.create(
        temperature=temp,
        ph=ph,
        pressure=pressure,
        sun_intensity=sun,
        methane_production=methane,
        solar_production=solar,
        algae_activity=algae
    )

    return JsonResponse({
        'temperature': temp,
        'ph': ph,
        'pressure': pressure,
        'sun_intensity': sun,
        'methane_production': methane,
        'solar_production': solar,
        'algae_activity': algae,
    })

# === Ancienne version de test — conservée mais non utilisée ===
@login_required
def donnees_temps_reel(request):
    data = {
        'temperature': round(random.uniform(20.0, 40.0), 1),
        'ph': round(random.uniform(6.0, 8.0), 2),
        'pressure': random.randint(100000, 102000)
    }
    return render(request, 'dashboard/home.html', data)

# === Ancienne API de test — remplaçable par sensor_data() ===
@login_required
def api_data(request):
    data = {
        "temperature": round(random.uniform(25, 40), 2),
        "ph": round(random.uniform(6.5, 8.5), 2),
        "pressure": round(random.uniform(95000, 105000), 0),
        "sun_intensity": round(random.uniform(300, 900), 1),
        "methane_production": round(random.uniform(0.1, 1.5), 3),
        "algae_activity": round(random.uniform(0.7, 1.0), 2)
    }
    return JsonResponse(data)

from .diagnostic import diagnostic_intelligent

@login_required
def diagnostic_view(request):
    diagnostic_data = None
    data = {}

    if request.method == "POST":
        data = {
            "temperature": round(random.uniform(25, 60), 1),
            "pH": round(random.uniform(5.5, 8.5), 1),
            "CH4": round(random.uniform(30, 70), 1),
            "CO2": round(random.uniform(10, 25), 1),
            "ensoleillement": random.randint(100, 600)
        }
        diagnostic_data = diagnostic_intelligent(data)

    return render(request, "dashboard/diagnostic.html", {
        "diagnostic": diagnostic_data,
        "donnees": data
    })
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # une fois inscrit, redirige vers login
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register.html', {'form': form})




from django.shortcuts import render

def welcome_view(request):
    return render(request, 'dashboard/welcome.html')


def mode_emploi_view(request):
    return render(request, 'dashboard/mode_emploi.html')