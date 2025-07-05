import pandas as pd
import os

def load_data():
    try:
        file_path = "data/meteo_clean.csv"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} non trouvé.")

        df = pd.read_csv(file_path)
        print(f"[✔] Données chargées depuis {file_path} :")
        print(df.head())

        # Tu pourrais ajouter ici un chargement vers une base PostgreSQL si besoin
    except Exception as e:
        print(f"[❌] Erreur durant le chargement : {e}")
        raise e
