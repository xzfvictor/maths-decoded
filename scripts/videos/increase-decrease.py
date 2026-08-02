"""
Manim scene for the lesson `increase-decrease`
(topic `l8-n-percentages-error`).

A percentage change rescales the original by a fixed ratio: the
multiplier is 1 + p/100 for an increase and 1 - p/100 for a decrease.

Target duration: ~91 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, beat_group,
    animate_intro, animate_final_definition,
)
from manim import *


class IncreaseDecreaseScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Percentage increase and decrease",
            "Turn the % into a multiplier, then multiply",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — 20% increase: $80 → $100, multiplier 1.20 (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("1. Increase by 20%   →   multiplier 1.20",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.3)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        eq = MathTex(r"80 \times 1.20 = 100", color=BLUE_TERM).scale(1.15)
        eq.move_to(BAND_CHART_CENTER + UP * 0.4)
        eq_bg = BackgroundRectangle(eq, color=BLACK, fill_opacity=1, buff=0.25)
        eq_bg.move_to(eq.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
            FadeIn(eq_bg, run_time=0.4),
            Write(eq, run_time=1.6),
        )
        self.wait(2.5)

        rule = MathTex(
            r"\text{Increase} \;=\; 1 + \dfrac{p}{100}",
            color=GREEN_OK,
        ).scale(0.95)
        rule.next_to(eq, DOWN, buff=0.6)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.22)
        rule_bg.move_to(rule.get_center())

        self.play(
            FadeIn(rule_bg, run_time=0.4),
            Write(rule, run_time=1.4),
        )
        self.wait(5.0)

        beat2 = beat_group(head, head_bg, eq, eq_bg, rule, rule_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — 15% decrease: $120 → $102, multiplier 0.85 (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("2. Decrease by 15%   →   multiplier 0.85",
                     font_size=24, color=TEAL_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        eq2 = MathTex(r"120 \times 0.85 = 102", color=TEAL_TERM).scale(1.15)
        eq2.move_to(BAND_CHART_CENTER + UP * 0.4)
        eq2_bg = BackgroundRectangle(eq2, color=BLACK, fill_opacity=1, buff=0.25)
        eq2_bg.move_to(eq2.get_center())

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
            FadeIn(eq2_bg, run_time=0.4),
            Write(eq2, run_time=1.6),
        )
        self.wait(2.5)

        rule2 = MathTex(
            r"\text{Decrease} \;=\; 1 - \dfrac{p}{100}",
            color=GREEN_OK,
        ).scale(0.95)
        rule2.next_to(eq2, DOWN, buff=0.6)
        rule2_bg = BackgroundRectangle(rule2, color=BLACK, fill_opacity=1, buff=0.22)
        rule2_bg.move_to(rule2.get_center())

        self.play(
            FadeIn(rule2_bg, run_time=0.4),
            Write(rule2, run_time=1.4),
        )
        self.wait(5.0)

        beat3 = beat_group(head2, head2_bg, eq2, eq2_bg, rule2, rule2_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Warning: 50% up then 50% down ≠ original (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("3. Trap:  +50% then -50%   ≠   original",
                     font_size=24, color=RED_REJECT)
        head3.move_to(BAND_CHART_CENTER + UP * 1.3)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())

        walk = MathTex(
            r"100 \;\to\; 150 \;\to\; 75",
            color=RED_REJECT,
        ).scale(1.15)
        walk.move_to(BAND_CHART_CENTER + UP * 0.4)
        walk_bg = BackgroundRectangle(walk, color=BLACK, fill_opacity=1, buff=0.25)
        walk_bg.move_to(walk.get_center())

        self.play(
            FadeIn(head3_bg, run_time=0.4),
            FadeIn(head3, run_time=0.9),
            FadeIn(walk_bg, run_time=0.4),
            Write(walk, run_time=1.6),
        )
        self.wait(2.0)

        # Highlight the second arrow
        second = walk[0][2:4]  # the "150" or thereabouts; just play indicate
        self.play(Indicate(walk, color=RED_REJECT, scale_factor=1.05), run_time=1.2)
        self.wait(1.0)

        note = Text(
            "The -50% runs on the new (bigger) amount.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(walk, DOWN, buff=0.6)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())

        self.play(
            FadeIn(note_bg, run_time=0.4),
            FadeIn(note, run_time=1.0),
        )
        self.wait(3.5)

        beat4 = beat_group(head3, head3_bg, walk, walk_bg, note, note_bg)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~35 s, total ≈ 91 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{new} \;=\; \text{original} \times \left(1 \pm \dfrac{p}{100}\right)",
            "Increase uses + p/100; decrease uses - p/100.",
            final_wait=35.0,
        )
