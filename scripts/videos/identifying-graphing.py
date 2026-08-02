"""
Manim scene for the lesson `identifying-graphing`
(topic `l9-a-quadratic-functions-equations`).

A quadratic in x has the form y = ax² + bx + c with a ≠ 0; its graph
is a parabola (U-shape if a > 0, upside-down U if a < 0). The animation
works through y = x² - 4x + 1 to find the vertex (2, -3), generalises
the shape, and rejects the confusion with a sharp V-shape (absolute
value).

Target duration: ~93 s (matches the audio narration length of 92.81 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class IdentifyingGraphingScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Identifying and graphing quadratics",
            "The graph is a parabola — find vertex, axis, y-intercept.",
            hold=2.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example y = x² - 4x + 1 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        eq1 = make_equation_card(r"y \;=\; x^{2} - 4x + 1",
                                  color=BLUE_TERM, scale=1.2)
        eq1.move_to(BAND_CHART_CENTER + UP * 1.3)
        for m in eq1:
            m.set_z_index(2)
        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.5))
        self.wait(1.8)

        # Vertex computation.
        head = Text("Vertex", font_size=22, color=GREEN_OK)
        head.move_to(BAND_CHART_CENTER + UP * 0.3)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        formula = MathTex(
            r"x_v \;=\; -\dfrac{b}{2a} \;=\; -\dfrac{-4}{2} \;=\; 2",
            color=GREEN_OK,
        ).scale(0.95)
        formula.next_to(head, DOWN, buff=0.4)
        formula_bg = BackgroundRectangle(formula, color=BLACK,
                                          fill_opacity=1, buff=0.25)
        formula_bg.move_to(formula.get_center())

        y_v = MathTex(
            r"y_v \;=\; (2)^{2} - 4(2) + 1 \;=\; -3",
            color=GREEN_OK,
        ).scale(0.95)
        y_v.next_to(formula, DOWN, buff=0.35)
        y_v_bg = BackgroundRectangle(y_v, color=BLACK,
                                      fill_opacity=1, buff=0.25)
        y_v_bg.move_to(y_v.get_center())

        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=0.9))
        self.wait(0.8)
        self.play(FadeIn(formula_bg, run_time=0.4), FadeIn(formula, run_time=1.4))
        self.wait(0.8)
        self.play(FadeIn(y_v_bg, run_time=0.4), FadeIn(y_v, run_time=1.4))
        self.wait(1.5)

        vertex = MathTex(r"\text{Vertex: } (2,\,-3)",
                         color=GREEN_OK).scale(1.0)
        vertex.next_to(y_v, DOWN, buff=0.45)
        vertex_bg = BackgroundRectangle(vertex, color=BLACK,
                                         fill_opacity=1, buff=0.25)
        vertex_bg.move_to(vertex.get_center())
        self.play(FadeIn(vertex_bg, run_time=0.4), FadeIn(vertex, run_time=1.2))
        self.wait(1.5)

        beat2_group = VGroup(eq1, head, head_bg, formula, formula_bg,
                             y_v, y_v_bg, vertex, vertex_bg)
        self.play(FadeOut(beat2_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — General shape: y = ax² + bx + c, draw a parabola (~14 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(r"y \;=\; a\,x^{2} + b\,x + c",
                                      color=BLUE_TERM, scale=1.1)
        general.move_to(BAND_CHART_CENTER + UP * 1.4)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.5))
        self.wait(1.5)

        # Draw a small parabola using ParametricFunction.
        parabola = ParametricFunction(
            lambda t: np.array([t, 0.4 * t**2 - 1.2, 0.0]),
            t_range=np.array([-2.0, 2.0, 0.05]),
            color=GREEN_OK,
            stroke_width=5,
        )
        parabola.move_to(BAND_CHART_CENTER + DOWN * 0.5)
        parabola.set_z_index(3)

        # Axes for the parabola.
        x_axis = Line(
            parabola.get_center() + LEFT * 2.8 + UP * 0.0,
            parabola.get_center() + RIGHT * 2.8 + UP * 0.0,
            color=WHITE, stroke_width=2,
        )
        y_axis = Line(
            parabola.get_center() + LEFT * 0.0 + DOWN * 1.5,
            parabola.get_center() + LEFT * 0.0 + UP * 1.5,
            color=WHITE, stroke_width=2,
        )
        x_axis.set_z_index(2)
        y_axis.set_z_index(2)

        # Vertex dot.
        vertex_pt = Dot(parabola.get_center() + DOWN * 1.2,
                        color=ORANGE_TERM, radius=0.09)
        vertex_pt.set_z_index(4)
        v_lbl = MathTex("(2,\,-3)", color=ORANGE_TERM).scale(0.7)
        v_lbl.next_to(vertex_pt, RIGHT, buff=0.15)
        v_lbl_bg = BackgroundRectangle(v_lbl, color=BLACK,
                                        fill_opacity=0.95, buff=0.12)
        v_lbl_bg.move_to(v_lbl.get_center())
        v_lbl.set_z_index(5)
        v_lbl_bg.set_z_index(4)

        # y-intercept dot.
        yint_pt = Dot(parabola.get_center() + UP * 0.8 + LEFT * 0.0,
                      color=TEAL_TERM, radius=0.09)
        yint_pt.set_z_index(4)
        yint_lbl = MathTex("(0,\,1)", color=TEAL_TERM).scale(0.7)
        yint_lbl.next_to(yint_pt, LEFT, buff=0.15)
        yint_lbl_bg = BackgroundRectangle(yint_lbl, color=BLACK,
                                           fill_opacity=0.95, buff=0.12)
        yint_lbl_bg.move_to(yint_lbl.get_center())
        yint_lbl.set_z_index(5)
        yint_lbl_bg.set_z_index(4)

        self.play(Create(x_axis, run_time=0.6), Create(y_axis, run_time=0.6))
        self.wait(0.6)
        self.play(Create(parabola, run_time=2.2))
        self.wait(0.8)
        self.play(FadeIn(vertex_pt, scale=0.5, run_time=0.6),
                  FadeIn(v_lbl_bg, run_time=0.4),
                  FadeIn(v_lbl, run_time=0.8))
        self.wait(0.8)
        self.play(FadeIn(yint_pt, scale=0.5, run_time=0.6),
                  FadeIn(yint_lbl_bg, run_time=0.4),
                  FadeIn(yint_lbl, run_time=0.8))
        self.wait(1.0)

        beat3_group = VGroup(general, x_axis, y_axis, parabola,
                             vertex_pt, v_lbl, v_lbl_bg,
                             yint_pt, yint_lbl, yint_lbl_bg)
        self.play(FadeOut(beat3_group, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: confusing the parabola with a sharp V (~8 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Not this", font_size=22, color=RED_REJECT)
        head.move_to(BAND_CHART_CENTER + UP * 1.5)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        # A sharp V-shape via two straight lines.
        v_left = Line(
            np.array([-1.2, -0.8, 0.0]),
            np.array([0.0, 0.0, 0.0]),
            color=RED_REJECT, stroke_width=6,
        )
        v_right = Line(
            np.array([0.0, 0.0, 0.0]),
            np.array([1.2, -0.8, 0.0]),
            color=RED_REJECT, stroke_width=6,
        )
        v_group = VGroup(v_left, v_right).move_to(BAND_CHART_CENTER + DOWN * 0.3)
        v_group.set_z_index(3)

        v_lbl = MathTex(r"|x|", color=RED_REJECT).scale(1.4)
        v_lbl.next_to(v_group, DOWN, buff=0.4)
        v_lbl_bg = BackgroundRectangle(v_lbl, color=BLACK, fill_opacity=1, buff=0.25)
        v_lbl_bg.move_to(v_lbl.get_center())

        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=0.8))
        self.wait(0.5)
        self.play(Create(v_left, run_time=0.7), Create(v_right, run_time=0.7))
        self.wait(0.6)
        self.play(FadeIn(v_lbl_bg, run_time=0.4), FadeIn(v_lbl, run_time=1.0))
        self.wait(1.0)

        # Cross it out.
        cross = Cross(v_lbl, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.7))
        self.wait(1.0)

        # Correctness note.
        ok = MathTex(r"\text{Parabola is curved, not sharp.}",
                     color=GREEN_OK).scale(0.9)
        ok.next_to(v_lbl, DOWN, buff=0.45)
        ok_bg = BackgroundRectangle(ok, color=BLACK, fill_opacity=0.95, buff=0.18)
        ok_bg.move_to(ok.get_center())
        self.play(FadeIn(ok_bg, run_time=0.4), FadeIn(ok, run_time=1.2))
        self.wait(1.2)
        self.play(
            FadeOut(VGroup(head, head_bg, v_group, v_lbl, v_lbl_bg,
                           cross, ok, ok_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=35 s, total ≈ 93 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y \;=\; a\,x^{2} + b\,x + c",
            "Smooth parabola — vertex at x = -b/(2a), y-intercept at (0, c).",
            final_wait=35.0,
        )