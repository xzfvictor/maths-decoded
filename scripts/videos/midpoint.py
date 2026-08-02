"""
Manim scene for the lesson `midpoint`
(topic `l9-a-gradient-midpoint-distance`).

Midpoint of a line segment between (x1, y1) and (x2, y2):
  M = ((x1 + x2)/2, (y1 + y2)/2)

Just average the x's and average the y's.

Target duration: ~71 s (matches the audio narration length of 71.42 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class MidpointScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Midpoint of a line interval",
            "Average the x's and average the y's",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example with the midpoint plotted (~17 s)
        # ──────────────────────────────────────────────────────────────────
        # Place a small segment on the chart with the midpoint marked.
        plane_center = LEFT * 0.4 + UP * 0.2
        SCALE = 0.55
        p1 = np.array([plane_center[0] + 2 * SCALE, plane_center[1] + 3 * SCALE, 0.0])
        p2 = np.array([plane_center[0] + 8 * SCALE, plane_center[1] + 7 * SCALE, 0.0])
        mid = np.array([plane_center[0] + 5 * SCALE, plane_center[1] + 5 * SCALE, 0.0])

        seg = Line(p1, p2, color=ORANGE_TERM, stroke_width=4)
        dot_p1 = Dot(p1, color=GREEN_OK, radius=0.09).set_z_index(3)
        dot_p2 = Dot(p2, color=GREEN_OK, radius=0.09).set_z_index(3)
        dot_mid = Dot(mid, color=GREEN_OK, radius=0.11).set_z_index(4)

        lbl_p1 = MathTex(r"(2, 3)", color=GREEN_OK).scale(0.75).next_to(dot_p1, DL, buff=0.12)
        lbl_p2 = MathTex(r"(8, 7)", color=GREEN_OK).scale(0.75).next_to(dot_p2, UR, buff=0.12)
        lbl_mid = MathTex(r"M(5, 5)", color=GREEN_OK).scale(0.75).next_to(dot_mid, DOWN, buff=0.18)

        # Two radius lines showing the midpoint is equidistant from both ends.
        r1 = DashedLine(p1, mid, color=TEAL_TERM, stroke_width=2).set_z_index(2)
        r2 = DashedLine(mid, p2, color=TEAL_TERM, stroke_width=2).set_z_index(2)

        self.play(Create(seg, run_time=1.2))
        self.play(
            FadeIn(dot_p1, scale=0.5, run_time=0.5),
            FadeIn(dot_p2, scale=0.5, run_time=0.5),
        )
        self.play(
            FadeIn(lbl_p1, run_time=0.5),
            FadeIn(lbl_p2, run_time=0.5),
        )
        self.wait(1.0)
        self.play(Create(r1, run_time=1.0), Create(r2, run_time=1.0))
        self.play(
            FadeIn(dot_mid, scale=0.5, run_time=0.6),
            FadeIn(lbl_mid, run_time=0.6),
        )
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(seg, dot_p1, dot_p2, dot_mid, lbl_p1, lbl_p2,
                           lbl_mid, r1, r2), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Plug into formula: x=5, y=5 (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Average the two x's and the two y's:",
                    font_size=22, color=WHITE)
        head.move_to(BAND_CHART_CENTER + UP * 1.4)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        line1 = MathTex(
            r"M_{x} \;=\; \dfrac{2 + 8}{2} \;=\; 5",
            color=BLUE_TERM,
        ).scale(1.05)
        line1.move_to(BAND_CHART_CENTER + UP * 0.4)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=1, buff=0.25)
        line1_bg.move_to(line1.get_center())

        line2 = MathTex(
            r"M_{y} \;=\; \dfrac{3 + 7}{2} \;=\; 5",
            color=TEAL_TERM,
        ).scale(1.05)
        line2.next_to(line1, DOWN, buff=0.45)
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=1, buff=0.25)
        line2_bg.move_to(line2.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
        )
        self.wait(1.0)
        self.play(FadeIn(line1_bg, run_time=0.4), Write(line1, run_time=1.5))
        self.wait(1.0)
        self.play(FadeIn(line2_bg, run_time=0.4), Write(line2, run_time=1.5))
        self.wait(1.5)

        result = MathTex(r"\therefore\; M \;=\; (5, 5)", color=GREEN_OK).scale(1.3)
        result.next_to(line2, DOWN, buff=0.5)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=1, buff=0.28)
        result_bg.move_to(result.get_center())
        self.play(FadeIn(result_bg, run_time=0.4), Write(result, run_time=1.5))
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(head, head_bg, line1, line1_bg, line2, line2_bg,
                           result, result_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — General formula (~10 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("For any two points:", font_size=22, color=WHITE)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        formula = MathTex(
            r"M \;=\; \left(\dfrac{x_{1} + x_{2}}{2}, \ \dfrac{y_{1} + y_{2}}{2}\right)",
        ).scale(1.05)
        formula.move_to(BAND_CHART_CENTER + UP * 0.0)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.3)
        formula_bg.move_to(formula.get_center())
        formula_box = SurroundingRectangle(formula, color=GREEN_OK, buff=0.3, stroke_width=3)

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
        )
        self.wait(1.0)
        self.play(FadeIn(formula_bg, run_time=0.4), Write(formula, run_time=2.0))
        self.play(Create(formula_box, run_time=1.0))
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(head2, head2_bg, formula, formula_bg, formula_box),
                    run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~29 s, total ≈ 71 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"M \;=\; \left(\dfrac{x_{1} + x_{2}}{2}, \ \dfrac{y_{1} + y_{2}}{2}\right)",
            "Equidistant from both endpoints.",
            final_wait=26.0,
        )