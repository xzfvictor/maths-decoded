"""
Manim scene for the lesson `change-of-base`
(topic `l10a-aa-exp-log-inverse`).

log_a(b) = log(b) / log(a). The animation derives the rule, applies it
to log_2(10), and rejects the mistake of swapping the numerator and
denominator.

Target duration: ~87.2 s (matches the audio narration length).
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


class ChangeOfBaseScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Change of base for logarithms",
            "log_a(b) = log(b) / log(a) — works for any base.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Derive the rule (~24 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Start with an unknown y", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        step1 = MathTex(
            r"\log_{a}(b) = y",
            color=BLUE_TERM,
        ).scale(1.1)
        step1.move_to(BAND_CHART_CENTER + UP * 0.7)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=1, buff=0.25)
        step1_bg.move_to(step1.get_center())
        beat_2 = beat_group(beat_2, step1, step1_bg)
        self.play(FadeIn(step1_bg, run_time=0.4), Write(step1, run_time=1.4))
        self.wait(1.0)

        step2 = MathTex(
            r"a^{y} = b",
            color=ORANGE_TERM,
        ).scale(1.1)
        step2.next_to(step1, DOWN, buff=0.5)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=1, buff=0.25)
        step2_bg.move_to(step2.get_center())
        beat_2 = beat_group(beat_2, step2, step2_bg)
        self.play(FadeIn(step2_bg, run_time=0.4), Write(step2, run_time=1.4))
        self.wait(1.0)

        step3 = MathTex(
            r"\log(a^{y}) = \log(b)",
            color=BLUE_TERM,
        ).scale(1.0)
        step3.next_to(step2, DOWN, buff=0.5)
        step3_bg = BackgroundRectangle(step3, color=BLACK, fill_opacity=1, buff=0.25)
        step3_bg.move_to(step3.get_center())
        beat_2 = beat_group(beat_2, step3, step3_bg)
        self.play(FadeIn(step3_bg, run_time=0.4), Write(step3, run_time=1.4))
        self.wait(1.0)

        # Clear the derivation before revealing the solved form so the
        # intermediate y = b fragment cannot cross-fade through the result.
        derivation = beat_group(step1, step1_bg, step2, step2_bg, step3, step3_bg)
        self.play(FadeOut(derivation, run_time=0.6))
        self.wait(0.2)

        # Final formula.
        result = MathTex(
            r"y = \dfrac{\log(b)}{\log(a)}",
            color=GREEN_OK,
        ).scale(1.2)
        result.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=1, buff=0.25)
        result_bg.move_to(result.get_center())
        beat_2 = beat_group(beat_2, result, result_bg)
        self.play(FadeIn(result_bg, run_time=0.4), Write(result, run_time=1.8))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: log_2(10) (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        ex = MathTex(
            r"\log_{2}(10) = \dfrac{\log 10}{\log 2}",
            color=BLUE_TERM,
        ).scale(1.1)
        ex.move_to(BAND_CHART_CENTER + UP * 0.7)
        ex_bg = BackgroundRectangle(ex, color=BLACK, fill_opacity=1, buff=0.25)
        ex_bg.move_to(ex.get_center())
        beat_3 = beat_group(beat_3, ex, ex_bg)
        self.play(FadeIn(ex_bg, run_time=0.4), Write(ex, run_time=1.6))
        self.wait(1.0)

        ans = MathTex(
            r"= \dfrac{1}{0.30103} \approx 3.3219",
            color=GREEN_OK,
        ).scale(1.1)
        ans.next_to(ex, DOWN, buff=0.5)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.25)
        ans_bg.move_to(ans.get_center())
        beat_3 = beat_group(beat_3, ans, ans_bg)
        self.play(FadeIn(ans_bg, run_time=0.4), Write(ans, run_time=1.8))
        self.wait(1.5)

        tip = Text(
            "Use base 10 for hand calc; use base e in growth / decay.",
            font_size=22, color=ORANGE_TERM,
        ).next_to(ans, DOWN, buff=0.5)
        tip_bg = BackgroundRectangle(tip, color=BLACK, fill_opacity=0.95, buff=0.15)
        tip_bg.move_to(tip.get_center())
        beat_3 = beat_group(beat_3, tip, tip_bg)
        self.play(FadeIn(tip_bg, run_time=0.3), FadeIn(tip, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: swapping numerator and denominator (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\log_{2}(10) = \dfrac{\log 2}{\log 10}\;\text{?}",
            color=RED_REJECT,
        ).scale(1.2)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.6),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        # Compare with the actual values.
        cmp = MathTex(
            r"\dfrac{\log 10}{\log 2} \approx 3.32,\quad \dfrac{\log 2}{\log 10} \approx 0.301",
            color=GREEN_OK,
        ).scale(0.85)
        cmp.next_to(wrong, DOWN, buff=0.5)
        cmp_bg = BackgroundRectangle(cmp, color=BLACK, fill_opacity=1, buff=0.2)
        cmp_bg.move_to(cmp.get_center())
        beat_4 = beat_group(beat_4, cmp, cmp_bg)
        self.play(FadeIn(cmp_bg, run_time=0.3), Write(cmp, run_time=1.5))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=39 s, total ≈ 87.2 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\log_{a}(b) = \dfrac{\log(b)}{\log(a)}",
            "Argument on top, base on the bottom — always.",
            final_wait=39.0,
        )
