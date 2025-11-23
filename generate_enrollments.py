import sqlite3
import random

DB_NAME = "learnfast.db"

def generate_inscriptions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("🎲 Génération des inscriptions...")

    # 1. Récupérer les IDs existants (pour ne pas inventer de faux IDs)
    students = cursor.execute("SELECT id_etudiant FROM etudiants").fetchall()
    courses = cursor.execute("SELECT id_cours FROM cours").fetchall()
    
    # On transforme les résultats [(1,), (2,)] en listes simples [1, 2]
    student_ids = [s[0] for s in students]
    course_ids = [c[0] for c in courses]

    inscriptions_creees = 0

    # 2. Pour chaque étudiant, on crée des inscriptions aléatoires
    for student_id in student_ids:
        # On choisit au hasard combien de cours il prend (entre 1 et 3)
        nb_cours = random.randint(1, 3)
        
        # On choisit QUELS cours (sans doublon pour cet étudiant)
        chosen_courses = random.sample(course_ids, k=min(nb_cours, len(course_ids)))
        
        for course_id in chosen_courses:
            # Génération d'une note (80% de chance d'avoir une note, 20% NULL)
            if random.random() > 0.2:
                note = round(random.uniform(10.0, 20.0), 1) # Note entre 10 et 20
            else:
                note = None # Cours en cours, pas encore noté
            
            # 3. Insertion SQL
            try:
                cursor.execute("""
                    INSERT INTO inscriptions (id_etudiant, id_cours, note_finale)
                    VALUES (?, ?, ?)
                """, (student_id, course_id, note))
                inscriptions_creees += 1
            except sqlite3.IntegrityError:
                pass # Ignore si doublon (géré par random.sample, mais sécurité)

    conn.commit()
    conn.close()
    print(f"✅ Terminé : {inscriptions_creees} inscriptions générées et insérées.")

if __name__ == "__main__":
    generate_inscriptions()