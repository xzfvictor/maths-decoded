"""
Manim scene for the lesson `three-laws`
(topic `l9-a-exponent-laws-variables`).

The three fundamental exponent laws applied to variables:
1. Product: a^m * a^n = a^(m+n)
2. Quotient: a^m / a^n = a^(m-n)
3. Power: (a^m)^n = a^(mn)

Target duration: ~116 s (matches the audio narration length of 116.35 s).
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
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "The three fundamental laws",
            "Same base → add, subtract or multiply exponents",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Product law with variables: x^3 * x^5 = x^8 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head1 = Text("1. Product law", font_size=24, color=BLUE_TERM)
        head1.move_to(BAND_CHART_CENTER + UP * 1.6)
        head1_bg = BackgroundRectangle(head1, color=BLACK, fill_opacity=0.95, buff=0.15)
        head1_bg.move_to(head1.get_center())

        raw1 = MathTex(r"x^{3} \cdot x^{5}", color=BLUE_TERM).scale(1.1)
        raw1.move_to(BAND_CHART_CENTER + UP * 0.5)
        raw1_bg = BackgroundRectangle(raw1, color=BLACK, fill_opacity=1, buff=0.2)
        raw1_bg.move_to(raw1.get_center())

        self.play(
            FadeIn(head1_bg, run_time=0.4),
            FadeIn(head1, run_time=0.9),
            FadeIn(raw1_bg, run_time=0.4),
            Write(raw1, run_time=1.6),
        )
        self.wait(2.0)

        step1 = MathTex(r"= x^{\,3 + 5}", color=BLUE_TERM).scale(1.1)
        step1.next_to(raw1, DOWN, buff=0.4)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=1, buff=0.2)
        step1_bg.move_to(step1.get_center())
        self.play(
            FadeIn(step1_bg, run_time=0.4),
            Write(step1, run_time=1.4),
        )
        self.wait(2.0)

        result1 = MathTex(r"= x^{8}", color=GREEN_OK).scale(1.2)
        result1.next_to(step1, DOWN, buff=0.4)
        result1_bg = BackgroundRectangle(result1, color=BLACK, fill_opacity=1, buff=0.25)
        result1_bg.move_to(result1.get_center())
        self.play(
            FadeIn(result1_bg, run_time=0.4),
            Write(result1, run_time=1.4),
        )
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(head1, head1_bg, raw1, raw1_bg, step1, step1_bg,
                           result1, result1_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Quotient law: x^10 / x^4 = x^6 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("2. Quotient law", font_size=24, color=TEAL_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.6)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        raw2 = MathTex(r"\dfrac{x^{10}}{x^{4}}", color=TEAL_TERM).scale(1.1)
        raw2.move_to(BAND_CHART_CENTER + UP * 0.5)
        raw2_bg = BackgroundRectangle(raw2, color=BLACK, fill_opacity=1, buff=0.2)
        raw2_bg.move_to(raw2.get_center())

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
            FadeIn(raw2_bg, run_time=0.4),
            Write(raw2, run_time=1.6),
        )
        self.wait(2.0)

        step2 = MathTex(r"= x^{\,10 - 4}", color=TEAL_TERM).scale(1.1)
        step2.next_to(raw2, DOWN, buff=0.4)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=1, buff=0.2)
        step2_bg.move_to(step2.get_center())
        self.play(
            FadeIn(step2_bg, run_time=0.4),
            Write(step2, run_time=1.4),
        )
        self.wait(2.0)

        result2 = MathTex(r"= x^{6}", color=GREEN_OK).scale(1.2)
        result2.next_to(step2, DOWN, buff=0.4)
        result2_bg = BackgroundRectangle(result2, color=BLACK, fill_opacity=1, buff=0.25)
        result2_bg.move_to(result2.get_center())
        self.play(
            FadeIn(result2_bg, run_time=0.4),
            Write(result2, run_time=1.4),
        )
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(head2, head2_bg, raw2, raw2_bg, step2, step2_bg,
                           result2, result2_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Power law: (x^2)^5 = x^10 (~16 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("3. Power-of-a-power law", font_size=24, color=ORANGE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.6)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())

        raw3 = MathTex(r"\left(x^{2}\right)^{5}", color=ORANGE_TERM).scale(1.1)
        raw3.move_to(BAND_CHART_CENTER + UP * 0.5)
        raw3_bg = BackgroundRectangle(raw3, color=BLACK, fill_opacity=1, buff=0.25)
        raw3_bg.move_to(raw3.get_center())

        self.play(
            FadeIn(head3_bg, run_time=0.4),
            FadeIn(head3, run_time=0.9),
            FadeIn(raw3_bg, run_time=0.4),
            Write(raw3, run_time=1.6),
        )
        self.wait(2.0)

        step3 = MathTex(r"= x^{\,2 \cdot 5}", color=ORANGE_TERM).scale(1.1)
        step3.next_to(raw3, DOWN, buff=0.4)
        step3_bg = BackgroundRectangle(step3, color=BLACK, fill_opacity=1, buff=0.2)
        step3_bg.move_to(step3.get_center())
        self.play(
            FadeIn(step3_bg, run_time=0.4),
            Write(step3, run_time=1.4),
        )
        self.wait(2.0)

        result3 = MathTex(r"= x^{10}", color=GREEN_OK).scale(1.2)
        result3.next_to(step3, DOWN, buff=0.4)
        result3_bg = BackgroundRectangle(result3, color=BLACK, fill_opacity=1, buff=0.25)
        result3_bg.move_to(result3.get_center())
        self.play(
            FadeIn(result3_bg, run_time=0.4),
            Write(result3, run_time=1.4),
        )
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(head3, head3_bg, raw3, raw3_bg, step3, step3_bg,
                           result3, result3_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~46 s, total ≈ 116 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{m} a^{n} \;=\; a^{m+n}, \quad \dfrac{a^{m}}{a^{n}} \;=\; a^{m-n}, \quad (a^{m})^{n} \;=\; a^{mn}",
            "Add (product), subtract (quotient), multiply (power of a power).",
            final_wait=45.0,
        )