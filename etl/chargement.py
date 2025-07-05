import pandas as pd
import os

def load_data():
    try:
        file_path = "data/donnees_finales.csv"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} non trouvé.")

        df = pd.read_csv(file_path)
        print(f"[✔] Données prêtes pour le dashboard Looker Studio :")
        print(df.head())
    except Exception as e:
        print(f" Erreur durant le chargement : {e}")
        raise e
