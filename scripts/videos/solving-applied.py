"""
Manim scene for the lesson `solving-applied`
(topic `l10a-aa-factorising-quadratics`).

Apply quadratic factoring to a real-world problem: "A rectangle has
length (x + 5) m and width (x - 2) m, with area 24 m². Find x."
The animation walks through define → equation → factor → solve → check,
and rejects the mistake of accepting a negative or zero length.

Target duration: ~88.8 s (matches the audio narration length).
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


class SolvingAppliedScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Solving applied quadratic problems",
            "Define → model → factorise → solve → check the context.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Set up the problem (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Rectangle: length (x+5), width (x−2), area 24",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        # Translate to equation: (x+5)(x-2) = 24.
        eq = MathTex(
            r"(x + 5)(x - 2) = 24",
            color=BLUE_TERM,
        ).scale(1.2)
        eq.move_to(BAND_CHART_CENTER + UP * 0.5)
        eq_bg = BackgroundRectangle(eq, color=BLACK, fill_opacity=1, buff=0.25)
        eq_bg.move_to(eq.get_center())
        beat_2 = beat_group(beat_2, eq, eq_bg)
        self.play(FadeIn(eq_bg, run_time=0.4), Write(eq, run_time=1.6))
        self.wait(1.0)

        # Move to standard form.
        expand = MathTex(
            r"x^{2} + 3x - 10 = 24",
            color=ORANGE_TERM,
        ).scale(1.1)
        expand.next_to(eq, DOWN, buff=0.5)
        expand_bg = BackgroundRectangle(expand, color=BLACK, fill_opacity=1, buff=0.25)
        expand_bg.move_to(expand.get_center())
        beat_2 = beat_group(beat_2, expand, expand_bg)
        self.play(FadeIn(expand_bg, run_time=0.4), Write(expand, run_time=1.4))
        self.wait(1.0)

        standard = MathTex(
            r"x^{2} + 3x - 34 = 0",
            color=GREEN_OK,
        ).scale(1.2)
        standard.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        standard_bg = BackgroundRectangle(standard, color=BLACK, fill_opacity=1, buff=0.3)
        standard_bg.move_to(standard.get_center())
        beat_2 = beat_group(beat_2, standard, standard_bg)
        self.play(FadeIn(standard_bg, run_time=0.4), Write(standard, run_time=1.6))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Solve with the quadratic formula (~24 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        # x² + 3x - 34 = 0. Discriminant = 9 + 136 = 145. Not a clean factor.
        # Use quadratic formula.
        qf = MathTex(
            r"x = \dfrac{-3 \pm \sqrt{9 + 136}}{2} = \dfrac{-3 \pm \sqrt{145}}{2}",
            color=BLUE_TERM,
        ).scale(0.9)
        qf.move_to(BAND_CHART_CENTER + UP * 0.6)
        qf_bg = BackgroundRectangle(qf, color=BLACK, fill_opacity=1, buff=0.25)
        qf_bg.move_to(qf.get_center())
        beat_3 = beat_group(beat_3, qf, qf_bg)
        self.play(FadeIn(qf_bg, run_time=0.4), Write(qf, run_time=2.0))
        self.wait(1.0)

        # Numerical approximations.
        num = MathTex(
            r"x \approx 4.52 \;\text{ or }\; x \approx -7.52",
            color=GREEN_OK,
        ).scale(1.0)
        num.next_to(qf, DOWN, buff=0.5)
        num_bg = BackgroundRectangle(num, color=BLACK, fill_opacity=1, buff=0.25)
        num_bg.move_to(num.get_center())
        beat_3 = beat_group(beat_3, num, num_bg)
        self.play(FadeIn(num_bg, run_time=0.4), Write(num, run_time=1.6))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: keeping the negative root (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(r"x = -7.52", color=RED_REJECT).scale(1.4)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.4)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.3)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.4),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        why = Text(
            "Width = x − 2 = −9.52  →  no such rectangle.",
            font_size=22, color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        beat_4 = beat_group(beat_4, why, why_bg)
        self.play(FadeIn(why_bg, run_time=0.3), FadeIn(why, run_time=1.2))
        self.wait(1.0)

        ok = MathTex(
            r"\text{Keep only } x = 4.52",
            color=GREEN_OK,
        ).scale(1.1)
        ok.next_to(why, DOWN, buff=0.5)
        ok_bg = BackgroundRectangle(ok, color=BLACK, fill_opacity=1, buff=0.25)
        ok_bg.move_to(ok.get_center())
        beat_4 = beat_group(beat_4, ok, ok_bg)
        self.play(FadeIn(ok_bg, run_time=0.3), Write(ok, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=40 s, total ≈ 88.8 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Define } \to \text{model} \to \text{factor/solve} \to \text{check the context}",
            "Reject any solution that violates the real-world constraints.",
            final_wait=40.0,
        )
