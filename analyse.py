import os
import django

# Initialiser Django dans un script externe
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capteurs_site.settings')
django.setup()

from dashboard.models import SensorData


# Récupérer les 20 dernières valeurs
data = SensorData.objects.order_by('-timestamp')[:20]

def extract(field):
    return [getattr(d, field) for d in data if getattr(d, field) is not None]

# Température
temps = extract("temperature")
print(f"🌡️ Température")
print(f"   Moyenne : {sum(temps)/len(temps):.2f} °C")
print(f"   Min     : {min(temps):.2f} °C")
print(f"   Max     : {max(temps):.2f} °C\n")

# pH
phs = extract("ph")
print(f"🧬 pH")
print(f"   Moyenne : {sum(phs)/len(phs):.2f}")
print(f"   Min     : {min(phs):.2f}")
print(f"   Max     : {max(phs):.2f}\n")

# Pression
press = extract("pressure")
print(f"🧪 Pression")
print(f"   Moyenne : {sum(press)/len(press):.2f} Pa")
print(f"   Min     : {min(press):.2f} Pa")
print(f"   Max     : {max(press):.2f} Pa\n")

# Production de méthane
meth = extract("methane_production")
print(f"🔥 Méthane")
print(f"   Moyenne : {sum(meth)/len(meth):.3f} m³")
print(f"   Min     : {min(meth):.3f} m³")
print(f"   Max     : {max(meth):.3f} m³\n")

# Activité des algues
algues = extract("algae_activity")
print(f"🌿 Activité des algues")
print(f"   Moyenne : {sum(algues)/len(algues):.2f}")
print(f"   Min     : {min(algues):.2f}")
print(f"   Max     : {max(algues):.2f}")



# Charger les 5 dernières mesures
latest_data = SensorData.objects.order_by('-timestamp')[:5]

for data in latest_data:
    print(f"{data.timestamp} | Temp: {data.temperature}°C | pH: {data.ph} | Pression: {data.pressure}")
    
