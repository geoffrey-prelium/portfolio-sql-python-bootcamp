/*
instructeurs

    Chaque instructeur a un ID unique.
    Nom obligatoire.
    Spécialité (ex: 'Data', 'Design') obligatoire.

cours

    ID unique.
    Titre obligatoire.
    Prix (peut être 0).
    Relation : Un cours est créé par un seul instructeur (Clé étrangère). 
        Si l'instructeur est supprimé, on ne veut pas supprimer le cours 
        (Gestion du ON DELETE ? À vous de choisir la stratégie, ou laissez par défaut).

etudiants

    ID unique.
    Nom complet.
    Email (doit être unique et obligatoire).
    Date d'inscription.

inscriptions (La table de liaison / Table de faits)

    C'est le cœur du système. Elle lie un étudiant à un cours.
    Elle contient la date_inscription.
    Elle contient une note (note_finale) qui peut être NULL (si le cours n'est pas fini).
    Contrainte Composite : Un étudiant ne peut pas s'inscrire deux fois au même cours 
        (La paire id_etudiant + id_cours doit être unique).
*/

CREATE TABLE instructeurs (
    id_instructeur INTEGER PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    specialite VARCHAR(50) NOT NULL
);

CREATE TABLE cours (
    id_cours INTEGER PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    prix REAL DEFAULT 0,
    id_instructeur INT,
    FOREIGN KEY (id_instructeur) REFERENCES instructeurs(id_instructeur)
    ON DELETE SET NULL
);

CREATE TABLE etudiants (
    id_etudiant INTEGER PRIMARY KEY,
    nom_complet VARCHAR(150),
    email VARCHAR(100) NOT NULL UNIQUE,
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE inscriptions (
    id_etudiant INT,
    id_cours INT,
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    note_finale DECIMAL(5, 2),
    PRIMARY KEY (id_etudiant, id_cours),
    FOREIGN KEY (id_etudiant) REFERENCES etudiants(id_etudiant),
    FOREIGN KEY (id_cours) REFERENCES cours(id_cours)
);
