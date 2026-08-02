"""
Manim scene for the lesson `with-integers`
(topic `l8-n-four-operations`).

Use sign rules, mental strategies (compensation, halving/doubling, factoring),
and estimating first to work efficiently with integers.

Target duration: ~88 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class WithIntegersScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Efficient strategies with integers",
            "Sign rules + mental tricks + estimate first",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Mental strategies: 99×7 and 15×16 (~16 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Mental strategies",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
        )

        # Compensation: 99 × 7 = 100 × 7 − 1 × 7 = 693.
        comp = make_equation_card(
            r"99 \times 7 \;=\; 100 \times 7 - 7 \;=\; 693",
            color=BLUE_TERM, scale=0.95,
        )
        comp.move_to(BAND_CHART_CENTER + UP * 0.6)
        comp_lbl = Text("compensation", font_size=22, color=BLUE_TERM)
        comp_lbl.next_to(comp, DOWN, buff=0.35)
        comp_lbl_bg = BackgroundRectangle(comp_lbl, color=BLACK,
                                          fill_opacity=0.95, buff=0.15)
        comp_lbl_bg.move_to(comp_lbl.get_center())
        comp_grp = VGroup(comp, comp_lbl, comp_lbl_bg)

        self.play(FadeIn(comp_grp, shift=UP * 0.2, run_time=1.2))
        self.wait(3.0)

        # Halving and doubling: 15 × 16 = 30 × 8 = 240.
        hd = make_equation_card(
            r"15 \times 16 \;=\; 30 \times 8 \;=\; 240",
            color=TEAL_TERM, scale=0.95,
        )
        hd.move_to(BAND_CHART_CENTER + DOWN * 0.7)
        hd_lbl = Text("halving and doubling", font_size=22, color=TEAL_TERM)
        hd_lbl.next_to(hd, DOWN, buff=0.35)
        hd_lbl_bg = BackgroundRectangle(hd_lbl, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        hd_lbl_bg.move_to(hd_lbl.get_center())
        hd_grp = VGroup(hd, hd_lbl, hd_lbl_bg)

        self.play(FadeIn(hd_grp, shift=UP * 0.2, run_time=1.2))
        self.wait(4.5)

        self.play(
            FadeOut(VGroup(head, head_bg, comp_grp, hd_grp), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Sign rules: same sign → +, different → − (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("Sign rules",
                     font_size=24, color=ORANGE_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.7)
        head2_bg = BackgroundRectangle(head2, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        rule = MathTex(
            r"\text{same sign} \;\Rightarrow\; +;\quad"
            r"\text{different} \;\Rightarrow\; -",
            color=ORANGE_TERM,
        ).scale(0.95)
        rule.move_to(BAND_CHART_CENTER + UP * 0.7)
        rule_bg = BackgroundRectangle(rule, color=BLACK,
                                      fill_opacity=1, buff=0.25)
        rule_bg.move_to(rule.get_center())

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
        )
        self.play(
            FadeIn(rule_bg, run_time=0.4),
            Write(rule, run_time=1.6),
        )
        self.wait(3.0)

        # Example: -18 × -3.
        eg = MathTex(
            r"-18 \times (-3) \;=\; +54",
            color=GREEN_OK,
        ).scale(1.2)
        eg.next_to(rule, DOWN, buff=0.5)
        eg_bg = BackgroundRectangle(eg, color=BLACK,
                                    fill_opacity=1, buff=0.3)
        eg_bg.move_to(eg.get_center())

        self.play(
            FadeIn(eg_bg, run_time=0.4),
            Write(eg, run_time=1.4),
        )
        self.wait(3.5)

        self.play(
            FadeOut(VGroup(head2, head2_bg, rule, rule_bg, eg, eg_bg),
                    run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Estimate first: 52 × 71 (~16 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Estimate first, then check",
                     font_size=24, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())

        est = MathTex(
            r"52 \times 71 \;\approx\; 50 \times 70 \;=\; 3500",
            color=BLUE_TERM,
        ).scale(1.0)
        est.move_to(BAND_CHART_CENTER + UP * 0.5)
        est_bg = BackgroundRectangle(est, color=BLACK,
                                     fill_opacity=1, buff=0.25)
        est_bg.move_to(est.get_center())

        est_lbl = Text("rough estimate", font_size=22, color=BLUE_TERM)
        est_lbl.next_to(est, DOWN, buff=0.3)
        est_lbl_bg = BackgroundRectangle(est_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        est_lbl_bg.move_to(est_lbl.get_center())
        est_grp = VGroup(est, est_lbl, est_lbl_bg)

        self.play(
            FadeIn(head3_bg, run_time=0.4),
            FadeIn(head3, run_time=0.9),
        )
        self.play(FadeIn(est_grp, shift=UP * 0.2, run_time=1.4))
        self.wait(3.0)

        exact = MathTex(
            r"52 \times 71 \;=\; 3692",
            color=GREEN_OK,
        ).scale(1.1)
        exact.next_to(est_grp, DOWN, buff=0.5)
        exact_bg = BackgroundRectangle(exact, color=BLACK,
                                       fill_opacity=1, buff=0.3)
        exact_bg.move_to(exact.get_center())

        self.play(
            FadeIn(exact_bg, run_time=0.4),
            Write(exact, run_time=1.4),
        )
        self.wait(3.5)

        # Compare side-by-side: estimate 3500 vs exact 3692 — close.
        ok = Text(
            "Estimate close to exact → answer is sensible.",
            font_size=22, color=GREEN_OK,
        )
        ok.next_to(exact, DOWN, buff=0.4)
        ok_bg = BackgroundRectangle(ok, color=BLACK,
                                    fill_opacity=0.95, buff=0.15)
        ok_bg.move_to(ok.get_center())

        self.play(
            FadeIn(ok_bg, run_time=0.4),
            FadeIn(ok, run_time=1.0),
        )
        self.wait(3.0)

        self.play(
            FadeOut(VGroup(head3, head3_bg, est_grp, exact, exact_bg,
                           ok, ok_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (total ≈ 88 s; final_wait = 32 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Strategy} = \text{sign rules} + \text{mental tricks}"
            r" + \text{estimate}",
            "Mental methods and an estimate catch slips before they matter.",
            final_wait=32.0,
        )
