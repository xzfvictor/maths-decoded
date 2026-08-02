"""
Manim scene for the lesson `relative-frequency`
(topic `l9-p-relative-frequencies`).

Relative frequency = (times the event happened) / (total trials). As
trials grow, it stabilises around the true probability. Reject the
"one trial = probability" mistake.

Target duration: ~69.8 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, YELLOW_HIGHLIGHT, make_term_card, make_equation_card,
    animate_intro, animate_final_definition, beat_group,
)
from manim import *


class RelativeFrequencyScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Relative frequency as an estimate",
            "Run it many times — count / n converges to the probability.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Definition and worked example (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None
        definition = MathTex(
            r"\text{relative frequency of } A \;=\; "
            r"\dfrac{\text{count of } A}{n}",
        ).scale(0.95)
        definition.move_to(BAND_CHART_CENTER + UP * 1.4)
        d_bg = BackgroundRectangle(definition, color=BLACK, fill_opacity=1, buff=0.28)
        d_bg.move_to(definition.get_center())
        beat_2 = VGroup(d_bg, definition)
        self.play(FadeIn(d_bg, run_time=0.4), Write(definition, run_time=2.0))
        self.wait(3.0)

        # Concrete: 47 / 200 = 0.235.
        example = MathTex(
            r"\text{red landed 47 times in 200 spins} \;\Rightarrow\; "
            r"\dfrac{47}{200} = 0.235",
            color=GREEN_OK,
        ).scale(0.85)
        example.move_to(BAND_CHART_CENTER + UP * 0.0)
        ex_bg = BackgroundRectangle(example, color=BLACK, fill_opacity=1, buff=0.25)
        ex_bg.move_to(example.get_center())
        beat_2 = VGroup(beat_2, ex_bg, example)
        self.play(FadeIn(ex_bg, run_time=0.4), FadeIn(example, run_time=1.6))
        self.wait(3.0)

        est = MathTex(
            r"\Pr(\text{red}) \approx 0.235",
            color=BLUE_TERM,
        ).scale(1.0)
        est.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        est_bg = BackgroundRectangle(est, color=BLACK, fill_opacity=1, buff=0.28)
        est_bg.move_to(est.get_center())
        beat_2 = VGroup(beat_2, est_bg, est)
        self.play(FadeIn(est_bg, run_time=0.4), Write(est, run_time=1.4))
        self.wait(4.0)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Convergence: more trials → closer to true probability (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None
        # Two bars converging to a true-probability line.
        true_line = DashedLine(
            start=BAND_CHART_CENTER + UP * 0.4 + LEFT * 2.8,
            end=BAND_CHART_CENTER + UP * 0.4 + RIGHT * 2.8,
            color=YELLOW_HIGHLIGHT, stroke_width=3,
        )
        true_lbl = Text("true probability", font_size=20, color=YELLOW_HIGHLIGHT)
        true_lbl.next_to(true_line, UP, buff=0.2)
        true_lbl_bg = BackgroundRectangle(true_lbl, color=BLACK,
                                          fill_opacity=0.95, buff=0.15)
        true_lbl_bg.move_to(true_lbl.get_center())
        beat_3 = VGroup(true_line, true_lbl, true_lbl_bg)

        bar_small = Rectangle(width=1.4, height=0.9, color=BLUE_TERM,
                              fill_opacity=0.6, stroke_width=2)
        bar_small.move_to(BAND_CHART_CENTER + DOWN * 0.6 + LEFT * 2.0)
        bar_big = Rectangle(width=1.4, height=1.6, color=GREEN_OK,
                            fill_opacity=0.6, stroke_width=2)
        bar_big.move_to(BAND_CHART_CENTER + DOWN * 0.6 + RIGHT * 2.0)

        lbl_small = Text("n = 20", font_size=22, color=WHITE)
        lbl_small.next_to(bar_small, DOWN, buff=0.25)
        lbl_big = Text("n = 200", font_size=22, color=WHITE)
        lbl_big.next_to(bar_big, DOWN, buff=0.25)

        self.play(Create(true_line, run_time=1.0),
                  FadeIn(true_lbl_bg, run_time=0.4),
                  FadeIn(true_lbl, run_time=0.8))
        self.wait(1.5)
        self.play(
            FadeIn(bar_small, run_time=1.0),
            FadeIn(bar_big, run_time=1.0),
        )
        beat_3 = VGroup(beat_3, bar_small, bar_big)
        self.play(
            FadeIn(lbl_small, run_time=0.6),
            FadeIn(lbl_big, run_time=0.6),
        )
        beat_3 = VGroup(beat_3, lbl_small, lbl_big)
        self.wait(2.5)

        cap = Text(
            "Bigger n → relative frequency closer to the truth.",
            font_size=22, color=GREEN_OK,
        )
        cap.next_to(VGroup(lbl_small, lbl_big), DOWN, buff=0.5)
        cap_bg = BackgroundRectangle(cap, color=BLACK, fill_opacity=0.95, buff=0.18)
        cap_bg.move_to(cap.get_center())
        beat_3 = VGroup(beat_3, cap_bg, cap)
        self.play(FadeIn(cap_bg, run_time=0.4), FadeIn(cap, run_time=1.4))
        self.wait(4.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: one trial is not a probability (~6 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None
        bad = Text(
            '"I tossed once and got heads — so the probability is 1."',
            font_size=22, color=WHITE,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.4)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        beat_4 = VGroup(bad_bg, bad)
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(1.5)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        beat_4 = VGroup(beat_4, cross)
        self.play(Create(cross, run_time=1.0))
        self.wait(2.0)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 69.8 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\Pr(A) \;\approx\; \dfrac{\text{count of } A}{n}",
            "Bigger n → closer to the true probability.",
            final_wait=26.0,
        )
