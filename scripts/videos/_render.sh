#!/usr/bin/env bash
# Render a manim scene file inside the official Docker image and mux audio.
# Usage: _render.sh <scene.py> <SceneClass> <topic> <lesson> [quality]
set -euo pipefail

PY_FILE="$1"
SCENE_CLASS="$2"
TOPIC="$3"
LESSON="$4"
QUALITY="${5:-qm}"

PROJECT_ROOT="/home/victor/maths-decoded"
SCENE_BASENAME="$(basename "$PY_FILE" .py)"

# Compose scene-based media dir
MEDIA_DIR="${PROJECT_ROOT}/videos-rerender/${TOPIC}"
mkdir -p "${MEDIA_DIR}"

# 1. Render scene (last frame / full)
echo "==[manim -${QUALITY}]== $SCENE_CLASS"
docker run --rm \
    -v "${PROJECT_ROOT}:/work" \
    -w /work \
    manimcommunity/manim:latest \
    manim "-q${QUALITY}" \
        --media_dir "/work/videos-rerender" \
        "/work/scripts/videos/${SCENE_BASENAME}.py" \
        "${SCENE_CLASS}"

# After render, manim puts mp4 at:
# videos-rerender/videos/<basename>/<quality>/<SceneClass>.mp4
VIDEO_PATH="${MEDIA_DIR}/videos/${SCENE_BASENAME}/${QUALITY}/${SCENE_CLASS}.mp4"
if [ ! -f "${VIDEO_PATH}" ]; then
    echo "Render failed: ${VIDEO_PATH} not found"
    ls -R "${MEDIA_DIR}" || true
    exit 1
fi

# 2. Mux with audio
echo "==[mux audio]== ${TOPIC}/${LESSON}"
OUTPUT_PATH="${PROJECT_ROOT}/public/video/lessons/${TOPIC}/${LESSON}.mp4"
mkdir -p "$(dirname "${OUTPUT_PATH}")"

docker run --rm \
    -v "${PROJECT_ROOT}:/work" \
    jrottenberg/ffmpeg:latest \
    -y \
    -i "${VIDEO_PATH}" \
    -i "/work/public/audio/lessons/${TOPIC}/${LESSON}.mp3" \
    -c:v copy -c:a aac -b:a 128k -shortest \
    "${OUTPUT_PATH}"

echo "Wrote: ${OUTPUT_PATH}"
ls -lh "${OUTPUT_PATH}"
