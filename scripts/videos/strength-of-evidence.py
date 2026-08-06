"""
Manim scene for the lesson `strength-of-evidence`
(topic `l9-st-statistical-investigations`).

Big random samples give strong evidence; small or biased samples give
weak evidence — even if the result is dramatic.

Render target: ~50-60 s, final_wait=46.1 s.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class StrengthOfEvidenceScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Strength of evidence",
            "Big random samples = strong. Small or biased = weak.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Large random sample → strong evidence
        # ──────────────────────────────────────────────────────────────────
        strong = make_term_card(
            r"n = 2000 \text{ (random)}",
            "strong evidence",
            GREEN_OK,
        )
        strong.move_to(BAND_CHART_CENTER + UP * 0.5)
        strong.set_z_index(2)

        self.play(FadeIn(strong, shift=UP * 0.2, run_time=1.0))
        self.wait(0.8)

        ok_note = Text(
            "Bigger random samples vary less.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(strong, DOWN, buff=0.5)
        ok_bg = BackgroundRectangle(ok_note, color=BLACK, fill_opacity=0.95, buff=0.18)
        ok_bg.move_to(ok_note.get_center())
        self.play(FadeIn(ok_bg, run_time=0.5), FadeIn(ok_note, run_time=1.0))
        self.wait(1.0)
        self.play(FadeOut(beat_group(strong, ok_note, ok_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Small or biased sample → weak evidence
        # ──────────────────────────────────────────────────────────────────
        weak = make_term_card(
            r"n = 5 \text{ (random)}",
            "weak evidence",
            RED_REJECT,
        )
        weak.move_to(BAND_CHART_CENTER + UP * 0.5)
        weak.set_z_index(2)

        self.play(FadeIn(weak, shift=UP * 0.2, run_time=1.0))
        self.wait(0.8)

        cross = Cross(weak, color=RED_REJECT, stroke_width=5)
        warn = Text(
            "Tiny samples = lots of noise — trust dramatic claims with care.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(weak, DOWN, buff=0.5)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.18)
        warn_bg.move_to(warn.get_center())
        self.play(Create(cross, run_time=0.8))
        self.play(FadeIn(warn_bg, run_time=0.5), FadeIn(warn, run_time=1.0))
        self.wait(1.0)
        self.play(FadeOut(
            beat_group(weak, cross, warn, warn_bg),
            run_time=0.8,
        ))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reporting findings
        # ──────────────────────────────────────────────────────────────────
        report = Text(
            "Report: result, effect size, sample size, limitations.",
            font_size=22,
            color=GREEN_OK,
        ).move_to(BAND_CHART_CENTER + UP * 0.4)
        report_bg = BackgroundRectangle(report, color=BLACK, fill_opacity=0.95, buff=0.18)
        report_bg.move_to(report.get_center())

        self.play(FadeIn(report_bg, run_time=0.5), FadeIn(report, run_time=1.0))
        self.wait(0.8)

        note = Text(
            "Don't claim more than the data supports.",
            font_size=22,
            color=YELLOW,
        ).next_to(report, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.5), FadeIn(note, run_time=1.0))
        self.wait(1.0)
        self.play(FadeOut(beat_group(report, report_bg, note, note_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"\text{Big + random} \Rightarrow \text{strong evidence}",
            "Small or biased samples give weak evidence — always.",
            final_wait=46.1,
        )
