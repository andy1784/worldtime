#!/bin/bash
# cron_localize_remaining.sh — docachka localization of EN blog posts.
# Runs _translate_all.py for each language in turn. Stops on MyMemory quota.
# Cache in /tmp/translate_cache.json persists progress across runs.
# Key summary is echoed to stdout (delivered to Telegram); full log to file.
cd /home/kaliuser/worldtime || exit 1
LOG=/home/kaliuser/.hermes/cron/output/localize_$(date +%Y%m%d).log
mkdir -p "$(dirname "$LOG")"
exec > >(tee -a "$LOG") 2>&1

# All localization cron job IDs (for self-cleanup on completion)
LOCALIZE_JOBS=(
  f7c045e79a05 a7638a600471 cbfa830e8272 b46fac3301cd
  24c4e52f1db8 061507a627e7 e59b3f4a0f9e 4b0e233ac0f1 b2dae7716b88
)

# Target: 167 EN posts * 7 languages = 1169 localized files
TARGET=1169

echo "=== Localization batch $(date) ==="
ADDED_TOTAL=0
for lang in ru es zh ja fr de uk; do
  echo "--- language: $lang ---"
  out=$(timeout 280 python3 blog/_translate_all.py "$lang" 2>&1)
  echo "$out"
  n=$(echo "$out" | grep -c "Written:")
  ADDED_TOTAL=$((ADDED_TOTAL + n))
  if echo "$out" | grep -q "QUOTA on"; then
    echo "Quota hit on $lang."
  fi
done
echo "=== Translation pass done. New files this run: $ADDED_TOTAL ==="

if [ "$ADDED_TOTAL" -gt 0 ]; then
  echo "--- rebuilding indexes + sitemap ---"
  python3 blog/make_blog_index_i18n.py 2>&1 | tail -2
  # Rebuild sitemap cleanly with full hreflang groups (overrides any raw appends)
  python3 gen_sitemap.py 2>&1 | tail -2
  git add -A
  git commit -q -m "Cron: localization batch $(date +%Y-%m-%d) — +$ADDED_TOTAL language files"
  git push origin main
  echo "--- pushed ---"
fi

# Final status
TOTAL=$(find blog -name "*-ru.html" -o -name "*-es.html" -o -name "*-zh.html" -o -name "*-ja.html" -o -name "*-fr.html" -o -name "*-de.html" -o -name "*-uk.html" | wc -l)
echo "=== SUMMARY: +$ADDED_TOTAL files this run | total localized: $TOTAL / $TARGET ==="

# Completion check: if we're at (or very near) target AND no new files added this run,
# assume localization is done -> remove remaining cron jobs.
if [ "$TOTAL" -ge $((TARGET - 20)) ] && [ "$ADDED_TOTAL" -eq 0 ]; then
  echo "=== LOCALIZATION COMPLETE (or quota-stalled at target). Cleaning up cron jobs... ==="
  if command -v hermes >/dev/null 2>&1; then
    for jid in "${LOCALIZE_JOBS[@]}"; do
      hermes cron remove "$jid" --accept-hooks >/dev/null 2>&1 && echo "removed $jid" || echo "failed to remove $jid"
    done
    echo "✅ All localization cron jobs removed. Localization finished at $TOTAL files."
  else
    echo "⚠️ hermes CLI not found — skipping auto-cleanup. Manual removal needed for jobs: ${LOCALIZE_JOBS[*]}"
  fi
fi
