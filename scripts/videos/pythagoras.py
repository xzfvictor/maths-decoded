"""
Manim scene for the lesson `pythagoras`
(topic `l9-m-pythagoras-trigonometry`).

Pythagoras' theorem in spatial problems: a² + b² = c² for any
right-angled triangle. The scene verifies the 6-8-10 triangle,
generalises the rule with two rearrangements, and rejects the
common mistake of applying it without a right angle.

Target duration: ~61 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class PythagorasScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Pythagoras' theorem",
            "a² + b² = c² for any right-angled triangle.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — 6-8-10 right triangle, verify 36 + 64 = 100 (~18 s)
        # ──────────────────────────────────────────────────────────────────
        # Right-angle corner at A, leg a = 8 horizontal, leg b = 6 vertical.
        A = np.array([-2.0, -0.8, 0.0])
        B = np.array([2.0, -0.8, 0.0])    # 8 across (scaled by 0.5)
        C = np.array([-2.0, 2.2, 0.0])    # 6 up
        tri = Polygon(A, B, C, color=BLUE_TERM, stroke_width=4)
        tri.move_to(BAND_CHART_CENTER + UP * 0.4)

        right_mark = Square(side_length=0.3, color=BLUE_TERM, stroke_width=2)
        right_mark.move_to(A + RIGHT * 0.15 + UP * 0.15)
        right_mark.shift(UP * 0.4 * 0)

        a_lbl = MathTex("a = 8", color=BLUE_TERM).scale(0.9)
        a_lbl.next_to(tri, DOWN, buff=0.3)
        a_bg = BackgroundRectangle(a_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        a_bg.move_to(a_lbl.get_center())

        b_lbl = MathTex("b = 6", color=TEAL_TERM).scale(0.9)
        b_lbl.next_to(tri, LEFT, buff=0.3)
        b_bg = BackgroundRectangle(b_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        b_bg.move_to(b_lbl.get_center())

        c_lbl = MathTex("c = ?", color=ORANGE_TERM).scale(0.9)
        c_lbl.next_to(tri.get_center(), UR, buff=0.2).shift(LEFT * 0.1)
        c_bg = BackgroundRectangle(c_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        c_bg.move_to(c_lbl.get_center())

        self.play(Create(tri, run_time=1.3))
        self.play(Create(right_mark, run_time=0.5))
        self.wait(0.4)
        self.play(FadeIn(a_bg, run_time=0.3), FadeIn(a_lbl, run_time=0.7))
        self.play(FadeIn(b_bg, run_time=0.3), FadeIn(b_lbl, run_time=0.7))
        self.play(FadeIn(c_bg, run_time=0.3), FadeIn(c_lbl, run_time=0.7))
        self.wait(1.0)

        verify = MathTex(
            r"6^{2} + 8^{2} = 36 + 64 = 100 = 10^{2}",
            color=GREEN_OK,
        ).scale(0.95)
        verify.next_to(tri, DOWN, buff=0.7)
        verify_bg = BackgroundRectangle(verify, color=BLACK, fill_opacity=1, buff=0.2)
        verify_bg.move_to(verify.get_center())
        self.play(FadeIn(verify_bg, run_time=0.4), Write(verify, run_time=1.6))
        self.wait(1.5)
        self.play(
            FadeOut(tri, run_time=0.6),
            FadeOut(right_mark, run_time=0.6),
            FadeOut(a_lbl, run_time=0.6),
            FadeOut(a_bg, run_time=0.6),
            FadeOut(b_lbl, run_time=0.6),
            FadeOut(b_bg, run_time=0.6),
            FadeOut(c_lbl, run_time=0.6),
            FadeOut(c_bg, run_time=0.6),
            FadeOut(verify, run_time=0.6),
            FadeOut(verify_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: a² + b² = c² + rearrangements (~15 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(
            r"a^{2} + b^{2} = c^{2}",
            color=BLUE_TERM, scale=1.4,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        rearr = VGroup(
            MathTex(r"c = \sqrt{a^{2} + b^{2}}", color=GREEN_OK).scale(0.85),
            MathTex(r"a = \sqrt{c^{2} - b^{2}}", color=GREEN_OK).scale(0.85),
        ).arrange(RIGHT, buff=0.6)
        rearr.next_to(general, DOWN, buff=0.55)
        rearr_bg = BackgroundRectangle(rearr, color=BLACK, fill_opacity=0.95, buff=0.18)
        rearr_bg.move_to(rearr.get_center())
        self.play(FadeIn(rearr_bg, run_time=0.4), FadeIn(rearr, run_time=1.3))
        self.wait(2.0)
        self.play(
            FadeOut(general, run_time=0.6),
            FadeOut(rearr, run_time=0.6),
            FadeOut(rearr_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: no right angle → theorem fails (~8 s)
        # ──────────────────────────────────────────────────────────────────
        # Skewed triangle (no right angle).
        D = np.array([-1.5, -0.8, 0.0])
        E = np.array([2.0, -0.8, 0.0])
        F = np.array([0.4, 2.4, 0.0])
        skewed = Polygon(D, E, F, color=RED_REJECT, stroke_width=3)
        skewed.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(Create(skewed, run_time=1.0))
        self.wait(0.6)

        warning = Text("No right angle → Pythagoras does NOT apply.",
                       font_size=22, color=RED_REJECT)
        warning.next_to(skewed, DOWN, buff=0.5)
        warning_bg = BackgroundRectangle(warning, color=BLACK, fill_opacity=0.95, buff=0.15)
        warning_bg.move_to(warning.get_center())
        self.play(FadeIn(warning_bg, run_time=0.3), FadeIn(warning, run_time=1.0))
        self.wait(1.5)
        self.play(
            FadeOut(skewed, run_time=0.5),
            FadeOut(warning, run_time=0.5),
            FadeOut(warning_bg, run_time=0.5),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~18 s, total ≈ 61 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{2} + b^{2} = c^{2}",
            "c is the hypotenuse — the side opposite the right angle.",
            final_wait=22.0,
        )
