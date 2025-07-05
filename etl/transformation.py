import json
import os
import pandas as pd
from datetime import datetime

def transform_data():
    try:
        os.makedirs("data", exist_ok=True)

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
            "city": data.get("name", "Unknown"),
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather": data["weather"][0]["main"]
        }

        
        final_file = "data/donnees_finales.csv"
        if os.path.exists(final_file):
            df = pd.read_csv(final_file)
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        else:
            df = pd.DataFrame([row])

        df.to_csv(final_file, index=False)
        print(f"[✔] Données transformées et ajoutées à {final_file}")

    except Exception as e:
        print(f" Erreur durant la transformation : {e}")
        raise e
