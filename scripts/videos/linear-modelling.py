"""
Manim scene for the lesson `linear-modelling`
(topic `l9-a-modelling-change`).

When something changes by a fixed amount each step, a linear model
fits: y = mx + b. The animation works a taxi-fare example
F = 3 + 2.20k, generalises to the rule, and rejects the common
mistake of mixing time units (per-minute × per-hour).

Target duration: ~80 s (matches the audio narration length of 79.96 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class LinearModellingScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Linear modelling",
            "y = mx + b when change is constant step by step.",
            hold=2.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete taxi fare example (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Taxi fare", font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 2.2)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        # Flag-fall: $3.00.
        flag = make_equation_card(r"\$3 \; \text{flag-fall}", color=BLUE_TERM, scale=1.0)
        flag.move_to(BAND_CHART_CENTER + UP * 0.7)
        for m in flag:
            m.set_z_index(2)

        # Per-km: $2.20 * k.
        rate = make_equation_card(r"+\; \$2.20\,k \; \text{per km}", color=ORANGE_TERM, scale=1.0)
        rate.next_to(flag, DOWN, buff=0.4)
        for m in rate:
            m.set_z_index(2)

        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=0.9))
        self.wait(1.0)
        self.play(FadeIn(flag, shift=UP * 0.2, run_time=1.2))
        self.wait(0.8)
        self.play(FadeIn(rate, shift=UP * 0.2, run_time=1.2))
        self.wait(1.5)

        # Combine into F = 3 + 2.20k.
        formula = make_equation_card(r"F \;=\; 3 + 2.20\,k",
                                     color=GREEN_OK, scale=1.3)
        formula.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        for m in formula:
            m.set_z_index(2)
        self.play(FadeIn(formula, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        # Numerical example: k = 10 → F = 25.
        eg = MathTex(r"k = 10 \;\Rightarrow\; F = 3 + 2.20(10) = 25",
                     color=GREEN_OK).scale(0.85)
        eg.next_to(formula, DOWN, buff=0.4)
        eg_bg = BackgroundRectangle(eg, color=BLACK, fill_opacity=0.95, buff=0.18)
        eg_bg.move_to(eg.get_center())
        self.play(FadeIn(eg_bg, run_time=0.4), FadeIn(eg, run_time=1.0))
        self.wait(2.0)

        beat2_group = VGroup(head, head_bg, flag, rate, formula, eg, eg_bg)
        self.play(FadeOut(beat2_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: y = mx + b with m = rate, b = start (~14 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(r"y \;=\; m\,x + b",
                                      color=BLUE_TERM, scale=1.4)
        general.move_to(BAND_CHART_CENTER + UP * 0.8)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.5))
        self.wait(1.8)

        line1 = MathTex(r"m \;=\; \text{change per step (rate)}",
                        color=GREEN_OK).scale(0.9)
        line2 = MathTex(r"b \;=\; \text{starting value (when } x=0\text{)}",
                        color=ORANGE_TERM).scale(0.9)
        line1.next_to(general, DOWN, buff=0.55)
        line2.next_to(line1, DOWN, buff=0.35)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=0.95, buff=0.18)
        line1_bg.move_to(line1.get_center())
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=0.95, buff=0.18)
        line2_bg.move_to(line2.get_center())
        self.play(FadeIn(line1_bg, run_time=0.4), FadeIn(line1, run_time=1.0))
        self.wait(0.6)
        self.play(FadeIn(line2_bg, run_time=0.4), FadeIn(line2, run_time=1.0))
        self.wait(2.0)

        beat3_group = VGroup(general, line1, line1_bg, line2, line2_bg)
        self.play(FadeOut(beat3_group, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: mixing per-minute and per-hour rates (~7 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(
            r"\$2.20\,/\text{km} \;\times\; 30\,\text{min}",
            color=RED_REJECT,
        ).scale(1.0)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())

        self.play(FadeIn(wrong_bg, run_time=0.5), Write(wrong, run_time=1.2))
        self.wait(0.8)

        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.6))
        self.wait(0.6)

        fix = MathTex(
            r"\text{km/h} \;\times\; \text{h} \;=\; \text{km}",
            color=GREEN_OK,
        ).scale(0.95)
        fix.next_to(wrong, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=1, buff=0.25)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.2))
        self.wait(1.2)
        self.play(
            FadeOut(VGroup(wrong, wrong_bg, cross, fix, fix_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=30 s, total ≈ 80 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y \;=\; m\,x + b",
            "m = rate of change, b = starting value.",
            final_wait=30.0,
        )