from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys

# ✅ Ajouter le chemin du dossier principal (racine projet)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# ✅ Import des modules ETL
try:
    from etl.extraction import extract_data
    from etl.transformation import transform_data
    from etl.chargement import load_data
except ImportError as e:
    raise ImportError(f"Erreur d'import des modules ETL : {e}")

# ✅ Paramètres par défaut
default_args = {
    "start_date": datetime(2024, 1, 1),
    "catchup": False,
}

# ✅ Création du DAG
with DAG(
    dag_id="meteo_pipeline",
    description="Pipeline ETL météo automatisé avec Airflow",
    schedule_interval="@daily",
    default_args=default_args,
    tags=["meteo"]
) as dag:

    t1 = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    t2 = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    t3 = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    # ✅ Dépendance entre les tâches
    t1 >> t2 >> t3
