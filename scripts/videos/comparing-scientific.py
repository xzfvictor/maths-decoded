"""
Manim scene for the lesson `comparing-scientific`
(topic `l9-m-scientific-notation`).

To compare numbers in scientific notation, compare the exponents
first; the larger exponent wins (for positive numbers). When the
exponents match, compare the coefficients.

Target duration: ~71 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ComparingScientificScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Comparing numbers in scientific notation",
            "Compare the exponents first; only then look at the coefficients.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: 4.2×10⁶ vs 8.7×10⁵ (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Two large cards side by side.
        a_card = make_term_card("4.2 \\times 10^{6}", "exponent: 6", BLUE_TERM)
        b_card = make_term_card("8.7 \\times 10^{5}", "exponent: 5", ORANGE_TERM)
        pair = VGroup(a_card, b_card).arrange(RIGHT, buff=0.6)
        pair.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in pair:
            m.set_z_index(2)
        self.play(
            FadeIn(a_card, shift=UP * 0.2, run_time=1.0),
            FadeIn(b_card, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(2.0)

        # Highlight that the exponents decide.
        cmp_exp = MathTex(
            r"6 \;>\; 5 \;\Rightarrow\; 10^{6} \text{ is bigger}",
            color=GREEN_OK,
        ).scale(1.0)
        cmp_exp.next_to(pair, DOWN, buff=0.55)
        cmp_exp_bg = BackgroundRectangle(cmp_exp, color=BLACK, fill_opacity=1, buff=0.22)
        cmp_exp_bg.move_to(cmp_exp.get_center())
        self.play(FadeIn(cmp_exp_bg, run_time=0.4), Write(cmp_exp, run_time=1.6))
        self.wait(2.5)

        # Verdict.
        verdict = Text("So 4.2×10⁶ is larger.", font_size=24, color=GREEN_OK)
        verdict.next_to(cmp_exp, DOWN, buff=0.5)
        verdict_bg = BackgroundRectangle(verdict, color=BLACK, fill_opacity=0.95, buff=0.15)
        verdict_bg.move_to(verdict.get_center())
        self.play(FadeIn(verdict_bg, run_time=0.4), FadeIn(verdict, run_time=1.2))
        self.wait(2.0)
        self.play(
            FadeOut(pair, run_time=0.7),
            FadeOut(cmp_exp, run_time=0.7),
            FadeOut(cmp_exp_bg, run_time=0.7),
            FadeOut(verdict, run_time=0.7),
            FadeOut(verdict_bg, run_time=0.7),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: exponents first (~15 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(
            r"\text{Exponent decides (for positives)}",
            color=BLUE_TERM, scale=1.1,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        sub = Text("Larger exponent → larger value (when the sign is +).",
                   font_size=22, color=BLUE_TERM)
        sub.next_to(general, DOWN, buff=0.5)
        sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.95, buff=0.15)
        sub_bg.move_to(sub.get_center())
        self.play(FadeIn(sub_bg, run_time=0.4), FadeIn(sub, run_time=1.2))
        self.wait(2.5)
        self.play(
            FadeOut(general, run_time=0.7),
            FadeOut(sub, run_time=0.7),
            FadeOut(sub_bg, run_time=0.7),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Same exponent → compare coefficients (~12 s)
        # ──────────────────────────────────────────────────────────────────
        same_exp = make_equation_card(
            r"\text{Exponents equal? Compare the coefficients.}",
            color=ORANGE_TERM, scale=0.95,
        )
        same_exp.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in same_exp:
            m.set_z_index(2)
        self.play(FadeIn(same_exp, shift=UP * 0.2, run_time=1.4))
        self.wait(1.2)

        # Tiny example: 3.5×10⁵ vs 7.2×10⁵ → 7.2×10⁵ wins.
        example = MathTex(
            r"3.5 \times 10^{5} \;\;<\;\; 7.2 \times 10^{5}",
            color=GREEN_OK,
        ).scale(0.95)
        example.next_to(same_exp, DOWN, buff=0.55)
        example_bg = BackgroundRectangle(example, color=BLACK, fill_opacity=1, buff=0.22)
        example_bg.move_to(example.get_center())
        self.play(FadeIn(example_bg, run_time=0.4), Write(example, run_time=1.4))
        self.wait(2.0)
        self.play(
            FadeOut(same_exp, run_time=0.7),
            FadeOut(example, run_time=0.7),
            FadeOut(example_bg, run_time=0.7),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~17 s, total ≈ 71 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Exponent first, then coefficient}",
            "Bigger exponent wins for positive numbers; tie? Compare a.",
            final_wait=17.0,
        )
