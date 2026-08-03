"""
Manim scene for the lesson `combining-laws`
(topic `l10a-an-fractional-exponents`).

Five index laws hold for fractional exponents too. Key strategy: rewrite
every term to the same base. Worked example: 4^(1/2) * 16^(1/4) = 2 * 2 = 4.
Also show a^(-1/2) flip, and sqrt(a) * a^(-1/2) = a^0 = 1.

Target duration: ~86 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class CombiningLawsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Combining fractional indices",
            "Five index laws still work — first rewrite to the same base.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: 4^(1/2) * 16^(1/4) (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        prod = MathTex(
            r"4^{1/2} \;\times\; 16^{1/4}",
            color=BLUE_TERM,
        ).scale(1.1)
        prod.move_to(BAND_CHART_CENTER + UP * 0.7)
        prod_bg = BackgroundRectangle(prod, color=BLACK, fill_opacity=1, buff=0.25)
        prod_bg.move_to(prod.get_center())
        beat_2 = beat_group(beat_2, prod, prod_bg)
        self.play(FadeIn(prod_bg, run_time=0.4), Write(prod, run_time=1.6))
        self.wait(1.5)

        # Step 1: rewrite both terms with base 2.
        rewrite = MathTex(
            r"(2^{2})^{1/2} \times (2^{4})^{1/4} \;=\; 2^{1} \times 2^{1}",
            color=ORANGE_TERM,
        ).scale(0.95)
        rewrite.next_to(prod, DOWN, buff=0.5)
        rewrite_bg = BackgroundRectangle(rewrite, color=BLACK, fill_opacity=1, buff=0.2)
        rewrite_bg.move_to(rewrite.get_center())
        beat_2 = beat_group(beat_2, rewrite, rewrite_bg)
        self.play(FadeIn(rewrite_bg, run_time=0.4), Write(rewrite, run_time=2.0))
        self.wait(2.0)

        # Step 2: apply the product law to add exponents.
        result = MathTex(
            r"2^{1} \times 2^{1} \;=\; 2^{1+1} \;=\; 2^{2} \;=\; 4",
            color=GREEN_OK,
        ).scale(1.0)
        result.next_to(rewrite, DOWN, buff=0.45)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=1, buff=0.2)
        result_bg.move_to(result.get_center())
        beat_2 = beat_group(beat_2, result, result_bg)
        self.play(FadeIn(result_bg, run_time=0.4), Write(result, run_time=2.0))
        self.wait(3.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Negative fractional exponents still flip (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head = Text("Negative fractional exponent", font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.1)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_3 = beat_group(beat_3, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        rule = MathTex(
            r"a^{-1/2} \;=\; \dfrac{1}{\sqrt{a}}",
            color=BLUE_TERM,
        ).scale(1.0)
        rule.move_to(BAND_CHART_CENTER + UP * 0.3)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.22)
        rule_bg.move_to(rule.get_center())
        beat_3 = beat_group(beat_3, rule, rule_bg)
        self.play(FadeIn(rule_bg, run_time=0.4), Write(rule, run_time=1.6))
        self.wait(2.0)

        # Apply it: sqrt(a) * a^(-1/2) = a^(1/2 - 1/2).
        product = MathTex(
            r"\sqrt{a} \cdot a^{-1/2} \;=\; a^{1/2 - 1/2}",
            color=ORANGE_TERM,
        ).scale(1.0)
        product.next_to(rule, DOWN, buff=0.45)
        product_bg = BackgroundRectangle(product, color=BLACK, fill_opacity=1, buff=0.2)
        product_bg.move_to(product.get_center())
        beat_3 = beat_group(beat_3, product, product_bg)
        self.play(FadeIn(product_bg, run_time=0.4), Write(product, run_time=1.8))
        self.wait(1.5)

        # Zero exponent collapses to 1.
        zero = MathTex(
            r"= a^{0} \;=\; 1",
            color=GREEN_OK,
        ).scale(1.0)
        zero.next_to(product, DOWN, buff=0.45)
        zero_bg = BackgroundRectangle(zero, color=BLACK, fill_opacity=1, buff=0.2)
        zero_bg.move_to(zero.get_center())
        beat_3 = beat_group(beat_3, zero, zero_bg)
        self.play(FadeIn(zero_bg, run_time=0.4), Write(zero, run_time=1.4))
        self.wait(4.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Final takeaway (~37 s, total ≈ 86 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Same base} \;\Rightarrow\; \text{add, subtract or multiply exponents.}",
            "Rewrite to a common base first; the laws still apply.",
            final_wait=37.0,
        )
