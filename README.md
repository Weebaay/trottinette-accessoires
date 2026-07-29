# 🛴 Trottinette Accessoires

**Site affilié Amazon** — Guides complets et comparatifs d'accessoires pour trottinette électrique.

🔗 **Site :** [trottinette-accessoires.fr](https://trottinette-accessoires.fr)

---

## Description

Site vitrine statique référençant les meilleurs accessoires pour trottinette électrique : casques, antivols, sacoches, éclairage, kits hiver, supports téléphone, etc.

Chaque article est un guide comparatif avec liens affiliés Amazon (Programme Partenaires).

## Structure

```
site/
├── index.html                ← Accueil
├── a-propos.html             ← Page À propos
├── mentions-legales.html     ← Mentions légales
├── css/
│   └── style.css             ← Thème urbain personnalisé
├── images/
│   ├── favicon.svg
│   └── icons/sprite.svg
├── seo/
│   ├── robots.txt
│   └── sitemap.xml
└── articles/                 ← 13 guides comparatifs
    ├── index.html
    ├── meilleur-antivol-trottinette-electrique.html
    ├── meilleur-casque-trottinette-electrique.html
    ├── top-10-accessoires-indispensables.html
    └── ...
```

## Déploiement

Hébergé sur **Oracle Cloud** (VPS), servi via **Caddy** (reverse proxy, HTTPS auto).

- Conteneur Docker : `caddy-site` (Caddy alpine)
- Fichier statique — pas de backend, pas de base de données
- Config Caddy : `/opt/caddy/Caddyfile`

## Technologies

- HTML5 sémantique
- CSS3 (thème urbain, tons foncés, design épuré)
- SVG inline
- Google Fonts (Inter)
- Schema.org JSON-LD (balisage enrichi)
- Pas de dépendances JavaScript côté client

## Affiliation

- Programme Partenaires Amazon EU
- ID Partenaire : `trottinetteac-21`
