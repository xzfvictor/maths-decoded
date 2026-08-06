"""
Manim scene for the lesson `proportion-rates`
(topic `l9-m-modelling-proportion`).

Direct proportion $y = kx$ scales by a constant rate. The animation
works a wage example, generalises to the unit-rate idea, and rejects
the trap of trying to add the rate instead of multiplying.

The audio narrative runs ~33 s; the scene is paced to match.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ProportionRatesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Direct proportion & rates",
            "y = kx. Find the unit rate, then scale up or down.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Worked example: wage rate (~8 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        given = Text("Worker earns $180 in 6 hours.",
                     font_size=20, color=BLUE_TERM)
        given.move_to(BAND_CHART_CENTER + UP * 1.4)
        given_bg = BackgroundRectangle(given, color=BLACK, fill_opacity=1, buff=0.2)
        given_bg.move_to(given.get_center())
        beat_2.add(given, given_bg)
        self.play(FadeIn(given_bg, run_time=0.4), FadeIn(given, run_time=1.0))
        self.wait(0.4)

        # Step 1: rate per hour.
        rate = MathTex(
            r"\text{rate} = \dfrac{\$180}{6 \text{ h}} = \$30 / \text{h}",
            color=GREEN_OK,
        ).scale(0.85)
        rate.move_to(BAND_CHART_CENTER + UP * 0.4)
        rate_bg = BackgroundRectangle(rate, color=BLACK, fill_opacity=1, buff=0.25)
        rate_bg.move_to(rate.get_center())
        beat_2.add(rate, rate_bg)
        self.play(FadeIn(rate_bg, run_time=0.4), Write(rate, run_time=1.6))
        self.wait(0.4)

        # Step 2: scale to 11 hours.
        scale = MathTex(
            r"\$30/\text{h} \times 11 \text{ h} = \$330",
            color=GREEN_OK,
        ).scale(0.85)
        scale.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        scale_bg = BackgroundRectangle(scale, color=BLACK, fill_opacity=1, buff=0.25)
        scale_bg.move_to(scale.get_center())
        beat_2.add(scale, scale_bg)
        self.play(FadeIn(scale_bg, run_time=0.4), Write(scale, run_time=1.6))
        self.wait(0.4)

        # Highlight the answer.
        ans_box = SurroundingRectangle(scale, color=GREEN_OK, buff=0.3, stroke_width=3)
        beat_2.add(ans_box)
        self.play(Create(ans_box, run_time=0.9))
        self.wait(0.6)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: y = kx (~7 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        formula = MathTex(r"y = k\,x", color=GREEN_OK).scale(1.0)
        formula.move_to(BAND_CHART_CENTER + UP * 1.4)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.25)
        formula_bg.move_to(formula.get_center())
        beat_3.add(formula, formula_bg)
        self.play(FadeIn(formula_bg, run_time=0.4), Write(formula, run_time=1.4))
        self.wait(0.4)

        notes = VGroup(
            Text("k = unit rate  (y per one x)", font_size=18, color=WHITE),
            Text("Scale up:  multiply by k",  font_size=18, color=BLUE_TERM),
            Text("Scale down:  divide by k",  font_size=18, color=TEAL_TERM),
        ).arrange(DOWN, buff=0.35)
        notes.move_to(BAND_CHART_CENTER + DOWN * 0.4)
        for n in notes:
            n_bg = BackgroundRectangle(n, color=BLACK, fill_opacity=0.95, buff=0.15)
            n_bg.move_to(n.get_center())
            beat_3.add(n, n_bg)
            self.play(FadeIn(n_bg, run_time=0.3), FadeIn(n, run_time=0.7))
            self.wait(0.3)

        self.wait(0.6)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: adding the rate instead of multiplying (~5 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        bad = MathTex(
            r"\$180 + \$30 \times 11 \;=\; ??",
            color=RED_REJECT,
        ).scale(0.85)
        bad.move_to(BAND_CHART_CENTER + UP * 0.6)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        beat_4.add(bad, bad_bg)
        self.play(FadeIn(bad_bg, run_time=0.4), Write(bad, run_time=1.4))
        self.wait(0.3)

        bad_note = Text(
            "Don't add the total — scale from the unit rate.",
            font_size=18, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.4)
        bad_note_bg = BackgroundRectangle(bad_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        bad_note_bg.move_to(bad_note.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        beat_4.add(cross, bad_note, bad_note_bg)
        self.play(Create(cross, run_time=0.9))
        self.play(FadeIn(bad_note_bg, run_time=0.4), FadeIn(bad_note, run_time=0.9))
        self.wait(0.6)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y = k\,x \quad (k = \text{unit rate})",
            "Find k from one pair; multiply to scale up, divide to scale down.",
            final_wait=65.8,
        )
