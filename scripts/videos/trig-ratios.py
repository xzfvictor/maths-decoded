"""
Manim scene for the lesson `trig-ratios`
(topic `l9-m-pythagoras-trigonometry`).

The three trigonometric ratios — sin, cos, tan — pair the sides of
a right triangle with an acute angle θ. The scene labels the
hypotenuse, opposite, and adjacent sides on a 30-60-90 triangle,
generalises the three ratios, and rejects the mistake of mixing
up which side is which.

Render target: ~14 s audio + 20 s final wait.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class TrigRatiosScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Trigonometric ratios",
            "sin, cos, tan — pair the sides of a right triangle with angle θ.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Label the sides: hypotenuse / opposite / adjacent
        # ──────────────────────────────────────────────────────────────────
        # Right triangle: right angle at A, acute angle θ at B.
        A = np.array([-2.0, -0.6, 0.0])
        B = np.array([1.4, -0.6, 0.0])
        C = np.array([-2.0, 2.2, 0.0])
        tri = Polygon(A, B, C, color=BLUE_TERM, stroke_width=4)
        tri.move_to(BAND_CHART_CENTER + UP * 0.3)

        right_mark = Square(side_length=0.28, color=BLUE_TERM, stroke_width=2)
        right_mark.move_to(A + RIGHT * 0.18 + UP * 0.18)

        theta_lbl = MathTex(r"\theta", color=ORANGE_TERM).scale(0.95)
        theta_lbl.next_to(B, DOWN, buff=0.2)
        theta_bg = BackgroundRectangle(theta_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        theta_bg.move_to(theta_lbl.get_center())

        # Hypotenuse label, on the slanted side.
        hyp_lbl = MathTex(r"\text{hyp}", color=GREEN_OK).scale(0.85)
        hyp_lbl.next_to(tri.get_center(), UR, buff=0.15).shift(LEFT * 0.1)
        hyp_bg = BackgroundRectangle(hyp_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        hyp_bg.move_to(hyp_lbl.get_center())

        # Opposite label (vertical leg).
        opp_lbl = MathTex(r"\text{opp}", color=TEAL_TERM).scale(0.85)
        opp_lbl.next_to(tri, LEFT, buff=0.25)
        opp_bg = BackgroundRectangle(opp_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        opp_bg.move_to(opp_lbl.get_center())

        # Adjacent label (horizontal leg).
        adj_lbl = MathTex(r"\text{adj}", color=BLUE_TERM).scale(0.85)
        adj_lbl.next_to(tri, DOWN, buff=0.3)
        adj_bg = BackgroundRectangle(adj_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        adj_bg.move_to(adj_lbl.get_center())

        self.play(Create(tri, run_time=1.0))
        self.play(Create(right_mark, run_time=0.4))
        self.wait(0.2)
        self.play(FadeIn(theta_bg, run_time=0.3), FadeIn(theta_lbl, run_time=0.5))
        self.wait(0.3)
        self.play(FadeIn(hyp_bg, run_time=0.3), FadeIn(hyp_lbl, run_time=0.5))
        self.wait(0.3)
        self.play(FadeIn(opp_bg, run_time=0.3), FadeIn(opp_lbl, run_time=0.5))
        self.wait(0.3)
        self.play(FadeIn(adj_bg, run_time=0.3), FadeIn(adj_lbl, run_time=0.5))
        self.wait(1.0)

        # Concrete: sin 30° = 5/10 = 0.5 with hypotenuse 10 and θ = 30°.
        concrete = MathTex(
            r"\sin 30^\circ = \dfrac{5}{10} = 0.5",
            color=GREEN_OK,
        ).scale(0.9)
        concrete.next_to(tri, DOWN, buff=0.55)
        concrete_bg = BackgroundRectangle(concrete, color=BLACK, fill_opacity=1, buff=0.18)
        concrete_bg.move_to(concrete.get_center())
        self.play(FadeIn(concrete_bg, run_time=0.4), Write(concrete, run_time=1.3))
        self.wait(0.8)

        beat2 = beat_group(
            tri, right_mark, theta_lbl, theta_bg,
            hyp_lbl, hyp_bg, opp_lbl, opp_bg,
            adj_lbl, adj_bg, concrete, concrete_bg,
        )
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise the three ratios
        # ──────────────────────────────────────────────────────────────────
        ratios = VGroup(
            MathTex(r"\sin\theta = \dfrac{\text{opp}}{\text{hyp}}", color=BLUE_TERM).scale(0.9),
            MathTex(r"\cos\theta = \dfrac{\text{adj}}{\text{hyp}}", color=TEAL_TERM).scale(0.9),
            MathTex(r"\tan\theta = \dfrac{\text{opp}}{\text{adj}}", color=ORANGE_TERM).scale(0.9),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        ratios.move_to(BAND_CHART_CENTER + UP * 0.3)
        ratios_bg = BackgroundRectangle(ratios, color=BLACK, fill_opacity=1, buff=0.22)
        ratios_bg.move_to(ratios.get_center())
        self.play(FadeIn(ratios_bg, run_time=0.4), FadeIn(ratios, run_time=1.8))
        self.wait(2.0)

        beat3 = beat_group(ratios, ratios_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: swapping opp and adj
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(
            r"\sin\theta = \dfrac{\text{adj}}{\text{hyp}} \;\;\text{?}",
            color=RED_REJECT,
        ).scale(0.95)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.4)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.2)
        wrong_bg.move_to(wrong.get_center())
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.2))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.6))
        self.wait(0.6)

        fix = Text("sin uses opposite, not adjacent.",
                   font_size=22, color=GREEN_OK)
        fix.next_to(wrong, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.15)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.3), FadeIn(fix, run_time=0.8))
        self.wait(0.6)

        beat4 = beat_group(wrong, wrong_bg, cross, fix, fix_bg)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"\sin\theta = \frac{\text{opp}}{\text{hyp}}",
            "Pick the ratio that has the two sides you know.",
            final_wait=75.0,
        )
