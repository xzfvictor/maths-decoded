import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class AngleBetweenLinesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Angle between two lines",
            "Use vectors and the dot product to find the 3D angle.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Draw two vectors from the origin (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Two vectors a and b", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.35)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        # Two vectors in screen space (we draw them as 2D for clarity).
        a_vec = np.array([2.0, 0.6, 0.0])
        b_vec = np.array([1.6, -0.5, 0.0])

        arrow_a = Arrow(ORIGIN, a_vec, color=BLUE_TERM, buff=0,
                        stroke_width=6, max_tip_length_to_length_ratio=0.15)
        arrow_b = Arrow(ORIGIN, b_vec, color=TEAL_TERM, buff=0,
                        stroke_width=6, max_tip_length_to_length_ratio=0.15)

        a_lbl = MathTex(r"\vec{a}", color=BLUE_TERM).scale(1.0)
        a_lbl.move_to(a_vec + RIGHT * 0.3 + UP * 0.2)
        a_lbl_bg = BackgroundRectangle(a_lbl, color=BLACK,
                                       fill_opacity=0.9, buff=0.15)
        a_lbl_bg.move_to(a_lbl.get_center())

        b_lbl = MathTex(r"\vec{b}", color=TEAL_TERM).scale(1.0)
        b_lbl.move_to(b_vec + RIGHT * 0.3 + DOWN * 0.25)
        b_lbl_bg = BackgroundRectangle(b_lbl, color=BLACK,
                                       fill_opacity=0.9, buff=0.15)
        b_lbl_bg.move_to(b_lbl.get_center())

        # Move origin to chart center.
        grp = VGroup(arrow_a, arrow_b, a_lbl_bg, a_lbl, b_lbl_bg, b_lbl)
        grp.scale(0.85)
        grp.move_to(BAND_CHART_CENTER + DOWN * 0.1)

        self.play(Create(arrow_a, run_time=1.0), Create(arrow_b, run_time=1.0))
        self.play(FadeIn(VGroup(a_lbl_bg, a_lbl, b_lbl_bg, b_lbl), run_time=0.8))
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, arrow_a, arrow_b,
                           a_lbl, a_lbl_bg, b_lbl, b_lbl_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The angle formula (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Dot product formula", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.35)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        formula = make_equation_card(
            r"\cos\theta \;=\; \dfrac{|\vec{a}\cdot\vec{b}|}{|\vec{a}|\,|\vec{b}|}",
            color=GREEN_OK, scale=1.0,
        )
        formula.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(formula, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        note = Text("theta is the angle between the vectors",
                    font_size=20, color=WHITE)
        note.next_to(formula, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, formula, note, note_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Concrete example: a=(1,2,3), b=(2,0,1) (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Worked example", font_size=26, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.35)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        v = make_equation_card(
            r"\vec{a}=(1,2,3),\; \vec{b}=(2,0,1)",
            color=ORANGE_TERM, scale=0.9,
        )
        v.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(v, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        ans = make_equation_card(
            r"\cos\theta = \dfrac{5}{\sqrt{14}\sqrt{5}},\quad"
            r" \theta \approx 53.3^\circ",
            color=GREEN_OK, scale=0.85,
        )
        ans.move_to(BAND_CHART_CENTER + DOWN * 0.7)
        self.play(FadeIn(ans, shift=UP * 0.2, run_time=1.4))
        self.wait(2.5)

        beat4 = beat_group(head4, head4_bg, v, ans)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 74.1 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\cos\theta = \dfrac{|\vec{a}\cdot\vec{b}|}{|\vec{a}|\,|\vec{b}|}",
            "Dot product over product of magnitudes gives cos of the angle.",
            final_wait=33.0,
        )