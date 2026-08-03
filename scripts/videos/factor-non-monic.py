"""
Manim scene for the lesson `factor-non-monic`
(topic `l10a-aa-factorising-quadratics`).

Factorise a non-monic quadratic ax^2 + bx + c with the AC (split-the-
middle) method. The animation walks through 2x^2 + 7x + 3, splits the
middle using ac = 6 with m + n = 7, then factors by grouping. Rejects
forgetting to multiply back through when undoing the split.

Target duration: ~86.6 s (matches the audio narration length).
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


class FactorNonMonicScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Factorising non-monic quadratics",
            "AC method: split the middle, then factor by grouping.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: 2x^2 + 7x + 3, find ac = 6 (~24 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("AC method on 2x² + 7x + 3", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        eq = MathTex(r"2x^{2} + 7x + 3", color=BLUE_TERM).scale(1.3)
        eq.move_to(BAND_CHART_CENTER + UP * 0.5)
        eq_bg = BackgroundRectangle(eq, color=BLACK, fill_opacity=1, buff=0.3)
        eq_bg.move_to(eq.get_center())
        beat_2 = beat_group(beat_2, eq, eq_bg)
        self.play(FadeIn(eq_bg, run_time=0.4), Write(eq, run_time=1.6))
        self.wait(1.0)

        # Compute a * c.
        ac = MathTex(
            r"a \cdot c = 2 \cdot 3 = 6",
            color=ORANGE_TERM,
        ).scale(1.0)
        ac.next_to(eq, DOWN, buff=0.5)
        ac_bg = BackgroundRectangle(ac, color=BLACK, fill_opacity=1, buff=0.25)
        ac_bg.move_to(ac.get_center())
        beat_2 = beat_group(beat_2, ac, ac_bg)
        self.play(FadeIn(ac_bg, run_time=0.4), Write(ac, run_time=1.4))
        self.wait(1.0)

        # Find two numbers with product 6, sum 7.
        found = MathTex(
            r"1 \cdot 6 = 6,\quad 1 + 6 = 7",
            color=GREEN_OK,
        ).scale(1.0)
        found.next_to(ac, DOWN, buff=0.5)
        found_bg = BackgroundRectangle(found, color=BLACK, fill_opacity=1, buff=0.25)
        found_bg.move_to(found.get_center())
        beat_2 = beat_group(beat_2, found, found_bg)
        self.play(FadeIn(found_bg, run_time=0.4), Write(found, run_time=1.6))
        self.wait(1.5)

        # Split the middle.
        split = MathTex(
            r"2x^{2} + x + 6x + 3",
            color=GREEN_OK,
        ).scale(1.0)
        split.move_to(BAND_CHART_CENTER + DOWN * 1.4)
        split_bg = BackgroundRectangle(split, color=BLACK, fill_opacity=1, buff=0.25)
        split_bg.move_to(split.get_center())
        beat_2 = beat_group(beat_2, split, split_bg)
        self.play(FadeIn(split_bg, run_time=0.4), Write(split, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Factor by grouping (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head3 = Text("Factor by grouping", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        beat_3 = beat_group(beat_3, head3, head3_bg)
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        g1 = MathTex(
            r"x(2x + 1) + 3(2x + 1)",
            color=BLUE_TERM,
        ).scale(1.0)
        g1.move_to(BAND_CHART_CENTER + UP * 0.5)
        g1_bg = BackgroundRectangle(g1, color=BLACK, fill_opacity=1, buff=0.25)
        g1_bg.move_to(g1.get_center())
        beat_3 = beat_group(beat_3, g1, g1_bg)
        self.play(FadeIn(g1_bg, run_time=0.4), Write(g1, run_time=1.6))
        self.wait(1.5)

        g2 = MathTex(
            r"(2x + 1)(x + 3)",
            color=GREEN_OK,
        ).scale(1.5)
        g2.move_to(BAND_CHART_CENTER + DOWN * 0.7)
        g2_bg = BackgroundRectangle(g2, color=BLACK, fill_opacity=1, buff=0.3)
        g2_bg.move_to(g2.get_center())
        beat_3 = beat_group(beat_3, g2, g2_bg)
        self.play(FadeIn(g2_bg, run_time=0.4), Write(g2, run_time=1.6))
        self.wait(1.0)

        check = Text(
            "Quick check: (2x + 1)(x + 3) = 2x² + 7x + 3 ✓",
            font_size=22, color=ORANGE_TERM,
        ).next_to(g2, DOWN, buff=0.5)
        check_bg = BackgroundRectangle(check, color=BLACK, fill_opacity=0.95, buff=0.15)
        check_bg.move_to(check.get_center())
        beat_3 = beat_group(beat_3, check, check_bg)
        self.play(FadeIn(check_bg, run_time=0.3), FadeIn(check, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: forgetting to multiply back through (~16 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"2x^{2} + 7x + 3 = (2x + 1)(x + 3)\;\text{? skip the check?}",
            color=RED_REJECT,
        ).scale(0.85)
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
            "Always expand back to confirm the middle term is b.",
            font_size=22, color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        beat_4 = beat_group(beat_4, fix, fix_bg)
        self.play(FadeIn(fix_bg, run_time=0.3), FadeIn(fix, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=39 s, total ≈ 86.6 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"ax^{2} + bx + c:\ mn = ac,\ m+n = b",
            "Split the middle, then factor by grouping.",
            final_wait=39.0,
        )
