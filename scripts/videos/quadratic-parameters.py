"""
Manim scene for the lesson `quadratic-parameters`
(topic `l9-a-variation-of-parameters`).

In $y = ax^2 + bx + c$, $a$ flips direction and stretches; $b$ shifts
the vertex sideways; $c$ slides the whole parabola up or down. The
animation isolates each parameter and shows a contrasting pair so the
effect becomes visible.

The audio narrative runs ~44 s; the scene is paced to match.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class QuadraticParametersScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Varying parameters in y = ax² + bx + c",
            "a shapes;  b shifts sideways;  c slides vertically.",
        )

        def parabola_in_axes(a_val, b_val, c_val, axes, color):
            """Plot y = a x^2 + b x + c within the given axes object."""
            center = axes.get_center()
            x_unit = axes.x_axis.get_unit_size()
            y_unit = axes.y_axis.get_unit_size()
            n = 60
            # Use a restricted x range so the parabola stays inside the
            # visible y_range, even when a_val is large.
            xs = np.linspace(-1.0, 1.0, n)
            ys = a_val * xs ** 2 + b_val * xs + c_val
            pts = [
                center + np.array([x * x_unit, y * y_unit, 0.0])
                for x, y in zip(xs, ys)
            ]
            return VMobject(stroke_width=4, color=color).set_points_as_corners(pts)

        def make_axes():
            # y_range constrained so the parabolas don't overshoot the
            # subtitle at the top or the safe-area lower bound.
            ax = Axes(
                x_range=[-3, 3, 1],
                y_range=[-1.5, 1.4, 1],
                x_length=5.2,
                y_length=2.4,
                tips=False,
                axis_config={"include_numbers": False, "stroke_width": 1.5},
            ).move_to(BAND_CHART_CENTER + DOWN * 0.2)
            ax_bg = BackgroundRectangle(ax, color=BLACK, fill_opacity=1, buff=0.2)
            ax_bg.move_to(ax.get_center())
            return ax, ax_bg

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Effect of a (shape & direction) (~10 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        eq_a = MathTex(r"y \;=\; a\,x^{2}", color=WHITE).scale(0.95)
        eq_a.move_to(BAND_CHART_CENTER + UP * 1.25)
        eq_a_bg = BackgroundRectangle(eq_a, color=BLACK, fill_opacity=1, buff=0.25)
        eq_a_bg.move_to(eq_a.get_center())
        beat_2.add(eq_a, eq_a_bg)
        self.play(FadeIn(eq_a_bg, run_time=0.4), Write(eq_a, run_time=1.2))
        self.wait(0.6)

        axes_a, axes_a_bg = make_axes()
        beat_2.add(axes_a, axes_a_bg)
        self.play(FadeIn(axes_a_bg, run_time=0.4), FadeIn(axes_a, run_time=0.6))
        self.wait(0.4)

        up_curve = parabola_in_axes(0.8, 0.0, 0.0, axes_a, BLUE_TERM)
        dn_curve = parabola_in_axes(-0.8, 0.0, 0.0, axes_a, RED_REJECT)
        self.play(Create(up_curve, run_time=1.6))
        self.wait(0.8)
        self.play(Create(dn_curve, run_time=1.4))
        self.wait(0.8)

        a_note = Text(
            "Sign of a flips direction. |a| controls width.",
            font_size=20, color=GREEN_OK,
        ).next_to(eq_a, UP, buff=0.25)
        a_note_bg = BackgroundRectangle(a_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        a_note_bg.move_to(a_note.get_center())
        beat_2.add(a_note, a_note_bg)
        self.play(FadeIn(a_note_bg, run_time=0.4), FadeIn(a_note, run_time=0.9))
        self.wait(1.0)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Effect of c (vertical slide) (~7 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        eq_c = MathTex(r"y \;=\; 0.8\,x^{2} \;+\; c", color=WHITE).scale(0.95)
        eq_c.move_to(BAND_CHART_CENTER + UP * 1.25)
        eq_c_bg = BackgroundRectangle(eq_c, color=BLACK, fill_opacity=1, buff=0.25)
        eq_c_bg.move_to(eq_c.get_center())
        beat_3.add(eq_c, eq_c_bg)
        self.play(FadeIn(eq_c_bg, run_time=0.4), Write(eq_c, run_time=1.2))
        self.wait(0.6)

        axes_c, axes_c_bg = make_axes()
        beat_3.add(axes_c, axes_c_bg)
        self.play(FadeIn(axes_c_bg, run_time=0.4), FadeIn(axes_c, run_time=0.6))
        self.wait(0.4)

        low = parabola_in_axes(0.8, 0.0, -0.5, axes_c, TEAL_TERM)
        mid = parabola_in_axes(0.8, 0.0,  0.0, axes_c, BLUE_TERM)
        high = parabola_in_axes(0.8, 0.0,  0.5, axes_c, ORANGE_TERM)
        self.play(Create(low, run_time=1.2))
        self.wait(0.4)
        self.play(Create(mid, run_time=1.0))
        self.wait(0.4)
        self.play(Create(high, run_time=1.0))
        self.wait(0.6)

        c_note = Text(
            "c slides the whole parabola up or down.",
            font_size=20, color=GREEN_OK,
        ).next_to(eq_c, UP, buff=0.25)
        c_note_bg = BackgroundRectangle(c_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        c_note_bg.move_to(c_note.get_center())
        beat_3.add(c_note, c_note_bg)
        self.play(FadeIn(c_note_bg, run_time=0.4), FadeIn(c_note, run_time=0.9))
        self.wait(0.6)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Effect of b (sideways shift) (~6 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        eq_b = MathTex(r"y \;=\; 0.8\,x^{2} \;+\; b\,x", color=WHITE).scale(0.95)
        eq_b.move_to(BAND_CHART_CENTER + UP * 1.25)
        eq_b_bg = BackgroundRectangle(eq_b, color=BLACK, fill_opacity=1, buff=0.25)
        eq_b_bg.move_to(eq_b.get_center())
        beat_4.add(eq_b, eq_b_bg)
        self.play(FadeIn(eq_b_bg, run_time=0.4), Write(eq_b, run_time=1.2))
        self.wait(0.4)

        axes_b, axes_b_bg = make_axes()
        beat_4.add(axes_b, axes_b_bg)
        self.play(FadeIn(axes_b_bg, run_time=0.4), FadeIn(axes_b, run_time=0.6))
        self.wait(0.3)

        centered = parabola_in_axes(0.8,  0.0, 0.0, axes_b, BLUE_TERM)
        left    = parabola_in_axes(0.8,  0.5, 0.0, axes_b, TEAL_TERM)
        right   = parabola_in_axes(0.8, -0.5, 0.0, axes_b, ORANGE_TERM)
        self.play(Create(centered, run_time=1.0))
        self.wait(0.3)
        self.play(Create(left, run_time=1.0))
        self.wait(0.3)
        self.play(Create(right, run_time=1.0))
        self.wait(0.4)

        b_note = Text(
            "b shifts the vertex sideways.",
            font_size=20, color=GREEN_OK,
        ).next_to(eq_b, UP, buff=0.25)
        b_note_bg = BackgroundRectangle(b_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        b_note_bg.move_to(b_note.get_center())
        beat_4.add(b_note, b_note_bg)
        self.play(FadeIn(b_note_bg, run_time=0.4), FadeIn(b_note, run_time=0.9))
        self.wait(0.6)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Reject a = 0 (no quadratic term left) (~5 s)
        # ──────────────────────────────────────────────────────────────────
        beat_5 = beat_group()
        reject_eq = MathTex(
            r"y \;=\; 0 \cdot x^{2} \;+\; bx \;+\; c", color=RED_REJECT,
        ).scale(0.9)
        reject_eq.move_to(BAND_CHART_CENTER + UP * 0.6)
        reject_eq_bg = BackgroundRectangle(reject_eq, color=BLACK, fill_opacity=1, buff=0.25)
        reject_eq_bg.move_to(reject_eq.get_center())
        beat_5.add(reject_eq, reject_eq_bg)
        self.play(FadeIn(reject_eq_bg, run_time=0.4), Write(reject_eq, run_time=1.4))
        self.wait(0.4)

        linear_eq = MathTex(
            r"\Rightarrow \; y \;=\; b\,x \;+\; c", color=RED_REJECT,
        ).scale(0.95)
        linear_eq.next_to(reject_eq, DOWN, buff=0.4)
        linear_eq_bg = BackgroundRectangle(linear_eq, color=BLACK, fill_opacity=1, buff=0.25)
        linear_eq_bg.move_to(linear_eq.get_center())
        beat_5.add(linear_eq, linear_eq_bg)
        self.play(FadeIn(linear_eq_bg, run_time=0.4), Write(linear_eq, run_time=1.2))
        self.wait(0.4)

        not_note = Text(
            "a = 0 — no quadratic term. Just a straight line.",
            font_size=18, color=RED_REJECT,
        ).next_to(linear_eq, DOWN, buff=0.4)
        not_note_bg = BackgroundRectangle(not_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        not_note_bg.move_to(not_note.get_center())
        cross2 = Cross(VGroup(reject_eq, linear_eq), color=RED_REJECT, stroke_width=5)
        beat_5.add(cross2, not_note, not_note_bg)
        self.play(Create(cross2, run_time=1.0))
        self.play(FadeIn(not_note_bg, run_time=0.4), FadeIn(not_note, run_time=0.9))
        self.wait(0.6)

        self.play(FadeOut(beat_5, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y \;=\; a\,x^{2} \;+\; b\,x \;+\; c",
            "a flips & stretches;  b slides sideways;  c slides vertically.",
            final_wait=20.0,
        )
