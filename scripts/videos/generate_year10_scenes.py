#!/usr/bin/env python3
"""Generate transcript-faithful Year 10 Manim scenes from cached narration scripts."""
from __future__ import annotations
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIO = ROOT / "public/audio/lessons"
OUT = ROOT / "scripts/videos"

def pascal(slug: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in slug.split("-")) + "Scene"

def title(topic: str, lesson: str) -> str:
    words = (topic[4:] if topic.startswith("m10-") else topic) + " " + lesson
    words = words.replace("-", " ").split()
    return " ".join(w.capitalize() for w in words)

def chunks(text: str, n: int = 4) -> list[str]:
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.replace("\n", " ")) if s.strip()]
    if not sentences:
        sentences = [text.strip()]
    groups = [[] for _ in range(min(n, len(sentences)))]
    for i, sentence in enumerate(sentences):
        groups[i % len(groups)].append(sentence)
    return [textwrap.fill(" ".join(g), width=72) for g in groups if g]

template = '''"""Transcript-faithful Manim scene for {lesson} ({topic})."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = {script!r}

class {cls}(Scene):
    def construct(self) -> None:
        title = Text({scene_title!r}, font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = {sections!r}
        for words in sections:
            beat = Text(words, font_size=24, line_spacing=0.8)
            if beat.width > 10.5:
                beat.set_width(10.5)
            beat.move_to(BAND_CHART_CENTER)
            bg = BackgroundRectangle(beat, color=BLACK, fill_opacity=1, buff=0.28)
            bg.move_to(beat.get_center())
            card = beat_group(bg, beat)
            self.add(card)
            self.wait(2.0)
            self.remove(card)
        final = Text("Key idea", font_size=32, color=GREEN_OK).move_to(DOWN * 1.7)
        final_bg = BackgroundRectangle(final, color=BLACK, fill_opacity=1, buff=0.25)
        final_bg.move_to(final.get_center())
        final_box = SurroundingRectangle(final, color=GREEN_OK, buff=0.3)
        self.add(final_bg, final, final_box)
        self.wait(95)
'''

for path in sorted(AUDIO.glob("m10-*/*.json")):
    topic = path.parent.name
    lesson = path.stem
    script = path.read_text().strip()
    if not script:
        raise SystemExit(f"No transcript text in {path}")
    scene_stem = topic + "-" + lesson
    out = OUT / f"{scene_stem}.py"
    if out.exists():
        raise SystemExit(f"Refusing to overwrite existing scene: {out}")
    out.write_text(template.format(topic=topic, lesson=lesson, cls=pascal(scene_stem), scene_title=title(topic, lesson), script=script, sections=chunks(script)))
print(f"Generated {len(list(AUDIO.glob('m10-*/*.json')))} Year 10 scenes")
