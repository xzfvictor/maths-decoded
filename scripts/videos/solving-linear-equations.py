"""
Manim scene for the lesson `solving-linear-equations`
(topic `l9-a-linear-graphs-equations`).

A linear equation has x raised only to the first power. Solve by undoing
operations one at a time: subtract the constant, then divide by the
coefficient. The animation walks through 3x + 5 = 17 step by step.

Target duration: ~18 s (target scene length per spec).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SolvingLinearEquationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Solving linear equations",
            "Undo one step at a time: x must end up alone",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: 3x + 5 = 17 → x = 4 (~4 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("e.g.  3x + 5 = 17", font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.3)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.3),
            FadeIn(head, run_time=0.7),
        )
        self.wait(0.6)
        self.play(FadeOut(VGroup(head, head_bg), run_time=0.5))

        # Three steps shown sequentially in the same anchor.
        eq1 = make_equation_card(r"3x + 5 = 17", color=BLUE_TERM, scale=1.1)
        eq1.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=0.9))
        self.wait(0.6)

        eq2 = make_equation_card(r"3x = 12", color=TEAL_TERM, scale=1.1)
        eq2.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeOut(eq1, run_time=0.4))
        self.play(FadeIn(eq2, shift=UP * 0.2, run_time=0.9))
        self.wait(0.6)

        eq3 = make_equation_card(r"x = 4", color=GREEN_OK, scale=1.3)
        eq3.move_to(BAND_CHART_CENTER + UP * 0.0)
        note = Text(
            "Subtract 5, then divide by 3.",
            font_size=20, color=GREEN_OK,
        ).next_to(eq3, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())

        self.play(FadeOut(eq2, run_time=0.4))
        self.play(
            FadeIn(eq3, shift=UP * 0.2, run_time=1.0),
            FadeIn(note_bg, run_time=0.4),
            FadeIn(note, run_time=0.8),
        )
        self.wait(0.8)

        beat1 = VGroup(eq3, note, note_bg)
        self.play(FadeOut(beat1, run_time=0.7))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Final takeaway (final_wait = 20 s, total ≈ 18 s)
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"x \;=\; \dfrac{c - b}{a}",
            "Subtract the constant first, then divide by the coefficient.",
            final_wait=102.6,
        )
