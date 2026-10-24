# État des lieux du site trottinette-accessoires.fr

Date : 24 octobre 2026 — analyse faite sur le contenu de la branche `main` (commit `fa333d0`), sans aucune modification du site.

Méthode : un script a lu les 20 fichiers HTML de `site/` et relevé, page par page, les balises SEO, les liens internes, les liens Amazon, les images, le tutoiement, les prix et les mentions de « test ». Les chiffres ci-dessous en sont issus.

---

## 1. Comment le site est organisé

**En bref : tout est copié-collé dans chaque fichier.** Il n'y a aucun système de gabarit (« template » : un modèle commun que chaque page réutilise). Modifier l'en-tête ou le pied de page oblige donc à modifier les 19 pages une par une — ou par script.

| Élément | Où il se trouve | Constat |
|---|---|---|
| En-tête / menu (`<nav>`) | Copié dans chaque page | **Identique partout** (seul le lien actif change). Bon point. |
| Pied de page (`<footer>`) | Copié dans chaque page | **5 versions différentes** : accueil, page Guides, articles, À propos, mentions légales. Textes et liens différents (3, 4 ou 5 catégories ; « Ton guide », « Votre guide »…). |
| CSS commun | `site/css/style.css` (806 lignes) | Chargé par toutes les pages. |
| CSS propre aux articles | Bloc `<style>` copié dans chaque article | **3 variantes** : une de 102 lignes (9 articles), une de 267 lignes (5 articles : casque, antivol, sacoche, éclairage, support), une de 124 lignes (Top 10). D'où des cartes produit et encadrés qui ne se ressemblent pas d'un article à l'autre. |
| JavaScript | `site/js/nav.js` (menu mobile) + un petit script de barre de progression copié dans chaque article | Léger, sans dépendance. |
| Polices et icônes | Google Fonts (Inter) + icônes Tabler depuis un CDN | Deux URL Inter différentes (avec ou sans graisse 900). Les icônes Tabler sont chargées en version `@latest` : la version peut changer à tout moment sans prévenir. |
| Statistiques | Script Umami dans le `<head>` | Présent sur les 19 pages. Bon point. |

