def diagnostic_intelligent(data):
    diagnostic = {
        "biogaz": "Normal",
        "algues": "Normal",
        "solaire": "Normal",
        "alerte": []
    }

    temp = data.get("temperature", 0)
    ph = data.get("pH", 7)
    ch4 = data.get("CH4", 0)
    co2 = data.get("CO2", 0)
    ensoleillement = data.get("ensoleillement", 0)

    if not (30 <= temp <= 55):
        diagnostic["biogaz"] = "Production instable : température hors zone optimale"
        diagnostic["alerte"].append("Température non optimale pour digestion anaérobie")

    if not (6.5 <= ph <= 8):
        diagnostic["biogaz"] = "pH déséquilibré"
        diagnostic["alerte"].append("pH acide ou basique pour les bactéries méthanogènes")

    if ch4 < 50:
        diagnostic["biogaz"] = "CH₄ insuffisant"
        diagnostic["alerte"].append("Production de méthane trop faible")

    if ensoleillement < 300:
        diagnostic["algues"] = "Carence lumineuse"
        diagnostic["alerte"].append("Luminosité insuffisante pour photosynthèse")

    if co2 > 15:
        diagnostic["algues"] = "Excès de CO₂"
        diagnostic["alerte"].append("CO₂ à réguler pour éviter acidification")

    if ensoleillement >= 400:
        diagnostic["solaire"] = "Production optimale"
    elif 200 <= ensoleillement < 400:
        diagnostic["solaire"] = "Production modérée"
    else:
        diagnostic["solaire"] = "Production faible"
        diagnostic["alerte"].append("Manque d'ensoleillement pour production solaire")

    return diagnostic
