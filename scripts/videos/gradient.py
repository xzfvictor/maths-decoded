"""
Manim scene for the lesson `gradient`
(topic `l9-a-gradient-midpoint-distance`).

Gradient (slope) of a line through (x1, y1) and (x2, y2):
  m = (y2 - y1) / (x2 - x1)

Rises (vertical change) over runs (horizontal change).

Target duration: ~76 s (matches the audio narration length of 75.74 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class GradientScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Gradient of a line segment",
            "Rise over run: vertical change ÷ horizontal change",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example with the rise/run triangle (~17 s)
        # ──────────────────────────────────────────────────────────────────
        # Place a small right triangle on the chart, showing rise and run.
        plane_center = LEFT * 0.6 + UP * 0.2
        SCALE = 0.45
        p1 = np.array([plane_center[0] + 1 * SCALE, plane_center[1] + 3 * SCALE, 0.0])
        p2 = np.array([plane_center[0] + 5 * SCALE, plane_center[1] + 11 * SCALE, 0.0])
        corner = np.array([plane_center[0] + 5 * SCALE, plane_center[1] + 3 * SCALE, 0.0])

        run_line = Line(p1, corner, color=BLUE_TERM, stroke_width=4)
        rise_line = Line(corner, p2, color=TEAL_TERM, stroke_width=4)
        hyp = Line(p1, p2, color=ORANGE_TERM, stroke_width=5)
        right_angle = Square(side_length=0.22, color=WHITE, stroke_width=2).move_to(corner + LEFT * 0.11 + UP * 0.11)

        dot_p1 = Dot(p1, color=GREEN_OK, radius=0.09).set_z_index(3)
        dot_p2 = Dot(p2, color=GREEN_OK, radius=0.09).set_z_index(3)

        lbl_p1 = MathTex(r"(1, 3)", color=GREEN_OK).scale(0.7).next_to(dot_p1, DL, buff=0.12)
        lbl_p2 = MathTex(r"(5, 11)", color=GREEN_OK).scale(0.7).next_to(dot_p2, UR, buff=0.12)
        lbl_run = MathTex("run = 4", color=BLUE_TERM).scale(0.8).next_to(run_line, DOWN, buff=0.2)
        lbl_rise = MathTex("rise = 8", color=TEAL_TERM).scale(0.8).next_to(rise_line, RIGHT, buff=0.18)

        self.play(
            Create(run_line, run_time=1.0),
            Create(rise_line, run_time=1.0),
            Create(right_angle, run_time=0.6),
        )
        self.play(Create(hyp, run_time=1.2))
        self.play(
            FadeIn(dot_p1, scale=0.5, run_time=0.5),
            FadeIn(dot_p2, scale=0.5, run_time=0.5),
        )
        self.play(
            FadeIn(lbl_p1, run_time=0.5),
            FadeIn(lbl_p2, run_time=0.5),
            FadeIn(lbl_run, run_time=0.5),
            FadeIn(lbl_rise, run_time=0.5),
        )
        self.wait(3.0)

        self.play(
            FadeOut(VGroup(run_line, rise_line, hyp, right_angle,
                           dot_p1, dot_p2, lbl_p1, lbl_p2,
                           lbl_run, lbl_rise), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Plug into formula: 8 / 4 = 2 (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Gradient = rise ÷ run:", font_size=22, color=WHITE)
        head.move_to(BAND_CHART_CENTER + UP * 1.4)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        line1 = MathTex(
            r"m \;=\; \dfrac{11 - 3}{5 - 1}",
            color=BLUE_TERM,
        ).scale(1.1)
        line1.move_to(BAND_CHART_CENTER + UP * 0.5)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=1, buff=0.25)
        line1_bg.move_to(line1.get_center())

        line2 = MathTex(r"= \dfrac{8}{4} \;=\; 2", color=GREEN_OK).scale(1.3)
        line2.next_to(line1, DOWN, buff=0.55)
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=1, buff=0.3)
        line2_bg.move_to(line2.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
        )
        self.wait(1.0)
        self.play(FadeIn(line1_bg, run_time=0.4), Write(line1, run_time=1.6))
        self.wait(1.5)
        self.play(FadeIn(line2_bg, run_time=0.4), Write(line2, run_time=1.6))
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(head, head_bg, line1, line1_bg, line2, line2_bg),
                    run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — General formula + sign convention (~12 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("For any two points:", font_size=22, color=WHITE)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        formula = MathTex(
            r"m \;=\; \dfrac{y_{2} - y_{1}}{x_{2} - x_{1}}",
        ).scale(1.1)
        formula.move_to(BAND_CHART_CENTER + UP * 0.1)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.3)
        formula_bg.move_to(formula.get_center())
        formula_box = SurroundingRectangle(formula, color=GREEN_OK, buff=0.3, stroke_width=3)

        sign_note = Text(
            "m > 0 goes up to the right; m < 0 goes down.",
            font_size=20, color=GREEN_OK,
        ).next_to(formula_box, DOWN, buff=0.35)
        sign_note_bg = BackgroundRectangle(sign_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        sign_note_bg.move_to(sign_note.get_center())

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
        )
        self.wait(1.0)
        self.play(FadeIn(formula_bg, run_time=0.4), Write(formula, run_time=1.8))
        self.play(Create(formula_box, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(sign_note_bg, run_time=0.4), FadeIn(sign_note, run_time=1.0))
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(head2, head2_bg, formula, formula_bg, formula_box,
                           sign_note, sign_note_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~30 s, total ≈ 76 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"m \;=\; \dfrac{y_{2} - y_{1}}{x_{2} - x_{1}}",
            "Rise over run: how much y changes per unit of x.",
            final_wait=28.0,
        )