#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FAIL=0
PASS=0
for audio in "$ROOT"/public/audio/lessons/m10-*/*.mp3; do
  topic="$(basename "$(dirname "$audio")")"; lesson="$(basename "$audio" .mp3)"
  video="$ROOT/public/video/lessons/$topic/$lesson.mp4"
  [ -s "$video" ] || { echo "FAIL missing $topic/$lesson"; FAIL=$((FAIL+1)); continue; }
  ad=$(docker run --rm --entrypoint ffprobe -v "$ROOT:/work" jrottenberg/ffmpeg:latest -v error -show_entries format=duration -of csv=p=0 -i "/work/public/audio/lessons/$topic/$lesson.mp3")
  vd=$(docker run --rm --entrypoint ffprobe -v "$ROOT:/work" jrottenberg/ffmpeg:latest -v error -show_entries format=duration -of csv=p=0 -i "/work/public/video/lessons/$topic/$lesson.mp4")
  python3 - "$ad" "$vd" <<'PY' || { echo "FAIL duration $topic/$lesson audio=$ad video=$vd"; FAIL=$((FAIL+1)); continue; }
import sys
ad, vd = map(float, sys.argv[1:])
if vd + 0.5 < ad or abs(vd-ad) > 1.0:
    raise SystemExit(1)
PY
  frame_dir="$ROOT/videos-rerender/validation/$topic/$lesson"
  mkdir -p "$frame_dir"
  docker run --rm -v "$ROOT:/work" jrottenberg/ffmpeg:latest -v error -y -i "/work/public/video/lessons/$topic/$lesson.mp4" -vf fps=1 "/work/videos-rerender/validation/$topic/$lesson/frame_%03d.png" >/dev/null
  count=$(find "$frame_dir" -name 'frame_*.png' | wc -l)
  [ "$count" -ge 10 ] || { echo "FAIL frames $topic/$lesson ($count)"; FAIL=$((FAIL+1)); continue; }
  echo "PASS $topic/$lesson audio=${ad}s video=${vd}s frames=$count"
  PASS=$((PASS+1))
done
echo "Year 10 video validation: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && [ "$PASS" -eq 77 ]
