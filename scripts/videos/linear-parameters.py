"""
Manim scene for the lesson `linear-parameters`
(topic `l9-a-variation-of-parameters`).

In $y = mx + c$, $m$ tilts the line and $c$ slides it up or down. The
animation fixes one parameter while varying the other, so the rotation
around $(0, c)$ and the family of parallel lines become visible.

Render target: ~99.25 s, matched to the audio narration length.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class LinearParametersScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (visible for entire animation) + intro (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Varying parameters in y = mx + c",
            "m tilts the line; c slides it up or down.",
        )

        # Helper to make a small line segment at a given slope through origin.
        def line_through(m_value: float, color, length: float = 2.0):
            # Build a line through (0,0) with slope m_value, scaled to length.
            dx = length / np.sqrt(1 + m_value ** 2)
            dy = m_value * dx
            start = np.array([-dx, -dy, 0.0])
            end = np.array([dx, dy, 0.0])
            return Line(start, end, color=color, stroke_width=4)

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Effect of m (rotate around fixed intercept) (~30 s)
        # ──────────────────────────────────────────────────────────────────
        # Card showing y = mx + 1 with m highlighted.
        eq = MathTex(r"y \;=\; m\,x \;+\; 1", color=WHITE).scale(1.0)
        eq.move_to(BAND_CHART_CENTER + UP * 1.2)
        eq_bg = BackgroundRectangle(eq, color=BLACK, fill_opacity=1, buff=0.25)
        eq_bg.move_to(eq.get_center())

        self.play(FadeIn(eq_bg, run_time=0.5), Write(eq, run_time=1.5))
        self.wait(1.5)

        # Show three lines all through (0, 0.5), rotating as m changes.
        # y_range is constrained to ≤ 1.2 so the line endpoints stay
        # below the subtitle and inside the safe area.
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1.5, 1.2, 1],
            x_length=5.0,
            y_length=2.2,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.3)
        axes_bg = BackgroundRectangle(axes, color=BLACK, fill_opacity=1, buff=0.2)
        axes_bg.move_to(axes.get_center())
        self.play(FadeIn(axes_bg, run_time=0.5), FadeIn(axes, run_time=1.0))

        # Three lines through (0, 0.5) in axes coordinates.
        def line_in_axes(m_val, color):
            center = axes.get_center()
            x_unit = axes.x_axis.get_unit_size()
            y_unit = axes.y_axis.get_unit_size()
            x1, x2 = -2.0, 2.0
            y1 = m_val * x1 + 0.5
            y2 = m_val * x2 + 0.5
            p1 = center + np.array([x1 * x_unit, y1 * y_unit, 0])
            p2 = center + np.array([x2 * x_unit, y2 * y_unit, 0])
            return Line(p1, p2, color=color, stroke_width=4)

        l1 = line_in_axes(-0.3, TEAL_TERM)
        l2 = line_in_axes( 0.0, ORANGE_TERM)
        l3 = line_in_axes( 0.3, BLUE_TERM)

        self.play(Create(l1, run_time=1.4))
        self.wait(1.5)
        self.play(Create(l2, run_time=1.4))
        self.wait(1.5)
        self.play(Create(l3, run_time=1.4))
        self.wait(2.0)

        m_note = Text(
            "Same y-intercept  —  varying m rotates the line.",
            font_size=20, color=GREEN_OK,
        ).next_to(eq, DOWN, buff=0.4)
        m_note_bg = BackgroundRectangle(m_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        m_note_bg.move_to(m_note.get_center())
        self.play(FadeIn(m_note_bg, run_time=0.4), FadeIn(m_note, run_time=1.0))
        self.wait(3.0)

        self.play(
            FadeOut(eq, run_time=0.6),
            FadeOut(eq_bg, run_time=0.6),
            FadeOut(m_note, run_time=0.6),
            FadeOut(m_note_bg, run_time=0.6),
            FadeOut(l1, run_time=0.6),
            FadeOut(l2, run_time=0.6),
            FadeOut(l3, run_time=0.6),
            FadeOut(axes, run_time=0.6),
            FadeOut(axes_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Effect of c (parallel lines) (~24 s)
        # ──────────────────────────────────────────────────────────────────
        eq2 = MathTex(r"y \;=\; 0.3\,x \;+\; c", color=WHITE).scale(1.0)
        eq2.move_to(BAND_CHART_CENTER + UP * 1.2)
        eq2_bg = BackgroundRectangle(eq2, color=BLACK, fill_opacity=1, buff=0.25)
        eq2_bg.move_to(eq2.get_center())

        self.play(FadeIn(eq2_bg, run_time=0.5), Write(eq2, run_time=1.5))
        self.wait(1.5)

        axes2 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1.5, 1.2, 1],
            x_length=5.0,
            y_length=2.2,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.3)
        axes2_bg = BackgroundRectangle(axes2, color=BLACK, fill_opacity=1, buff=0.2)
        axes2_bg.move_to(axes2.get_center())
        self.play(FadeIn(axes2_bg, run_time=0.5), FadeIn(axes2, run_time=1.0))

        def line_in_axes2(m_val, c_val, color):
            center = axes2.get_center()
            x_unit = axes2.x_axis.get_unit_size()
            y_unit = axes2.y_axis.get_unit_size()
            x1, x2 = -2.0, 2.0
            y1 = m_val * x1 + c_val
            y2 = m_val * x2 + c_val
            p1 = center + np.array([x1 * x_unit, y1 * y_unit, 0])
            p2 = center + np.array([x2 * x_unit, y2 * y_unit, 0])
            return Line(p1, p2, color=color, stroke_width=4)

        p1 = line_in_axes2(0.3, -0.4, TEAL_TERM)
        p2 = line_in_axes2(0.3,  0.0, ORANGE_TERM)
        p3 = line_in_axes2(0.3,  0.4, BLUE_TERM)

        self.play(Create(p1, run_time=1.4))
        self.wait(1.0)
        self.play(Create(p2, run_time=1.4))
        self.wait(1.0)
        self.play(Create(p3, run_time=1.4))
        self.wait(1.5)

        c_note = Text(
            "Same gradient  —  varying c slides the line.",
            font_size=20, color=GREEN_OK,
        ).next_to(eq2, DOWN, buff=0.4)
        c_note_bg = BackgroundRectangle(c_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        c_note_bg.move_to(c_note.get_center())
        self.play(FadeIn(c_note_bg, run_time=0.4), FadeIn(c_note, run_time=1.0))
        self.wait(2.5)

        self.play(
            FadeOut(eq2, run_time=0.6),
            FadeOut(eq2_bg, run_time=0.6),
            FadeOut(c_note, run_time=0.6),
            FadeOut(c_note_bg, run_time=0.6),
            FadeOut(p1, run_time=0.6),
            FadeOut(p2, run_time=0.6),
            FadeOut(p3, run_time=0.6),
            FadeOut(axes2, run_time=0.6),
            FadeOut(axes2_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: m and c both at 0 (not a family) (~10 s)
        # ──────────────────────────────────────────────────────────────────
        reject = MathTex(r"y \;=\; 0 \cdot x \;+\; 0", color=RED_REJECT).scale(1.0)
        reject.move_to(BAND_CHART_CENTER + UP * 0.4)
        reject_bg = BackgroundRectangle(reject, color=BLACK, fill_opacity=1, buff=0.25)
        reject_bg.move_to(reject.get_center())
        self.play(FadeIn(reject_bg, run_time=0.5), Write(reject, run_time=1.4))

        # Reveal the trivial line y = 0.
        trivial = MathTex(r"\Rightarrow \;y \;=\; 0", color=RED_REJECT).scale(1.0)
        trivial.next_to(reject, DOWN, buff=0.5)
        trivial_bg = BackgroundRectangle(trivial, color=BLACK, fill_opacity=1, buff=0.25)
        trivial_bg.move_to(trivial.get_center())
        self.play(FadeIn(trivial_bg, run_time=0.4), Write(trivial, run_time=1.0))
        self.wait(1.0)

        cross = Cross(VGroup(reject, trivial), color=RED_REJECT, stroke_width=5)
        not_lbl = Text("trivial line  —  not a useful family", font_size=20, color=RED_REJECT)
        not_lbl.next_to(VGroup(reject, trivial), DOWN, buff=0.5)
        not_lbl_bg = BackgroundRectangle(not_lbl, color=BLACK, fill_opacity=0.95, buff=0.15)
        not_lbl_bg.move_to(not_lbl.get_center())
        self.play(Create(cross, run_time=1.0))
        self.play(FadeIn(not_lbl_bg, run_time=0.4), FadeIn(not_lbl, run_time=1.0))
        self.wait(2.5)

        self.play(
            FadeOut(reject, run_time=0.8),
            FadeOut(reject_bg, run_time=0.8),
            FadeOut(trivial, run_time=0.8),
            FadeOut(trivial_bg, run_time=0.8),
            FadeOut(cross, run_time=0.8),
            FadeOut(not_lbl, run_time=0.8),
            FadeOut(not_lbl_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~final_wait = 38 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y \;=\; m\,x \;+\; c",
            "m tilts (gradient);  c slides (y-intercept).",
            final_wait=38.0,
        )