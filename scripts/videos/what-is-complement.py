"""
Manim scene for the lesson `what-is-complement`
(topic `l8-p-complementary-events`).

The complement of an event A is "everything that is not A". Their
probabilities always sum to 1, so P(A') = 1 - P(A). The lesson builds
the rule with a concrete coin toss and then rejects the confusion with
mutually exclusive.

Target duration: ~86.5 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class WhatIsComplementScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "What is a complementary event?",
            "The complement covers everything A is not.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: coin toss (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None
        h_card = make_term_card("H", "Heads", BLUE_TERM)
        t_card = make_term_card("T", "Tails", TEAL_TERM)
        coin_row = VGroup(
            h_card, MathTex("+", color=WHITE).scale(1.4), t_card
        ).arrange(RIGHT, buff=0.45)
        coin_row.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in coin_row:
            m.set_z_index(2)
        beat_2 = beat_group(beat_2, h_card, coin_row[1], t_card)

        self.play(FadeIn(h_card, shift=UP * 0.2, run_time=1.2))
        self.wait(1.5)
        self.play(
            FadeIn(coin_row[1], run_time=0.6),
            FadeIn(t_card, shift=UP * 0.2, run_time=1.2),
        )
        self.wait(2.0)

        # Probabilities summing to 1 — H label sits LEFT of "=" and 0.5,
        # T label sits RIGHT of "=" and 0.5 so neither collides with the
        # central "+" sign between the two outcome cards.
        h_lbl = MathTex(r"\Pr(H)", color=BLUE_TERM).scale(0.9)
        h_eq = MathTex(r"=", color=WHITE).scale(1.0)
        h_val = MathTex(r"0.5", color=BLUE_TERM).scale(0.9)
        h_prob_row = VGroup(h_lbl, h_eq, h_val).arrange(RIGHT, buff=0.2)
        h_prob_row.next_to(h_card[0], LEFT, buff=0.4)
        beat_2 = beat_group(beat_2, h_lbl, h_eq, h_val)

        t_lbl = MathTex(r"\Pr(T)", color=TEAL_TERM).scale(0.9)
        t_eq = MathTex(r"=", color=WHITE).scale(1.0)
        t_val = MathTex(r"0.5", color=TEAL_TERM).scale(0.9)
        t_prob_row = VGroup(t_lbl, t_eq, t_val).arrange(RIGHT, buff=0.2)
        t_prob_row.next_to(t_card[0], RIGHT, buff=0.4)
        beat_2 = beat_group(beat_2, t_lbl, t_eq, t_val)

        self.play(
            FadeIn(h_prob_row, run_time=0.8),
            FadeIn(t_prob_row, run_time=0.8),
        )
        self.wait(3.0)

        cap = Text(
            "Heads and Tails together cover every outcome.",
            font_size=22, color=GREEN_OK,
        ).next_to(coin_row, DOWN, buff=0.55)
        cap_bg = BackgroundRectangle(cap, color=BLACK, fill_opacity=0.95, buff=0.18)
        cap_bg.move_to(cap.get_center())
        beat_2 = beat_group(beat_2, cap_bg, cap)
        self.play(FadeIn(cap_bg, run_time=0.4), FadeIn(cap, run_time=1.2))
        self.wait(4.0)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: P(A) + P(A') = 1 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None
        rule = MathTex(
            r"\Pr(A) \;+\; \Pr(A') \;=\; 1",
        ).scale(1.05)
        rule.move_to(BAND_CHART_CENTER + UP * 0.6)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.28)
        rule_bg.move_to(rule.get_center())
        beat_3 = beat_group(beat_3, rule_bg, rule)

        self.play(FadeIn(rule_bg, run_time=0.5), Write(rule, run_time=2.2))
        self.wait(3.0)

        rearr = MathTex(
            r"\Pr(A') \;=\; 1 \;-\; \Pr(A)",
            color=GREEN_OK,
        ).scale(1.1)
        rearr.next_to(rule, DOWN, buff=0.6)
        rearr_bg = BackgroundRectangle(rearr, color=BLACK, fill_opacity=1, buff=0.28)
        rearr_bg.move_to(rearr.get_center())
        beat_3 = beat_group(beat_3, rearr_bg, rearr)
        self.play(FadeIn(rearr_bg, run_time=0.5), Write(rearr, run_time=2.2))
        self.wait(3.0)

        # Worked example: not a 6.
        ex = Text(
            "e.g. die:  P(not 6) = 1 - 1/6 = 5/6",
            font_size=24, color=GREEN_OK,
        ).next_to(rearr, DOWN, buff=0.55)
        ex_bg = BackgroundRectangle(ex, color=BLACK, fill_opacity=0.95, buff=0.18)
        ex_bg.move_to(ex.get_center())
        beat_3 = beat_group(beat_3, ex_bg, ex)
        self.play(FadeIn(ex_bg, run_time=0.4), FadeIn(ex, run_time=1.4))
        self.wait(5.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject the "mutually exclusive = complementary" confusion (~11 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None
        bad = Text(
            '"Mutually exclusive" means the same as "complementary".',
            font_size=22, color=WHITE,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.7)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        beat_4 = beat_group(beat_4, bad_bg, bad)
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(2.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        beat_4 = beat_group(beat_4, cross)
        self.play(Create(cross, run_time=1.0))

        fix = Text(
            '"Rolled a 1" and "rolled a 2" are mutually exclusive — but not complementary.',
            font_size=20, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        beat_4 = beat_group(beat_4, fix_bg, fix)
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.4))
        self.wait(3.0)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 86.5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\Pr(A') \;=\; 1 \;-\; \Pr(A)",
            "A and not A together cover every possible outcome.",
            final_wait=32.0,
        )
