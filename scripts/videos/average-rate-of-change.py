"""
Manim scene for the lesson `average-rate-of-change`
(topic `l10a-am-rates-limiting`).

Average rate of change of f between a and b is (f(b) - f(a)) / (b - a).
Show on a curve, the secant, and reject the mistake of dividing by
f(b) - f(a) (the inverse).

Target duration: ~87 s (matches the audio narration length).
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


class AverageRateOfChangeScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Average rate of change",
            "The slope of the secant between two points",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Show the secant on a parabola (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        ax = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 9, 1],
            x_length=6.4,
            y_length=2.4,
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
            for i in range(1, 9, 2)
        ])
        zero_origin = MathTex("0", font_size=22).next_to(ax.c2p(0, 0), DL, buff=0.1)
        beat_2 = beat_group(beat_2, x_lbls, y_lbls, zero_origin)

        # f(x) = x^2. a = 1, b = 3 → f(a)=1, f(b)=9, slope = 4. Curve
        # plotted only where its y is inside the chart so it never
        # extends past the safe top of the screen.
        curve = ax.plot(
            lambda x: x**2,
            x_range=[0.3, 3.0],
            color=BLUE_TERM,
            stroke_width=4,
        )
        beat_2 = beat_group(beat_2, curve)

        # Points.
        a_pt = ax.c2p(1, 1)
        b_pt = ax.c2p(3, 9)
        a_dot = Dot(a_pt, color=GREEN_OK, radius=0.08)
        b_dot = Dot(b_pt, color=GREEN_OK, radius=0.08)
        a_lbl = MathTex(r"(1,\ 1)", color=GREEN_OK).scale(0.85)
        a_lbl.next_to(a_dot, DR, buff=0.25)
        a_lbl_bg = BackgroundRectangle(a_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        a_lbl_bg.move_to(a_lbl.get_center())
        b_lbl = MathTex(r"(3,\ 9)", color=GREEN_OK).scale(0.85)
        b_lbl.next_to(b_dot, UL, buff=0.25)
        b_lbl_bg = BackgroundRectangle(b_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        b_lbl_bg.move_to(b_lbl.get_center())
        beat_2 = beat_group(beat_2, a_dot, b_dot, a_lbl, a_lbl_bg, b_lbl, b_lbl_bg)

        self.play(Create(ax), run_time=1.2)
        self.play(
            *[Write(lbl) for lbl in x_lbls],
            *[Write(lbl) for lbl in y_lbls],
            Write(zero_origin),
            run_time=1.3,
        )
        self.play(Create(curve), run_time=1.6)
        self.play(FadeIn(a_dot, run_time=0.3), FadeIn(b_dot, run_time=0.3))
        self.play(
            FadeIn(a_lbl_bg, run_time=0.2), FadeIn(a_lbl, run_time=0.5),
            FadeIn(b_lbl_bg, run_time=0.2), FadeIn(b_lbl, run_time=0.5),
        )
        self.wait(1.0)

        # Secant.
        secant = Line(a_pt, b_pt, color=ORANGE_TERM, stroke_width=4)
        beat_2 = beat_group(beat_2, secant)
        self.play(Create(secant), run_time=1.2)
        self.wait(1.0)

        # Slope label.
        slope_lbl = MathTex(r"\text{slope} = \dfrac{9-1}{3-1} = 4", color=ORANGE_TERM).scale(0.95)
        slope_lbl.next_to(secant, DOWN, buff=0.3).shift(LEFT * 0.3)
        slope_lbl_bg = BackgroundRectangle(slope_lbl, color=BLACK, fill_opacity=1, buff=0.2)
        slope_lbl_bg.move_to(slope_lbl.get_center())
        beat_2 = beat_group(beat_2, slope_lbl, slope_lbl_bg)
        self.play(FadeIn(slope_lbl_bg, run_time=0.3), Write(slope_lbl, run_time=1.4))
        self.wait(1.5)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — General formula (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        formula = MathTex(
            r"\text{Av.\ rate} = \dfrac{f(b) - f(a)}{b - a}",
            color=GREEN_OK,
        ).scale(1.1)
        formula.move_to(BAND_CHART_CENTER + UP * 0.7)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.3)
        formula_bg.move_to(formula.get_center())
        beat_3 = beat_group(beat_3, formula, formula_bg)
        self.play(FadeIn(formula_bg, run_time=0.4), Write(formula, run_time=1.8))
        self.wait(1.5)

        # Δ notation.
        delta = MathTex(
            r"= \dfrac{\Delta f}{\Delta x}",
            color=BLUE_TERM,
        ).scale(1.1)
        delta.next_to(formula, DOWN, buff=0.5)
        delta_bg = BackgroundRectangle(delta, color=BLACK, fill_opacity=1, buff=0.25)
        delta_bg.move_to(delta.get_center())
        beat_3 = beat_group(beat_3, delta, delta_bg)
        self.play(FadeIn(delta_bg, run_time=0.4), Write(delta, run_time=1.5))
        self.wait(2.0)

        # The Δx is the horizontal change, Δy is the vertical change.
        interp = Text("change in y, divided by change in x", font_size=22, color=GREEN_OK)
        interp.next_to(delta, DOWN, buff=0.4)
        interp_bg = BackgroundRectangle(interp, color=BLACK, fill_opacity=0.95, buff=0.15)
        interp_bg.move_to(interp.get_center())
        beat_3 = beat_group(beat_3, interp, interp_bg)
        self.play(FadeIn(interp_bg, run_time=0.3), FadeIn(interp, run_time=0.9))
        self.wait(1.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: inverting the fraction (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\text{rate} = \dfrac{b - a}{f(b) - f(a)}?",
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

        expl = Text(
            "Always put the y-change on top, x-change on the bottom.",
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
        # Beat 5 — Final takeaway (~39 s, total ≈ 87 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Average rate of change} = \dfrac{f(b) - f(a)}{b - a} = \dfrac{\Delta y}{\Delta x}",
            "The slope of the secant between two points.",
            final_wait=39.0,
        )
