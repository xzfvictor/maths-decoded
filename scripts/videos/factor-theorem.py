"""
Manim scene for the lesson `factor-theorem`
(topic `l10a-aa-polynomials`).

P(a) = 0 iff (x - a) is a factor of P(x). Show that P(2) = 0 implies
(x - 2) divides P(x), and reject the reverse mistake of assuming any
factor gives a zero automatically without substitution.

Target duration: ~95 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *
import numpy as np


class FactorTheoremScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "The factor theorem",
            "P(a) = 0  ⇔  (x - a) is a factor of P(x)",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example P(x) = x^3 - 6x^2 + 11x - 6, P(2) = 0 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        P_eq = MathTex(r"P(x) = x^{3} - 6x^{2} + 11x - 6", color=BLUE_TERM).scale(1.0)
        P_eq.move_to(BAND_CHART_CENTER + UP * 0.8)
        P_eq_bg = BackgroundRectangle(P_eq, color=BLACK, fill_opacity=1, buff=0.2)
        P_eq_bg.move_to(P_eq.get_center())
        beat_2 = beat_group(beat_2, P_eq, P_eq_bg)

        self.play(FadeIn(P_eq_bg, run_time=0.4), Write(P_eq, run_time=1.6))
        self.wait(1.5)

        # Substitute x = 2.
        sub_step = MathTex(r"P(2) = 8 - 24 + 22 - 6 = 0", color=GREEN_OK).scale(1.0)
        sub_step.next_to(P_eq, DOWN, buff=0.5)
        sub_step_bg = BackgroundRectangle(sub_step, color=BLACK, fill_opacity=1, buff=0.2)
        sub_step_bg.move_to(sub_step.get_center())
        beat_2 = beat_group(beat_2, sub_step, sub_step_bg)
        self.play(FadeIn(sub_step_bg, run_time=0.4), Write(sub_step, run_time=1.6))
        self.wait(1.5)

        # Argue that (x - 2) must be a factor.
        arith = Text(
            "0 remainder  →  (x − 2) is a factor",
            font_size=24,
            color=GREEN_OK,
        ).next_to(sub_step, DOWN, buff=0.5)
        arith_bg = BackgroundRectangle(arith, color=BLACK, fill_opacity=0.95, buff=0.15)
        arith_bg.move_to(arith.get_center())
        beat_2 = beat_group(beat_2, arith, arith_bg)
        self.play(FadeIn(arith_bg, run_time=0.4), FadeIn(arith, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Factor out (x - 2) and verify (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        factor_eq = MathTex(
            r"P(x) = (x - 2)(x^{2} - 4x + 3)",
            color=BLUE_TERM,
        ).scale(1.0)
        factor_eq.move_to(BAND_CHART_CENTER + UP * 0.7)
        factor_eq_bg = BackgroundRectangle(factor_eq, color=BLACK, fill_opacity=1, buff=0.2)
        factor_eq_bg.move_to(factor_eq.get_center())
        beat_3 = beat_group(beat_3, factor_eq, factor_eq_bg)
        self.play(FadeIn(factor_eq_bg, run_time=0.4), Write(factor_eq, run_time=1.8))
        self.wait(1.5)

        # Further factor the quadratic.
        full = MathTex(
            r"= (x - 2)(x - 1)(x - 3)",
            color=GREEN_OK,
        ).scale(1.1)
        full.next_to(factor_eq, DOWN, buff=0.5)
        full_bg = BackgroundRectangle(full, color=BLACK, fill_opacity=1, buff=0.2)
        full_bg.move_to(full.get_center())
        beat_3 = beat_group(beat_3, full, full_bg)
        self.play(FadeIn(full_bg, run_time=0.4), Write(full, run_time=1.6))
        self.wait(1.5)

        # Roots list.
        roots = MathTex(
            r"\text{roots: } x = 1,\ 2,\ 3",
            color=GREEN_OK,
        ).scale(1.0)
        roots.next_to(full, DOWN, buff=0.5)
        roots_bg = BackgroundRectangle(roots, color=BLACK, fill_opacity=0.95, buff=0.18)
        roots_bg.move_to(roots.get_center())
        beat_3 = beat_group(beat_3, roots, roots_bg)
        self.play(FadeIn(roots_bg, run_time=0.4), FadeIn(roots, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reverse: if (x - a) is a factor, then P(a) = 0 (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        reverse = MathTex(
            r"(x - 2) \text{ is a factor } \Rightarrow P(2) = 0",
            color=BLUE_TERM,
        ).scale(1.0)
        reverse.move_to(BAND_CHART_CENTER + UP * 0.7)
        reverse_bg = BackgroundRectangle(reverse, color=BLACK, fill_opacity=1, buff=0.2)
        reverse_bg.move_to(reverse.get_center())
        beat_4 = beat_group(beat_4, reverse, reverse_bg)
        self.play(FadeIn(reverse_bg, run_time=0.4), Write(reverse, run_time=1.6))
        self.wait(1.5)

        expl = Text(
            "Set x = 2: every term in (x − 2) vanishes, so P(2) = 0.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(reverse, DOWN, buff=0.5)
        expl_bg = BackgroundRectangle(expl, color=BLACK, fill_opacity=0.95, buff=0.18)
        expl_bg.move_to(expl.get_center())
        beat_4 = beat_group(beat_4, expl, expl_bg)
        self.play(FadeIn(expl_bg, run_time=0.4), FadeIn(expl, run_time=1.2))
        self.wait(2.0)

        # Reject the "always" mistake.
        wrong = MathTex(
            r"(x - 2)\ \text{factor? skip checking?}",
            color=RED_REJECT,
        ).scale(0.95)
        wrong.next_to(expl, DOWN, buff=0.5)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.2)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.3),
            Write(wrong, run_time=1.2),
            Create(cross, run_time=0.7),
        )
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~43 s, total ≈ 95 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Factor theorem:}\quad P(a) = 0 \iff (x - a)\ \text{divides}\ P(x)",
            "Both directions hold — but always substitute to verify.",
            final_wait=43.0,
        )
