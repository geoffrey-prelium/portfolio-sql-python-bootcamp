import pandas as pd
import sqlite3
import os

# Configuration
DB_NAME = "learnfast.db"
DATA_FOLDER = "data"

def extract_and_load(table_name, csv_filename, conn):
    """
    Fonction générique pour charger un CSV dans une table SQL.
    """
    csv_path = os.path.join(DATA_FOLDER, csv_filename)
    
    if not os.path.exists(csv_path):
        print(f"⚠️ Fichier introuvable : {csv_path}")
        return

    print(f"📥 Chargement de {table_name}...")
    
    # 1. EXTRACT (Lecture du CSV)
    df = pd.read_csv(csv_path)
    
    # 2. TRANSFORM (Nettoyage basique)
    # Pandas charge souvent les dates comme des chaînes, c'est OK pour SQLite.
    # Ici, on pourrait ajouter df.dropna(), df['prix'] * 1.2, etc.
    print(f"   - {len(df)} lignes trouvées.")

    # 3. LOAD (Insertion SQL)
    # if_exists='append' : ajoute les données sans supprimer la table
    # index=False : ne pas ajouter l'index Pandas (0, 1, 2...) comme colonne
    try:
        df.to_sql(table_name, conn, if_exists='append', index=False)
        print(f"   ✅ Succès : {table_name} chargée.")
    except Exception as e:
        print(f"   ❌ Erreur lors de l'insertion dans {table_name}: {e}")

def run_etl():
    # Connexion à la base
    conn = sqlite3.connect(DB_NAME)
    
    try:
        # Charger les tables dans l'ordre (attention aux Clés Étrangères !)
        # On doit charger les instructeurs AVANT les cours (car un cours dépend d'un instructeur)
        extract_and_load("instructeurs", "instructeurs.csv", conn)
        extract_and_load("cours", "cours.csv", conn)
        extract_and_load("etudiants", "etudiants.csv", conn)
        
        print("\n--- ETL Terminé avec succès ---")
        
    finally:
        conn.close()

if __name__ == "__main__":
    run_etl()