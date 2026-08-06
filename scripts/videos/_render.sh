#!/usr/bin/env bash
# Render a manim scene file inside the official Docker image and mux audio.
# Usage: _render.sh <scene.py> <SceneClass> <topic> <lesson> [quality]
set -euo pipefail

PY_FILE="$1"
SCENE_CLASS="$2"
TOPIC="$3"
LESSON="$4"
QUALITY="${5:-qm}"
case "${QUALITY}" in
    qm) MANIM_QUALITY="m" ;;
    ql) MANIM_QUALITY="l" ;;
    qh) MANIM_QUALITY="h" ;;
    l|m|h|p|k) MANIM_QUALITY="${QUALITY}" ;;
    *) echo "Unknown quality: ${QUALITY}" >&2; exit 2 ;;
esac
case "${MANIM_QUALITY}" in
    l) MEDIA_QUALITY="480p15" ;;
    m) MEDIA_QUALITY="720p30" ;;
    h) MEDIA_QUALITY="1080p60" ;;
    p) MEDIA_QUALITY="2160p60" ;;
    k) MEDIA_QUALITY="" ;;
esac

PROJECT_ROOT="/home/victor/maths-decoded"
SCENE_BASENAME="$(basename "$PY_FILE" .py)"
MEDIA_DIR="${PROJECT_ROOT}/videos-rerender/${TOPIC}"
mkdir -p "${MEDIA_DIR}"

echo "==[manim -${QUALITY}]== $SCENE_CLASS"
docker run --rm \
    -v "${PROJECT_ROOT}:/work" \
    -w /work \
    manimcommunity/manim:latest \
    manim "-q${MANIM_QUALITY}" \
        --media_dir "/work/videos-rerender" \
        "/work/scripts/videos/${SCENE_BASENAME}.py" \
        "${SCENE_CLASS}"

VIDEO_PATH="${PROJECT_ROOT}/videos-rerender/videos/${SCENE_BASENAME}/${MEDIA_QUALITY}/${SCENE_CLASS}.mp4"
if [ ! -f "${VIDEO_PATH}" ]; then
    echo "Render failed: ${VIDEO_PATH} not found"
    find "${MEDIA_DIR}" -type f -maxdepth 6 -print || true
    exit 1
fi

echo "==[mux audio]== ${TOPIC}/${LESSON}"
OUTPUT_PATH="${PROJECT_ROOT}/public/video/lessons/${TOPIC}/${LESSON}.mp4"
mkdir -p "$(dirname "${OUTPUT_PATH}")"
AUDIO_DURATION="$(docker run --rm --entrypoint ffprobe -v "${PROJECT_ROOT}:/work" jrottenberg/ffmpeg:latest -v error -show_entries stream=duration -of csv=p=0 -select_streams a -i "/work/public/audio/lessons/${TOPIC}/${LESSON}.mp3")"
docker run --rm \
    -v "${PROJECT_ROOT}:/work" \
    jrottenberg/ffmpeg:latest \
    -y \
    -i "/work/videos-rerender/videos/${SCENE_BASENAME}/${MEDIA_QUALITY}/${SCENE_CLASS}.mp4" \
    -i "/work/public/audio/lessons/${TOPIC}/${LESSON}.mp3" \
    -t "${AUDIO_DURATION}" \
    -c:v copy -c:a aac -b:a 128k -shortest \
    "/work/public/video/lessons/${TOPIC}/${LESSON}.mp4"

echo "Wrote: ${OUTPUT_PATH} (target ${AUDIO_DURATION}s)"
ls -lh "${OUTPUT_PATH}"
