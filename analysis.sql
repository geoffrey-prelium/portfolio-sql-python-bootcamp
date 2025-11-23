/* Requête 1 : Performance des Cours */
SELECT
    c.titre,
    i.nom AS nom_instructeur,
    COUNT(inc.id_etudiant) AS nb_inscrits,
    ROUND(AVG(inc.note_finale), 1) AS moyenne_notes
FROM
    cours c
JOIN
    instructeurs i ON c.id_instructeur = i.id_instructeur
LEFT JOIN
    inscriptions inc ON c.id_cours = inc.id_cours
GROUP BY
    c.id_cours
ORDER BY
    nb_inscrits DESC;

/* Requête 2 : Classement des étudiants (Leaderboard) */
SELECT
    e.nom_complet,
    ROUND(AVG(inc.note_finale), 2) AS moyenne_generale,
    -- La Window Function s'applique APRÈS le GROUP BY
    RANK() OVER (ORDER BY AVG(inc.note_finale) DESC) AS rang
FROM
    etudiants e
JOIN
    inscriptions inc ON e.id_etudiant = inc.id_etudiant
WHERE
    inc.note_finale IS NOT NULL -- On ignore les cours non notés
GROUP BY
    e.id_etudiant
ORDER BY
    rang;

/* Requête 3 : Chiffre d'Affaires par Instructeur */
SELECT
    i.nom AS nom_instructeur,
    -- On remplace NULL par 0 pour faire propre si aucune vente
    COALESCE(SUM(c.prix), 0) AS chiffre_affaires_total
FROM
    instructeurs i
JOIN
    cours c ON i.id_instructeur = c.id_instructeur
LEFT JOIN
    inscriptions inc ON c.id_cours = inc.id_cours
GROUP BY
    i.id_instructeur
ORDER BY
    chiffre_affaires_total DESC;