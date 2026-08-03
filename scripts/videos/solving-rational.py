"""
Manim scene for the lesson `solving-rational`
(topic `l10a-aa-linear-rational`).

Solve f(x)/g(x) = 0. The fraction is zero exactly when the numerator
f(x) is zero AND the denominator g(x) is non-zero. Example:
(x^2 - 4) / (x - 2) = 0 gives x = -2 (NOT x = 2).

Target duration: ~82.4 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class SolvingRationalScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Solving a rational equation",
            "Set the numerator to zero — but exclude zeros of the denominator.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The rule (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("The rule", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        rule = make_equation_card(
            r"\dfrac{f(x)}{g(x)} = 0 \iff f(x)=0\ \text{and}\ g(x)\neq 0",
            color=BLUE_TERM, scale=0.95,
        )
        rule.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(rule, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        note = Text(
            "Zero divided by a non-zero is zero.",
            font_size=20, color=WHITE,
        ).next_to(rule, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4),
                  FadeIn(note, run_time=1.0))
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, rule, note, note_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: (x^2 - 4)/(x - 2) = 0 (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Worked example", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.45)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        problem = make_equation_card(
            r"\dfrac{x^{2}-4}{x-2} = 0",
            color=GREEN_OK, scale=0.95,
        )
        problem.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(problem, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        # Replace the original rational equation before showing the
        # numerator equation; keeping both cards visible caused a cross-fade overlap.
        self.play(FadeOut(problem, run_time=0.5))
        self.wait(0.2)

        step1 = MathTex(
            r"x^{2} - 4 = 0",
            color=BLUE_TERM,
        ).scale(0.95)
        step1.move_to(BAND_CHART_CENTER + UP * 0.2)
        step1_bg = BackgroundRectangle(step1, color=BLACK,
                                       fill_opacity=1, buff=0.2)
        step1_bg.move_to(step1.get_center())
        self.play(FadeIn(step1_bg, run_time=0.3),
                  FadeIn(step1, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        step2 = make_equation_card(
            r"x = \pm 2",
            color=ORANGE_TERM, scale=0.95,
        )
        step2.move_to(BAND_CHART_CENTER + DOWN * 0.85)
        self.play(FadeIn(step2, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        beat3 = beat_group(head3, head3_bg, problem, step1, step1_bg, step2)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject x = 2 because denominator is zero (~10 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Reject x = 2", font_size=26, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.45)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        reject = MathTex(
            r"x = 2\ \Rightarrow\ \text{denom} = 0",
            color=RED_REJECT,
        ).scale(0.9)
        reject.move_to(BAND_CHART_CENTER + UP * 0.4)
        reject_bg = BackgroundRectangle(reject, color=BLACK,
                                       fill_opacity=1, buff=0.2)
        reject_bg.move_to(reject.get_center())
        self.play(FadeIn(reject_bg, run_time=0.3),
                  FadeIn(reject, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        ans = make_equation_card(
            r"\therefore\ x = -2\ \text{only}",
            color=GREEN_OK, scale=0.95,
        )
        ans.move_to(BAND_CHART_CENTER + DOWN * 0.85)
        self.play(FadeIn(ans, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        beat4 = beat_group(head4, head4_bg, reject, reject_bg, ans)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 82.4 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\dfrac{f(x)}{g(x)}=0\ \Rightarrow\ f(x)=0,\ g(x)\neq 0",
            "Solve the numerator, then exclude zeros of the denominator.",
            final_wait=37.0,
        )