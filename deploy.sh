#!/usr/bin/env bash
# ------------------------------------------------------------------
# deploy.sh — Mise en ligne du site trottinette-accessoires.fr
#
# Usage :  ./deploy.sh
#
# Sécurité : fast-forward uniquement. Si le VPS a des commits locaux
# absents de GitHub, le script s'arrête sans rien écraser.
# ------------------------------------------------------------------
set -euo pipefail

REPO="/opt/trottinette-accessoires"
BRANCH="main"
URL="https://trottinette-accessoires.fr/"

cd "$REPO"

echo "=================================================="
echo " Déploiement — $(date '+%d/%m/%Y %H:%M:%S')"
echo "=================================================="

# --- 1. État local -------------------------------------------------
DIRTY=$(git status --porcelain --untracked-files=no || true)
if [[ -n "$DIRTY" ]]; then
  echo "⚠️  Modifications locales non commitées sur le VPS :"
  echo "$DIRTY" | sed 's/^/   /'
  echo "   → Elles sont DÉJÀ en ligne (Caddy lit le disque)."
  echo "   → Elles ne seront pas écrasées tant qu'il n'y a pas de conflit."
  echo
fi

# --- 2. Récupération ----------------------------------------------
echo "→ git fetch origin $BRANCH"
git fetch --quiet origin "$BRANCH"

LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse "origin/$BRANCH")

if [[ "$LOCAL" == "$REMOTE" ]]; then
  echo "✅ Déjà à jour (${LOCAL:0:7}) — aucun changement à appliquer."
else
  echo "→ Mise à jour ${LOCAL:0:7} → ${REMOTE:0:7}"
  if git merge --ff-only "origin/$BRANCH" >/dev/null 2>&1; then
    echo "✅ Fast-forward appliqué"
    echo "   Fichiers modifiés :"
    git diff --name-only "${LOCAL}" "${REMOTE}" | sed 's/^/   /'
    if git diff --name-only "${LOCAL}" "${REMOTE}" | grep -qE '\.(css|js|svg|ico|webp|jpg|jpeg|png|gif)$'; then
      echo
      echo "⚠️  Des fichiers statiques ont changé : ils sont mis en cache 1 an."
      echo "   Pense à renommer le fichier ou ajouter ?v=2 dans le HTML."
    fi
  else
    echo "❌ Divergence détectée : le VPS a des commits absents de GitHub."
    echo "   Commits locaux non poussés :"
    git log --oneline "origin/$BRANCH..HEAD" | sed 's/^/   /'
    echo
    echo "   Rien n'a été modifié. Corrige manuellement puis relance."
    exit 2
  fi
fi

# --- 3. Vérification HTTP -----------------------------------------
echo -n "→ Vérification HTTP : "
CODE=$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 "$URL" || echo "000")
if [[ "$CODE" == "200" ]]; then
  echo "✅ $CODE — $URL répond correctement"
else
  echo "❌ $CODE — le site ne répond pas comme prévu !"
  exit 3
fi

echo "=================================================="
echo " Terminé."
echo "=================================================="
