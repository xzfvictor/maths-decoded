"""
Manim scene for the lesson `sketching-lines`
(topic `l9-a-linear-graphs-equations`).

Sketching a linear graph: slope-intercept form y = mx + c, table of
values, plot the points, draw the line.

Target duration: ~29 s (target scene length per spec).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SketchingLinesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Sketching linear graphs",
            "Two points are enough to draw a line",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Slope-intercept form y = mx + c (~3 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Slope-intercept form:", font_size=22, color=WHITE)
        head.move_to(BAND_CHART_CENTER + UP * 1.3)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        eq = make_equation_card(
            r"y \;=\; m\,x + c",
            color=ORANGE_TERM, scale=1.2,
        )
        eq.move_to(BAND_CHART_CENTER + UP * 0.0)

        self.play(
            FadeIn(head_bg, run_time=0.3),
            FadeIn(head, run_time=0.6),
            FadeIn(eq, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(1.5)

        beat1 = VGroup(head, head_bg, eq)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Mini table of values: y = 2x - 1 (~3 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("e.g.  y = 2x - 1:", font_size=22, color=WHITE)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        rows = VGroup(
            MathTex(r"x = 0, \; y = -1", color=BLUE_TERM).scale(0.95),
            MathTex(r"x = 1, \; y = 1",  color=BLUE_TERM).scale(0.95),
            MathTex(r"x = 2, \; y = 3",  color=BLUE_TERM).scale(0.95),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        rows.move_to(BAND_CHART_CENTER + UP * 0.0)
        rows_bg = BackgroundRectangle(rows, color=BLACK, fill_opacity=0.95, buff=0.25)
        rows_bg.move_to(rows.get_center())

        self.play(
            FadeIn(head2_bg, run_time=0.3),
            FadeIn(head2, run_time=0.6),
            FadeIn(rows_bg, run_time=0.4),
            FadeIn(rows, run_time=1.0),
        )
        self.wait(1.5)

        beat2 = VGroup(head2, head2_bg, rows, rows_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Plot two points and connect them with a line (~3 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Plot the points and connect:",
                     font_size=22, color=WHITE)
        head3.move_to(BAND_CHART_CENTER + UP * 1.3)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())

        # Small coordinate plane on the chart band.
        plane_center = BAND_CHART_CENTER + DOWN * 0.1
        x_axis = NumberLine(
            x_range=[-1, 3, 1],
            length=4.0,
            color=WHITE,
            stroke_width=2,
            include_tip=False,
        )
        x_axis.move_to(plane_center + DOWN * 0.9)
        y_axis = NumberLine(
            x_range=[-2, 4, 1],
            length=2.6,
            color=WHITE,
            stroke_width=2,
            include_tip=False,
            rotation=90 * DEGREES,
        )
        y_axis.move_to(plane_center + LEFT * 2.0)

        # Two plot points: (0, -1) and (2, 3).
        sx0 = x_axis.number_to_point(0)[0]; sy0 = y_axis.number_to_point(-1)[1]
        sx1 = x_axis.number_to_point(2)[0]; sy1 = y_axis.number_to_point(3)[1]
        p0 = Dot(point=np.array([sx0, sy0, 0.0]), color=ORANGE_TERM, radius=0.08)
        p1 = Dot(point=np.array([sx1, sy1, 0.0]), color=ORANGE_TERM, radius=0.08)

        # Line extended slightly past the two points.
        ext_left = sx0 - 0.4
        ext_right = sx1 + 0.4
        slope_sy = (sy1 - sy0) / (sx1 - sx0)
        y_left = sy0 + slope_sy * (ext_left - sx0)
        y_right = sy0 + slope_sy * (ext_right - sx0)
        line = Line(
            start=np.array([ext_left, y_left, 0.0]),
            end=np.array([ext_right, y_right, 0.0]),
            color=GREEN_OK,
            stroke_width=4,
        )

        # Point labels.
        lbl0 = MathTex(r"(0,\,-1)", color=ORANGE_TERM).scale(0.7).next_to(p0, DL, buff=0.15)
        lbl1 = MathTex(r"(2,\;3)", color=ORANGE_TERM).scale(0.7).next_to(p1, UR, buff=0.15)

        self.play(
            FadeIn(head3_bg, run_time=0.3),
            FadeIn(head3, run_time=0.6),
            Create(x_axis, run_time=0.8),
            Create(y_axis, run_time=0.8),
            run_time=1.0,
        )
        self.play(
            FadeIn(p0, scale=0.5, run_time=0.4),
            FadeIn(p1, scale=0.5, run_time=0.4),
        )
        self.play(
            FadeIn(lbl0, run_time=0.4),
            FadeIn(lbl1, run_time=0.4),
        )
        self.play(Create(line, run_time=1.4))
        self.wait(1.0)

        beat3 = VGroup(
            head3, head3_bg, x_axis, y_axis, p0, p1, lbl0, lbl1, line,
        )
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait = 20 s, total ≈ 29 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y \;=\; m\,x + c",
            "m is the gradient, c is the y-intercept — two points sketch the line.",
            final_wait=20.0,
        )
