"""
Manim scene for the lesson `solving-with-logs`
(topic `l10a-aa-exp-log-inverse`).

Solve 2^x = 7 by taking logarithms of both sides, then x = log(7)/log(2).
The animation contrasts the two cases (unknown inside log, unknown in
exponent) and rejects the mistake of writing log(2^x) = x without the
power law.

Target duration: ~85.1 s (matches the audio narration length).
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


class SolvingWithLogsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Solving equations with logs",
            "Free the unknown by undoing log or exponent.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Case 1: unknown in the exponent (~26 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Case 1: unknown in the exponent",
                    font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        eq = MathTex(r"2^{x} = 7", color=BLUE_TERM).scale(1.4)
        eq.move_to(BAND_CHART_CENTER + UP * 0.5)
        eq_bg = BackgroundRectangle(eq, color=BLACK, fill_opacity=1, buff=0.3)
        eq_bg.move_to(eq.get_center())
        beat_2 = beat_group(beat_2, eq, eq_bg)
        self.play(FadeIn(eq_bg, run_time=0.4), Write(eq, run_time=1.6))
        self.wait(1.0)

        # Take log of both sides.
        step = MathTex(
            r"\log(2^{x}) = \log(7)",
            color=ORANGE_TERM,
        ).scale(1.1)
        step.next_to(eq, DOWN, buff=0.5)
        step_bg = BackgroundRectangle(step, color=BLACK, fill_opacity=1, buff=0.25)
        step_bg.move_to(step.get_center())
        beat_2 = beat_group(beat_2, step, step_bg)
        self.play(FadeIn(step_bg, run_time=0.4), Write(step, run_time=1.6))
        self.wait(1.0)

        # Power law.
        step2 = MathTex(
            r"x\,\log(2) = \log(7)",
            color=ORANGE_TERM,
        ).scale(1.1)
        step2.next_to(step, DOWN, buff=0.5)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=1, buff=0.25)
        step2_bg.move_to(step2.get_center())
        beat_2 = beat_group(beat_2, step2, step2_bg)
        self.play(FadeIn(step2_bg, run_time=0.4), Write(step2, run_time=1.4))
        self.wait(1.0)

        # Solve.
        ans = MathTex(
            r"x = \dfrac{\log 7}{\log 2} \approx 2.807",
            color=GREEN_OK,
        ).scale(1.2)
        ans.move_to(BAND_CHART_CENTER + DOWN * 1.3)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.3)
        ans_bg.move_to(ans.get_center())
        beat_2 = beat_group(beat_2, ans, ans_bg)
        self.play(FadeIn(ans_bg, run_time=0.4), Write(ans, run_time=2.0))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Case 2: unknown inside a log (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head3 = Text("Case 2: unknown inside a log",
                     font_size=26, color=BLUE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        beat_3 = beat_group(beat_3, head3, head3_bg)
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        eq2 = MathTex(r"\log_{2}(x) = 5", color=BLUE_TERM).scale(1.4)
        eq2.move_to(BAND_CHART_CENTER + UP * 0.5)
        eq2_bg = BackgroundRectangle(eq2, color=BLACK, fill_opacity=1, buff=0.3)
        eq2_bg.move_to(eq2.get_center())
        beat_3 = beat_group(beat_3, eq2, eq2_bg)
        self.play(FadeIn(eq2_bg, run_time=0.4), Write(eq2, run_time=1.4))
        self.wait(1.0)

        eq3 = MathTex(
            r"x = 2^{5} = 32",
            color=GREEN_OK,
        ).scale(1.2)
        eq3.next_to(eq2, DOWN, buff=0.5)
        eq3_bg = BackgroundRectangle(eq3, color=BLACK, fill_opacity=1, buff=0.25)
        eq3_bg.move_to(eq3.get_center())
        beat_3 = beat_group(beat_3, eq3, eq3_bg)
        self.play(FadeIn(eq3_bg, run_time=0.4), Write(eq3, run_time=1.6))
        self.wait(1.0)

        tip = Text(
            "If the right side is already a power of the base, match powers.",
            font_size=22, color=ORANGE_TERM,
        ).next_to(eq3, DOWN, buff=0.5)
        tip_bg = BackgroundRectangle(tip, color=BLACK, fill_opacity=0.95, buff=0.15)
        tip_bg.move_to(tip.get_center())
        beat_3 = beat_group(beat_3, tip, tip_bg)
        self.play(FadeIn(tip_bg, run_time=0.3), FadeIn(tip, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: writing log(2^x) = x without the power law (~16 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\log(2^{x}) = x\;\text{?}",
            color=RED_REJECT,
        ).scale(1.2)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.4),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        right = MathTex(
            r"\log(2^{x}) = x\,\log(2)",
            color=GREEN_OK,
        ).scale(1.1)
        right.next_to(wrong, DOWN, buff=0.5)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=1, buff=0.25)
        right_bg.move_to(right.get_center())
        beat_4 = beat_group(beat_4, right, right_bg)
        self.play(FadeIn(right_bg, run_time=0.3), Write(right, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=38 s, total ≈ 85.1 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{In exponent} \to \log;\ \text{in log} \to \text{exp}",
            "Pick the operation that undoes what wraps the variable.",
            final_wait=38.0,
        )
