"""
Manim scene for the lesson `pythagoras`
(topic `l9-m-pythagoras-trigonometry`).

Pythagoras' theorem in spatial problems: a² + b² = c² for any
right-angled triangle. The scene verifies a 6-8-10 right triangle,
generalises the rule with both rearrangements, and rejects the
common mistake of applying it without a right angle.

Render target: ~2 s audio + 20 s final wait. Beats are timed with
explicit self.wait(...) calls.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class PythagorasScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (audio is short, so this is the breath)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Pythagoras' theorem",
            "a² + b² = c² for any right-angled triangle.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — 6-8-10 right triangle, verify 36 + 64 = 100
        # ──────────────────────────────────────────────────────────────────
        # Right-angle corner at A, leg a = 8 horizontal, leg b = 6 vertical.
        A = np.array([-2.0, -0.6, 0.0])
        B = np.array([2.0, -0.6, 0.0])    # 8 across (scaled)
        C = np.array([-2.0, 2.0, 0.0])    # 6 up
        tri = Polygon(A, B, C, color=BLUE_TERM, stroke_width=4)
        tri.move_to(BAND_CHART_CENTER + UP * 0.3)

        right_mark = Square(side_length=0.28, color=BLUE_TERM, stroke_width=2)
        right_mark.move_to(A + RIGHT * 0.18 + UP * 0.18)

        a_lbl = MathTex("a = 8", color=BLUE_TERM).scale(0.85)
        a_lbl.next_to(tri, DOWN, buff=0.25)
        a_bg = BackgroundRectangle(a_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        a_bg.move_to(a_lbl.get_center())

        b_lbl = MathTex("b = 6", color=TEAL_TERM).scale(0.85)
        b_lbl.next_to(tri, LEFT, buff=0.25)
        b_bg = BackgroundRectangle(b_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        b_bg.move_to(b_lbl.get_center())

        c_lbl = MathTex("c = ?", color=ORANGE_TERM).scale(0.85)
        c_lbl.next_to(tri.get_center(), UR, buff=0.15).shift(LEFT * 0.1)
        c_bg = BackgroundRectangle(c_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        c_bg.move_to(c_lbl.get_center())

        self.play(Create(tri, run_time=1.2))
        self.play(Create(right_mark, run_time=0.5))
        self.wait(0.3)
        self.play(FadeIn(a_bg, run_time=0.3), FadeIn(a_lbl, run_time=0.6))
        self.play(FadeIn(b_bg, run_time=0.3), FadeIn(b_lbl, run_time=0.6))
        self.play(FadeIn(c_bg, run_time=0.3), FadeIn(c_lbl, run_time=0.6))
        self.wait(0.6)

        # Verify a² + b² = c²
        verify = MathTex(
            r"6^{2} + 8^{2} = 36 + 64 = 100 = 10^{2}",
            color=GREEN_OK,
        ).scale(0.9)
        verify.next_to(tri, DOWN, buff=0.55)
        verify_bg = BackgroundRectangle(verify, color=BLACK, fill_opacity=1, buff=0.18)
        verify_bg.move_to(verify.get_center())
        self.play(FadeIn(verify_bg, run_time=0.4), Write(verify, run_time=1.4))
        self.wait(1.0)

        beat2 = beat_group(
            tri, right_mark, a_lbl, a_bg, b_lbl, b_bg,
            c_lbl, c_bg, verify, verify_bg,
        )
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: a² + b² = c² + the two rearrangements
        # ──────────────────────────────────────────────────────────────────
        general = MathTex(r"a^{2} + b^{2} = c^{2}", color=BLUE_TERM).scale(1.4)
        general.move_to(BAND_CHART_CENTER + UP * 0.6)
        general_bg = BackgroundRectangle(general, color=BLACK, fill_opacity=1, buff=0.3)
        general_bg.move_to(general.get_center())

        self.play(FadeIn(general_bg, run_time=0.4), Write(general, run_time=1.5))
        self.wait(1.0)

        # The two rearrangements stacked.
        rearr = VGroup(
            MathTex(r"c = \sqrt{a^{2} + b^{2}}", color=GREEN_OK).scale(0.85),
            MathTex(r"a = \sqrt{c^{2} - b^{2}}", color=GREEN_OK).scale(0.85),
        ).arrange(DOWN, buff=0.35)
        rearr.next_to(general, DOWN, buff=0.6)
        rearr_bg = BackgroundRectangle(rearr, color=BLACK, fill_opacity=0.95, buff=0.2)
        rearr_bg.move_to(rearr.get_center())
        self.play(FadeIn(rearr_bg, run_time=0.4), FadeIn(rearr, run_time=1.2))
        self.wait(1.5)

        beat3 = beat_group(general, general_bg, rearr, rearr_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: no right angle → theorem does NOT apply
        # ──────────────────────────────────────────────────────────────────
        # Skewed triangle (no right angle).
        D = np.array([-1.6, -0.6, 0.0])
        E = np.array([2.0, -0.6, 0.0])
        F = np.array([0.4, 2.2, 0.0])
        skewed = Polygon(D, E, F, color=RED_REJECT, stroke_width=3)
        skewed.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(Create(skewed, run_time=1.0))
        self.wait(0.4)

        warning = MathTex(
            r"\text{No right angle} \;\Rightarrow\; a^{2}+b^{2} \neq c^{2}",
            color=RED_REJECT,
        ).scale(0.9)
        warning.next_to(skewed, DOWN, buff=0.5)
        warning_bg = BackgroundRectangle(warning, color=BLACK, fill_opacity=1, buff=0.2)
        warning_bg.move_to(warning.get_center())
        self.play(FadeIn(warning_bg, run_time=0.4), Write(warning, run_time=1.2))
        self.wait(1.0)

        beat4 = beat_group(skewed, warning, warning_bg)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final boxed takeaway
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"a^{2} + b^{2} = c^{2}",
            "c is the hypotenuse — the side opposite the right angle.",
            final_wait=51.0,
        )
