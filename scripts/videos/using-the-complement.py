"""
Manim scene for the lesson `using-the-complement`
(topic `l8-p-complementary-events`).

The complement rule shines for "at least one" or "all" problems where
the complement is one easy case. Show "at least one head in 3 tosses"
solved by computing "no heads" = (1/2)^3, then subtract from 1.

Target duration: ~102.4 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class UsingTheComplementScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Using the complement to solve problems",
            "When 'at least one' is messy, count 'none' instead.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: at least one head in 3 tosses (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None
        direct = MathTex(
            r"\Pr(\text{at least one H in 3 tosses}) = \,?",
        ).scale(0.95)
        direct.move_to(BAND_CHART_CENTER + UP * 1.3)
        direct_bg = BackgroundRectangle(direct, color=BLACK, fill_opacity=1, buff=0.25)
        direct_bg.move_to(direct.get_center())
        beat_2 = beat_group(beat_2, direct_bg, direct)
        self.play(FadeIn(direct_bg, run_time=0.4), FadeIn(direct, run_time=1.6))
        self.wait(2.0)

        # Direct list — many cases.
        lbl1 = Text(
            "Direct: HH?, H?H, ?HH, HHH ... — many cases",
            font_size=20, color=ORANGE_TERM,
        ).next_to(direct, DOWN, buff=0.6)
        lbl1_bg = BackgroundRectangle(lbl1, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl1_bg.move_to(lbl1.get_center())
        beat_2 = beat_group(beat_2, lbl1_bg, lbl1)
        self.play(FadeIn(lbl1_bg, run_time=0.4), FadeIn(lbl1, run_time=1.4))
        self.wait(3.0)

        # Complement.
        comp = MathTex(
            r"\text{Complement:}\quad \Pr(\text{no H at all}) = \Pr(TTT)",
            color=GREEN_OK,
        ).scale(0.85)
        comp.next_to(lbl1, DOWN, buff=0.45)
        comp_bg = BackgroundRectangle(comp, color=BLACK, fill_opacity=1, buff=0.2)
        comp_bg.move_to(comp.get_center())
        beat_2 = beat_group(beat_2, comp_bg, comp)
        self.play(FadeIn(comp_bg, run_time=0.4), FadeIn(comp, run_time=1.6))
        self.wait(3.0)

        # Computation.
        no_h = MathTex(
            r"\Pr(TTT) = (1/2)(1/2)(1/2) = 1/8",
            color=GREEN_OK,
        ).scale(1.0)
        no_h.next_to(comp, DOWN, buff=0.45)
        no_h_bg = BackgroundRectangle(no_h, color=BLACK, fill_opacity=1, buff=0.22)
        no_h_bg.move_to(no_h.get_center())
        beat_2 = beat_group(beat_2, no_h_bg, no_h)
        self.play(FadeIn(no_h_bg, run_time=0.4), FadeIn(no_h, run_time=1.6))
        self.wait(2.0)

        ans = MathTex(
            r"\Pr(\text{at least one H}) = 1 - 1/8 = 7/8",
            color=GREEN_OK,
        ).scale(1.0)
        ans.next_to(no_h, DOWN, buff=0.45)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.22)
        ans_bg.move_to(ans.get_center())
        beat_2 = beat_group(beat_2, ans_bg, ans)
        self.play(FadeIn(ans_bg, run_time=0.4), FadeIn(ans, run_time=1.8))
        self.wait(4.0)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The recipe (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None
        step1 = make_term_card("1.\,\text{Identify } A",   "what you want",        BLUE_TERM).scale(0.55)
        step2 = make_term_card("2.\,\text{Find } A'",       "the easy complement",  TEAL_TERM).scale(0.55)
        step3 = make_term_card("3.\,\Pr(A')",                "one calculation",      ORANGE_TERM).scale(0.55)
        step4 = make_term_card("4.\,1 - \Pr(A')",           "answer is automatic",  GREEN_OK).scale(0.55)
        # Two columns to keep the stack within the y safe area [-1.5, 1.8].
        left_col = VGroup(step1, step3).arrange(DOWN, buff=0.2)
        right_col = VGroup(step2, step4).arrange(DOWN, buff=0.2)
        steps_row = VGroup(left_col, right_col).arrange(RIGHT, buff=0.5)
        steps_row.move_to(BAND_CHART_CENTER)
        # Keep the full card grid below the subtitle and within the chart band.
        steps_row.shift(DOWN * (steps_row.get_top()[1] - 0.8))
        for s in steps_row:
            s.set_z_index(2)

        for s in steps_row:
            beat_3 = beat_group(beat_3, s)
            self.play(FadeIn(s, shift=RIGHT * 0.15, run_time=0.7))
            self.wait(0.7)

        self.wait(6.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: ignoring the complement path for two dice (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None
        bad = MathTex(
            r"\text{List every pair that has a 6: } (6,1),(6,2),\ldots,(1,6),\ldots",
            color=RED_REJECT,
        ).scale(0.85)
        bad.move_to(BAND_CHART_CENTER + UP * 0.5)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.22)
        bad_bg.move_to(bad.get_center())
        beat_4 = beat_group(beat_4, bad_bg, bad)
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=2.0))
        self.wait(3.0)

        much = Text(
            "Works — but easy to miss a case.",
            font_size=22, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        much_bg = BackgroundRectangle(much, color=BLACK, fill_opacity=0.95, buff=0.18)
        much_bg.move_to(much.get_center())
        beat_4 = beat_group(beat_4, much_bg, much)
        self.play(FadeIn(much_bg, run_time=0.4), FadeIn(much, run_time=1.4))
        self.wait(2.0)

        fix = MathTex(
            r"\Pr(\text{no 6}) = (5/6)(5/6) = 25/36 \Rightarrow 1 - 25/36 = 11/36",
            color=GREEN_OK,
        ).scale(0.85)
        fix.next_to(much, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=1, buff=0.22)
        fix_bg.move_to(fix.get_center())
        beat_4 = beat_group(beat_4, fix_bg, fix)
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=2.2))
        self.wait(5.0)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 102.4 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\Pr(\text{at least one}) = 1 - \Pr(\text{none})",
            "Compute the easy 'none' case, then subtract from 1.",
            final_wait=40.0,
        )
