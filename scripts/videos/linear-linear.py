"""
Manim scene for the lesson `linear-linear`
(topic `l10a-aa-simultaneous-equations`).

Solve the system {y = 2x + 1, y = -x + 4} by substitution. Show the
graph and the intersection point, then reject the mistake of adding
slopes instead of equating right-hand sides.

Target duration: ~71 s (matches the audio narration length).
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


class LinearLinearScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Solving simultaneous linear equations",
            "Two lines, one intersection point",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Plot the two lines and their intersection (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        ax = Axes(
            x_range=[-2, 6, 1],
            y_range=[-1, 3.5, 1],
            x_length=6.4,
            y_length=2.6,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        beat_2 = beat_group(beat_2, ax)

        x_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(i, 0), DOWN, buff=0.15)
            for i in range(-1, 4)
        ])
        y_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(0, i), LEFT, buff=0.15)
            for i in range(-1, 4)
        ])
        zero_origin = MathTex("0", font_size=22).next_to(ax.c2p(0, 0), DL, buff=0.1)
        beat_2 = beat_group(beat_2, x_lbls, y_lbls, zero_origin)

        # y = 2x + 1 and y = -x + 4. Solve: 2x+1 = -x+4 → 3x = 3 → x = 1, y = 3.
        line1 = ax.plot(lambda x: 2 * x + 1, x_range=[-1, 0.2], color=BLUE_TERM, stroke_width=4)
        line2 = ax.plot(lambda x: -x + 4, x_range=[-1.5, 5.5], color=ORANGE_TERM, stroke_width=4)
        beat_2 = beat_group(beat_2, line1, line2)

        self.play(Create(ax), run_time=1.2)
        self.play(
            *[Write(lbl) for lbl in x_lbls],
            *[Write(lbl) for lbl in y_lbls],
            Write(zero_origin),
            run_time=1.4,
        )
        self.play(Create(line1), run_time=1.5)
        self.play(Create(line2), run_time=1.5)

        # Intersection point.
        inter_dot = Dot(ax.c2p(1, 3), color=GREEN_OK, radius=0.1)
        inter_lbl = MathTex(r"(1,\ 3)", color=GREEN_OK).scale(0.95)
        inter_lbl.next_to(inter_dot, UR, buff=0.2)
        inter_lbl_bg = BackgroundRectangle(inter_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        inter_lbl_bg.move_to(inter_lbl.get_center())
        beat_2 = beat_group(beat_2, inter_dot, inter_lbl, inter_lbl_bg)
        self.play(FadeIn(inter_dot, run_time=0.3))
        self.play(FadeIn(inter_lbl_bg, run_time=0.3), FadeIn(inter_lbl, run_time=0.7))
        self.wait(1.5)

        # Equations in the chart.
        eq1 = MathTex(r"y = 2x + 1", color=BLUE_TERM).scale(0.85)
        eq1.next_to(line1, RIGHT, buff=0.2)
        eq1_bg = BackgroundRectangle(eq1, color=BLACK, fill_opacity=0.95, buff=0.1)
        eq1_bg.move_to(eq1.get_center())
        eq2 = MathTex(r"y = -x + 4", color=ORANGE_TERM).scale(0.85)
        eq2.next_to(line2, LEFT, buff=0.2).shift(DOWN * 0.3)
        eq2_bg = BackgroundRectangle(eq2, color=BLACK, fill_opacity=0.95, buff=0.1)
        eq2_bg.move_to(eq2.get_center())
        beat_2 = beat_group(beat_2, eq1, eq1_bg, eq2, eq2_bg)
        self.play(
            FadeIn(eq1_bg, run_time=0.3), FadeIn(eq1, run_time=0.7),
            FadeIn(eq2_bg, run_time=0.3), FadeIn(eq2, run_time=0.7),
        )
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Algebraic solution: equate, solve (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        eq_set = MathTex(
            r"\begin{cases} y = 2x + 1 \\ y = -x + 4 \end{cases}",
            color=BLUE_TERM,
        ).scale(0.9)
        eq_set.move_to(BAND_CHART_CENTER + UP * 1.0)
        eq_set_bg = BackgroundRectangle(eq_set, color=BLACK, fill_opacity=1, buff=0.25)
        eq_set_bg.move_to(eq_set.get_center())
        beat_3 = beat_group(beat_3, eq_set, eq_set_bg)
        self.play(FadeIn(eq_set_bg, run_time=0.4), Write(eq_set, run_time=1.6))
        self.wait(1.0)

        sub_step = MathTex(
            r"2x + 1 = -x + 4 \quad\Rightarrow\quad 3x = 3 \quad\Rightarrow\quad x = 1",
            color=GREEN_OK,
        ).scale(0.95)
        sub_step.next_to(eq_set, DOWN, buff=0.5)
        sub_step_bg = BackgroundRectangle(sub_step, color=BLACK, fill_opacity=1, buff=0.2)
        sub_step_bg.move_to(sub_step.get_center())
        beat_3 = beat_group(beat_3, sub_step, sub_step_bg)
        self.play(FadeIn(sub_step_bg, run_time=0.4), Write(sub_step, run_time=1.8))
        self.wait(1.0)

        # y = 2(1) + 1 = 3.
        y_step = MathTex(
            r"y = 2(1) + 1 = 3",
            color=GREEN_OK,
        ).scale(0.95)
        y_step.next_to(sub_step, DOWN, buff=0.5)
        y_step_bg = BackgroundRectangle(y_step, color=BLACK, fill_opacity=1, buff=0.2)
        y_step_bg.move_to(y_step.get_center())
        beat_3 = beat_group(beat_3, y_step, y_step_bg)
        self.play(FadeIn(y_step_bg, run_time=0.4), Write(y_step, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: adding slopes (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\text{slope: } 2 + (-1) = 1?",
            color=RED_REJECT,
        ).scale(1.0)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.7)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.3),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        expl = Text(
            "Equate the y-expressions, then solve for x.",
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
        # Beat 5 — Final takeaway (~30 s, total ≈ 71 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Substitute or eliminate} \to (x,\ y) = (1,\ 3)",
            "Set the two right-hand sides equal, then solve for x.",
            final_wait=30.0,
        )
