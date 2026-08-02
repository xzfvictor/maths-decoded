"""
Manim scene for the lesson `rational-irrational`
(topic `l9-n-real-numbers`).

The real number system splits into rationals (a/b) and irrationals
(non-repeating decimals). The animation builds a concrete rational
example, contrasts it with sqrt(2), then anchors the key test:
"perfect square ⇒ rational, otherwise irrational".

Target duration: ~101.6 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class RationalIrrationalScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Rational vs. irrational numbers",
            "Rational = a/b with integers. Irrational = no such fraction.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Rational numbers: a/b with terminating or recurring decimal (~26 s)
        # ──────────────────────────────────────────────────────────────────
        # The defining form: a/b.
        head = Text("Rational", font_size=30, color=GREEN_OK)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        frac = MathTex(
            r"\dfrac{a}{b}", r"\quad (a, b \in \mathbb{Z},\ b \neq 0)",
        ).scale(1.1)
        frac[0].set_color(BLUE_TERM)
        frac.move_to(BAND_CHART_CENTER + UP * 0.4)
        frac_bg = BackgroundRectangle(frac, color=BLACK, fill_opacity=1, buff=0.28)
        frac_bg.move_to(frac.get_center())

        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)
        self.play(FadeIn(frac_bg, run_time=0.4), Write(frac, run_time=1.6))
        self.wait(3.0)

        # Two example decimals: terminating + recurring.
        term_card = make_equation_card(r"0.75", color=GREEN_OK, scale=1.0)
        term_card.move_to(BAND_CHART_CENTER + DOWN * 0.5)
        term_lbl = MathTex(r"= \dfrac{3}{4}", color=GREEN_OK).scale(0.85)
        term_lbl.next_to(term_card, DOWN, buff=0.25)
        term_lbl_bg = BackgroundRectangle(term_lbl, color=BLACK,
                                          fill_opacity=0.95, buff=0.15)
        term_lbl_bg.move_to(term_lbl.get_center())
        term_grp = VGroup(term_card, term_lbl, term_lbl_bg)

        rec_card = make_equation_card(r"0.\overline{3}", color=GREEN_OK, scale=1.0)
        rec_card.move_to(BAND_CHART_CENTER + DOWN * 2.0)
        rec_lbl = MathTex(r"= \dfrac{1}{3}", color=GREEN_OK).scale(0.85)
        rec_lbl.next_to(rec_card, DOWN, buff=0.25)
        rec_lbl_bg = BackgroundRectangle(rec_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        rec_lbl_bg.move_to(rec_lbl.get_center())
        rec_grp = VGroup(rec_card, rec_lbl, rec_lbl_bg)

        self.play(FadeIn(term_grp, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)
        self.play(FadeIn(rec_grp, shift=UP * 0.2, run_time=1.4))
        self.wait(4.0)

        self.play(
            FadeOut(VGroup(head, head_bg, frac, frac_bg, term_grp, rec_grp),
                    run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Irrational numbers: sqrt(2), pi, never-repeating decimals (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("Irrational", font_size=30, color=RED_REJECT)
        head2.move_to(BAND_CHART_CENTER + UP * 1.7)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        self.play(FadeIn(head2_bg, run_time=0.4), FadeIn(head2, run_time=1.0))
        self.wait(1.0)

        sq2 = make_equation_card(
            r"\sqrt{2} \approx 1.41421356\ldots",
            color=RED_REJECT, scale=1.0,
        )
        sq2.move_to(BAND_CHART_CENTER + UP * 0.4)
        sq2_lbl = Text("never repeats", font_size=22, color=RED_REJECT)
        sq2_lbl.next_to(sq2, DOWN, buff=0.3)
        sq2_lbl_bg = BackgroundRectangle(sq2_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        sq2_lbl_bg.move_to(sq2_lbl.get_center())
        sq2_grp = VGroup(sq2, sq2_lbl, sq2_lbl_bg)

        pi = make_equation_card(
            r"\pi \approx 3.14159265\ldots",
            color=RED_REJECT, scale=1.0,
        )
        pi.move_to(BAND_CHART_CENTER + DOWN * 1.1)
        pi_lbl = Text("never terminates, never repeats", font_size=22, color=RED_REJECT)
        pi_lbl.next_to(pi, DOWN, buff=0.3)
        pi_lbl_bg = BackgroundRectangle(pi_lbl, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        pi_lbl_bg.move_to(pi_lbl.get_center())
        pi_grp = VGroup(pi, pi_lbl, pi_lbl_bg)

        self.play(FadeIn(sq2_grp, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)
        self.play(FadeIn(pi_grp, shift=UP * 0.2, run_time=1.4))
        self.wait(5.0)

        self.play(
            FadeOut(VGroup(head2, head2_bg, sq2_grp, pi_grp), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Quick test: perfect square ⇒ rational, else irrational (~12 s)
        # ──────────────────────────────────────────────────────────────────
        ok = make_equation_card(
            r"\sqrt{9} = 3",
            color=GREEN_OK, scale=1.0,
        )
        ok.move_to(BAND_CHART_CENTER + UP * 0.6)
        ok_lbl = Text("perfect square → rational", font_size=22, color=GREEN_OK)
        ok_lbl.next_to(ok, DOWN, buff=0.3)
        ok_lbl_bg = BackgroundRectangle(ok_lbl, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        ok_lbl_bg.move_to(ok_lbl.get_center())
        ok_grp = VGroup(ok, ok_lbl, ok_lbl_bg)

        bad = make_equation_card(
            r"\sqrt{5} = \text{?}",
            color=RED_REJECT, scale=1.0,
        )
        bad.move_to(BAND_CHART_CENTER + DOWN * 0.9)
        bad_lbl = Text("non-perfect square → irrational", font_size=22, color=RED_REJECT)
        bad_lbl.next_to(bad, DOWN, buff=0.3)
        bad_lbl_bg = BackgroundRectangle(bad_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        bad_lbl_bg.move_to(bad_lbl.get_center())
        bad_grp = VGroup(bad, bad_lbl, bad_lbl_bg)

        self.play(FadeIn(ok_grp, shift=UP * 0.2, run_time=1.3))
        self.wait(1.5)
        self.play(FadeIn(bad_grp, shift=UP * 0.2, run_time=1.3))
        self.wait(4.0)

        self.play(
            FadeOut(VGroup(ok_grp, bad_grp), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 101.6 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Real} \;=\; \text{Rational} \;\cup\; \text{Irrational}",
            "Rational = a/b. Irrational = decimal that never repeats.",
            final_wait=39.0,
        )
