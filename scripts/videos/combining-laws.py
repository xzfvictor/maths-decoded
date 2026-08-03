"""
Manim scene for the lesson `combining-laws`
(topic `l10a-an-fractional-exponents`).

Combine the power laws with fractional exponents: a^(m/n) = (a^(1/n))^m
= n-th root of a^m. Show 8^(2/3) worked two ways. Reject the "just halve
the exponent" mistake.

Target duration: ~86 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *
import numpy as np


class CombiningLawsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Combining exponent laws",
            "Fractional exponents combine the power and root laws",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Start with a^(m/n) and apply m first, then n (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        start = MathTex(r"8^{2/3}", color=BLUE_TERM).scale(1.2)
        start.move_to(BAND_CHART_CENTER + UP * 1.0)
        start_bg = BackgroundRectangle(start, color=BLACK, fill_opacity=1, buff=0.25)
        start_bg.move_to(start.get_center())
        beat_2 = beat_group(beat_2, start, start_bg)
        self.play(FadeIn(start_bg, run_time=0.4), Write(start, run_time=1.5))
        self.wait(1.0)

        # Method 1: power first, then root.
        way1 = MathTex(
            r"8^{2/3} = (8^{2})^{1/3} = 64^{1/3} = 4",
            color=GREEN_OK,
        ).scale(1.0)
        way1.next_to(start, DOWN, buff=0.5)
        way1_bg = BackgroundRectangle(way1, color=BLACK, fill_opacity=1, buff=0.2)
        way1_bg.move_to(way1.get_center())
        beat_2 = beat_group(beat_2, way1, way1_bg)
        self.play(FadeIn(way1_bg, run_time=0.4), Write(way1, run_time=1.8))
        self.wait(1.0)

        # Method 2: root first, then power.
        way2 = MathTex(
            r"8^{2/3} = (8^{1/3})^{2} = 2^{2} = 4",
            color=GREEN_OK,
        ).scale(1.0)
        way2.next_to(way1, DOWN, buff=0.5)
        way2_bg = BackgroundRectangle(way2, color=BLACK, fill_opacity=1, buff=0.2)
        way2_bg.move_to(way2.get_center())
        beat_2 = beat_group(beat_2, way2, way2_bg)
        self.play(FadeIn(way2_bg, run_time=0.4), Write(way2, run_time=1.8))
        self.wait(1.5)

        # Annotation that both work.
        note = Text("Both orders give the same answer.", font_size=22, color=BLUE_TERM)
        note.next_to(way2, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        beat_2 = beat_group(beat_2, note, note_bg)
        self.play(FadeIn(note_bg, run_time=0.3), FadeIn(note, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: a^(m/n) = n-th root of a^m (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        formula = MathTex(
            r"a^{m/n} = \left(a^{m}\right)^{1/n} = \sqrt[n]{a^{m}}",
            color=GREEN_OK,
        ).scale(1.0)
        formula.move_to(BAND_CHART_CENTER + UP * 0.6)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.3)
        formula_bg.move_to(formula.get_center())
        beat_3 = beat_group(beat_3, formula, formula_bg)
        self.play(FadeIn(formula_bg, run_time=0.4), Write(formula, run_time=2.0))
        self.wait(1.5)

        # Apply to a different example: 27^(2/3).
        ex2 = MathTex(
            r"27^{2/3} = \sqrt[3]{27^{2}} = \sqrt[3]{729} = 9",
            color=BLUE_TERM,
        ).scale(0.95)
        ex2.next_to(formula, DOWN, buff=0.5)
        ex2_bg = BackgroundRectangle(ex2, color=BLACK, fill_opacity=1, buff=0.2)
        ex2_bg.move_to(ex2.get_center())
        beat_3 = beat_group(beat_3, ex2, ex2_bg)
        self.play(FadeIn(ex2_bg, run_time=0.4), Write(ex2, run_time=1.8))
        self.wait(1.5)

        # Why m/n ≠ m/2.
        expl = Text("Don't divide the exponent by 2 — the n is the index, not 2.", font_size=22, color=GREEN_OK)
        expl.next_to(ex2, DOWN, buff=0.4)
        expl_bg = BackgroundRectangle(expl, color=BLACK, fill_opacity=0.95, buff=0.15)
        expl_bg.move_to(expl.get_center())
        beat_3 = beat_group(beat_3, expl, expl_bg)
        self.play(FadeIn(expl_bg, run_time=0.3), FadeIn(expl, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: halving the exponent (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"8^{2/3} = 8^{1/3} = 2?",
            color=RED_REJECT,
        ).scale(1.1)
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

        right = Text(
            "8^(2/3) means take the cube root of 8, then square: 2² = 4.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=0.95, buff=0.18)
        right_bg.move_to(right.get_center())
        beat_4 = beat_group(beat_4, right, right_bg)
        self.play(FadeIn(right_bg, run_time=0.3), FadeIn(right, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~38 s, total ≈ 86 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{m/n} = \sqrt[n]{a^{m}} = \left(\sqrt[n]{a}\right)^{m}",
            "The denominator is the root; the numerator is the power.",
            final_wait=38.0,
        )
