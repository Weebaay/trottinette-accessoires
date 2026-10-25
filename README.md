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

- Hébergement : VPS Oracle Cloud. Caddy (conteneur Docker `caddy-site`, configuration dans `/opt/caddy/Caddyfile`) sert directement le dossier `/opt/trottinette-accessoires/site/`, en HTTPS automatique.
- Pas de déploiement automatique : le propriétaire copie lui-même le contenu de `site/` sur le serveur.
- Penser à copier aussi les dossiers `fonts/`, `css/` et `images/` (dont `icons.svg`) : sans eux, la police, les styles et les icônes ne s'affichent pas.

## Licences des ressources tierces

- Icônes : [Tabler Icons](https://tabler.io/icons) 3.49.0, licence MIT (mention conservée dans `site/images/icons.svg`).
- Police : [Inter](https://rsms.me/inter/), SIL Open Font License 1.1 (texte dans `site/fonts/OFL-Inter.txt`).
