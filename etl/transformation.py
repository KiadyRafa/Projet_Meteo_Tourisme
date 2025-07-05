import json
import os
import pandas as pd

def transform_data():
    try:
        os.makedirs("data", exist_ok=True)
        # Ne garder que les fichiers JSON météo
        json_files = sorted([
            f for f in os.listdir("data")
            if f.startswith("meteo_") and f.endswith(".json")
        ])
        if not json_files:
            raise FileNotFoundError("Aucun fichier météo trouvé dans le dossier data/")

        latest_file = os.path.join("data", json_files[-1])
        with open(latest_file, "r") as f:
            data = json.load(f)

        row = {
            "city": data["name"],
            "datetime": pd.to_datetime("now"),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather": data["weather"][0]["main"]
        }

        df = pd.DataFrame([row])
        df.to_csv("data/meteo_clean.csv", index=False)

        print(f"[✔] Données transformées à partir de {latest_file} et enregistrées dans meteo_clean.csv")

    except Exception as e:
        print(f"[❌] Erreur durant la transformation : {e}")
        raise e
