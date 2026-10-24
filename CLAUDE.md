# Projet : trottinette-accessoires.fr

Site de guides et comparatifs d'accessoires pour trottinette électrique, monétisé par l'affiliation Amazon (tag `trottinetteac-21`). Objectif : un site bien référencé, crédible et agréable à lire, qui génère des clics vers Amazon.

## Architecture (à connaître avant toute modification)

- Site 100 % statique : HTML + CSS + JS, aucun build, aucune base de données, aucun PHP.
- Les fichiers publics sont dans `site/` (accueil, `articles/`, `images/`, `a-propos.html`, `mentions-legales.html`, `sitemap.xml`, `robots.txt`).
- En production, Caddy sert directement `/opt/trottinette-accessoires/site/` sur un VPS Oracle Cloud. Il n'y a aucun déploiement automatique.
- Le propriétaire déploie lui-même. Tu travailles uniquement dans ce dépôt local.
- Statistiques : Umami (script dans le `<head>` de chaque page). Google Search Console vérifié via `site/google135cd7e1e75b3a44.html`.

## Règles Git (non négociables)

- Ne jamais travailler, committer ni fusionner sur `main`. Tout le travail se fait sur la branche `optimisation-seo-ui` (ou une branche indiquée par le propriétaire).
- Ne jamais faire `git push`, `git merge` dans main, `git rebase` de main, ni réécrire l'historique.
- Un commit par étape logique, message en français, au format : `type: description courte` (types : `fix`, `seo`, `ui`, `contenu`, `affiliation`, `docs`, `chore`).
- Avant chaque commit : `git status` et `git diff --stat` pour vérifier que seuls les fichiers voulus changent.

## Ce que tu ne dois jamais faire

- Te connecter au serveur (ssh, scp, rsync) ou tenter de déployer.
- Changer l'URL d'une page existante, renommer ou supprimer un fichier `.html` publié : il n'y a pas de redirections en place, ce serait une page 404 et une perte de référencement. Si un changement d'URL te semble nécessaire, propose-le et attends l'accord.
- Supprimer ou modifier le script Umami, le fichier de vérification Google, ou le tag `trottinetteac-21`.
- Inventer quoi que ce soit : faits, chiffres, tests, avis, prix, normes, références produits (ASIN), noms de personnes, coordonnées légales. Si une information manque, laisse un marqueur `<!-- TODO-PROPRIO: ... -->` et liste-le dans ton rapport.
- Écrire « testé », « on a testé », « nos tests » si le propriétaire n'a pas fourni la preuve d'un test réel. Formulation honnête par défaut : « sélectionné d'après les fiches techniques, les normes et les avis d'acheteurs ».
- Afficher un prix fixe (« ~59 € ») : les règles du Programme Partenaires Amazon encadrent l'affichage des prix. Utilise « Voir le prix sur Amazon ».
- Ajouter un framework, un CMS, un outil de build ou une dépendance sans accord explicite.

## Style éditorial

- Vouvoiement partout, sans exception (accueil, articles, boutons, pied de page).
- Français correct : accents, accords, ponctuation française (espace avant `:` `;` `?` `!`).
- Ton : clair, direct, utile. Phrases courtes. Pas de superlatifs creux (« ultra-percutant », « incontesté »).
- Pas d'émoji dans les balises `<title>`, les `<h1>` ni les meta descriptions.
- Chaque affirmation de sécurité ou de réglementation doit être exacte et datée (« depuis le 7 août 2026 »).

## Standards techniques de chaque page

- Un seul `<h1>`, hiérarchie H2/H3 logique.
- `<title>` de 50 à 60 caractères, meta description de 140 à 160 caractères, uniques sur tout le site.
- `canonical`, balises Open Graph complètes (dont `og:image`), `lang="fr"`.
- Données structurées JSON-LD : `Article` (avec `datePublished`, `dateModified`, auteur) et `BreadcrumbList` sur les articles ; `FAQPage` seulement si la FAQ est visible sur la page.
- Images : format WebP, attributs `width`, `height`, `alt` descriptif, `loading="lazy"` sauf l'image principale.
- Liens Amazon : `rel="sponsored nofollow noopener"` et `target="_blank"`.
- En-tête, navigation et pied de page identiques sur toutes les pages.
- Mise en page lisible sur mobile (largeur 360 px), contrastes accessibles, focus clavier visible.
- Tout fichier `.html` ajouté ou modifié doit apparaître dans `site/sitemap.xml` avec un `lastmod` à jour.

## Vérification avant chaque fin d'étape

1. Aucun lien interne cassé (vérifier par script les `href` vers des fichiers locaux).
2. Toutes les pages publiées sont accessibles depuis la navigation, la page Guides ou un autre article (aucune page orpheline).
3. Le sitemap liste exactement les pages publiées.
4. Relecture du diff : rien de cassé, aucun contenu supprimé par erreur.

## Rapport de fin d'étape

À la fin de chaque étape, arrête-toi et donne au propriétaire, en français simple :
- ce qui a été fait (3 à 6 lignes) ;
- les fichiers modifiés ;
- les `TODO-PROPRIO` (informations qu'il doit fournir) ;
- la prochaine étape proposée.

Attends sa réponse avant de continuer. Le propriétaire débute avec Claude Code : explique les termes techniques en une phrase quand tu les utilises.


## Utilisation de Superpowers sur ce projet

- Utilise `brainstorming`, `writing-plans`, `verification-before-completion` et `systematic-debugging`.
- N'utilise pas `test-driven-development` : le site est en HTML statique, la vérification se fait par le script de liens et la relecture du diff.
- N'utilise pas `using-git-worktrees` : travaille directement sur la branche `optimisation-seo-ui` dans ce dossier.
- Préfère `executing-plans` à `subagent-driven-development` (moins coûteux).
- Pour `finishing-a-development-branch` : ne fusionne jamais et ne pousse jamais ; laisse la branche telle quelle et fais ton rapport.
- Les règles de ce fichier priment sur celles de Superpowers en cas de conflit.