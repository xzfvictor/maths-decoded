"""
Manim scene for the lesson `distance`
(topic `l9-a-gradient-midpoint-distance`).

Distance between two points (x1, y1) and (x2, y2):
  d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

A right-triangle picture (legs = horizontal/vertical change, hypotenuse =
distance) drives the Pythagoras intuition home.

Target duration: ~73 s (matches the audio narration length of 73.40 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class DistanceScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Distance between two points",
            "Pythagoras: legs² + legs² = hypotenuse²",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Show the two points and the right triangle (~17 s)
        # ──────────────────────────────────────────────────────────────────
        # Build a small coordinate plane on the right side of the screen.
        plane_center = RIGHT * 2.4 + UP * 0.2

        # Triangle vertices: P1=(1,2), P2=(4,6), right corner=(4,2).
        # Use a 0.5 unit scale; P1→(screen (0.5, 1.0)), P2→(2.0, 3.0), C→(2.0, 1.0).
        SCALE = 0.5
        p1 = np.array([plane_center[0] + 1 * SCALE, plane_center[1] + 2 * SCALE, 0.0])
        p2 = np.array([plane_center[0] + 4 * SCALE, plane_center[1] + 6 * SCALE, 0.0])
        corner = np.array([plane_center[0] + 4 * SCALE, plane_center[1] + 2 * SCALE, 0.0])

        # Draw the three line segments.
        leg_h = Line(p1, corner, color=BLUE_TERM, stroke_width=4)
        leg_v = Line(corner, p2, color=TEAL_TERM, stroke_width=4)
        hyp = Line(p1, p2, color=ORANGE_TERM, stroke_width=5)
        right_angle = Square(side_length=0.22, color=WHITE, stroke_width=2).move_to(corner + LEFT * 0.11 + UP * 0.11)

        # Dot for each point.
        dot_p1 = Dot(p1, color=GREEN_OK, radius=0.09).set_z_index(3)
        dot_p2 = Dot(p2, color=GREEN_OK, radius=0.09).set_z_index(3)

        # Point labels.
        lbl_p1 = MathTex(r"(1, 2)", color=GREEN_OK).scale(0.7).next_to(dot_p1, DL, buff=0.12)
        lbl_p2 = MathTex(r"(4, 6)", color=GREEN_OK).scale(0.7).next_to(dot_p2, UR, buff=0.12)
        lbl_h = MathTex("3", color=BLUE_TERM).scale(0.8).next_to(leg_h, DOWN, buff=0.18)
        lbl_v = MathTex("4", color=TEAL_TERM).scale(0.8).next_to(leg_v, RIGHT, buff=0.18)
        lbl_hyp = MathTex("d", color=ORANGE_TERM).scale(0.9).next_to(hyp.get_center(), UL, buff=0.18)

        self.play(
            Create(leg_h, run_time=1.0),
            Create(leg_v, run_time=1.0),
            Create(right_angle, run_time=0.6),
        )
        self.play(Create(hyp, run_time=1.2))
        self.wait(0.5)
        self.play(
            FadeIn(dot_p1, scale=0.5, run_time=0.6),
            FadeIn(dot_p2, scale=0.5, run_time=0.6),
        )
        self.play(
            FadeIn(lbl_p1, run_time=0.5),
            FadeIn(lbl_p2, run_time=0.5),
            FadeIn(lbl_h, run_time=0.5),
            FadeIn(lbl_v, run_time=0.5),
            FadeIn(lbl_hyp, run_time=0.5),
        )
        self.wait(3.0)

        self.play(
            FadeOut(VGroup(leg_h, leg_v, hyp, right_angle,
                           dot_p1, dot_p2, lbl_p1, lbl_p2,
                           lbl_h, lbl_v, lbl_hyp), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Plug into Pythagoras: 3² + 4² = d² → d = 5 (~16 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Apply Pythagoras:", font_size=22, color=WHITE)
        head.move_to(BAND_CHART_CENTER + UP * 1.4)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        line1 = MathTex(r"3^{2} + 4^{2} \;=\; d^{2}", color=BLUE_TERM).scale(1.1)
        line1.move_to(BAND_CHART_CENTER + UP * 0.5)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=1, buff=0.25)
        line1_bg.move_to(line1.get_center())

        line2 = MathTex(r"9 + 16 \;=\; d^{2}", color=TEAL_TERM).scale(1.1)
        line2.next_to(line1, DOWN, buff=0.45)
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=1, buff=0.25)
        line2_bg.move_to(line2.get_center())

        line3 = MathTex(r"d \;=\; \sqrt{25} \;=\; 5", color=GREEN_OK).scale(1.3)
        line3.next_to(line2, DOWN, buff=0.5)
        line3_bg = BackgroundRectangle(line3, color=BLACK, fill_opacity=1, buff=0.28)
        line3_bg.move_to(line3.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
        )
        self.wait(1.0)
        self.play(FadeIn(line1_bg, run_time=0.4), Write(line1, run_time=1.5))
        self.wait(1.5)
        self.play(FadeIn(line2_bg, run_time=0.4), Write(line2, run_time=1.5))
        self.wait(1.5)
        self.play(FadeIn(line3_bg, run_time=0.4), Write(line3, run_time=1.6))
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(head, head_bg, line1, line1_bg, line2, line2_bg,
                           line3, line3_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — General formula (~12 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("General formula for any two points:",
                     font_size=22, color=WHITE)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        formula = MathTex(
            r"d \;=\; \sqrt{(x_{2} - x_{1})^{2} + (y_{2} - y_{1})^{2}}",
        ).scale(1.05)
        formula.move_to(BAND_CHART_CENTER + UP * 0.0)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.3)
        formula_bg.move_to(formula.get_center())
        formula_box = SurroundingRectangle(formula, color=GREEN_OK, buff=0.3, stroke_width=3)

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
        )
        self.wait(1.5)
        self.play(FadeIn(formula_bg, run_time=0.4), Write(formula, run_time=1.8))
        self.play(Create(formula_box, run_time=1.0))
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(head2, head2_bg, formula, formula_bg, formula_box),
                    run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~30 s, total ≈ 73 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"d \;=\; \sqrt{(x_{2} - x_{1})^{2} + (y_{2} - y_{1})^{2}}",
            "Pythagoras with horizontal change and vertical change.",
            final_wait=27.0,
        )