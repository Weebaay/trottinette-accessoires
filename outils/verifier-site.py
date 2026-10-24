#!/usr/bin/env python3
"""Vérifie le site statique avant chaque fin d'étape.

Usage (depuis la racine du dépôt) :  python3 outils/verifier-site.py

Erreurs (bloquantes, code de sortie 1) :
  - lien interne vers un fichier inexistant ;
  - image locale inexistante ;
  - page orpheline (aucune autre page ne pointe vers elle) ;
  - différence entre les pages publiées et site/sitemap.xml.
Avertissements (à corriger, non bloquants) :
  - article absent de la page Guides ;
  - émoji dans <title>, <h1> ou meta description ;
  - tutoiement dans le texte visible.
Aucune dépendance : bibliothèque standard Python uniquement.
"""
import os
import re
import sys
from html.parser import HTMLParser

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
DOMAINE = "https://trottinette-accessoires.fr"
# Fichiers HTML qui ne sont pas des pages publiques (vérification Google).
EXCLUS = {"google135cd7e1e75b3a44.html"}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐]")
TUTOIEMENT = re.compile(r"(?<![\w-])(tu|toi|ton|ta|tes|tien|tienne|t'|te)(?![\w-])", re.I)


class Analyse(HTMLParser):
    def __init__(self):
        super().__init__()
        self.liens, self.images = [], []
        self.titre, self.h1, self.description = "", "", ""
        self._dans = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.liens.append(a["href"])
        elif tag == "img" and a.get("src"):
            self.images.append(a["src"])
        elif tag == "meta" and a.get("name") == "description":
            self.description = a.get("content", "")
        elif tag in ("title", "h1"):
            self._dans = tag

    def handle_endtag(self, tag):
        if tag == self._dans:
            self._dans = None

    def handle_data(self, data):
        if self._dans == "title":
            self.titre += data
        elif self._dans == "h1":
            self.h1 += data


def url_de(chemin):
    if chemin == "index.html":
        return "/"
    if chemin.endswith("/index.html"):
        return "/" + chemin[: -len("index.html")]
    return "/" + chemin


def cible_locale(href, page):
    """Chemin du fichier visé par un lien, relatif à site/ (None si externe)."""
    href = href.split("#")[0].split("?")[0]
    if href.startswith(DOMAINE):
        href = href[len(DOMAINE):] or "/"
    if not href or re.match(r"^[a-z]+:", href) or href.startswith("//"):
        return None
    if not href.startswith("/"):
        href = "/" + os.path.normpath(os.path.join(os.path.dirname(page), href))
    chemin = href.lstrip("/")
    return chemin + "index.html" if href.endswith("/") else chemin


def texte_visible(html):
    html = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>|<!--.*?-->", " ", html)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))


def main():
    pages = sorted(
        os.path.relpath(os.path.join(d, f), RACINE)
        for d, _, fichiers in os.walk(RACINE)
        for f in fichiers
        if f.endswith(".html") and f not in EXCLUS
    )
    erreurs, avertissements = [], []
    entrants = {p: set() for p in pages}

    for page in pages:
        html = open(os.path.join(RACINE, page), encoding="utf-8").read()
        a = Analyse()
        a.feed(html)
        for href in a.liens:
            cible = cible_locale(href, page)
            if cible is None:
                continue
            if not os.path.isfile(os.path.join(RACINE, cible)):
                erreurs.append(f"Lien cassé : {page} -> {href}")
            elif cible in entrants and cible != page:
                entrants[cible].add(page)
        for src in a.images:
            cible = cible_locale(src, page)
            if cible and not os.path.isfile(os.path.join(RACINE, cible)):
                erreurs.append(f"Image manquante : {page} -> {src}")
        for nom, valeur in (("title", a.titre), ("h1", a.h1), ("description", a.description)):
            if EMOJI.search(valeur):
                avertissements.append(f"Émoji dans {nom} : {page}")
        tu = TUTOIEMENT.findall(texte_visible(html))
        if tu:
            avertissements.append(f"Tutoiement ({len(tu)}) : {page}")

    for page, sources in entrants.items():
        if page != "index.html" and not sources:
            erreurs.append(f"Page orpheline : {page}")
        if page.startswith("articles/") and page != "articles/index.html" \
                and "articles/index.html" not in sources:
            avertissements.append(f"Absent de la page Guides : {page}")

    sitemap = open(os.path.join(RACINE, "sitemap.xml"), encoding="utf-8").read()
    dans_sitemap = {u[len(DOMAINE):] for u in re.findall(r"<loc>([^<]+)</loc>", sitemap)}
    publiees = {url_de(p) for p in pages}
    for u in sorted(publiees - dans_sitemap):
        erreurs.append(f"Absente du sitemap : {u}")
    for u in sorted(dans_sitemap - publiees):
        erreurs.append(f"Dans le sitemap mais sans fichier : {u}")

    print(f"{len(pages)} pages analysées.\n")
    for titre, liste in (("ERREURS", erreurs), ("AVERTISSEMENTS", avertissements)):
        print(f"{titre} ({len(liste)})")
        for ligne in liste:
            print("  - " + ligne)
        print()
    sys.exit(1 if erreurs else 0)


if __name__ == "__main__":
    main()
