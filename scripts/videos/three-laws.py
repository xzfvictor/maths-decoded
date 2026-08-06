"""
Manim scene for the lesson `three-laws`
(topic `l9-a-exponent-laws-variables`).

The three fundamental exponent laws applied to variables:
1. Product: x^m * x^n = x^(m+n)
2. Quotient: x^m / x^n = x^(m-n)
3. Power: (x^m)^n = x^(mn)

Target duration: ~57 s (target scene length per spec).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ThreeLawsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~4 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "The three fundamental laws",
            "Same base → add, subtract or multiply exponents",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Product law: x^3 * x^5 = x^8 (~6 s)
        # ──────────────────────────────────────────────────────────────────
        head1 = Text("1. Product law", font_size=24, color=BLUE_TERM)
        head1.move_to(BAND_CHART_CENTER + UP * 1.3)
        head1_bg = BackgroundRectangle(head1, color=BLACK, fill_opacity=0.95, buff=0.15)
        head1_bg.move_to(head1.get_center())

        eq1 = make_equation_card(
            r"x^{3} \cdot x^{5} \;=\; x^{\,3 + 5} \;=\; x^{8}",
            color=BLUE_TERM, scale=1.0,
        )
        eq1.move_to(BAND_CHART_CENTER + UP * 0.0)

        self.play(
            FadeIn(head1_bg, run_time=0.3),
            FadeIn(head1, run_time=0.7),
            FadeIn(eq1, shift=UP * 0.2, run_time=1.4),
        )
        self.wait(3.0)

        beat1 = VGroup(head1, head1_bg, eq1)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Quotient law: x^10 / x^4 = x^6 (~6 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("2. Quotient law", font_size=24, color=TEAL_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        eq2 = make_equation_card(
            r"\dfrac{x^{10}}{x^{4}} \;=\; x^{\,10 - 4} \;=\; x^{6}",
            color=TEAL_TERM, scale=1.0,
        )
        eq2.move_to(BAND_CHART_CENTER + UP * 0.0)

        self.play(
            FadeIn(head2_bg, run_time=0.3),
            FadeIn(head2, run_time=0.7),
            FadeIn(eq2, shift=UP * 0.2, run_time=1.4),
        )
        self.wait(3.0)

        beat2 = VGroup(head2, head2_bg, eq2)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Power law: (x^2)^5 = x^10 (~5 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("3. Power-of-a-power law", font_size=24, color=ORANGE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.3)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())

        eq3 = make_equation_card(
            r"\left(x^{2}\right)^{5} \;=\; x^{\,2 \cdot 5} \;=\; x^{10}",
            color=ORANGE_TERM, scale=1.0,
        )
        eq3.move_to(BAND_CHART_CENTER + UP * 0.0)

        self.play(
            FadeIn(head3_bg, run_time=0.3),
            FadeIn(head3, run_time=0.7),
            FadeIn(eq3, shift=UP * 0.2, run_time=1.4),
        )
        self.wait(2.5)

        beat3 = VGroup(head3, head3_bg, eq3)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait = 32 s, total ≈ 57 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{m} a^{n} \;=\; a^{m+n}, \quad \dfrac{a^{m}}{a^{n}} \;=\; a^{m-n}, \quad (a^{m})^{n} \;=\; a^{mn}",
            "Add (product), subtract (quotient), multiply (power of a power).",
            final_wait=32.0,
        )
