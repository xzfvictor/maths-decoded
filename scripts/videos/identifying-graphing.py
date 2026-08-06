"""
Manim scene for the lesson `identifying-graphing`
(topic `l9-a-quadratic-functions-equations`).

A quadratic has x² as the highest power; its graph is a smooth
U-shape (parabola). The animation walks through y = x² - 4x + 1
to find the vertex (2, -3) and y-intercept (0, 1), generalises to
y = a x² + b x + c (axis of symmetry, opens up if a > 0), and
rejects the confusion with a sharp V (absolute value).

Target duration: ~57 s (target scene length per spec).
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
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Identifying and graphing quadratics",
            "Smooth U-shape (parabola) — vertex, axis, y-intercept.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: y = x² - 4x + 1 (~14 s)
        # ──────────────────────────────────────────────────────────────────
        eq1 = make_equation_card(
            r"y \;=\; x^{2} - 4x + 1",
            color=BLUE_TERM, scale=1.2,
        )
        eq1.move_to(BAND_CHART_CENTER + UP * 1.3)

        head = Text("Vertex (turning point)", font_size=24, color=GREEN_OK)
        head.move_to(BAND_CHART_CENTER + UP * 0.1)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        vertex = MathTex(r"(2,\,-3)", color=GREEN_OK).scale(1.1)
        vertex.next_to(head, DOWN, buff=0.4)
        vertex_bg = BackgroundRectangle(vertex, color=BLACK, fill_opacity=1, buff=0.22)
        vertex_bg.move_to(vertex.get_center())

        yint_head = Text("y-intercept", font_size=22, color=TEAL_TERM)
        yint_head.next_to(vertex, DOWN, buff=0.5)
        yint_head_bg = BackgroundRectangle(yint_head, color=BLACK,
                                           fill_opacity=0.95, buff=0.13)
        yint_head_bg.move_to(yint_head.get_center())

        yint = MathTex(r"(0,\,1)", color=TEAL_TERM).scale(1.0)
        yint.next_to(yint_head, DOWN, buff=0.35)
        yint_bg = BackgroundRectangle(yint, color=BLACK, fill_opacity=1, buff=0.22)
        yint_bg.move_to(yint.get_center())

        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.4))
        self.wait(0.4)
        self.play(
            FadeIn(head_bg, run_time=0.3),
            FadeIn(head, run_time=0.7),
            FadeIn(vertex_bg, run_time=0.3),
            FadeIn(vertex, run_time=0.8),
        )
        self.wait(0.6)
        self.play(
            FadeIn(yint_head_bg, run_time=0.3),
            FadeIn(yint_head, run_time=0.6),
            FadeIn(yint_bg, run_time=0.3),
            FadeIn(yint, run_time=0.7),
        )
        self.wait(1.4)

        beat2 = VGroup(eq1, head, head_bg, vertex, vertex_bg,
                       yint_head, yint_head_bg, yint, yint_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — General shape and direction (~10 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(
            r"y \;=\; a\,x^{2} + b\,x + c",
            color=BLUE_TERM, scale=1.1,
        )
        general.move_to(BAND_CHART_CENTER + UP * 1.3)

        opens = MathTex(
            r"a > 0 \;\Rightarrow\; \text{opens up (smile)}",
            color=GREEN_OK,
        ).scale(0.9)
        opens.next_to(general, DOWN, buff=0.45)
        opens_bg = BackgroundRectangle(opens, color=BLACK, fill_opacity=1, buff=0.2)
        opens_bg.move_to(opens.get_center())

        frown = MathTex(
            r"a < 0 \;\Rightarrow\; \text{opens down (frown)}",
            color=ORANGE_TERM,
        ).scale(0.9)
        frown.next_to(opens, DOWN, buff=0.35)
        frown_bg = BackgroundRectangle(frown, color=BLACK, fill_opacity=1, buff=0.2)
        frown_bg.move_to(frown.get_center())

        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.4))
        self.wait(0.4)
        self.play(
            FadeIn(opens_bg, run_time=0.3),
            FadeIn(opens, run_time=0.9),
        )
        self.wait(0.5)
        self.play(
            FadeIn(frown_bg, run_time=0.3),
            FadeIn(frown, run_time=0.9),
        )
        self.wait(1.2)

        beat3 = VGroup(general, opens, opens_bg, frown, frown_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: confusing the parabola with a sharp V (~7 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Not this", font_size=24, color=RED_REJECT)
        head.move_to(BAND_CHART_CENTER + UP * 1.4)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        v_left = Line(
            np.array([-1.4, -0.6, 0.0]),
            np.array([0.0, 0.0, 0.0]),
            color=RED_REJECT, stroke_width=6,
        )
        v_right = Line(
            np.array([0.0, 0.0, 0.0]),
            np.array([1.4, -0.6, 0.0]),
            color=RED_REJECT, stroke_width=6,
        )
        v_group = VGroup(v_left, v_right).move_to(BAND_CHART_CENTER + DOWN * 0.2)
        v_group.set_z_index(3)

        v_lbl = MathTex(r"|x|", color=RED_REJECT).scale(1.3)
        v_lbl.next_to(v_group, DOWN, buff=0.35)
        v_lbl_bg = BackgroundRectangle(v_lbl, color=BLACK,
                                        fill_opacity=1, buff=0.2)
        v_lbl_bg.move_to(v_lbl.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.3),
            FadeIn(head, run_time=0.7),
        )
        self.wait(0.3)
        self.play(Create(v_left, run_time=0.6), Create(v_right, run_time=0.6))
        self.wait(0.3)
        self.play(
            FadeIn(v_lbl_bg, run_time=0.3),
            FadeIn(v_lbl, run_time=0.8),
        )
        self.wait(0.6)
        cross = Cross(v_lbl, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.6))
        self.wait(0.8)

        beat4 = VGroup(head, head_bg, v_group, v_lbl, v_lbl_bg, cross)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait = 28 s, total ≈ 57 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y \;=\; a\,x^{2} + b\,x + c",
            "Smooth parabola — vertex, axis of symmetry, y-intercept at (0, c).",
            final_wait=28.0,
        )