Les articles semblent avoir été produits en deux vagues avec deux modèles différents (même structure ligne pour ligne à l'intérieur de chaque vague).

---

## 2. Inventaire des pages

20 fichiers HTML : 19 pages publiques + le fichier de vérification Google (qui ne doit pas être dans le sitemap : c'est correct).

Légende : **Accueil / Guides** = la page est-elle liée depuis l'accueil / la page Guides ? **Liens entrants** = nombre de pages du site qui pointent vers elle (menu et pied de page compris).

| Page | Sitemap | Accueil | Guides | Liens entrants | Statut |
|---|---|---|---|---|---|
| `index.html` (accueil) | oui | — | oui | 18 | OK |
| `articles/index.html` (Guides) | oui | oui | — | 18 | OK |
| `a-propos.html` | oui | oui | oui | 18 | OK |
| `mentions-legales.html` | oui | oui | oui | 18 | OK |
| top-10-accessoires-indispensables | oui | oui | oui | 2 | Peu lié |
| meilleur-casque-trottinette-electrique | oui | oui | oui | 18 | OK (via pied de page) |
| meilleur-antivol-trottinette-electrique | oui | oui | oui | 18 | OK (via pied de page) |
| sacoche-trottinette-electrique | oui | oui | oui | 17 | OK (via pied de page) |
| kit-eclairage-trottinette-electrique | oui | oui | oui | 4 | Peu lié |
| support-telephone-trottinette | oui | oui | oui | 4 | Peu lié |
| gants-trottinette-electrique-hiver | oui | oui | oui | 3 | Peu lié |
| guide-entretien-trottinette-electrique | oui | oui | oui | 3 | Peu lié |
| accessoires-trottinette-pas-chers | oui | oui | oui | 3 | Peu lié |
| accessoires-trottinette-hiver | oui | non | oui | 1 | Quasi orpheline |
| trottinette-sous-la-pluie | oui | non | **non** | 1 (Top 10 seulement) | **Quasi orpheline** |
| accessoires-trottinette-trajet-travail | oui | non | **non** | 1 (Top 10 seulement) | **Quasi orpheline** |
| budget-accessoires-trottinette-debutant | oui | non | **non** | **0** | **Orpheline** |
| confort-trottinette-electrique | oui | non | **non** | **0** | **Orpheline** |
| securiser-trottinette-electrique | oui | non | **non** | **0** | **Orpheline** |

**À retenir :**
- **3 pages totalement orphelines** (aucun lien vers elles) : budget débutant, confort, sécuriser. L'audit n'en citait que 2 ; il y en a en réalité 5 sans lien depuis la page Guides.
- La page Guides ne liste que **10 articles sur 15**.
- Le sitemap liste bien les 19 pages publiques, sans page fantôme. Mais il n'a **aucune date `lastmod`** (date de dernière modification que Google utilise pour savoir quoi revisiter).
- `robots.txt` est correct.

## 3. Liens internes

- **Aucun lien interne cassé** (tous les `href` vers des fichiers locaux existent).
- **Maillage faible** : 14 articles sur 15 ne lient, dans leur contenu, que vers les 3 mêmes pages (casque, antivol, sacoche) — en réalité il s'agit des liens du pied de page. Seul le Top 10 fait de vrais liens contextuels (10 articles).
- Boucle sans issue : la page À propos dit « Consultez nos mentions légales pour nous contacter », mais les mentions légales ne contiennent aucun moyen de contact.

## 4. Images

| Problème | Pages concernées |
|---|---|
| **Image cassée + légende « Illustration - Image à venir. »** : le fichier `placeholder.webp` n'existe pas, le visiteur voit une image brisée. | hiver, pas-chers, trajet-travail, budget-débutant, confort, sécuriser (6 articles) |
| Image servie en JPG alors que le format WebP est la règle | Top 10 (`flatlay-pack-accessoires.jpg`, 187 Ko), gants (172 Ko), entretien (130 Ko), pluie (151 Ko) — pas de version WebP existante |
| Fichiers JPG **inutilisés** (doublons des WebP) | 7 fichiers, environ 1,7 Mo au total (antivol, 3 casques, phare, sacoche, support) |
| Aucun attribut `width` / `height` | Toutes les images du site (provoque des « sauts » de mise en page au chargement) |
| Pas de `loading="lazy"` | Les images d'articles (acceptable pour l'image principale, à vérifier pour les suivantes) |
| `alt` génériques | « Illustration article » sur les 6 images cassées |

Les images existantes ne sont pas vraiment trop lourdes (43 à 129 Ko en WebP, 1024 px de large). La plus lourde est `sacoche-guidon-etanche.webp` (129 Ko). Le favicon `.ico` pèse 60 Ko, ce qui est beaucoup pour une icône.

**Outillage** : aucun outil de conversion WebP n'est installé sur votre machine (`cwebp`, ImageMagick ou la bibliothèque Python Pillow). Il faudra en installer un pour convertir les 4 JPG — voir les questions en fin de document.

## 5. SEO technique (balises dans le `<head>`)

| Point | Constat |
|---|---|
| `<title>` (cible 50–60 caractères) | **15 articles sur 15 trop longs** (61 à 84 caractères). À propos (34) et Guides (41) trop courts. **Mentions légales : aucun title.** Le title du guide casque contient un émoji. |
| Meta description (cible 140–160) | 8 pages hors cible (132 à 178 caractères). **Mentions légales : aucune.** |
| `<h1>` | Un seul par page (bon point), mais **les 15 H1 d'articles se terminent par l'émoji 🛴**. |
| `canonical` | Présent partout sauf **mentions légales**. |
| Open Graph | **`og:image` absent sur toutes les pages.** `og:url` et `og:type` présents uniquement sur l'accueil. |
| JSON-LD (données structurées) | `Article` présent sur les 15 articles, mais : auteur = « Organization », **pas de `dateModified`**, même date `2026-07-28` partout. **Aucun `BreadcrumbList`** (fil d'Ariane). Aucune FAQ sur le site. |
| Dates visibles | Les cartes affichent « Juillet 2026 » ; aucune date de mise à jour dans les articles. |
| Mentions légales | En plus des balises manquantes, la feuille de style des icônes est chargée dans le `<body>` au lieu du `<head>`. |

## 6. Texte et crédibilité

**Tutoiement** : au moins **230 occurrences** de « tu / ta / ton / tes » dans les 15 articles et la page À propos (l'accueil et la page Guides sont au vouvoiement). Les articles mélangent souvent les deux dans la même phrase, avec des fautes d'accord typiques du remplacement automatique : « ta téléphone », « ta casque », « ta écran », « ta modèle », « ta trajet », « ta chargeur ».

**Accents manquants** (exemples) : « a l'air libre », « plus tot », « a condition », « preparer », « n'hesitez », « arriere », « Pret a », « chaine », « lacher », « etre » ; dans les mentions légales : « Editeur », « Hebergement », « Donnees ».

**Promesses de tests sans preuve** :
- À propos : « Chaque guide est testé, retesté », titre « Comment on teste », « financer nos tests ».
- Budget débutant : « On a testé les meilleurs produits », « produits testés et approuvés ».
- Accueil et page Guides : « On a testé les meilleurs antivols ».
- Pied de page de l'accueil : « Tests, comparatifs et conseils », « financer nos tests ».

**Conseils d'éclairage contradictoires** :

| Article | Ce qui est écrit |
|---|---|
| Accessoires pas chers | « 50 à 100 lumens, ce qui est suffisant pour la ville » (et recommande un pack à 50 lumens) |
| Budget débutant | Recommande un pack avec feu avant de 50 lumens |
| Hiver | « minimum 100 lumens, idéalement 200 » |
| Trajet travail | « 100-200 lumens […] sont le minimum » en hiver |
| Kit éclairage | Ville éclairée 100–300, rues sombres 400–800, hors agglomération 1000+ |
| Top 10 | « au moins 300 à 500 lumens […] indispensable » |

**Affirmations réglementaires à vérifier ou dater** (je ne les corrige pas sans source) :
- Budget débutant : « le casque n'est pas obligatoire pour les plus de 16 ans » — devenu inexact en Île-de-France depuis le 7 août 2026 (information que vous m'avez fournie pour l'étape 6).
- Guide casque : « EN 1078 : la norme européenne obligatoire » — à nuancer ou sourcer.
- Pas chers / budget : « gilet réfléchissant obligatoire hors agglomération la nuit », « sonnette obligatoire sur toutes les trottinettes » — à sourcer et dater.
- Sécuriser : « responsabilité civile obligatoire » — à sourcer et dater.
- Kit éclairage : paragraphe « Ce que dit la réglementation française » — à sourcer et dater.

**Ton** : nombreux superlatifs et majuscules (« RÈGLE DE SÉCURITÉ ABSOLUE : N'achète JAMAIS… »), émojis dans les encadrés et sommaires.

## 7. Affiliation Amazon

- **32 liens Amazon, tous vers des pages de recherche** (`amazon.fr/s?k=…`), aucun vers une fiche produit.
- Le tag `trottinetteac-21` est présent sur les 32 liens, avec `target="_blank"`. Bon point.
- Attribut `rel` = `nofollow sponsored` : il manque `noopener`.
- **17 cartes produit** : seules 6 citent une vraie marque et un vrai modèle (Kryptonite Evolution Mini-7, Abus Bordo 6000/6055, Wild Man 3L/4L, Abus Urban-I 3.0/2.0, Bollé Eco-React/Eco-Activ, Casco Active MC-10), et 4 d'entre elles mélangent deux références. Les 11 autres sont génériques (« Poncho imperméable trottinette », « Kit d'entretien trottinette électrique »…) : impossible d'y associer un ASIN sans que vous choisissiez un produit précis.
- **Prix fixes** : chaque carte affiche un prix (« ~59 € », « ~34€ »…), et le texte contient de nombreuses fourchettes (« 15-25€ », « moins de 30€ »). Les titres de deux articles contiennent un montant (« moins de 30€ », « moins de 50€ »).
- Aucun tableau comparatif, aucune FAQ.

## 8. Mentions légales et contact

Contenu actuel : éditeur « JP Depannage Informatique Thonon », directeur de publication, hébergeur « Oracle Cloud Infrastructure, France », mention Amazon, données personnelles.

Manquants (à fournir par vous, je ne les inventerai pas) : forme juridique et numéro SIREN/SIRET de l'éditeur, adresse postale, moyen de contact (e-mail ou formulaire), adresse complète de l'hébergeur, mention de l'outil de statistiques Umami dans la partie données personnelles.

## 9. Divers

- `README.md` est obsolète (cite `favicon.svg`, un dossier `seo/` et « 13 guides » qui n'existent pas). À mettre à jour en fin de projet.

---

## 10. Plan proposé pour la suite

Je garde vos 6 étapes et leur ordre. Ajustements proposés suite à l'état des lieux :

**Étape 1 — Corrections éditoriales** (15 articles + À propos + accueil + Guides)
1. Vouvoiement et accords (≈ 230 occurrences), un commit par groupe d'articles.
2. Accents et ponctuation française.
3. Émojis retirés des 15 H1 et du title casque.
4. Harmonisation de l'éclairage sur une seule grille de référence (voir question 2).
5. Remplacement des « testé » non prouvés par la formulation honnête.
6. Affirmations réglementaires : chacune sourcée et datée, ou retirée, ou marquée `TODO-PROPRIO`.

**Étape 2 — Structure et SEO technique**
1. Un seul pied de page pour les 19 pages (fusion des 5 versions), appliqué par script.
2. Page Guides complète (15 articles) et ajout des 5 articles manquants ; accueil enrichi.
3. Maillage : 3 à 5 liens contextuels par article.
4. Titles, descriptions, Open Graph complets (`og:image` = image de l'article), canonical et head des mentions légales.
5. JSON-LD `Article` complété + `BreadcrumbList`, dates visibles, sitemap avec `lastmod`.
6. Images : 6 images cassées (voir question 3), conversion des 4 JPG en WebP, `width`/`height`/`lazy` partout.

**Étape 3 — Crédibilité et légal** : comme prévu, avec une liste précise de `TODO-PROPRIO`.

**Étape 4 — Affiliation** : comme prévu. Le fichier `docs/asin-a-fournir.md` distinguera les 6 produits nommés (il vous suffit de donner l'ASIN) et les 11 produits génériques (il faut d'abord choisir un modèle précis).

**Étape 5 — Interface** : je propose d'y regrouper les 3 variantes de CSS d'articles dans `style.css` (une seule apparence pour les cartes, encadrés, boutons), de fixer la version des icônes Tabler et d'unifier la police Inter. Page d'exemple d'abord, comme demandé.

**Étape 6 — Contenu** : comme prévu.

### Questions pour vous

1. ~~Branche Git~~ — réglé : la branche `optimisation-seo-ui` existait déjà, en retard sur `main` et sans travail propre ; elle a été recréée depuis `main` avec votre accord.
2. **Éclairage** : je propose de prendre la grille de l'article Kit éclairage comme référence unique (ville éclairée 100–300 lumens, rues sombres 400–800, hors agglomération 1000+) et d'aligner les autres articles dessus, en précisant qu'il s'agit d'une recommandation et non d'une obligation légale. D'accord ?
3. **6 images cassées** : je les retire en attendant vos images (recommandé), ou vous fournissez des images maintenant ?
4. **Conversion WebP** : puis-je installer un outil de conversion d'images sur votre machine (par exemple `sudo apt install webp`) ? Ce n'est pas une dépendance du site, seulement un outil local.
5. **Fichiers JPG inutilisés** (1,7 Mo) : puis-je les supprimer du dépôt ? Ce ne sont pas des pages, aucune URL indexée n'en dépend à ma connaissance (à vérifier dans Search Console si vous le souhaitez).
6. **Fourchettes de prix dans le texte** (« 15-25 € », « moins de 30 € », y compris dans deux titres) : CLAUDE.md interdit les prix fixes. Je propose de retirer les prix des cartes produit (étape 4) et de garder seulement des ordres de grandeur prudents dans le texte (« moins de 30 € ») là où ils servent le lecteur. Voulez-vous plutôt supprimer tout montant ?
7. **Script de vérification** : puis-je ajouter au dépôt un petit script Python (`outils/verifier-site.py`, sans dépendance) qui vérifie liens cassés, pages orphelines et sitemap ? Il servira à chaque fin d'étape, et vous pourrez le relancer vous-même.
