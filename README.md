# Trottinette Accessoires

Site de guides et de comparatifs d'accessoires pour trottinette électrique, financé par le Programme Partenaires d'Amazon (identifiant `trottinetteac-21`).

Site : [trottinette-accessoires.fr](https://trottinette-accessoires.fr)

## En bref

- Site 100 % statique : HTML, CSS et un petit fichier JavaScript. Pas de build, pas de base de données, pas de dépendance à installer.
- 19 pages publiques : l'accueil, la page Guides, 15 articles, la page À propos et les mentions légales.
- Aucune ressource externe chargée par les pages, sauf l'outil de statistiques Umami (`stats.depannage-thonon.fr`). La police et les icônes sont hébergées sur le site.
- Les règles du projet (Git, style éditorial, standards SEO, interdits) sont dans [CLAUDE.md](CLAUDE.md). La procédure pour rédiger ou modifier un article est dans [.claude/skills/article-trottinette/SKILL.md](.claude/skills/article-trottinette/SKILL.md).

## Structure du dépôt

```
site/                         ← tout ce qui est publié
├── index.html                ← accueil
├── a-propos.html             ← rédaction, méthode de sélection, financement
├── mentions-legales.html
├── articles/
│   ├── index.html            ← page Guides : les 15 articles en 3 rubriques
│   └── *.html                ← 15 guides et comparatifs
├── css/
│   ├── style.css             ← styles communs (en-tête, pied de page, accueil, couleurs, police)
│   └── article.css           ← styles des articles (cartes produit, encadrés, tableaux, FAQ)
├── fonts/
│   ├── inter-latin.woff2     ← police Inter (variable, graisses 400 à 900, caractères latins)
│   └── OFL-Inter.txt         ← licence de la police (SIL Open Font License)
├── images/
│   ├── icons.svg             ← les 40 icônes du site (Tabler Icons, licence MIT)
│   ├── hero.webp             ← image de l'accueil
│   └── articles/             ← images des articles (WebP affiché, JPG pour les aperçus de partage)
├── js/nav.js                 ← menu mobile
├── sitemap.xml
├── robots.txt
└── google135cd7e1e75b3a44.html  ← vérification Google Search Console (ne pas supprimer)

docs/
├── etat-des-lieux.md         ← audit de départ (octobre 2026)
└── asin-a-fournir.md         ← produits Amazon et leurs ASIN

outils/
└── verifier-site.py          ← vérification avant chaque mise en ligne

deploy.sh                     ← mise en ligne, à lancer sur le serveur (voir « Déploiement »)
```

L'en-tête (menu) et le pied de page sont copiés à l'identique dans chaque page : une modification doit être reportée sur les 19 pages.

## Conventions à respecter

- **Liens Amazon** : lien direct vers la fiche produit, `https://www.amazon.fr/dp/ASIN?tag=trottinetteac-21`, avec `target="_blank" rel="sponsored nofollow noopener"`. Aucun prix affiché : le bouton dit « Voir le prix sur Amazon ». Une mention d'affiliation précède le premier lien Amazon de chaque article.
- **Icônes** : `<svg class="icon" aria-hidden="true" focusable="false"><use href="/images/icons.svg?v=20261025#i-NOM"></use></svg>`. Pour une nouvelle icône, ajouter son `<symbol id="i-NOM">` dans `images/icons.svg`.
- **Couleurs** : l'accent vert d'eau `#12E8C6` sert aux fonds et aux décors. Pour du texte sur fond clair, utiliser `--accent-text` (`#0F766E`) ; pour du texte sur fond vert d'eau, `--on-accent` (`#06302B`). Ces couleurs respectent un contraste d'au moins 4,5:1.
- **Données structurées** : chaque article a un JSON-LD `Article` (avec `dateModified`) et `BreadcrumbList`, plus `FAQPage` quand une FAQ est visible sur la page (guide casque).
- **Dates** : quand un article change, mettre à jour sa date visible (« Mis à jour le… »), son `dateModified` et son `lastmod` dans `sitemap.xml`.
- **Nouvelle page** : l'ajouter au sitemap, à la page Guides et la relier depuis au moins un autre article.

## Cache : le paramètre de version

Les fichiers communs sont appelés avec un paramètre de version, par exemple `/css/style.css?v=20261025`. Les navigateurs gardent ces fichiers en mémoire : changer le paramètre les oblige à télécharger la nouvelle version.

Concerne : `css/style.css`, `css/article.css`, `images/icons.svg` et `fonts/inter-latin.woff2` (y compris dans le `@font-face` de `style.css`).

Après une modification de l'un de ces fichiers, remplacer la date partout (exemple pour passer au 1er décembre 2026, depuis la racine du dépôt) :

```bash
grep -rl "v=20261025" site | xargs sed -i 's/v=20261025/v=20261201/g'
```

## Vérifier avant de mettre en ligne

```bash
python3 outils/verifier-site.py
```

Le script (bibliothèque standard Python, sans dépendance) signale les liens internes cassés, les images manquantes, les pages orphelines, les écarts entre les pages et le sitemap, ainsi que le tutoiement et les émojis dans les titres. Code de sortie 0 : tout va bien.

Pour prévisualiser le site sur votre ordinateur :

```bash
python3 -m http.server 8080 --directory site
```

puis ouvrir http://localhost:8080/.

## Déploiement

### Comment le site est hébergé

- VPS Oracle Cloud. Le dépôt Git est cloné dans `/opt/trottinette-accessoires`.
- Caddy (conteneur Docker `caddy-site`, configuration dans `/opt/caddy/Caddyfile`) sert directement le dossier `/opt/trottinette-accessoires/site/`, en HTTPS automatique. Caddy lit les fichiers sur le disque : tout fichier modifié sur le serveur est en ligne immédiatement.
- La mise en ligne n'est pas automatique : elle se fait en lançant `deploy.sh` sur le serveur, qui récupère la branche `main` de GitHub.

### Mettre une modification en ligne

1. Travailler sur une branche (jamais directement sur `main`), puis lancer `python3 outils/verifier-site.py`.
2. Si un fichier CSS, les icônes ou la police ont changé, mettre à jour le paramètre de version (voir « Cache » ci-dessus).
3. Fusionner la branche dans `main` en avance rapide, puis envoyer sur GitHub :

   ```bash
   git checkout main
   git merge --ff-only NOM-DE-LA-BRANCHE
   git push origin main
   ```

   Si GitHub refuse le `push` parce que `main` y a avancé entre-temps, intégrer d'abord ces changements sans réécrire l'historique : `git pull --no-rebase --no-edit origin main`, puis refaire le `push`.
4. Sur le serveur :

   ```bash
   cd /opt/trottinette-accessoires
   git status        # doit n'afficher aucun fichier modifié
   ./deploy.sh
   ```

### Ce que fait `deploy.sh`

1. **Contrôle de l'état du serveur** : il signale les fichiers modifiés sur le serveur et non enregistrés dans Git (ils sont déjà en ligne).
2. **Récupération** : `git fetch` de `main` depuis GitHub. Si le serveur est déjà à jour, il ne fait rien. Sinon, il applique la mise à jour **en avance rapide uniquement** (`git merge --ff-only`) et liste les fichiers modifiés. Il n'écrase jamais rien.
3. **Avertissement de cache** : si des fichiers `.css`, `.js`, `.svg`, `.ico` ou des images ont changé, il rappelle qu'ils sont mis en cache un an et qu'il faut changer leur paramètre `?v=`. Les polices `.woff2` ne déclenchent pas cet avertissement : y penser soi-même.
4. **Vérification** : il contrôle que https://trottinette-accessoires.fr/ répond avec le code 200.

Codes de sortie :

| Code | Signification | Que faire |
|---|---|---|
| 0 | Mise en ligne réussie, ou déjà à jour | Rien |
| 2 | L'avance rapide a échoué : soit le serveur a des commits absents de GitHub, soit des fichiers modifiés directement sur le serveur entrent en conflit avec la mise à jour. Rien n'a été modifié. | Lancer `git status` et `git log origin/main..HEAD` sur le serveur, et régler la situation avant de relancer |
| 3 | Le site ne répond pas avec le code 200 | Vérifier Caddy et le site immédiatement |
| Autre | Une commande a échoué et le script s'est arrêté (par exemple GitHub injoignable lors du `git fetch`) | Lire le message affiché, corriger, relancer |

**À éviter** : modifier des fichiers directement sur le serveur. Ces modifications bloquent les déploiements suivants (code 2) et risquent d'être perdues. Toute modification doit passer par Git et GitHub.

## Licences des ressources tierces

- Icônes : [Tabler Icons](https://tabler.io/icons) 3.49.0, licence MIT (mention conservée dans `site/images/icons.svg`).
- Police : [Inter](https://rsms.me/inter/), SIL Open Font License 1.1 (texte dans `site/fonts/OFL-Inter.txt`).
