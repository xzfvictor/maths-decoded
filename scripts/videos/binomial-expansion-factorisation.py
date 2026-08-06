"""
Manim scene for the lesson `binomial-expansion-factorisation`
(topic `l9-a-simplifying-expanding-factorising`).

Expanding a binomial product (x + m)(x + n) by FOIL gives
x² + (m + n)x + mn; factorising a monic quadratic reverses the
process — find two numbers whose product is c and sum is b. The
animation walks through (x + 3)(x + 5) = x² + 8x + 15, generalises
the rule, and rejects the common mistake of forgetting the FOIL
middle terms.

Target duration: ~101 s (matches the audio narration length of 100.73 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class BinomialExpansionFactorisationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Expanding and factorising binomials",
            "FOIL expands; the reverse factors.",
            hold=2.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: (x + 3)(x + 5) → x² + 8x + 15 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Original product.
        left = make_equation_card(r"(x + 3)(x + 5)",
                                   color=BLUE_TERM, scale=1.3)
        left.move_to(BAND_CHART_CENTER + UP * 1.0)
        for m in left:
            m.set_z_index(2)
        self.play(FadeIn(left, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        # FOIL labels.
        foil_lbl = Text("FOIL", font_size=22, color=GREEN_OK)
        foil_lbl.move_to(BAND_CHART_CENTER + UP * 0.0)
        foil_lbl_bg = BackgroundRectangle(foil_lbl, color=BLACK,
                                            fill_opacity=0.95, buff=0.15)
        foil_lbl_bg.move_to(foil_lbl.get_center())

        rows = VGroup(
            MathTex(r"\text{F: } x \cdot x = x^{2}", color=BLUE_TERM).scale(0.8),
            MathTex(r"\text{O: } x \cdot 5 = 5x", color=ORANGE_TERM).scale(0.8),
            MathTex(r"\text{I: } 3 \cdot x = 3x", color=ORANGE_TERM).scale(0.8),
            MathTex(r"\text{L: } 3 \cdot 5 = 15", color=TEAL_TERM).scale(0.8),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        rows.next_to(foil_lbl, DOWN, buff=0.4)
        for r in rows:
            rbg = BackgroundRectangle(r, color=BLACK, fill_opacity=0.9, buff=0.12)
            rbg.move_to(r.get_center())
            r.bg = rbg

        self.play(FadeIn(foil_lbl_bg, run_time=0.4),
                  FadeIn(foil_lbl, run_time=0.9))
        self.wait(0.6)
        for r in rows:
            self.play(FadeIn(r.bg, run_time=0.3), FadeIn(r, run_time=0.6))
            self.wait(0.4)
        self.wait(1.0)

        # Combine the four pieces into the final expanded form.
        beat2_foil = VGroup(left, foil_lbl, foil_lbl_bg, rows,
                             rows[0].bg, rows[1].bg, rows[2].bg, rows[3].bg)
        self.play(FadeOut(beat2_foil, run_time=1.0))

        right = make_equation_card(r"x^{2} + 8x + 15",
                                    color=GREEN_OK, scale=1.4)
        right.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in right:
            m.set_z_index(2)
        self.play(FadeIn(right, shift=UP * 0.2, run_time=1.5))
        self.wait(1.5)

        # Annotate the coefficient of x and the constant.
        ann1 = Text("8 = 3 + 5 (sum of the inner numbers)",
                    font_size=22, color=ORANGE_TERM)
        ann2 = Text("15 = 3 × 5 (product)",
                    font_size=22, color=TEAL_TERM)
        ann1.next_to(right, DOWN, buff=0.5)
        ann2.next_to(right, DOWN, buff=0.5)
        ann1_bg = BackgroundRectangle(ann1, color=BLACK, fill_opacity=0.95, buff=0.15)
        ann1_bg.move_to(ann1.get_center())
        ann2_bg = BackgroundRectangle(ann2, color=BLACK, fill_opacity=0.95, buff=0.15)
        ann2_bg.move_to(ann2.get_center())
        self.play(FadeIn(ann1_bg, run_time=0.4), FadeIn(ann1, run_time=1.0))
        self.wait(1.0)
        self.play(
            FadeOut(ann1, run_time=0.6),
            FadeOut(ann1_bg, run_time=0.6),
        )
        self.wait(0.6)
        self.play(FadeIn(ann2_bg, run_time=0.4), FadeIn(ann2, run_time=1.0))
        self.wait(1.5)

        beat2_group = VGroup(right, ann2, ann2_bg)
        self.play(FadeOut(beat2_group, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — General pattern (x + m)(x + n) (~18 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(
            r"(x + m)(x + n) \;=\; x^{2} + (m + n)\,x + m\,n",
            color=BLUE_TERM,
            scale=1.0,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.7)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.6))
        self.wait(2.0)

        # Highlight m + n and mn.
        line1 = MathTex(r"\text{coefficient of } x \;=\; m + n",
                        color=ORANGE_TERM).scale(0.95)
        line2 = MathTex(r"\text{constant term} \;=\; m \cdot n",
                        color=TEAL_TERM).scale(0.95)
        line1.next_to(general, DOWN, buff=0.55)
        line2.next_to(line1, DOWN, buff=0.35)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=0.95, buff=0.18)
        line1_bg.move_to(line1.get_center())
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=0.95, buff=0.18)
        line2_bg.move_to(line2.get_center())
        self.play(FadeIn(line1_bg, run_time=0.4), FadeIn(line1, run_time=1.0))
        self.wait(0.6)
        self.play(FadeIn(line2_bg, run_time=0.4), FadeIn(line2, run_time=1.0))
        self.wait(1.8)

        beat3_group = VGroup(general, line1, line1_bg, line2, line2_bg)
        self.play(FadeOut(beat3_group, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: forgetting the middle terms (~10 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(
            r"(x + 3)(x + 5) \;=\; x^{2} + 15",
            color=RED_REJECT,
        ).scale(1.3)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())

        self.play(FadeIn(wrong_bg, run_time=0.5), Write(wrong, run_time=1.4))
        self.wait(1.0)

        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.7))
        self.wait(0.8)

        fix = MathTex(
            r"\text{Don't forget the } x \text{ terms (5x and 3x)}.",
            color=GREEN_OK,
        ).scale(0.85)
        fix.next_to(wrong, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.5))
        self.wait(1.0)
        self.play(
            FadeOut(VGroup(wrong, wrong_bg, cross, fix, fix_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=55.9 s, total ≈ 101 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"(x + m)(x + n) \;=\; x^{2} + (m + n)\,x + m\,n",
            "Sum of m, n gives the x-coefficient; product gives the constant.",
            final_wait=38.0,
        )