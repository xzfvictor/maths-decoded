"""
Manim scene for the lesson `pyramids-and-cones`
(topic `l10a-am-pyramids-cones-spheres`).

Pyramid and cone volumes: V = (1/3) × base area × height. Animation
shows a pyramid and a cone, then generalises. Reject the mistake of
forgetting the 1/3 factor.

Target duration: ~93 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *
import numpy as np


class PyramidsAndConesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Pyramids and cones",
            "Volume is one-third the prism around them",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Show a square pyramid with V = (1/3) Ah (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        # Square pyramid: apex above centre of square base.
        base_size = 1.4
        height = 2.0
        apex = np.array([0, height / 2 + 0.2, 0])
        base_pts = [
            np.array([base_size, -height / 2, 0]),
            np.array([-base_size, -height / 2, 0]),
            np.array([-base_size, -height / 2 - 0.3, 0]),  # back
            np.array([base_size, -height / 2 - 0.3, 0]),
        ]
        base_poly = Polygon(*base_pts, color=BLUE_TERM, fill_color=BLUE_TERM, fill_opacity=0.25, stroke_width=3)
        # Front edges from apex to each base corner (visible ones).
        e1 = Line(apex, base_pts[0], color=BLUE_TERM, stroke_width=3)
        e2 = Line(apex, base_pts[1], color=BLUE_TERM, stroke_width=3)
        e3 = Line(apex, base_pts[2], color=BLUE_TERM, stroke_width=3)
        e4 = Line(apex, base_pts[3], color=BLUE_TERM, stroke_width=3)
        # Base edges (top side of the rectangle as drawn).
        b1 = Line(base_pts[0], base_pts[3], color=BLUE_TERM, stroke_width=3)
        b2 = Line(base_pts[0], base_pts[1], color=BLUE_TERM, stroke_width=3)
        b3 = Line(base_pts[2], base_pts[1], color=BLUE_TERM, stroke_width=3)
        b4 = Line(base_pts[2], base_pts[3], color=BLUE_TERM, stroke_width=3)

        pyramid = VGroup(base_poly, e1, e2, e3, e4, b1, b2, b3, b4)
        pyramid.move_to(BAND_CHART_CENTER + LEFT * 3.0 + DOWN * 0.1)
        beat_2 = beat_group(beat_2, pyramid)

        # Label h.
        h_arrow = DoubleArrow(
            start=apex + np.array([0.5, 0, 0]),
            end=np.array([0.5, -height / 2 - 0.3, 0]),
            color=ORANGE_TERM,
            buff=0.0,
            stroke_width=4,
        ).shift(LEFT * 3.0)
        h_lbl = MathTex("h", color=ORANGE_TERM).scale(1.0)
        h_lbl.next_to(h_arrow, RIGHT, buff=0.2)
        h_lbl_bg = BackgroundRectangle(h_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        h_lbl_bg.move_to(h_lbl.get_center())
        beat_2 = beat_group(beat_2, h_arrow, h_lbl, h_lbl_bg)

        # Volume formula.
        V_eq = MathTex(r"V = \dfrac{1}{3}\, A\, h", color=GREEN_OK).scale(1.1)
        V_eq.move_to(BAND_CHART_CENTER + RIGHT * 2.5 + UP * 0.5)
        V_eq_bg = BackgroundRectangle(V_eq, color=BLACK, fill_opacity=1, buff=0.25)
        V_eq_bg.move_to(V_eq.get_center())
        beat_2 = beat_group(beat_2, V_eq, V_eq_bg)

        self.play(FadeIn(pyramid, run_time=1.5))
        self.wait(1.0)
        self.play(Create(h_arrow), run_time=1.0)
        self.play(FadeIn(h_lbl_bg, run_time=0.3), FadeIn(h_lbl, run_time=0.7))
        self.wait(1.0)
        self.play(FadeIn(V_eq_bg, run_time=0.4), Write(V_eq, run_time=1.6))
        self.wait(1.5)
        # A label.
        A_lbl = Text("A = base area", font_size=22, color=BLUE_TERM)
        A_lbl.next_to(V_eq, DOWN, buff=0.4)
        A_lbl_bg = BackgroundRectangle(A_lbl, color=BLACK, fill_opacity=0.95, buff=0.15)
        A_lbl_bg.move_to(A_lbl.get_center())
        beat_2 = beat_group(beat_2, A_lbl, A_lbl_bg)
        self.play(FadeIn(A_lbl_bg, run_time=0.3), FadeIn(A_lbl, run_time=0.8))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Cone with same formula (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        cone = Cone(
            base_radius=1.2,
            height=2.2,
            direction=UP,
            show_base=True,
            fill_color=BLUE_TERM,
            fill_opacity=0.3,
            stroke_width=3,
            checkerboard_colors=False,
        )
        cone.move_to(BAND_CHART_CENTER + LEFT * 3.0 + DOWN * 0.3)
        beat_3 = beat_group(beat_3, cone)

        V_eq2 = MathTex(r"V = \dfrac{1}{3}\, \pi r^{2}\, h", color=GREEN_OK).scale(1.1)
        V_eq2.move_to(BAND_CHART_CENTER + RIGHT * 2.5 + UP * 0.6)
        V_eq2_bg = BackgroundRectangle(V_eq2, color=BLACK, fill_opacity=1, buff=0.25)
        V_eq2_bg.move_to(V_eq2.get_center())
        beat_3 = beat_group(beat_3, V_eq2, V_eq2_bg)

        self.play(FadeIn(cone, run_time=1.6))
        self.wait(1.0)
        self.play(FadeIn(V_eq2_bg, run_time=0.4), Write(V_eq2, run_time=1.6))
        self.wait(1.5)
        # Sub note.
        note = Text("A = πr² (circular base)", font_size=22, color=BLUE_TERM)
        note.next_to(V_eq2, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        beat_3 = beat_group(beat_3, note, note_bg)
        self.play(FadeIn(note_bg, run_time=0.3), FadeIn(note, run_time=0.8))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: forgetting the 1/3 factor (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(r"V = A\,h\ \text{?}", color=RED_REJECT).scale(1.4)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.3)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.4),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        expl = Text(
            "Without the 1/3, you have the prism's volume, not the pyramid's.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        expl_bg = BackgroundRectangle(expl, color=BLACK, fill_opacity=0.95, buff=0.18)
        expl_bg.move_to(expl.get_center())
        beat_4 = beat_group(beat_4, expl, expl_bg)
        self.play(FadeIn(expl_bg, run_time=0.3), FadeIn(expl, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~42 s, total ≈ 93 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"V_{\text{pyramid}} = V_{\text{cone}} = \dfrac{1}{3}\times\text{base area}\times h",
            "Same shape rule — always one-third of the prism around it.",
            final_wait=42.0,
        )
