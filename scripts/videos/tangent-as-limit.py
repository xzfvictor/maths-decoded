"""
Manim scene for the lesson `tangent-as-limit`
(topic `l10a-am-rates-limiting`).

The tangent slope at x = a is the limit of the average rate of change
as the second point approaches a. Show three secants and the limiting
tangent line. Reject "tangent touches at one point" without gradient.

Target duration: ~94 s (matches the audio narration length).
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


class TangentAsLimitScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Tangent as a limiting secant",
            "As the second point → the first, the secant becomes the tangent",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — A parabola with one point and three secants (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        ax = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 10, 1],
            x_length=6.4,
            y_length=3.0,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.1)
        beat_2 = beat_group(beat_2, ax)

        x_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(i, 0), DOWN, buff=0.15)
            for i in range(5)
        ])
        y_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(0, i), LEFT, buff=0.15)
            for i in range(1, 5)
        ])
        zero_origin = MathTex("0", font_size=22).next_to(ax.c2p(0, 0), DL, buff=0.1)
        beat_2 = beat_group(beat_2, x_lbls, y_lbls, zero_origin)

        curve = ax.plot(lambda x: x**2, x_range=[-0.7, 4.6], color=BLUE_TERM, stroke_width=4)
        beat_2 = beat_group(beat_2, curve)

        # Point P at x = 2, f(2) = 4.
        p = ax.c2p(2, 4)
        p_dot = Dot(p, color=GREEN_OK, radius=0.09)
        p_lbl = MathTex("P", color=GREEN_OK).scale(0.95)
        p_lbl.next_to(p_dot, UL, buff=0.2)
        p_lbl_bg = BackgroundRectangle(p_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        p_lbl_bg.move_to(p_lbl.get_center())
        beat_2 = beat_group(beat_2, p_dot, p_lbl, p_lbl_bg)

        self.play(Create(ax), run_time=1.2)
        self.play(
            *[Write(lbl) for lbl in x_lbls],
            *[Write(lbl) for lbl in y_lbls],
            Write(zero_origin),
            run_time=1.3,
        )
        self.play(Create(curve), run_time=1.5)
        self.play(FadeIn(p_dot, run_time=0.3))
        self.play(FadeIn(p_lbl_bg, run_time=0.2), FadeIn(p_lbl, run_time=0.5))
        self.wait(0.8)

        # Three secants: Q at x = 3, 2.5, 2.1.
        secant_data = [
            (3.0, ORANGE_TERM),
            (2.5, TEAL_TERM),
            (2.1, "#c81e7a"),
        ]
        secant_lines = []
        for xq, col in secant_data:
            q = ax.c2p(xq, xq**2)
            line = Line(p, q, color=col, stroke_width=3)
            q_dot = Dot(q, color=col, radius=0.07)
            secant_lines.append((line, q_dot))

        for line, q_dot in secant_lines:
            beat_2 = beat_group(beat_2, line, q_dot)
            self.play(Create(line, run_time=0.8), FadeIn(q_dot, run_time=0.3))
            self.wait(0.6)

        self.wait(1.5)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The limiting tangent line at x = 2, slope = 4 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        ax2 = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 10, 1],
            x_length=6.4,
            y_length=3.0,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.1)
        beat_3 = beat_group(beat_3, ax2)
        x_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(i, 0), DOWN, buff=0.15)
            for i in range(5)
        ])
        y_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(0, i), LEFT, buff=0.15)
            for i in range(1, 5)
        ])
        zero2 = MathTex("0", font_size=22).next_to(ax2.c2p(0, 0), DL, buff=0.1)
        beat_3 = beat_group(beat_3, x_lbls2, y_lbls2, zero2)
        curve2 = ax2.plot(lambda x: x**2, x_range=[-0.7, 4.6], color=BLUE_TERM, stroke_width=4)
        beat_3 = beat_group(beat_3, curve2)
        p2 = ax2.c2p(2, 4)
        p_dot2 = Dot(p2, color=GREEN_OK, radius=0.09)
        beat_3 = beat_group(beat_3, p_dot2)

        self.play(Create(ax2), run_time=0.8)
        self.play(
            *[Write(lbl) for lbl in x_lbls2],
            *[Write(lbl) for lbl in y_lbls2],
            Write(zero2),
            Create(curve2),
            FadeIn(p_dot2),
            run_time=1.8,
        )

        # Tangent: slope 4 at x = 2: y = 4 + 4(x - 2) = 4x - 4. At x = 0, y = -4. At x = 3, y = 8.
        # Use x_range that stays on the chart: y = 4x - 4. At x = 1, y = 0. At x = 4, y = 12 (too high).
        # Restrict x in [0.4, 3.5] so y in [-2.4, 10] which exceeds y_max 5. Use [0.6, 2.25] so y in [-1.6, 5].
        tan = ax2.plot(lambda x: 4 * x - 4, x_range=[0.7, 2.25], color=ORANGE_TERM, stroke_width=4)
        beat_3 = beat_group(beat_3, tan)
        self.play(Create(tan), run_time=1.4)
        self.wait(1.0)

        # Tangent label.
        tan_lbl = MathTex(r"\text{tangent, slope } 4", color=ORANGE_TERM).scale(0.9)
        tan_lbl.next_to(tan, UP, buff=0.3).shift(RIGHT * 0.4)
        tan_lbl_bg = BackgroundRectangle(tan_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        tan_lbl_bg.move_to(tan_lbl.get_center())
        beat_3 = beat_group(beat_3, tan_lbl, tan_lbl_bg)
        self.play(FadeIn(tan_lbl_bg, run_time=0.3), FadeIn(tan_lbl, run_time=0.8))
        self.wait(1.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: "tangent = line that touches the curve" (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\text{any line that just touches?}",
            color=RED_REJECT,
        ).scale(1.0)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.4),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        right = Text(
            "Tangent has the same slope as the curve at that point — gradient matters.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=0.95, buff=0.18)
        right_bg.move_to(right.get_center())
        beat_4 = beat_group(beat_4, right, right_bg)
        self.play(FadeIn(right_bg, run_time=0.3), FadeIn(right, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~42 s, total ≈ 94 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Tangent slope at } a = \lim_{b \to a} \dfrac{f(b) - f(a)}{b - a}",
            "Tangent = secant in the limit.",
            final_wait=42.0,
        )
