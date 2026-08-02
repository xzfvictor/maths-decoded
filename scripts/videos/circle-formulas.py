"""
Manim scene for the lesson `circle-formulas`
(topic `l8-m-circumference-area-circle`).

The two key circle formulas: circumference C = 2πr and area A = πr².
The scene draws a circle, labels r and d, then generalises the formulas
and rejects the common mistake of squaring the diameter instead of
the radius.

Target duration: ~109 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class CircleFormulasScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Circumference and area of a circle",
            "C = 2πr,  A = πr²",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Draw a circle, label radius r and diameter d (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Build ALL beat-2 mobjects FIRST and add them to beat_2 BEFORE
        # any animations run. The previous version added c_eq to beat_2
        # *after* the FadeIn play, which leaked the C = 2πr card into
        # beat 3 because the FadeOut was never guaranteed to cover it.
        beat_2 = beat_group()
        circle = Circle(radius=1.6, color=BLUE_TERM, stroke_width=4)
        circle.move_to(BAND_CHART_CENTER + UP * 0.4)
        beat_2 = beat_group(beat_2, circle)

        centre_dot = Dot(circle.get_center(), color=BLUE_TERM, radius=0.06)
        edge_dot = Dot(circle.get_right(), color=BLUE_TERM, radius=0.06)
        left_dot = Dot(circle.get_left(), color=BLUE_TERM, radius=0.06)
        beat_2 = beat_group(beat_2, centre_dot, edge_dot, left_dot)

        # Radius arrow: centre → right edge.
        r_arrow = Arrow(
            start=circle.get_center(),
            end=circle.get_right(),
            color=BLUE_TERM,
            buff=0.05,
            stroke_width=5,
        )
        r_lbl = MathTex("r", color=BLUE_TERM).scale(1.0)
        r_lbl.next_to(r_arrow, UP, buff=0.15)
        r_lbl_bg = BackgroundRectangle(r_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        r_lbl_bg.move_to(r_lbl.get_center())
        beat_2 = beat_group(beat_2, r_arrow, r_lbl, r_lbl_bg)

        # Diameter arrow: left edge → right edge (passing through centre).
        d_arrow = DoubleArrow(
            start=circle.get_left(),
            end=circle.get_right(),
            color=ORANGE_TERM,
            buff=0.05,
            stroke_width=5,
        )
        d_arrow.shift(DOWN * 0.4)
        d_lbl = MathTex("d = 2r", color=ORANGE_TERM).scale(1.0)
        d_lbl.next_to(d_arrow, DOWN, buff=0.15)
        d_lbl_bg = BackgroundRectangle(d_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        d_lbl_bg.move_to(d_lbl.get_center())
        beat_2 = beat_group(beat_2, d_arrow, d_lbl, d_lbl_bg)

        # C formula, anchored next to the circle. Built BEFORE the
        # animations so the final beat_2 FadeOut is guaranteed to clean
        # it up. Anchor well clear of beat 3's disc + A = πr² card
        # (BAND_CHART_CENTER + UP*0.5).
        c_eq = MathTex(r"C = 2 \pi r", color=GREEN_OK).scale(1.0)
        c_eq.next_to(circle, LEFT, buff=0.6).shift(UP * 0.2)
        c_eq_bg = BackgroundRectangle(c_eq, color=BLACK, fill_opacity=1, buff=0.2)
        c_eq_bg.move_to(c_eq.get_center())
        beat_2 = beat_group(beat_2, c_eq, c_eq_bg)

        self.play(Create(circle), run_time=1.4)
        self.play(FadeIn(centre_dot, run_time=0.3), FadeIn(edge_dot, run_time=0.3))
        self.play(Create(r_arrow, run_time=1.0))
        self.play(FadeIn(r_lbl_bg, run_time=0.3), FadeIn(r_lbl, run_time=0.8))
        self.wait(1.5)

        self.play(FadeIn(left_dot, run_time=0.3))
        self.play(Create(d_arrow, run_time=1.0))
        self.play(FadeIn(d_lbl_bg, run_time=0.3), FadeIn(d_lbl, run_time=0.8))
        self.wait(3.0)

        self.play(FadeIn(c_eq_bg, run_time=0.4), Write(c_eq, run_time=1.6))
        self.wait(3.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Area A = πr², with shaded disc and numeric example (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = VGroup()
        disc = Circle(radius=1.8, color=BLUE_TERM, stroke_width=3,
                      fill_color=BLUE_TERM, fill_opacity=0.25)
        disc.move_to(BAND_CHART_CENTER + UP * 0.5)
        beat_3.add(disc)
        self.play(FadeIn(disc, run_time=1.0))
        self.wait(1.0)

        a_eq = make_equation_card(r"A = \pi r^{2}", color=BLUE_TERM, scale=1.5)
        a_eq.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in a_eq:
            m.set_z_index(3)
        beat_3.add(a_eq)
        self.play(FadeIn(a_eq, shift=UP * 0.2, run_time=1.5))
        self.wait(2.0)

        # Numerical: r = 3, A = 9π.
        num = MathTex(r"r = 3 \;\Rightarrow\; A = \pi \times 3^{2} = 9\pi\ \text{cm}^{2}", color=GREEN_OK).scale(0.95)
        num.next_to(a_eq, DOWN, buff=0.55)
        num_bg = BackgroundRectangle(num, color=BLACK, fill_opacity=1, buff=0.2)
        num_bg.move_to(num.get_center())
        beat_3.add(num, num_bg)
        self.play(FadeIn(num_bg, run_time=0.4), Write(num, run_time=2.0))
        self.wait(3.0)
        self.play(FadeOut(beat_3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: A = π d² is WRONG (answer 4× too big) (~15 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = VGroup()
        wrong_eq = MathTex(
            r"A = \pi d^{2}\ \text{?}",
            color=RED_REJECT,
        ).scale(1.2)
        wrong_eq.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_eq_bg = BackgroundRectangle(wrong_eq, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_eq_bg.move_to(wrong_eq.get_center())
        beat_4.add(wrong_eq, wrong_eq_bg)
        self.play(FadeIn(wrong_eq_bg, run_time=0.4), Write(wrong_eq, run_time=1.5))
        cross = Cross(wrong_eq, color=RED_REJECT, stroke_width=5)
        beat_4.add(cross)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.5)

        explain = Text(
            "If d = 7, then A = π × 7² = 49π — but the true answer (r = 3.5) is only 12.25π.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong_eq, DOWN, buff=0.5)
        explain_bg = BackgroundRectangle(explain, color=BLACK, fill_opacity=0.95, buff=0.18)
        explain_bg.move_to(explain.get_center())
        beat_4.add(explain, explain_bg)
        self.play(FadeIn(explain_bg, run_time=0.4), FadeIn(explain, run_time=1.4))
        self.wait(3.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~42 s, total ≈ 109 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"C = 2\pi r, \quad A = \pi r^{2}",
            "Always square the radius — never the diameter.",
            final_wait=42.0,
        )
