# ASIN à fournir

Mis à jour le 25 octobre 2026.

## À quoi sert ce fichier

Aujourd'hui, tous les boutons Amazon du site mènent à une **page de recherche** Amazon. Le visiteur doit alors chercher lui-même le produit, ce qui fait perdre des ventes. L'idéal est un lien direct vers la **fiche du produit**, de la forme `https://www.amazon.fr/dp/ASIN?tag=trottinetteac-21`.

L'**ASIN** est le code unique d'un produit sur Amazon (10 caractères, par exemple `B0XXXXXXXX`). Vous le trouvez sur la fiche Amazon, dans la section « Informations sur le produit », ou dans l'adresse de la page, juste après `/dp/`. Le plus simple est d'utiliser la barre SiteStripe d'Amazon Partenaires, qui donne le lien court déjà tagué.

Je n'ai pas accès à Amazon et je n'invente jamais d'ASIN : remplissez la dernière colonne, puis donnez-moi ce fichier. Je remplacerai les liens dans les cartes, les tableaux et les boutons de verdict. Chaque carte porte aussi un commentaire `TODO-PROPRIO` dans le code.

**Total : 17 produits**, dont 6 modèles déjà nommés et 11 produits génériques.

## 1. Modèles déjà nommés (6)

Le modèle est connu : il suffit de retrouver la fiche Amazon, après avoir choisi une seule référence quand deux sont citées.

