"""
Manim scene for the lesson `what-is-irrational`
(topic `l8-n-irrational-numbers`).

Rational numbers can be written as p / q and have decimals that either
terminate (e.g. 0.75) or recur (e.g. 0.overline{3}). Irrational numbers
are the rest — decimals that never terminate and never repeat.

Target duration: ~79 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class WhatIsIrrationalScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "What makes a number irrational?",
            "Decimals that never terminate and never repeat",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Rational: p/q with terminating or recurring decimal (~14 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        rat = make_term_card(
            r"\dfrac{p}{q}",
            r"p,\, q,\; q \neq 0",
            BLUE_TERM,
        )
        rat.move_to(BAND_CHART_CENTER + UP * 0.3)
        rat.set_z_index(2)
        beat_2 = beat_group(beat_2, rat)

        self.play(FadeIn(rat, shift=UP * 0.2, run_time=1.2))
        self.wait(3.0)

        # Two decimal cards: terminating vs recurring.
        term = make_equation_card(r"0.75", color=GREEN_OK, scale=1.0)
        term_lbl = Text("terminates", font_size=22, color=GREEN_OK)
        term_lbl.next_to(term, DOWN, buff=0.3)
        term_lbl_bg = BackgroundRectangle(term_lbl, color=BLACK,
                                          fill_opacity=0.95, buff=0.15)
        term_lbl_bg.move_to(term_lbl.get_center())
        term_grp = VGroup(term, term_lbl, term_lbl_bg)

        rec = make_equation_card(r"0.\overline{3}", color=GREEN_OK, scale=1.0)
        rec_lbl = Text("recurring block", font_size=22, color=GREEN_OK)
        rec_lbl.next_to(rec, DOWN, buff=0.3)
        rec_lbl_bg = BackgroundRectangle(rec_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        rec_lbl_bg.move_to(rec_lbl.get_center())
        rec_grp = VGroup(rec, rec_lbl, rec_lbl_bg)

        decimals = VGroup(term_grp, rec_grp).arrange(RIGHT, buff=1.2).scale(0.9)
        decimals.move_to(BAND_CHART_CENTER + DOWN * 1.45)
        beat_2 = beat_group(beat_2, decimals)

        self.play(
            FadeIn(term_grp, shift=UP * 0.2, run_time=1.4),
            FadeIn(rec_grp, shift=UP * 0.2, run_time=1.4),
        )
        self.wait(5.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Irrational: decimals that never repeat (~14 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        sq2 = make_equation_card(
            r"\sqrt{2} \approx 1.41421356\ldots",
            color=RED_REJECT, scale=1.0,
        )
        sq2.move_to(BAND_CHART_CENTER + UP * 1.0)
        sq2_lbl = Text("never repeats", font_size=22, color=RED_REJECT)
        sq2_lbl.next_to(sq2, DOWN, buff=0.35)
        sq2_lbl_bg = BackgroundRectangle(sq2_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        sq2_lbl_bg.move_to(sq2_lbl.get_center())
        sq2_grp = VGroup(sq2, sq2_lbl, sq2_lbl_bg)
        beat_3 = beat_group(beat_3, sq2_grp)

        pi = make_equation_card(
            r"\pi \approx 3.14159265\ldots",
            color=RED_REJECT, scale=1.0,
        )
        pi.move_to(BAND_CHART_CENTER + DOWN * 0.5)
        pi_lbl = Text("never repeats", font_size=22, color=RED_REJECT)
        pi_lbl.next_to(pi, DOWN, buff=0.35)
        pi_lbl_bg = BackgroundRectangle(pi_lbl, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        pi_lbl_bg.move_to(pi_lbl.get_center())
        pi_grp = VGroup(pi, pi_lbl, pi_lbl_bg)
        beat_3 = beat_group(beat_3, pi_grp)

        self.play(FadeIn(sq2_grp, shift=UP * 0.2, run_time=1.4))
        self.wait(2.5)
        self.play(FadeIn(pi_grp, shift=UP * 0.2, run_time=1.4))
        self.wait(5.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Contrast: non-repeating pattern is still irrational (~12 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        irr = make_equation_card(
            r"0.101001000100001\ldots",
            color=RED_REJECT, scale=0.95,
        )
        irr.move_to(BAND_CHART_CENTER + UP * 0.8)
        irr_lbl = Text(
            "no repeating block → irrational",
            font_size=22, color=RED_REJECT,
        )
        irr_lbl.next_to(irr, DOWN, buff=0.35)
        irr_lbl_bg = BackgroundRectangle(irr_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        irr_lbl_bg.move_to(irr_lbl.get_center())
        irr_grp = VGroup(irr, irr_lbl, irr_lbl_bg)
        beat_4 = beat_group(beat_4, irr_grp)

        rat_ex = make_equation_card(
            r"0.\overline{142857}",
            color=GREEN_OK, scale=1.0,
        )
        rat_ex.move_to(BAND_CHART_CENTER + DOWN * 0.7)
        rat_ex_lbl = Text(
            "block repeats → rational",
            font_size=22, color=GREEN_OK,
        )
        rat_ex_lbl.next_to(rat_ex, DOWN, buff=0.35)
        rat_ex_lbl_bg = BackgroundRectangle(rat_ex_lbl, color=BLACK,
                                            fill_opacity=0.95, buff=0.15)
        rat_ex_lbl_bg.move_to(rat_ex_lbl.get_center())
        rat_ex_grp = VGroup(rat_ex, rat_ex_lbl, rat_ex_lbl_bg)
        beat_4 = beat_group(beat_4, rat_ex_grp)

        self.play(FadeIn(irr_grp, shift=UP * 0.2, run_time=1.3))
        self.wait(2.0)
        self.play(FadeIn(rat_ex_grp, shift=UP * 0.2, run_time=1.3))
        self.wait(5.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (total ≈ 79 s; final_wait = 30 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Irrational} \;=\; \text{never terminates AND never repeats}",
            "Rational = repeating block or terminating decimal.",
            final_wait=30.0,
        )
