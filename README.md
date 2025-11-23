# LearnFast - Backend Data & Analytics 🎓

Ce projet est une simulation complète du **backend de données** d'une plateforme d'e-learning (Type Udemy/Coursera).

L'objectif est de démontrer la mise en place d'un workflow **Data Engineering** complet : de la modélisation de la base de données (DDL) à l'analyse métier (DQL avancé), en passant par un pipeline ETL automatisé en Python.

## 🛠️ Stack Technique

* **Langage :** Python 3.x
* **Base de Données :** SQLite (Relationnelle)
* **Librairies :** `pandas`, `sqlite3`, `random`
* **Concepts Clés :** ETL, Data Modeling, Normalisation, Window Functions, CTEs, Joins complexes.

## 📂 Structure du Projet

| Fichier | Description |
| :--- | :--- |
| **`schema.sql`** | Script DDL définissant l'architecture de la BDD (Tables, Clés primaires/étrangères, Contraintes). |
| **`main.py`** | Script d'initialisation qui déploie le schéma SQL et crée la base `learnfast.db`. |
| **`etl.py`** | **Pipeline ETL**. Extrait les données brutes (CSV), les nettoie avec Pandas et les charge en SQL. |
| **`generate_enrollments.py`** | Script de **Data Faking**. Simule des inscriptions et des notes aléatoires pour peupler la base de données de manière réaliste. |
| **`analysis.sql`** | Requêtes SQL analytiques répondant à des problématiques business (KPIs, Classements, Revenus). |
| **`/data`** | Dossier contenant les données sources (CSV). |

## 🏗️ Architecture de Données

Le schéma respecte les principes de normalisation et d'intégrité référentielle :

* **`instructeurs`** : Liste des formateurs.
* **`cours`** : Catalogue des formations (Lié aux instructeurs via FK).
* **`etudiants`** : Base utilisateurs.
* **`inscriptions`** : Table de liaison (Many-to-Many) contenant les faits (dates, notes). Utilise une **Clé Primaire Composite** pour éviter les doublons.

## 🚀 Installation et Exécution

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/geoffrey-prelium/portfolio-sql-python-bootcamp.git](https://github.com/geoffrey-prelium/portfolio-sql-python-bootcamp.git)
    cd learnfast-sql-project
    ```

2.  **Installer les dépendances :**
    ```bash
    pip install pandas
    ```

3.  **Lancer le Pipeline :**
    Exécutez les scripts dans cet ordre pour reproduire l'environnement :

    ```bash
    # 1. Création de la structure (Tables vides)
    python main.py

    # 2. ETL : Ingestion des données de référence (CSV -> SQL)
    python etl.py

    # 3. Simulation : Génération des inscriptions et notes
    python generate_enrollments.py
    ```

## 📊 Analyse & Insights (SQL)

Le fichier `analysis.sql` contient les requêtes permettant de piloter l'activité. Voici des exemples de problèmes résolus :

### 1. Dashboard de Performance des Cours
* **Technique :** `LEFT JOIN` + Agrégation (`COUNT`, `AVG`) + `GROUP BY`.
* **But :** Identifier les cours les plus populaires et la satisfaction étudiante.

### 2. Classement des Meilleurs Étudiants (Leaderboard)
* **Technique :** **Window Functions** (`RANK() OVER...`).
* **But :** Classer les étudiants selon leur moyenne générale sans utiliser de sous-requêtes complexes.

### 3. Analyse Financière par Instructeur
* **Technique :** Multi-Jointures (`instructeurs` -> `cours` -> `inscriptions`) + Gestion des NULL (`COALESCE`).
* **But :** Calculer le Chiffre d'Affaires généré par chaque formateur.

## 👤 Auteur

**Geoffrey Lecluse** - *Data Analyst / Data Engineer en formation*

---
*Projet réalisé dans le cadre d'un Bootcamp intensif SQL & Python.*