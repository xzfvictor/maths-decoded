"""
Manim scene for the lesson `graphing-linear-relations`
(topic `l8-a-linear-equations-inequalities`).

A linear relation is an equation whose graph is a straight line.
The animation builds a table of values for y = 2x - 1, plots the points on
a small Cartesian plane, then connects them with a line that extends past
the outermost points. The final takeaway summarises y = mx + c.

Render target: ~85-88 s, matched to the audio narration length so the
two streams align cleanly when muxed with ffmpeg. Beats are timed with
explicit self.wait(...) calls; total budget is the sum of beats.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_TITLE, BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM,
    GREEN_OK, make_title_pair, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class GraphingLinearRelationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Graphing linear relations",
            "Make a table, plot the points, draw the line.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Show the equation y = 2x - 1 (~7 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = VGroup()
        eq = make_equation_card(r"y = 2x - 1", color=ORANGE_TERM, scale=1.05)
        eq.move_to(BAND_CHART_CENTER + UP * 1.3)
        self.play(FadeIn(eq, run_time=1.2))
        self.wait(2.5)
        beat_2.add(eq)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Build a table of values (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = VGroup()
        # Header row + 4 data rows. Layout on the left so the plane has room.
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
        table_cells.move_to(LEFT * 3.6 + UP * 0.6)

        # Column headers above the table for "x | y".
        x_header = Text("x", font_size=22, color=WHITE)
        y_header = Text("y", font_size=22, color=WHITE)
        x_header.next_to(table_cells[0], UP, buff=0.05).align_to(table_cells[0][0], LEFT)
        y_header.next_to(x_header, RIGHT, buff=0.7)
        headers = VGroup(x_header, y_header)

        # Opaque panel behind the table so it reads on any background.
        table_bg = BackgroundRectangle(
            VGroup(headers, table_cells),
            color=BLACK,
            fill_opacity=0.95,
            buff=0.25,
        )
        table_bg.move_to(VGroup(headers, table_cells).get_center())
        table_bg.set_z_index(1)

        self.play(FadeIn(table_bg, run_time=0.6))
        self.play(
            FadeIn(headers, shift=DOWN * 0.2, run_time=0.8),
        )
        for row in table_cells:
            self.play(FadeIn(row, shift=RIGHT * 0.2, run_time=0.45))
            self.wait(0.5)
        self.wait(3.0)

        beat_3.add(table_bg, headers, table_cells)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Build axes and plot the 4 points (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = VGroup()
        # Manually built NumberLines instead of Axes — gives full control
        # over tick density and avoids the pitfalls of Axes' built-in labels.
        # Chart shrunk to fit within chart band y=[-1.5, 1.5] so it doesn't
        # overlap the subtitle above. Y-axis x_range extended to [-2.5, 5]
        # so the y=5 point lands at screen y=1.5 instead of leaking above
        # the subtitle.
        plane_center = ORIGIN
        plane_half   = 1.5  # half-extent on each axis (chart band y=[-1.5, 1.5])

        x_axis = NumberLine(
            x_range=[-2.5, 3.5, 1],
            length=3.0,
            color=WHITE,
            stroke_width=3,
            include_tip=False,
        )
        x_axis.move_to(plane_center + DOWN * 1.4)
        x_axis.set_z_index(2)

        y_axis = NumberLine(
            x_range=[-2.5, 5, 1],
            length=3.0,
            color=WHITE,
            stroke_width=3,
            include_tip=False,
            rotation=90 * DEGREES,
        )
        y_axis.move_to(plane_center + ORIGIN)
        y_axis.set_z_index(2)

        # Tick numbers along the x-axis (compact, only key values).
        x_labels = VGroup()
        for xv in [-2, -1, 1, 2, 3]:
            lbl = MathTex(str(xv), font_size=20, color=WHITE).next_to(
                x_axis.number_to_point(xv), DOWN, buff=0.15,
            )
            x_labels.add(lbl)

        # Tick numbers along the y-axis (compact).
        y_labels = VGroup()
        for yv in [-1, 1, 2, 3, 4, 5]:
            lbl = MathTex(str(yv), font_size=20, color=WHITE).next_to(
                y_axis.number_to_point(yv), LEFT, buff=0.15,
            )
            y_labels.add(lbl)

        # Origin label "0".
        origin_lbl = MathTex("0", font_size=20, color=WHITE).next_to(
            x_axis.number_to_point(0), DOWN, buff=0.15,
        ).shift(LEFT * 0.25)

        # Axis labels.
        x_axis_label = MathTex("x", font_size=26, color=WHITE).next_to(
            x_axis, RIGHT, buff=0.15,
        )
        y_axis_label = MathTex("y", font_size=26, color=WHITE).next_to(
            y_axis, UP, buff=0.1,
        )

        self.play(
            Create(x_axis, run_time=1.2),
            Create(y_axis, run_time=1.2),
        )
        self.play(
            FadeIn(x_labels, run_time=0.7),
            FadeIn(y_labels, run_time=0.7),
            FadeIn(origin_lbl, run_time=0.5),
        )
        self.wait(1.5)

        # Plot the 4 points. Use a fixed scale factor so x=2 lands at +1.4 etc.
        # x in [-2, 3] -> screen x = x_axis.number_to_point(x)
        # y in [-1, 3] -> screen y = y_axis.number_to_point(y)
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
            self.wait(0.5)
        self.wait(2.0)

        beat_4.add(
            x_axis, y_axis, x_labels, y_labels, origin_lbl,
            x_axis_label, y_axis_label, points,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Draw the line through the points, extending past them (~12 s)
        # ──────────────────────────────────────────────────────────────────
        beat_5 = VGroup()
        # Line extends a bit past the first and last points.
        first_sx = x_axis.number_to_point(0)[0]
        last_sx  = x_axis.number_to_point(3)[0]
        first_sy = y_axis.number_to_point(-1)[1]
        last_sy  = y_axis.number_to_point(5)[1]

        # The straight line has slope 2 and passes through both end points
        # on the chart, so the screen line goes through the dots exactly.
        # Extend half a unit past on each side.
        x_min = first_sx - 0.5
        x_max = last_sx + 0.5
        slope_screen = (last_sy - first_sy) / (last_sx - first_sx)
        y_left  = first_sy + slope_screen * (x_min - first_sx)
        y_right = first_sy + slope_screen * (x_max - first_sx)
        line = Line(
            start=np.array([x_min, y_left, 0.0]),
            end=np.array([x_max, y_right, 0.0]),
            color=GREEN_OK,
            stroke_width=5,
        )
        line.set_z_index(3)

        self.play(Create(line, run_time=2.5))
        self.wait(4.0)

        # Caption: "Connect with a straight line."
        caption = Text(
            "Connect with a straight line.",
            font_size=22,
            color=GREEN_OK,
        )
        caption.next_to(plane_center, DOWN * 3.5).shift(UP * 0.5)
        caption_bg = BackgroundRectangle(caption, color=BLACK, fill_opacity=0.95, buff=0.18)
        caption_bg.move_to(caption.get_center())
        # Place caption safely above BAND_BOTTOM.
        caption.move_to(DOWN * 2.7)
        caption_bg.move_to(caption.get_center())
        self.play(FadeIn(caption_bg, run_time=0.4), FadeIn(caption, run_time=1.0))
        self.wait(4.0)

        beat_5.add(line, caption, caption_bg)
        self.play(FadeOut(beat_5, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (~30 s, total ≈ 86 s)
        # ──────────────────────────────────────────────────────────────────
        # Beat groups already faded individually above; just animate final.

        animate_final_definition(
            self,
            r"y \;=\; m\,x + c",
            "m is the gradient, c is the y-intercept.",
            final_wait=43.0,
        )