"""
Manim scene for the lesson `strength-of-evidence`
(topic `l9-st-statistical-investigations`).

Big random samples give strong evidence; small or biased samples give weak
evidence — even if the result looks dramatic.

Target duration: ~68 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class StrengthOfEvidenceScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Strength of evidence",
            "Big random samples = strong. Small or biased = weak.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Large random sample → strong evidence (~18 s)
        # ──────────────────────────────────────────────────────────────────
        strong = make_term_card(
            "n = 2000 \\text{ (random)}",
            "strong evidence",
            GREEN_OK,
        )
        strong.move_to(BAND_CHART_CENTER + UP * 0.5)
        strong.set_z_index(2)

        self.play(FadeIn(strong, shift=UP * 0.2, run_time=1.2))
        self.wait(2.5)

        ok_note = Text(
            "Bigger random samples vary less.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(strong, DOWN, buff=0.5)
        ok_bg = BackgroundRectangle(ok_note, color=BLACK, fill_opacity=0.95, buff=0.18)
        ok_bg.move_to(ok_note.get_center())
        self.play(FadeIn(ok_bg, run_time=0.5), FadeIn(ok_note, run_time=1.2))
        self.wait(5.0)
        self.play(
            FadeOut(strong, run_time=1.0),
            FadeOut(VGroup(ok_note, ok_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Small or biased sample → weak evidence (~18 s)
        # ──────────────────────────────────────────────────────────────────
        weak = make_term_card(
            "n = 5 \\text{ (random)}",
            "weak evidence",
            RED_REJECT,
        )
        weak.move_to(BAND_CHART_CENTER + UP * 0.5)
        weak.set_z_index(2)

        self.play(FadeIn(weak, shift=UP * 0.2, run_time=1.2))
        self.wait(2.5)

        # Reject dramatic claims from tiny samples.
        cross = Cross(weak, color=RED_REJECT, stroke_width=5)
        warn = Text(
            "Tiny samples = lots of noise — don't trust dramatic claims.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(weak, DOWN, buff=0.5)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.18)
        warn_bg.move_to(warn.get_center())
        self.play(Create(cross, run_time=1.0))
        self.play(FadeIn(warn_bg, run_time=0.5), FadeIn(warn, run_time=1.2))
        self.wait(6.0)
        self.play(
            FadeOut(weak, run_time=1.0),
            FadeOut(cross, run_time=1.0),
            FadeOut(VGroup(warn, warn_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reporting findings (the third beat pairs with the last) (~14 s)
        # ──────────────────────────────────────────────────────────────────
        report = Text(
            "Report: result, effect size, sample size, limitations.",
            font_size=22,
            color=GREEN_OK,
        ).move_to(BAND_CHART_CENTER + UP * 0.5)
        report_bg = BackgroundRectangle(report, color=BLACK, fill_opacity=0.95, buff=0.18)
        report_bg.move_to(report.get_center())

        self.play(FadeIn(report_bg, run_time=0.5), FadeIn(report, run_time=1.2))
        self.wait(2.5)

        note = Text(
            "Don't claim more than the data supports.",
            font_size=22,
            color=YELLOW,
        ).next_to(report, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.5), FadeIn(note, run_time=1.2))
        self.wait(4.0)
        self.play(
            FadeOut(VGroup(report, report_bg), run_time=1.0),
            FadeOut(VGroup(note, note_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (total ≈ 68 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Big + random} \Rightarrow \text{strong evidence}",
            "Small or biased samples give weak evidence — always.",
            final_wait=25.0,
        )
