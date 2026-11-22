#pylint: disable='missing-module-docstring
#pylint: disable='unused-variable'

import duckdb
import pandas as pd


def init_database(database_path: str) -> None:
    """
    Initialise la base de données DuckDB et crée la table des salaires du mois N.

    Charge les données du fichier CSV `data/salaires_mois_N.csv` dans un
    DataFrame Pandas, puis crée la table `wages_n_table` dans la base de
    données spécifiée.

    Si la table existe déjà, elle n'est pas recréée.

    Args:
        database_path (str): Chemin vers le fichier de la base de données DuckDB.

    Returns:
        None
    """

    with duckdb.connect(database=database_path) as conn:
        wages_n_df = pd.read_csv("data/salaires_mois_N.csv", sep=";")

        conn.execute("""
                    CREATE TABLE IF NOT EXISTS wages_n_table AS
                    SELECT *
                    FROM wages_n_df;
                    """)
