"""
Manim scene for the lesson `remainder-theorem`
(topic `l10a-aa-polynomials`).

When P(x) is divided by (x - a), the remainder is P(a). The animation
shows a worked example, then rejects the common mistake of returning
the divisor's sign instead of the polynomial's value.

Target duration: ~93 s (matches the audio narration length).
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


class RemainderTheoremScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "The remainder theorem",
            "Dividing P(x) by (x - a) leaves remainder P(a)",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Worked example: P(x) = 2x^3 - 5x + 3, divide by (x - 1) (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        P_eq = MathTex(
            r"P(x) = 2x^{3} - 5x + 3",
            color=BLUE_TERM,
        ).scale(1.0)
        P_eq.move_to(BAND_CHART_CENTER + UP * 0.8)
        P_eq_bg = BackgroundRectangle(P_eq, color=BLACK, fill_opacity=1, buff=0.2)
        P_eq_bg.move_to(P_eq.get_center())
        beat_2 = beat_group(beat_2, P_eq, P_eq_bg)
        self.play(FadeIn(P_eq_bg, run_time=0.4), Write(P_eq, run_time=1.4))
        self.wait(1.0)

        div_eq = MathTex(
            r"\text{divide by } (x - 1) \quad\Rightarrow\quad a = 1",
            color=ORANGE_TERM,
        ).scale(1.0)
        div_eq.next_to(P_eq, DOWN, buff=0.5)
        div_eq_bg = BackgroundRectangle(div_eq, color=BLACK, fill_opacity=1, buff=0.2)
        div_eq_bg.move_to(div_eq.get_center())
        beat_2 = beat_group(beat_2, div_eq, div_eq_bg)
        self.play(FadeIn(div_eq_bg, run_time=0.4), Write(div_eq, run_time=1.4))
        self.wait(1.0)

        # Substitute x = 1.
        sub = MathTex(
            r"P(1) = 2(1) - 5(1) + 3 = 0",
            color=GREEN_OK,
        ).scale(1.0)
        sub.next_to(div_eq, DOWN, buff=0.5)
        sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=1, buff=0.2)
        sub_bg.move_to(sub.get_center())
        beat_2 = beat_group(beat_2, sub, sub_bg)
        self.play(FadeIn(sub_bg, run_time=0.4), Write(sub, run_time=1.4))
        self.wait(1.5)

        # Conclude.
        result = MathTex(
            r"\text{remainder} = P(1) = 0",
            color=GREEN_OK,
        ).scale(1.0)
        result.next_to(sub, DOWN, buff=0.5)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=1, buff=0.2)
        result_bg.move_to(result.get_center())
        beat_2 = beat_group(beat_2, result, result_bg)
        self.play(FadeIn(result_bg, run_time=0.4), Write(result, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — A second example, non-zero remainder (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        # Same P(x), but divide by (x - 2).
        div2 = MathTex(
            r"\text{divide by } (x - 2) \quad\Rightarrow\quad a = 2",
            color=ORANGE_TERM,
        ).scale(1.0)
        div2.move_to(BAND_CHART_CENTER + UP * 0.8)
        div2_bg = BackgroundRectangle(div2, color=BLACK, fill_opacity=1, buff=0.2)
        div2_bg.move_to(div2.get_center())
        beat_3 = beat_group(beat_3, div2, div2_bg)
        self.play(FadeIn(div2_bg, run_time=0.4), Write(div2, run_time=1.4))
        self.wait(1.0)

        sub2 = MathTex(
            r"P(2) = 2(8) - 5(2) + 3 = 16 - 10 + 3 = 9",
            color=GREEN_OK,
        ).scale(1.0)
        sub2.next_to(div2, DOWN, buff=0.5)
        sub2_bg = BackgroundRectangle(sub2, color=BLACK, fill_opacity=1, buff=0.2)
        sub2_bg.move_to(sub2.get_center())
        beat_3 = beat_group(beat_3, sub2, sub2_bg)
        self.play(FadeIn(sub2_bg, run_time=0.4), Write(sub2, run_time=1.6))
        self.wait(1.5)

        result2 = MathTex(
            r"\text{remainder} = P(2) = 9",
            color=GREEN_OK,
        ).scale(1.0)
        result2.next_to(sub2, DOWN, buff=0.5)
        result2_bg = BackgroundRectangle(result2, color=BLACK, fill_opacity=1, buff=0.2)
        result2_bg.move_to(result2.get_center())
        beat_3 = beat_group(beat_3, result2, result2_bg)
        self.play(FadeIn(result2_bg, run_time=0.4), Write(result2, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: remainder ≠ divisor sign (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\text{remainder} = 1 \text{ (the divisor's sign)?}",
            color=RED_REJECT,
        ).scale(1.0)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.7)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.4),
            Create(cross, run_time=0.7),
        )
        self.wait(1.5)

        expl = Text(
            "Substitute x = a into P(x), not into the divisor.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        expl_bg = BackgroundRectangle(expl, color=BLACK, fill_opacity=0.95, buff=0.18)
        expl_bg.move_to(expl.get_center())
        beat_4 = beat_group(beat_4, expl, expl_bg)
        self.play(FadeIn(expl_bg, run_time=0.3), FadeIn(expl, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~42 s, total ≈ 93 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Remainder theorem:}\quad P(x) \div (x - a)\ \text{leaves remainder}\ P(a)",
            "Always substitute into the polynomial, not the divisor.",
            final_wait=42.0,
        )
