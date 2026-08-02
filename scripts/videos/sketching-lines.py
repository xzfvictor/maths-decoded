"""
Manim scene for the lesson `sketching-lines`
(topic `l9-a-linear-graphs-equations`).

Sketching a linear graph: build a table of values for y = 2x - 1, plot
the points on a small Cartesian plane, and connect them with a line.
The whole workflow of "make a table, plot the points, draw the line".

Target duration: ~88 s (matches the audio narration length of 88.42 s).
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
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Sketching linear graphs",
            "Make a table, plot the points, draw the line",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Show the equation y = 2x - 1 (~7 s)
        # ──────────────────────────────────────────────────────────────────
        eq = make_equation_card(r"y = 2x - 1", color=ORANGE_TERM, scale=1.05)
        eq.move_to(BAND_CHART_CENTER + UP * 1.6)
        self.play(FadeIn(eq, run_time=1.2))
        self.wait(2.5)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Build a table of values (~16 s)
        # ──────────────────────────────────────────────────────────────────
        rows = [
            ("x", "y", WHITE),
            ("0", "-1", BLUE_TERM),
            ("1", "1", BLUE_TERM),
            ("2", "3", BLUE_TERM),
            ("3", "5", BLUE_TERM),
        ]

        table_cells = VGroup()
        for i, (x_val, y_val, color) in enumerate(rows):
            x_txt = MathTex(x_val, color=color).scale(0.85)
            y_txt = MathTex(y_val, color=color).scale(0.85)
            row = VGroup(x_txt, y_txt).arrange(RIGHT, buff=0.7)
            table_cells.add(row)
        table_cells.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        table_cells.move_to(LEFT * 4.2 + UP * 0.7)

        x_header = Text("x", font_size=22, color=WHITE)
        y_header = Text("y", font_size=22, color=WHITE)
        x_header.next_to(table_cells[0], UP, buff=0.05).align_to(table_cells[0][0], LEFT)
        y_header.next_to(x_header, RIGHT, buff=0.7)
        headers = VGroup(x_header, y_header)

        table_bg = BackgroundRectangle(
            VGroup(headers, table_cells),
            color=BLACK, fill_opacity=0.95, buff=0.25,
        )
        table_bg.move_to(VGroup(headers, table_cells).get_center())
        table_bg.set_z_index(1)

        self.play(FadeIn(table_bg, run_time=0.6))
        self.play(FadeIn(headers, shift=DOWN * 0.2, run_time=0.8))
        for row in table_cells:
            self.play(FadeIn(row, shift=RIGHT * 0.2, run_time=0.45))
            self.wait(0.4)
        self.wait(2.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Build axes and plot the 4 points (~16 s)
        # ──────────────────────────────────────────────────────────────────
        plane_center = RIGHT * 1.6 + UP * 0.0
        plane_half = 1.7

        x_axis = NumberLine(
            x_range=[-2.5, 3.5, 1],
            length=5.0,
            color=WHITE,
            stroke_width=3,
            include_tip=False,
        )
        x_axis.move_to(plane_center + DOWN * 1.4)
        x_axis.set_z_index(2)

        y_axis = NumberLine(
            x_range=[-2.5, 3.5, 1],
            length=5.0,
            color=WHITE,
            stroke_width=3,
            include_tip=False,
            rotation=90 * DEGREES,
        )
        y_axis.move_to(plane_center + LEFT * 2.5)
        y_axis.set_z_index(2)

        x_labels = VGroup()
        for xv in [-2, -1, 1, 2, 3]:
            lbl = MathTex(str(xv), font_size=20, color=WHITE).next_to(
                x_axis.number_to_point(xv), DOWN, buff=0.15,
            )
            x_labels.add(lbl)

        y_labels = VGroup()
        for yv in [-1, 1, 2, 3, 5]:
            lbl = MathTex(str(yv), font_size=20, color=WHITE).next_to(
                y_axis.number_to_point(yv), LEFT, buff=0.15,
            )
            y_labels.add(lbl)

        origin_lbl = MathTex("0", font_size=20, color=WHITE).next_to(
            x_axis.number_to_point(0), DOWN, buff=0.15,
        ).shift(LEFT * 0.25)

        x_axis_label = MathTex("x", font_size=26, color=WHITE).next_to(
            x_axis, RIGHT, buff=0.15,
        )
        y_axis_label = MathTex("y", font_size=26, color=WHITE).next_to(
            y_axis, UP, buff=0.1,
        )

        self.play(Create(x_axis, run_time=1.2), Create(y_axis, run_time=1.2))
        self.play(
            FadeIn(x_labels, run_time=0.7),
            FadeIn(y_labels, run_time=0.7),
            FadeIn(origin_lbl, run_time=0.5),
        )
        self.wait(1.0)

        # Plot the 4 points.
        point_coords = [(0, -1), (1, 1), (2, 3), (3, 5)]
        points = VGroup()
        for (px, py) in point_coords:
            sx = x_axis.number_to_point(px)[0]
            sy = y_axis.number_to_point(py)[1]
            dot = Dot(point=np.array([sx, sy, 0.0]), color=ORANGE_TERM, radius=0.1)
            dot.set_z_index(4)
            points.add(dot)

        for d in points:
            self.play(FadeIn(d, scale=0.5, run_time=0.5))
            self.wait(0.4)
        self.wait(1.5)

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Draw the line through the points, extending past (~9 s)
        # ──────────────────────────────────────────────────────────────────
        first_sx = x_axis.number_to_point(0)[0]
        last_sx = x_axis.number_to_point(3)[0]
        first_sy = y_axis.number_to_point(-1)[1]
        last_sy = y_axis.number_to_point(5)[1]

        x_min = first_sx - 0.5
        x_max = last_sx + 0.5
        slope_screen = (last_sy - first_sy) / (last_sx - first_sx)
        y_left = first_sy + slope_screen * (x_min - first_sx)
        y_right = first_sy + slope_screen * (x_max - first_sx)
        line = Line(
            start=np.array([x_min, y_left, 0.0]),
            end=np.array([x_max, y_right, 0.0]),
            color=GREEN_OK,
            stroke_width=5,
        )
        line.set_z_index(3)

        self.play(Create(line, run_time=2.5))
        self.wait(3.0)

        caption = Text(
            "Connect with a straight line.",
            font_size=22, color=GREEN_OK,
        )
        caption.move_to(DOWN * 2.7)
        caption_bg = BackgroundRectangle(caption, color=BLACK, fill_opacity=0.95, buff=0.18)
        caption_bg.move_to(caption.get_center())
        self.play(FadeIn(caption_bg, run_time=0.4), FadeIn(caption, run_time=1.0))
        self.wait(2.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (~40 s, total ≈ 88 s)
        # ──────────────────────────────────────────────────────────────────
        beat2_5_group = VGroup(
            eq, table_bg, headers, table_cells,
            x_axis, y_axis, x_labels, y_labels, origin_lbl,
            x_axis_label, y_axis_label,
            points, line, caption, caption_bg,
        )
        self.play(FadeOut(beat2_5_group, run_time=1.5))

        animate_final_definition(
            self,
            r"y \;=\; m\,x + c",
            "m is the gradient, c is the y-intercept — two points sketch the line.",
            final_wait=33.0,
        )