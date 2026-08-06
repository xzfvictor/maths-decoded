"""
Manim scene for the lesson `comparing-scientific`
(topic `l9-m-scientific-notation`).

To compare numbers in scientific notation, compare the exponents
first; the larger exponent wins (for positive numbers). When the
exponents match, compare the coefficients.

Render target: ~12 s audio + 20 s final wait.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class ComparingScientificScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Comparing numbers in scientific notation",
            "Look at the exponents first; only then look at the coefficients.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: 4.2×10⁶ vs 8.7×10⁵
        # ──────────────────────────────────────────────────────────────────
        a_card = make_term_card("4.2 \\times 10^{6}", "exponent: 6", BLUE_TERM)
        b_card = make_term_card("8.7 \\times 10^{5}", "exponent: 5", ORANGE_TERM)
        pair = VGroup(a_card, b_card).arrange(RIGHT, buff=0.5)
        pair.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in pair:
            m.set_z_index(2)
        self.play(
            FadeIn(a_card, shift=UP * 0.2, run_time=0.9),
            FadeIn(b_card, shift=UP * 0.2, run_time=0.9),
        )
        self.wait(0.6)

        # Highlight that the exponents decide.
        cmp_exp = MathTex(
            r"6 \;>\; 5 \;\Rightarrow\; 10^{6} \text{ is bigger}",
            color=GREEN_OK,
        ).scale(0.9)
        cmp_exp.next_to(pair, DOWN, buff=0.5)
        cmp_exp_bg = BackgroundRectangle(cmp_exp, color=BLACK, fill_opacity=1, buff=0.18)
        cmp_exp_bg.move_to(cmp_exp.get_center())
        self.play(FadeIn(cmp_exp_bg, run_time=0.4), Write(cmp_exp, run_time=1.4))
        self.wait(0.6)

        # Verdict.
        verdict = Text("So 4.2×10⁶ is larger.", font_size=22, color=GREEN_OK)
        verdict.next_to(cmp_exp, DOWN, buff=0.4)
        verdict_bg = BackgroundRectangle(verdict, color=BLACK, fill_opacity=0.95, buff=0.15)
        verdict_bg.move_to(verdict.get_center())
        self.play(FadeIn(verdict_bg, run_time=0.3), FadeIn(verdict, run_time=0.8))
        self.wait(0.8)

        beat2 = beat_group(
            a_card, b_card, cmp_exp, cmp_exp_bg, verdict, verdict_bg,
        )
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: exponents first
        # ──────────────────────────────────────────────────────────────────
        general = MathTex(
            r"\text{Exponent decides (for positives)}",
            color=BLUE_TERM,
        ).scale(1.0)
        general.move_to(BAND_CHART_CENTER + UP * 0.6)
        general_bg = BackgroundRectangle(general, color=BLACK, fill_opacity=1, buff=0.25)
        general_bg.move_to(general.get_center())
        self.play(FadeIn(general_bg, run_time=0.4), Write(general, run_time=1.2))
        self.wait(0.6)

        sub = Text(
            "Larger exponent → larger value (when the sign is +).",
            font_size=22, color=BLUE_TERM,
        ).next_to(general, DOWN, buff=0.5)
        sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.95, buff=0.15)
        sub_bg.move_to(sub.get_center())
        self.play(FadeIn(sub_bg, run_time=0.3), FadeIn(sub, run_time=0.9))
        self.wait(1.0)

        beat3 = beat_group(general, general_bg, sub, sub_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Same exponent → compare coefficients
        # ──────────────────────────────────────────────────────────────────
        same_exp = MathTex(
            r"\text{Exponents equal? Compare the coefficients.}",
            color=ORANGE_TERM,
        ).scale(0.9)
        same_exp.move_to(BAND_CHART_CENTER + UP * 0.6)
        same_exp_bg = BackgroundRectangle(same_exp, color=BLACK, fill_opacity=1, buff=0.22)
        same_exp_bg.move_to(same_exp.get_center())
        self.play(FadeIn(same_exp_bg, run_time=0.4), Write(same_exp, run_time=1.2))
        self.wait(0.4)

        # Tiny example: 3.5×10⁵ vs 7.2×10⁵ → 7.2×10⁵ wins.
        example = MathTex(
            r"3.5 \times 10^{5} \;\;<\;\; 7.2 \times 10^{5}",
            color=GREEN_OK,
        ).scale(0.9)
        example.next_to(same_exp, DOWN, buff=0.5)
        example_bg = BackgroundRectangle(example, color=BLACK, fill_opacity=1, buff=0.18)
        example_bg.move_to(example.get_center())
        self.play(FadeIn(example_bg, run_time=0.4), Write(example, run_time=1.2))
        self.wait(0.8)

        beat4 = beat_group(same_exp, same_exp_bg, example, example_bg)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"\text{Exponent first, then coefficient}",
            "Bigger exponent wins for positives; tie? Compare the coefficient.",
            final_wait=75.8,
        )
