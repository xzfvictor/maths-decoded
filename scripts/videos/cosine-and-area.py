import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class CosineAndAreaScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Cosine rule and area",
            "Two formulas for non-right-angle triangles.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Draw a triangle and label sides & angle (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("A general triangle", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.35 + RIGHT * 4.5)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        # Triangle vertices.
        a = np.array([-2.6, -0.7, 0.0]) + BAND_CHART_CENTER
        b = np.array([2.4, -0.7, 0.0]) + BAND_CHART_CENTER
        c = np.array([-1.2, 1.0, 0.0]) + BAND_CHART_CENTER
        ab = Line(a, b, color=WHITE, stroke_width=4)
        bc = Line(b, c, color=WHITE, stroke_width=4)
        ca = Line(c, a, color=WHITE, stroke_width=4)
        # Labels.
        a_lbl = MathTex("A", color=BLUE_TERM).scale(0.9).next_to(a, DL, buff=0.15)
        b_lbl = MathTex("B", color=BLUE_TERM).scale(0.9).next_to(b, DR, buff=0.15)
        c_lbl = MathTex("C", color=BLUE_TERM).scale(0.9).next_to(c, UP, buff=0.15)
        # Side labels (a opposite A, b opposite B, c opposite C).
        side_a_lbl = MathTex("a", color=ORANGE_TERM).scale(1.0)
        side_a_lbl.move_to((b + c) / 2 + RIGHT * 0.25 + UP * 0.15)
        side_a_lbl_bg = BackgroundRectangle(side_a_lbl, color=BLACK,
                                             fill_opacity=0.9, buff=0.15)
        side_a_lbl_bg.move_to(side_a_lbl.get_center())
        side_b_lbl = MathTex("b", color=ORANGE_TERM).scale(1.0)
        side_b_lbl.move_to((a + c) / 2 + LEFT * 0.2)
        side_b_lbl_bg = BackgroundRectangle(side_b_lbl, color=BLACK,
                                             fill_opacity=0.9, buff=0.15)
        side_b_lbl_bg.move_to(side_b_lbl.get_center())
        side_c_lbl = MathTex("c", color=ORANGE_TERM).scale(1.0)
        side_c_lbl.move_to((a + b) / 2 + DOWN * 0.3)
        side_c_lbl_bg = BackgroundRectangle(side_c_lbl, color=BLACK,
                                             fill_opacity=0.9, buff=0.15)
        side_c_lbl_bg.move_to(side_c_lbl.get_center())

        triangle = VGroup(ab, bc, ca, a_lbl, b_lbl, c_lbl,
                          side_a_lbl, side_a_lbl_bg,
                          side_b_lbl, side_b_lbl_bg,
                          side_c_lbl, side_c_lbl_bg)

        self.play(Create(ab), Create(bc), Create(ca), run_time=1.6)
        self.play(FadeIn(a_lbl), FadeIn(b_lbl), FadeIn(c_lbl), run_time=0.6)
        self.play(FadeIn(side_a_lbl_bg), FadeIn(side_a_lbl),
                  FadeIn(side_b_lbl_bg), FadeIn(side_b_lbl),
                  FadeIn(side_c_lbl_bg), FadeIn(side_c_lbl), run_time=1.2)
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, triangle)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Cosine rule (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Cosine rule", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.35)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        rule = make_equation_card(
            r"a^{2} \;=\; b^{2} + c^{2} - 2bc\cos A",
            color=GREEN_OK, scale=1.1,
        )
        rule.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(rule, shift=UP * 0.2, run_time=1.8))
        self.wait(2.5)

        note = Text("Find a side given the opposite angle (or vice versa).",
                    font_size=20, color=WHITE)
        note.next_to(rule, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, rule, note, note_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Area formula (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Area with two sides", font_size=26, color=TEAL_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.35)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        area = make_equation_card(
            r"\text{Area} \;=\; \tfrac{1}{2}\,a\,b\,\sin C",
            color=TEAL_TERM, scale=1.2,
        )
        area.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(area, shift=UP * 0.2, run_time=1.8))
        self.wait(2.5)

        ex = make_equation_card(
            r"= \tfrac{1}{2}\,(3)(4)\,\sin 60^\circ \;\approx\; 5.20",
            color=GREEN_OK, scale=0.9,
        )
        ex.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        self.play(FadeIn(ex, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        beat4 = beat_group(head4, head4_bg, area, ex)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 99.4 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{2} = b^{2}+c^{2}-2bc\cos A, \quad "
            r"\text{Area} = \tfrac{1}{2}\,ab\sin C",
            "Cosine rule for sides; area uses the included angle.",
            final_wait=45.0,
        )