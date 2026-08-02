"""
Manim scene for the lesson `quadratic-parameters`
(topic `l9-a-variation-of-parameters`).

In $y = ax^2 + bx + c$, $a$ controls the shape and direction, $c$ slides
the graph vertically, and $b$ shifts it horizontally. The animation
isolates each parameter and shows a contrasting pair so the effect
becomes visible.

Render target: ~103.25 s, matched to the audio narration length.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class QuadraticParametersScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (visible for entire animation) + intro (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Varying parameters in y = ax² + bx + c",
            "a shapes;  c slides;  b shifts sideways.",
        )

        def parabola_in_axes(a_val, b_val, c_val, axes, color):
            """Plot y = a x^2 + b x + c within the given axes object."""
            center = axes.get_center()
            x_unit = axes.x_axis.get_unit_size()
            y_unit = axes.y_axis.get_unit_size()
            n = 60
            xs = np.linspace(-2.6, 2.6, n)
            ys = a_val * xs ** 2 + b_val * xs + c_val
            pts = [
                center + np.array([x * x_unit, y * y_unit, 0.0])
                for x, y in zip(xs, ys)
            ]
            return VMobject(stroke_width=4, color=color).set_points_as_corners(pts)

        def make_axes():
            ax = Axes(
                x_range=[-3, 3, 1],
                y_range=[-2, 3, 1],
                x_length=5.2,
                y_length=3.6,
                tips=False,
                axis_config={"include_numbers": False, "stroke_width": 1.5},
            ).move_to(BAND_CHART_CENTER + DOWN * 0.6)
            ax_bg = BackgroundRectangle(ax, color=BLACK, fill_opacity=1, buff=0.2)
            ax_bg.move_to(ax.get_center())
            return ax, ax_bg

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Effect of a (shape & direction) (~30 s)
        # ──────────────────────────────────────────────────────────────────
        eq_a = MathTex(r"y \;=\; a\,x^{2}", color=WHITE).scale(1.0)
        eq_a.move_to(BAND_CHART_CENTER + UP * 1.6)
        eq_a_bg = BackgroundRectangle(eq_a, color=BLACK, fill_opacity=1, buff=0.25)
        eq_a_bg.move_to(eq_a.get_center())
        self.play(FadeIn(eq_a_bg, run_time=0.5), Write(eq_a, run_time=1.4))
        self.wait(1.0)

        axes_a, axes_a_bg = make_axes()
        self.play(FadeIn(axes_a_bg, run_time=0.4), FadeIn(axes_a, run_time=0.8))
        self.wait(0.6)

        # a = +1 (opens up) vs a = -1 (opens down) — same vertex.
        up_curve = parabola_in_axes(1.0, 0.0, 0.0, axes_a, BLUE_TERM)
        dn_curve = parabola_in_axes(-1.0, 0.0, 0.0, axes_a, RED_REJECT)
        self.play(Create(up_curve, run_time=2.0))
        self.wait(1.5)
        self.play(Create(dn_curve, run_time=2.0))
        self.wait(1.5)

        a_note = Text(
            "Sign of a  —  flip direction.  |a|  —  narrow vs wide.",
            font_size=20, color=GREEN_OK,
        ).next_to(eq_a, DOWN, buff=0.35)
        a_note_bg = BackgroundRectangle(a_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        a_note_bg.move_to(a_note.get_center())
        self.play(FadeIn(a_note_bg, run_time=0.4), FadeIn(a_note, run_time=1.0))
        self.wait(2.5)

        self.play(
            FadeOut(eq_a, run_time=0.6),
            FadeOut(eq_a_bg, run_time=0.6),
            FadeOut(a_note, run_time=0.6),
            FadeOut(a_note_bg, run_time=0.6),
            FadeOut(up_curve, run_time=0.6),
            FadeOut(dn_curve, run_time=0.6),
            FadeOut(axes_a, run_time=0.6),
            FadeOut(axes_a_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Effect of c (vertical slide) (~22 s)
        # ──────────────────────────────────────────────────────────────────
        eq_c = MathTex(r"y \;=\; x^{2} \;+\; c", color=WHITE).scale(1.0)
        eq_c.move_to(BAND_CHART_CENTER + UP * 1.6)
        eq_c_bg = BackgroundRectangle(eq_c, color=BLACK, fill_opacity=1, buff=0.25)
        eq_c_bg.move_to(eq_c.get_center())
        self.play(FadeIn(eq_c_bg, run_time=0.5), Write(eq_c, run_time=1.4))
        self.wait(1.0)

        axes_c, axes_c_bg = make_axes()
        self.play(FadeIn(axes_c_bg, run_time=0.4), FadeIn(axes_c, run_time=0.8))
        self.wait(0.6)

        low = parabola_in_axes(1.0, 0.0, -1.0, axes_c, TEAL_TERM)
        mid = parabola_in_axes(1.0, 0.0,  0.0, axes_c, BLUE_TERM)
        high = parabola_in_axes(1.0, 0.0,  1.0, axes_c, ORANGE_TERM)

        self.play(Create(low, run_time=1.6))
        self.wait(1.0)
        self.play(Create(mid, run_time=1.6))
        self.wait(1.0)
        self.play(Create(high, run_time=1.6))
        self.wait(1.5)

        c_note = Text(
            "c slides the whole parabola up or down.",
            font_size=20, color=GREEN_OK,
        ).next_to(eq_c, DOWN, buff=0.35)
        c_note_bg = BackgroundRectangle(c_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        c_note_bg.move_to(c_note.get_center())
        self.play(FadeIn(c_note_bg, run_time=0.4), FadeIn(c_note, run_time=1.0))
        self.wait(2.0)

        self.play(
            FadeOut(eq_c, run_time=0.6),
            FadeOut(eq_c_bg, run_time=0.6),
            FadeOut(c_note, run_time=0.6),
            FadeOut(c_note_bg, run_time=0.6),
            FadeOut(low, run_time=0.6),
            FadeOut(mid, run_time=0.6),
            FadeOut(high, run_time=0.6),
            FadeOut(axes_c, run_time=0.6),
            FadeOut(axes_c_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Effect of b (sideways shift) and reject a = 0 (~18 s)
        # ──────────────────────────────────────────────────────────────────
        eq_b = MathTex(r"y \;=\; x^{2} \;+\; b\,x", color=WHITE).scale(1.0)
        eq_b.move_to(BAND_CHART_CENTER + UP * 1.6)
        eq_b_bg = BackgroundRectangle(eq_b, color=BLACK, fill_opacity=1, buff=0.25)
        eq_b_bg.move_to(eq_b.get_center())
        self.play(FadeIn(eq_b_bg, run_time=0.5), Write(eq_b, run_time=1.4))
        self.wait(1.0)

        axes_b, axes_b_bg = make_axes()
        self.play(FadeIn(axes_b_bg, run_time=0.4), FadeIn(axes_b, run_time=0.8))
        self.wait(0.6)

        left = parabola_in_axes(1.0, 1.5, 0.0, axes_b, TEAL_TERM)
        centered = parabola_in_axes(1.0, 0.0, 0.0, axes_b, BLUE_TERM)
        right = parabola_in_axes(1.0, -1.5, 0.0, axes_b, ORANGE_TERM)
        self.play(Create(centered, run_time=1.6))
        self.wait(0.8)
        self.play(Create(left, run_time=1.6))
        self.wait(0.8)
        self.play(Create(right, run_time=1.6))
        self.wait(1.0)

        b_note = Text(
            "b shifts the vertex sideways.",
            font_size=20, color=GREEN_OK,
        ).next_to(eq_b, DOWN, buff=0.35)
        b_note_bg = BackgroundRectangle(b_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        b_note_bg.move_to(b_note.get_center())
        self.play(FadeIn(b_note_bg, run_time=0.4), FadeIn(b_note, run_time=1.0))
        self.wait(1.5)

        self.play(
            FadeOut(eq_b, run_time=0.6),
            FadeOut(eq_b_bg, run_time=0.6),
            FadeOut(b_note, run_time=0.6),
            FadeOut(b_note_bg, run_time=0.6),
            FadeOut(left, run_time=0.6),
            FadeOut(centered, run_time=0.6),
            FadeOut(right, run_time=0.6),
            FadeOut(axes_b, run_time=0.6),
            FadeOut(axes_b_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Reject a = 0 (no longer a parabola) (~10 s)
        # ──────────────────────────────────────────────────────────────────
        reject_eq = MathTex(r"y \;=\; 0 \cdot x^{2} \;+\; bx \;+\; c", color=RED_REJECT).scale(0.95)
        reject_eq.move_to(BAND_CHART_CENTER + UP * 0.5)
        reject_eq_bg = BackgroundRectangle(reject_eq, color=BLACK, fill_opacity=1, buff=0.25)
        reject_eq_bg.move_to(reject_eq.get_center())
        self.play(FadeIn(reject_eq_bg, run_time=0.5), Write(reject_eq, run_time=1.6))
        self.wait(0.8)

        linear_eq = MathTex(r"\Rightarrow \; y \;=\; b\,x \;+\; c", color=RED_REJECT).scale(1.0)
        linear_eq.next_to(reject_eq, DOWN, buff=0.5)
        linear_eq_bg = BackgroundRectangle(linear_eq, color=BLACK, fill_opacity=1, buff=0.25)
        linear_eq_bg.move_to(linear_eq.get_center())
        self.play(FadeIn(linear_eq_bg, run_time=0.4), Write(linear_eq, run_time=1.2))
        self.wait(0.8)

        not_note = Text("a = 0  —  no quadratic term left, just a line.",
                       font_size=20, color=RED_REJECT)
        not_note.next_to(VGroup(reject_eq, linear_eq), DOWN, buff=0.5)
        not_note_bg = BackgroundRectangle(not_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        not_note_bg.move_to(not_note.get_center())
        cross2 = Cross(VGroup(reject_eq, linear_eq), color=RED_REJECT, stroke_width=5)
        self.play(Create(cross2, run_time=1.0))
        self.play(FadeIn(not_note_bg, run_time=0.4), FadeIn(not_note, run_time=1.0))
        self.wait(2.0)

        self.play(
            FadeOut(reject_eq, run_time=0.8),
            FadeOut(reject_eq_bg, run_time=0.8),
            FadeOut(linear_eq, run_time=0.8),
            FadeOut(linear_eq_bg, run_time=0.8),
            FadeOut(cross2, run_time=0.8),
            FadeOut(not_note, run_time=0.8),
            FadeOut(not_note_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (~final_wait = 40 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y \;=\; a\,x^{2} \;+\; b\,x \;+\; c",
            "a shapes;  c slides vertically;  b shifts the vertex.",
            final_wait=40.0,
        )