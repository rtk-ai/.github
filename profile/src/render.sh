#!/bin/sh
# Renders the three product cards to ../card-*.png at 2x. CHROME=/path/to/chrome ./render.sh
set -e
cd "$(dirname "$0")"
python3 -I gen-cards.py
CHROME="${CHROME:-$(command -v chromium || command -v google-chrome || true)}"
[ -n "$CHROME" ] || { echo "set CHROME to a Chromium binary" >&2; exit 1; }
for c in rtk pro icm; do
  "$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=420,520 \
    --default-background-color=00000000 --virtual-time-budget=8000 --screenshot="../card-$c.png" "file://$PWD/card-$c.html" >/dev/null 2>&1
  echo "../card-$c.png"
done
