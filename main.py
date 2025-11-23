import sqlite3
import os

# Configuration
DB_NAME = "learnfast.db"
SCHEMA_FILE = "schema.sql"

def init_db():
    """Crée la base de données et les tables à partir du schéma."""
    
    # 1. Vérifier si le fichier schéma existe
    if not os.path.exists(SCHEMA_FILE):
        print(f"Erreur : Le fichier {SCHEMA_FILE} est introuvable.")
        return

    # 2. Connexion à la base (elle est créée si elle n'existe pas)
    try:
        with sqlite3.connect(DB_NAME) as conn:
            print(f"Connexion réussie à la base '{DB_NAME}'.")
            
            # Important pour SQLite : activer les clés étrangères
            conn.execute("PRAGMA foreign_keys = ON;")
            
            # 3. Lecture du fichier SQL
            with open(SCHEMA_FILE, 'r') as f:
                sql_script = f.read()
            
            # 4. Exécution du script
            cursor = conn.cursor()
            cursor.executescript(sql_script)
            print("Tables créées avec succès selon le schéma.")
            
    except sqlite3.Error as e:
        print(f"Une erreur SQLite est survenue : {e}")

if __name__ == "__main__":
    init_db()