| Article | Modèle sur le site | À faire | Lien actuel | ASIN |
|---|---|---|---|---|
| `meilleur-antivol-trottinette-electrique.html` | Kryptonite Evolution Mini-7 | Référence unique : il suffit de l'ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=antivol+trottinette+%C3%A9lectrique+kryptonite&tag=trottinetteac-21) |  |
| `meilleur-antivol-trottinette-electrique.html` | Abus Bordo 6000 / 6055 | Deux références citées : choisissez-en une (la carte, le tableau et le verdict seront alignés dessus). | [recherche actuelle](https://www.amazon.fr/s?k=antivol+abus+bordo+trottinette&tag=trottinetteac-21) |  |
| `meilleur-casque-trottinette-electrique.html` | Abus Urban-I 3.0 / 2.0 | Deux versions citées : choisissez celle qui est vendue actuellement. | [recherche actuelle](https://www.amazon.fr/s?k=casque+trottinette+%C3%A9lectrique+abus&tag=trottinetteac-21) |  |
| `meilleur-casque-trottinette-electrique.html` | Bollé Eco-React / Eco-Activ | Deux modèles cités : choisissez-en un. | [recherche actuelle](https://www.amazon.fr/s?k=casque+trottinette+bolle&tag=trottinetteac-21) |  |
| `meilleur-casque-trottinette-electrique.html` | Casco Active MC-10 | Référence unique : il suffit de l'ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=casque+trottinette+casco&tag=trottinetteac-21) |  |
| `sacoche-trottinette-electrique.html` | Sacoche Rigide Wild Man 3L / 4L | Deux contenances citées : choisissez-en une (l'article recommande 3 L dans son verdict). | [recherche actuelle](https://www.amazon.fr/s?k=sacoche+trottinette+%C3%A9lectrique+guidon&tag=trottinetteac-21) |  |

## 2. Produits génériques (11)

La carte décrit un type de produit, pas un modèle précis. Il faut d'abord **choisir un modèle réel** qui correspond à la description (et me donner son nom exact), puis son ASIN. Je mettrai alors à jour le nom et les caractéristiques de la carte pour qu'ils correspondent exactement au produit choisi.

| Article | Produit sur le site | À faire | Lien actuel | Modèle choisi + ASIN |
|---|---|---|---|---|
| `accessoires-trottinette-hiver.html` | Housse imperméable trottinette électrique | Produit générique : choisissez un modèle précis correspondant à la description de la carte, puis donnez son ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=housse+trottinette+%C3%A9lectrique+imperm%C3%A9able+hiver&tag=trottinetteac-21) |  |
| `accessoires-trottinette-pas-chers.html` | Lot éclairage LED + gilet réfléchissant | Produit générique : choisissez un modèle précis correspondant à la description de la carte, puis donnez son ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=accessoires+trottinette+%C3%A9lectrique+pas+cher&tag=trottinetteac-21) |  |
| `accessoires-trottinette-trajet-travail.html` | Top case trottinette verrouillable | Produit générique : choisissez un modèle précis correspondant à la description de la carte, puis donnez son ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=sacoche+trottinette+%C3%A9lectrique+top+case&tag=trottinetteac-21) |  |
| `budget-accessoires-trottinette-debutant.html` | Pack sécurité débutant trottinette | Produit générique : choisissez un modèle précis correspondant à la description de la carte, puis donnez son ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=accessoires+trottinette+%C3%A9lectrique+kit+d%C3%A9butant&tag=trottinetteac-21) |  |
| `confort-trottinette-electrique.html` | Kit selle confort trottinette électrique | À décider d'abord : garder ou non la recommandation de selle (voir l'avertissement légal ajouté à l'étape 1). | [recherche actuelle](https://www.amazon.fr/s?k=selle+trottinette+%C3%A9lectrique+confort&tag=trottinetteac-21) |  |
| `gants-trottinette-electrique-hiver.html` | Gants d'hiver tactiles imperméables | Produit générique : choisissez un modèle précis correspondant à la description de la carte, puis donnez son ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=gants+trottinette+%C3%A9lectrique+hiver+tactiles&tag=trottinetteac-21) |  |
| `guide-entretien-trottinette-electrique.html` | Kit d'entretien trottinette électrique | Produit générique : choisissez un modèle précis correspondant à la description de la carte, puis donnez son ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=entretien+trottinette+%C3%A9lectrique+kit&tag=trottinetteac-21) |  |
| `kit-eclairage-trottinette-electrique.html` | Kit Éclairage LED USB 2-en-1 (Avant & Arrière) | Choisissez un kit précis ; vérifiez qu'il annonce bien 500 lumens à l'avant, la recharge USB-C et l'IPX5, comme indiqué sur la carte. | [recherche actuelle](https://www.amazon.fr/s?k=%C3%A9clairage+trottinette+%C3%A9lectrique+kit+led&tag=trottinetteac-21) |  |
| `securiser-trottinette-electrique.html` | Lot sécurisation trottinette | La carte décrit un pack « Kryptonite Evolution Mini-7 + traceur GPS avec 3 mois d'abonnement » : vérifiez qu'un tel pack existe sur Amazon. Sinon, choisissez un traceur GPS précis (l'antivol a déjà sa carte dans le comparatif). | [recherche actuelle](https://www.amazon.fr/s?k=s%C3%A9curiser+trottinette+%C3%A9lectrique+antivol+GPS&tag=trottinetteac-21) |  |
| `support-telephone-trottinette.html` | Support Smartphone Housse Étanche Universel | Produit générique : choisissez un modèle précis correspondant à la description de la carte, puis donnez son ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=support+t%C3%A9l%C3%A9phone+trottinette+%C3%A9lectrique+guidon&tag=trottinetteac-21) |  |
| `trottinette-sous-la-pluie.html` | Poncho imperméable trottinette | Produit générique : choisissez un modèle précis correspondant à la description de la carte, puis donnez son ASIN. | [recherche actuelle](https://www.amazon.fr/s?k=poncho+trottinette+%C3%A9lectrique+pluie&tag=trottinetteac-21) |  |

## 3. Liens de catégorie (aucune action nécessaire)

Les boutons de fin d'article du type « Voir tous les casques sur Amazon » mènent volontairement à une recherche par catégorie. Ils peuvent rester ainsi.

## Comparatifs à compléter (suggestion)

Les articles Éclairage, Sacoche et Support téléphone ne présentent qu'un seul produit. Un tableau comparatif n'a de sens qu'à partir de 2 ou 3 modèles. Si vous le souhaitez, indiquez-moi 2 modèles supplémentaires par article (avec leur ASIN) : j'ajouterai les cartes et le tableau « Notre sélection en bref ».
