"""
Manim scene for the lesson `bisection`
(topic `l10a-aa-algorithms-simulations`).

Bisection finds a root of a continuous function by halving an interval
where f(a) and f(b) have opposite signs. The animation shows the
sign-of-product rule, a worked example on f(x) = x^3 - x - 2 in [1, 2],
and rejects the mistake of not checking that the endpoints straddle zero.

Target duration: ~77.6 s (matches the audio narration length).
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


class BisectionScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Bisection: trapping a root",
            "Cut the interval in half until the root is boxed in.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The sign-of-product rule (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Opposite signs ⇒ root inside",
                    font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.5)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        # Visual: a number line with a (positive) and b (negative).
        line = Line([-5.0, 0.0, 0.0], [5.0, 0.0, 0.0], color=WHITE, stroke_width=2)
        a_dot = Dot([-3.0, 0.0, 0.0], color=BLUE_TERM, radius=0.09)
        b_dot = Dot([3.0, 0.0, 0.0], color=ORANGE_TERM, radius=0.09)
        a_lbl = MathTex("a", color=BLUE_TERM).scale(0.9).next_to(a_dot, UP, buff=0.15)
        b_lbl = MathTex("b", color=ORANGE_TERM).scale(0.9).next_to(b_dot, UP, buff=0.15)
        f_a = MathTex("f(a) > 0", color=BLUE_TERM).scale(0.8).next_to(a_dot, DOWN, buff=0.18)
        f_b = MathTex("f(b) < 0", color=ORANGE_TERM).scale(0.8).next_to(b_dot, DOWN, buff=0.18)
        for m in (a_lbl, b_lbl, f_a, f_b):
            mb = BackgroundRectangle(m, color=BLACK, fill_opacity=0.9, buff=0.08)
            mb.move_to(m.get_center())
            m.bg = mb
            beat_2 = beat_group(beat_2, m, mb)

        zone = Line([-3.0, 0.0, 0.0], [3.0, 0.0, 0.0], color=GREEN_OK, stroke_width=6)
        zone.set_z_index(0)
        beat_2 = beat_group(beat_2, line, a_dot, b_dot, a_lbl, b_lbl, f_a, f_b, zone)

        self.play(Create(line), run_time=1.0)
        self.play(Create(zone), run_time=1.0)
        self.play(FadeIn(a_dot), FadeIn(b_dot), run_time=0.4)
        for m in (a_lbl, b_lbl, f_a, f_b):
            self.play(FadeIn(m.bg, run_time=0.2), FadeIn(m, run_time=0.5))
        self.wait(1.5)

        # Rule card.
        rule = make_equation_card(
            r"\text{if } f(a)\,f(b) < 0 \!\Rightarrow\! r \in (a,b)",
            color=GREEN_OK, scale=0.7,
        )
        rule.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        beat_2 = beat_group(beat_2, rule)
        self.play(FadeIn(rule, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: root of f(x) = x^3 - x - 2 in [1, 2] (~24 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        # f(x) = x^3 - x - 2. f(1) = -2, f(2) = 4. Midpoint m = 1.5.
        f_def = MathTex(
            r"f(x) = x^{3} - x - 2",
            color=BLUE_TERM,
        ).scale(1.0)
        f_def.move_to(BAND_CHART_CENTER + UP * 1.0)
        f_def_bg = BackgroundRectangle(f_def, color=BLACK, fill_opacity=1, buff=0.25)
        f_def_bg.move_to(f_def.get_center())
        beat_3 = beat_group(beat_3, f_def, f_def_bg)
        self.play(FadeIn(f_def_bg, run_time=0.4), Write(f_def, run_time=1.6))
        self.wait(1.0)

        # Step 1: evaluate at endpoints.
        step1 = MathTex(
            r"f(1) = -2,\;\; f(2) = 4",
            color=BLUE_TERM,
        ).scale(1.0)
        step1.next_to(f_def, DOWN, buff=0.5)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=1, buff=0.2)
        step1_bg.move_to(step1.get_center())
        beat_3 = beat_group(beat_3, step1, step1_bg)
        self.play(FadeIn(step1_bg, run_time=0.4), Write(step1, run_time=1.6))
        self.wait(1.0)

        # Step 2: midpoint.
        step2 = MathTex(
            r"m = \tfrac{1 + 2}{2} = 1.5,\;\; f(1.5) = 1.5^{3} - 1.5 - 2 = -0.125",
            color=GREEN_OK,
        ).scale(0.9)
        step2.next_to(step1, DOWN, buff=0.5)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=1, buff=0.2)
        step2_bg.move_to(step2.get_center())
        beat_3 = beat_group(beat_3, step2, step2_bg)
        self.play(FadeIn(step2_bg, run_time=0.4), Write(step2, run_time=1.8))
        self.wait(1.5)

        # Clear the calculation stack before showing the new interval.
        calculation = beat_group(f_def, f_def_bg, step1, step1_bg, step2, step2_bg)
        self.play(FadeOut(calculation, run_time=0.5))
        self.wait(0.2)

        # Step 3: f(1.5) < 0, matches f(1), so root is in (1.5, 2).
        step3 = MathTex(
            r"\text{new interval: } (1.5,\; 2)",
            color=GREEN_OK,
        ).scale(1.0)
        step3.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        step3_bg = BackgroundRectangle(step3, color=BLACK, fill_opacity=1, buff=0.2)
        step3_bg.move_to(step3.get_center())
        beat_3 = beat_group(beat_3, step3, step3_bg)
        self.play(FadeIn(step3_bg, run_time=0.4), Write(step3, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: endpoints with same sign (~16 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"f(a) \cdot f(b) > 0 \;\Rightarrow\; \text{root in } (a,b)\;\text{?}",
            color=RED_REJECT,
        ).scale(0.95)
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

        fix = Text(
            "Same sign on both ends ⇒ no guaranteed root there.",
            font_size=22, color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        beat_4 = beat_group(beat_4, fix, fix_bg)
        self.play(FadeIn(fix_bg, run_time=0.3), FadeIn(fix, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=35 s, total ≈ 77.6 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Bisection: half the interval whose ends have opposite signs}",
            "Each step shrinks the bracket; ~20 steps ⇒ accuracy to a millionth.",
            final_wait=35.0,
        )
