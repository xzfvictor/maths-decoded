"""
Manim scene for the lesson `one-solution`
(topic `l10a-asp-trig-equations`).

Solving sin(theta) = alpha in [0, 2 pi) gives two answers in general,
but only one when alpha = 1 or alpha = 0. The animation builds the
recipe step by step and lands the "one solution" case as a contrast.

Target duration: ~80 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class OneSolutionScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Solving trig equations with one solution",
            "Sin(theta) = alpha in [0, 2pi) usually gives two answers.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The question: sin(theta) = 0.5 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        eq = make_equation_card(r"\sin(\theta) \;=\; 0.5", color=BLUE_TERM, scale=1.1)
        eq.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(eq, run_time=1.4))
        self.wait(3.0)

        # The principal angle pi/6.
        principal = MathTex(r"\alpha = \dfrac{\pi}{6}", color=BLUE_TERM).scale(1.0)
        principal.next_to(eq, DOWN, buff=0.6)
        principal_bg = BackgroundRectangle(principal, color=BLACK, fill_opacity=0.95, buff=0.18)
        principal_bg.move_to(principal.get_center())
        self.play(FadeIn(principal_bg, run_time=0.4), FadeIn(principal, run_time=1.2))
        self.wait(4.0)

        # Where is sin positive? Quadrants I and II.
        where = Text("Sine is positive in quadrants I and II.", font_size=22, color=BLUE_TERM)
        where.next_to(principal, DOWN, buff=0.5)
        where_bg = BackgroundRectangle(where, color=BLACK, fill_opacity=0.95, buff=0.15)
        where_bg.move_to(where.get_center())
        self.play(FadeIn(where_bg, run_time=0.4), FadeIn(where, run_time=1.2))
        self.wait(6.0)

        beat1 = beat_group(eq, principal, principal_bg, where, where_bg)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Two solutions: pi/6 and 5pi/6 (~24 s)
        # ──────────────────────────────────────────────────────────────────
        ans1 = make_term_card(r"\dfrac{\pi}{6}", "Q I", BLUE_TERM)
        ans2 = make_term_card(r"\dfrac{5\pi}{6}", "Q II", TEAL_TERM)
        pair = VGroup(ans1, ans2).arrange(RIGHT, buff=1.2)
        pair.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in pair:
            m.set_z_index(2)
        self.play(FadeIn(ans1, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)
        self.play(FadeIn(ans2, shift=UP * 0.2, run_time=1.2))
        self.wait(4.0)

        # The two-quadrant relationship.
        rel = MathTex(
            r"\text{2nd answer} \;=\; \pi - \alpha",
            color=GREEN_OK,
        ).scale(0.95)
        rel.next_to(pair, DOWN, buff=0.7)
        rel_bg = BackgroundRectangle(rel, color=BLACK, fill_opacity=0.95, buff=0.18)
        rel_bg.move_to(rel.get_center())
        self.play(FadeIn(rel_bg, run_time=0.4), FadeIn(rel, run_time=1.4))
        self.wait(7.0)

        beat2 = beat_group(ans1, ans2, rel, rel_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Contrast: sin(theta) = 1 has only ONE solution (~22 s)
        # ──────────────────────────────────────────────────────────────────
        eq2 = make_equation_card(r"\sin(\theta) \;=\; 1", color=ORANGE_TERM, scale=1.1)
        eq2.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(eq2, run_time=1.4))
        self.wait(3.0)

        # The single answer.
        only = make_term_card(r"\dfrac{\pi}{2}", "Q II only", ORANGE_TERM)
        only.move_to(BAND_CHART_CENTER + DOWN * 0.3)
        only.set_z_index(2)
        self.play(FadeIn(only, shift=UP * 0.2, run_time=1.2))
        self.wait(3.5)

        # Why only one? Q I and Q II collapse to the same point.
        why = Text(
            "Q I and Q II answers meet at the same point.",
            font_size=22,
            color=ORANGE_TERM,
        ).next_to(only, DOWN, buff=0.7)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.15)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.2))
        self.wait(7.0)

        beat3 = beat_group(eq2, only, why, why_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~35 s, total ≈ 80 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\sin(\theta) = 1 \;\Rightarrow\; \theta = \dfrac{\pi}{2}",
            "Only one angle in [0, 2pi) — the two quadrants collapse.",
            final_wait=35.0,
        )
