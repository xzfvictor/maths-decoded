"""
Manim scene for the lesson `simplifying-rational`
(topic `l10a-aa-linear-rational`).

Cancel a common polynomial factor from numerator and denominator.
Example: (x^2 - 1) / (x - 1) = (x + 1) for x ≠ 1. Watch out — the
restriction x ≠ 1 stays even after the simplification.

Target duration: ~69.9 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class SimplifyingRationalScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Simplifying rational expressions",
            "Cancel common factors from top and bottom.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Identify a common factor (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Find a common factor", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        original = make_equation_card(
            r"\dfrac{x^{2}-1}{x-1}",
            color=BLUE_TERM, scale=1.3,
        )
        original.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(original, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        factor_note = Text(
            "Factor: x^2 - 1 = (x-1)(x+1)",
            font_size=22, color=TEAL_TERM,
        ).next_to(original, DOWN, buff=0.4)
        factor_note_bg = BackgroundRectangle(factor_note, color=BLACK,
                                             fill_opacity=0.95, buff=0.15)
        factor_note_bg.move_to(factor_note.get_center())
        self.play(FadeIn(factor_note_bg, run_time=0.4),
                  FadeIn(factor_note, run_time=1.2))
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, original, factor_note, factor_note_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Cancel (x - 1) (~12 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Cancel", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.45)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        factored = make_equation_card(
            r"\dfrac{(x-1)(x+1)}{x-1}",
            color=TEAL_TERM, scale=0.95,
        )
        factored.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(factored, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        result = make_equation_card(
            r"= x + 1",
            color=GREEN_OK, scale=0.95,
        )
        result.move_to(BAND_CHART_CENTER + DOWN * 0.85)
        self.play(FadeIn(result, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        beat3 = beat_group(head3, head3_bg, factored, result)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Keep the restriction x ≠ 1 (~6 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("But — note", font_size=26, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        restrict = make_equation_card(
            r"x \neq 1",
            color=RED_REJECT, scale=1.3,
        )
        restrict.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(restrict, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        warn = Text(
            "Original denominator was zero at x = 1 — keep that exclusion.",
            font_size=18, color=RED_REJECT,
        ).next_to(restrict, DOWN, buff=0.4)
        warn_bg = BackgroundRectangle(warn, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        warn_bg.move_to(warn.get_center())
        self.play(FadeIn(warn_bg, run_time=0.4),
                  FadeIn(warn, run_time=1.0))
        self.wait(1.5)

        beat4 = beat_group(head4, head4_bg, restrict, warn, warn_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 69.9 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\dfrac{(x-1)(x+1)}{x-1} = x+1,\ x\neq 1",
            "Cancel common polynomial factors; keep the restrictions.",
            final_wait=30.0,
        )