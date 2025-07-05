import requests
import json
import os
from datetime import datetime

API_KEY = "b3d757e1eb33d2908754666841267f7e"
CITY = "Antananarivo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def extract_data():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        os.makedirs("data", exist_ok=True)
        file_name = f"data/meteo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

        print(f"[✔] Données météo extraites : {file_name}")
    except Exception as e:
        print(f" Erreur durant l'extraction : {e}")
        raise e
