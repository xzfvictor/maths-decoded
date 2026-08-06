"""
Manim scene for the lesson `zero-and-negative`
(topic `l9-a-exponent-laws-variables`).

Zero exponent: a^0 = 1 for any non-zero a (with variables too).
Negative exponent: a^(-n) = 1/a^n flips the term upside down.

Target duration: ~36 s (target scene length per spec).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ZeroAndNegativeScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Zero and negative exponents",
            "a^0 = 1,  and  a^(-n) = 1 / a^n",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Zero exponent: 5^0 = 1, (-3)^0 = 1, (x+1)^0 = 1 (~4 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Any non-zero base to the power 0 is 1:",
                    font_size=22, color=WHITE)
        head.move_to(BAND_CHART_CENTER + UP * 1.3)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        eq = make_equation_card(
            r"5^{0} = 1, \quad (-3)^{0} = 1, \quad (x+1)^{0} = 1",
            color=BLUE_TERM, scale=0.9,
        )
        eq.move_to(BAND_CHART_CENTER + UP * 0.0)

        self.play(
            FadeIn(head_bg, run_time=0.3),
            FadeIn(head, run_time=0.7),
            FadeIn(eq, shift=UP * 0.2, run_time=1.2),
        )
        self.wait(2.0)

        beat1 = VGroup(head, head_bg, eq)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Negative exponent: 3^(-2) = 1/9, x^(-3) = 1/x^3 (~4 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("Negative exponent flips the term upside down:",
                     font_size=22, color=WHITE)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        eq2 = make_equation_card(
            r"3^{-2} = \dfrac{1}{3^{2}} = \dfrac{1}{9}",
            color=ORANGE_TERM, scale=0.95,
        )
        eq2.move_to(BAND_CHART_CENTER + UP * 0.2)

        eq3 = make_equation_card(
            r"x^{-3} = \dfrac{1}{x^{3}}",
            color=GREEN_OK, scale=1.0,
        )
        eq3.move_to(BAND_CHART_CENTER + DOWN * 0.8)

        self.play(
            FadeIn(head2_bg, run_time=0.3),
            FadeIn(head2, run_time=0.7),
            FadeIn(eq2, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(1.0)
        self.play(FadeIn(eq3, shift=UP * 0.2, run_time=1.0))
        self.wait(1.5)

        beat2 = VGroup(head2, head2_bg, eq2, eq3)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Final takeaway (final_wait = 20 s, total ≈ 36 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{0} \;=\; 1, \quad a^{-n} \;=\; \dfrac{1}{a^{n}} \quad (\text{for } a \neq 0)",
            "Zero exponent → 1; negative exponent → reciprocal.",
            final_wait=20.0,
        )
