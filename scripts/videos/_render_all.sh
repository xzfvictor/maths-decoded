#!/usr/bin/env bash
# Render and re-mux all 11 fixed scene files (uses cached partial files when possible).
set -uo pipefail

PROJECT_ROOT="/home/victor/maths-decoded"
MEDIA_DIR="${PROJECT_ROOT}/videos-rerender"
mkdir -p "${MEDIA_DIR}"

# Args: scene-stem  TopicId                       LessonId                          SceneClass
run_one() {
    local stem="$1" topic="$2" lesson="$3" cls="$4"

    local video_mp4="${MEDIA_DIR}/videos/${stem}/720p30/${cls}.mp4"
    local out="${PROJECT_ROOT}/public/video/lessons/${topic}/${lesson}.mp4"

    mkdir -p "$(dirname "${out}")"

    echo "==[render]== ${stem}/${cls}"
    timeout 600 docker run --rm \
        -v "${PROJECT_ROOT}:/work" \
        -w /work \
        manimcommunity/manim:latest \
        manim -qm \
            --media_dir "/work/videos-rerender" \
            "/work/scripts/videos/${stem}.py" "${cls}" 2>&1 \
        | grep -E "Rendered|File ready|Error" | head -5

    if [ ! -f "${video_mp4}" ]; then
        echo "FAIL render: ${video_mp4} not found"
        return 1
    fi
    echo "  ok: $(basename ${video_mp4}) ($(stat -c %s ${video_mp4}) bytes)"

    echo "==[mux audio]== ${topic}/${lesson}"
    # Translate host paths to in-container paths under /work.
    docker_video="/work/videos-rerender/videos/${stem}/720p30/${cls}.mp4"
    docker_out="/work/public/video/lessons/${topic}/${lesson}.mp4"
    timeout 120 docker run --rm \
        -v "${PROJECT_ROOT}:/work" \
        jrottenberg/ffmpeg:latest \
        -hide_banner -loglevel warning \
        -y \
        -i "${docker_video}" \
        -i "/work/public/audio/lessons/${topic}/${lesson}.mp3" \
        -c:v copy -c:a aac -b:a 128k -shortest \
        "${docker_out}" 2>&1 | tail -3

    if [ -f "${out}" ]; then
        echo "  ok: ${out} ($(stat -c %s ${out}) bytes)"
    else
        echo "FAIL mux: ${out}"
        return 1
    fi
    echo
}

run_one combining-laws           l10a-an-fractional-exponents  combining-laws              CombiningLawsScene
run_one fractional-index-definition l10a-an-fractional-exponents  fractional-index-definition  FractionalIndexDefinitionScene
run_one log-definition           l10a-an-logarithms-scales    log-definition              LogDefinitionScene
run_one log-laws                 l10a-an-logarithms-scales    log-laws                    LogLawsScene
run_one log-scales               l10a-an-logarithms-scales    log-scales                  LogScalesScene
run_one one-solution             l10a-asp-trig-equations      one-solution                OneSolutionScene
run_one design-test-refine       l10a-asp-spatial-algorithms  design-test-refine          DesignTestRefineScene
run_one linear-fit-equation      l10a-ast-bivariate-lines     linear-fit-equation         LinearFitEquationScene
run_one predictions-caveats      l10a-ast-bivariate-lines     predictions-caveats         PredictionsCaveatsScene
run_one mean-and-stddev          l10a-ast-mean-standard-deviation mean-and-stddev          MeanAndStddevScene
run_one range-iqr                l10a-ast-measures-of-spread  range-iqr                   RangeIqrScene

echo "All 11 scenes rendered and re-muxed."
