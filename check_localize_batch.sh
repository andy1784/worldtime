#!/bin/bash
# check_localize_batch.sh — verify the localization batch ran successfully.
# Runs next morning, checks log + live site, reports to Telegram via stdout.
cd /home/kaliuser/worldtime || exit 1
LOGDIR=/home/kaliuser/.hermes/cron/output
TODAY=$(date +%Y%m%d)
YEST=$(date -d "yesterday" +%Y%m%d 2>/dev/null || date -v-1d +%Y%m%d)

exec > >(tee -a "$LOGDIR/check_$TODAY.log") 2>&1
echo "=== Localization batch check $(date) ==="

# 1. Check yesterday's log
LOG="$LOGDIR/localize_$YEST.log"
if [ -f "$LOG" ]; then
  echo "--- Log from $YEST ---"
  grep -E "SUMMARY|pushed|QUOTA|no new translations|error" "$LOG" | tail -10
  ADDED=$(grep -oE "New files this run: [0-9]+" "$LOG" | grep -oE "[0-9]+" | tail -1)
  echo "Files added (from log): ${ADDED:-unknown}"
else
  echo "No log found for $YEST (batch may not have run yet)"
fi

# 2. Count localized files in repo
TOTAL=$(find blog -name "*-ru.html" -o -name "*-es.html" -o -name "*-zh.html" -o -name "*-ja.html" -o -name "*-fr.html" -o -name "*-de.html" -o -name "*-uk.html" | wc -l)
echo "Localized files in repo now: $TOTAL / 1169 target"

# 3. Check live sitemap
LIVE=$(curl -sL --max-time 20 "https://worldtimessync.com/sitemap.xml" | grep -oE "blog/[a-z0-9-]+-(ru|es|zh|ja|fr|de|uk)\.html" | sort -u | wc -l)
echo "Localized URLs in live sitemap: $LIVE"

# 4. Check git last commit
LASTCOMMIT=$(git log -1 --pretty=format:"%h %s" 2>/dev/null)
echo "Last commit: $LASTCOMMIT"

# 5. Verify cron jobs still scheduled (or cleaned up)
JOBS=$(hermes cron list 2>&1 | grep -c "Localization batch")
echo "Localization cron jobs remaining: $JOBS"

echo "=== CHECK DONE ==="
if [ "$TOTAL" -gt 178 ]; then
  echo "✅ Progress confirmed: +$((TOTAL - 178)) files since Jul 16."
else
  echo "⚠️ No new files detected. Check MyMemory quota or script errors."
fi
