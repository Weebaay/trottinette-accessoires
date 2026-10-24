---
name: article-trottinette
description: Procédure pour rédiger, réécrire ou optimiser un article de guide ou de comparatif du site trottinette-accessoires.fr (SEO, crédibilité, liens affiliés Amazon, mise en page). À utiliser pour toute création ou modification d'une page dans site/articles/.
---

# Rédiger ou optimiser un article

Suis ces étapes dans l'ordre pour chaque article. Les règles générales du projet sont dans `CLAUDE.md` et restent prioritaires.

## 1. Comprendre l'article

- Identifie la requête principale visée (ex. « meilleur antivol trottinette électrique ») et 3 à 5 requêtes secondaires (questions que se pose l'acheteur).
- Relis l'article en entier et note : erreurs de français, passages au tutoiement, affirmations non sourcées, produits flous, prix affichés, liens Amazon de recherche.

## 2. Structure attendue d'un comparatif

1. `<h1>` contenant la requête principale (sans émoji).
2. Introduction de 2 à 3 phrases : le problème du lecteur et la réponse courte.
3. Ligne auteur : nom, « Mis à jour le JJ mois AAAA ».
4. Encadré « Notre sélection en bref » : tableau comparatif (modèle, point fort, pour qui, bouton « Voir sur Amazon »).
5. Critères de choix (H2), concrets et chiffrés quand c'est possible.
6. Une carte par produit (H3) : nom exact du modèle (une seule référence), pour qui, points forts, points faibles, bouton.
7. Encadré « Comment nous sélectionnons » (honnête, voir CLAUDE.md).
8. Verdict, suivi immédiatement d'un bouton vers le produit recommandé.
9. FAQ de 4 à 6 questions réelles (H2 « Questions fréquentes »), avec le JSON-LD `FAQPage` correspondant.
10. Bloc « Guides liés » : 3 à 5 liens vers d'autres articles du site.
11. Mention d'affiliation visible près du premier lien Amazon.

Un guide pratique (entretien, pluie, trajet travail) suit la même logique sans tableau comparatif obligatoire.

## 3. Liens Amazon

- Lien vers la fiche produit : `https://www.amazon.fr/dp/ASIN?tag=trottinetteac-21`.
- Tu n'as pas accès à Amazon pour trouver les ASIN : n'en invente jamais. Garde le lien de recherche existant, ajoute `<!-- TODO-PROPRIO: ASIN pour [modèle exact] -->`, et ajoute une ligne au fichier `docs/asin-a-fournir.md` (article, modèle, lien de recherche actuel).
- Attributs : `rel="sponsored nofollow noopener" target="_blank"`.
- Aucun prix fixe.

## 4. Maillage interne

- 3 à 5 liens contextuels dans le texte vers d'autres guides, avec une ancre descriptive (« choisir un antivol en U », pas « cliquez ici »).
- Vérifie que l'article est lui-même lié depuis la page Guides et depuis au moins un autre article.

## 5. Contrôles finaux de l'article

- [ ] Vouvoiement partout, aucune faute d'accord ni d'accent
- [ ] `<title>` 50-60 caractères, meta description 140-160 caractères, uniques
- [ ] Un seul `<h1>`, aucun émoji dans title, H1, description
- [ ] JSON-LD `Article` + `BreadcrumbList` (+ `FAQPage` si FAQ visible), `dateModified` à jour
- [ ] Images avec `alt`, `width`, `height`, `loading="lazy"` ; aucune image « à venir » publiée
- [ ] Aucun fait, test, prix ou ASIN inventé ; les manques sont en `TODO-PROPRIO`
- [ ] `lastmod` mis à jour dans `site/sitemap.xml`
- [ ] Liens internes vérifiés
