"""
Manim scene for the lesson `sketching-process`
(topic `l10a-aa-polynomial-features`).

Step-by-step process for sketching a polynomial: roots → y-intercept →
turning points → join with a smooth curve. Reject "connect-the-dots"
with straight lines.

Target duration: ~70 s (matches the audio narration length).
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


class SketchingProcessScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Sketching a polynomial step by step",
            "Roots → y-intercept → turning points → smooth curve",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Set up axes + place roots on x-axis (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        ax = Axes(
            x_range=[-2.5, 3.5, 1],
            y_range=[-3, 1.4, 1],
            x_length=6.0,
            y_length=2.4,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        beat_2 = beat_group(beat_2, ax)

        x_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(i, 0), DOWN, buff=0.15)
            for i in [-2, -1, 1, 2, 3]
        ])
        y_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(0, i), LEFT, buff=0.15)
            for i in [-2, 2]
        ])
        zero_origin = MathTex("0", font_size=22).next_to(ax.c2p(0, 0), DL, buff=0.1)
        beat_2 = beat_group(beat_2, x_lbls, y_lbls, zero_origin)

        self.play(Create(ax), run_time=1.4)
        self.play(
            *[Write(lbl) for lbl in x_lbls],
            *[Write(lbl) for lbl in y_lbls],
            Write(zero_origin),
            run_time=1.4,
        )

        # Step 1: place roots on x-axis.
        step1 = Text("Step 1: plot the roots", font_size=22, color=BLUE_TERM)
        step1.move_to(BAND_CHART_CENTER + UP * 1.3)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=0.95, buff=0.12)
        step1_bg.move_to(step1.get_center())
        beat_2 = beat_group(beat_2, step1, step1_bg)
        self.play(FadeIn(step1_bg, run_time=0.3), FadeIn(step1, run_time=0.8))

        # Two simple roots.
        root1 = Dot(ax.c2p(-1, 0), color=GREEN_OK, radius=0.08)
        root2 = Dot(ax.c2p(2, 0), color=GREEN_OK, radius=0.08)
        r1_lbl = MathTex(r"x = -1", color=GREEN_OK).scale(0.85)
        r1_lbl.next_to(root1, DOWN, buff=0.2)
        r1_lbl_bg = BackgroundRectangle(r1_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        r1_lbl_bg.move_to(r1_lbl.get_center())
        r2_lbl = MathTex(r"x = 2", color=GREEN_OK).scale(0.85)
        r2_lbl.next_to(root2, DOWN, buff=0.2)
        r2_lbl_bg = BackgroundRectangle(r2_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        r2_lbl_bg.move_to(r2_lbl.get_center())
        beat_2 = beat_group(beat_2, root1, root2, r1_lbl, r1_lbl_bg, r2_lbl, r2_lbl_bg)
        self.play(
            FadeIn(root1, run_time=0.3),
            FadeIn(root2, run_time=0.3),
        )
        self.play(
            FadeIn(r1_lbl_bg, run_time=0.2), FadeIn(r1_lbl, run_time=0.5),
            FadeIn(r2_lbl_bg, run_time=0.2), FadeIn(r2_lbl, run_time=0.5),
        )
        self.wait(1.5)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — y-intercept + turning point (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        ax2 = Axes(
            x_range=[-2.5, 3.5, 1],
            y_range=[-3, 1.4, 1],
            x_length=6.0,
            y_length=2.4,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        beat_3 = beat_group(beat_3, ax2)
        x_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(i, 0), DOWN, buff=0.15)
            for i in [-2, -1, 1, 2, 3]
        ])
        y_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(0, i), LEFT, buff=0.15)
            for i in [-2, 2]
        ])
        zero2 = MathTex("0", font_size=22).next_to(ax2.c2p(0, 0), DL, buff=0.1)
        beat_3 = beat_group(beat_3, x_lbls2, y_lbls2, zero2)
        r1 = Dot(ax2.c2p(-1, 0), color=GREEN_OK, radius=0.08)
        r2 = Dot(ax2.c2p(2, 0), color=GREEN_OK, radius=0.08)
        beat_3 = beat_group(beat_3, r1, r2)

        self.play(Create(ax2), run_time=1.0)
        self.play(
            *[Write(lbl) for lbl in x_lbls2],
            *[Write(lbl) for lbl in y_lbls2],
            Write(zero2),
            run_time=1.0,
        )
        self.play(FadeIn(r1, run_time=0.2), FadeIn(r2, run_time=0.2))

        step2 = Text("Step 2: y-intercept & turning point", font_size=22, color=ORANGE_TERM)
        step2.move_to(BAND_CHART_CENTER + UP * 1.3)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=0.95, buff=0.12)
        step2_bg.move_to(step2.get_center())
        beat_3 = beat_group(beat_3, step2, step2_bg)
        self.play(FadeIn(step2_bg, run_time=0.3), FadeIn(step2, run_time=0.8))

        # y-intercept at (0, -2). y = (x+1)(x-2) * 1 gives y(0) = -2.
        yint = Dot(ax2.c2p(0, -2), color=ORANGE_TERM, radius=0.08)
        yint_lbl = MathTex(r"(0,-2)", color=ORANGE_TERM).scale(0.8)
        yint_lbl.next_to(yint, LEFT, buff=0.2)
        yint_lbl_bg = BackgroundRectangle(yint_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        yint_lbl_bg.move_to(yint_lbl.get_center())
        # Turning point at x = 0.5, y = -2.25.
        tp = Dot(ax2.c2p(0.5, -2.25), color=ORANGE_TERM, radius=0.08)
        tp_lbl = MathTex(r"\text{min}", color=ORANGE_TERM).scale(0.8)
        tp_lbl.next_to(tp, DR, buff=0.2)
        tp_lbl_bg = BackgroundRectangle(tp_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        tp_lbl_bg.move_to(tp_lbl.get_center())
        beat_3 = beat_group(beat_3, yint, yint_lbl, yint_lbl_bg, tp, tp_lbl, tp_lbl_bg)

        self.play(FadeIn(yint, run_time=0.2))
        self.play(FadeIn(yint_lbl_bg, run_time=0.2), FadeIn(yint_lbl, run_time=0.5))
        self.wait(0.5)
        self.play(FadeIn(tp, run_time=0.2))
        self.play(FadeIn(tp_lbl_bg, run_time=0.2), FadeIn(tp_lbl, run_time=0.5))
        self.wait(1.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Sketch the smooth curve, reject straight lines (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        ax3 = Axes(
            x_range=[-2.5, 3.5, 1],
            y_range=[-3, 1.4, 1],
            x_length=6.0,
            y_length=2.4,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        beat_4 = beat_group(beat_4, ax3)
        x_lbls3 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax3.c2p(i, 0), DOWN, buff=0.15)
            for i in [-2, -1, 1, 2, 3]
        ])
        y_lbls3 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax3.c2p(0, i), LEFT, buff=0.15)
            for i in [-2, 2]
        ])
        zero3 = MathTex("0", font_size=22).next_to(ax3.c2p(0, 0), DL, buff=0.1)
        beat_4 = beat_group(beat_4, x_lbls3, y_lbls3, zero3)
        r1d = Dot(ax3.c2p(-1, 0), color=GREEN_OK, radius=0.08)
        r2d = Dot(ax3.c2p(2, 0), color=GREEN_OK, radius=0.08)
        beat_4 = beat_group(beat_4, r1d, r2d)

        self.play(Create(ax3), run_time=0.8)
        self.play(
            *[Write(lbl) for lbl in x_lbls3],
            *[Write(lbl) for lbl in y_lbls3],
            Write(zero3),
            FadeIn(r1d, run_time=0.2),
            FadeIn(r2d, run_time=0.2),
            run_time=1.0,
        )

        # Sketch the smooth quadratic y = x^2 - x - 2, scaled so the
        # curve sits inside y ∈ [-1.4, 1.4] on screen.
        curve = ax3.plot(
            lambda x: 0.4 * (x**2 - x - 2),
            x_range=[-1.45, 2.7],
            color=BLUE_TERM,
            stroke_width=4,
        )
        beat_4 = beat_group(beat_4, curve)
        self.play(Create(curve), run_time=2.0)

        # Reject: straight lines connecting dots.
        wrong = MathTex(r"\text{connect with straight lines?}", color=RED_REJECT).scale(0.95)
        wrong.next_to(ax3, DOWN, buff=0.4)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.18)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.3),
            Write(wrong, run_time=1.0),
            Create(cross, run_time=0.7),
        )

        # Right way.
        right = Text("Use a smooth curve through the points.", font_size=22, color=GREEN_OK)
        right.next_to(wrong, DOWN, buff=0.4)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=0.95, buff=0.15)
        right_bg.move_to(right.get_center())
        beat_4 = beat_group(beat_4, right, right_bg)
        self.play(FadeIn(right_bg, run_time=0.3), FadeIn(right, run_time=0.8))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~30 s, total ≈ 70 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Roots} \to \text{y-intercept} \to \text{turning points} \to \text{smooth curve}",
            "Sketch carefully — no straight lines between features.",
            final_wait=30.0,
        )
