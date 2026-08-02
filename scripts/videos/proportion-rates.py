"""
Manim scene for the lesson `proportion-rates`
(topic `l9-m-modelling-proportion`).

Direct proportion $y = kx$ scales by a constant rate. The animation
works through a wage example, generalises to the unit-rate idea, and
rejects the trap of using the wrong arithmetic operation.

Render target: ~92.38 s, matched to the audio narration length.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ProportionRatesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (visible for entire animation) + intro (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Direct proportion & rates",
            "y = kx. Find the unit rate, then scale up or down.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Worked example: wage rate (~28 s)
        # ──────────────────────────────────────────────────────────────────
        # Given: 6 hours → $180.  Find: 11 hours → ?
        given = Text("Worker earns $180 in 6 hours.",
                     font_size=22, color=BLUE_TERM)
        given.move_to(BAND_CHART_CENTER + UP * 1.6)
        given_bg = BackgroundRectangle(given, color=BLACK, fill_opacity=1, buff=0.2)
        given_bg.move_to(given.get_center())
        self.play(FadeIn(given_bg, run_time=0.4), FadeIn(given, run_time=1.2))
        self.wait(1.0)

        # Step 1: rate per hour.
        rate = MathTex(
            r"\text{rate} \;=\; \dfrac{\$180}{6 \text{ h}} \;=\; \$30 / \text{h}",
            color=GREEN_OK,
        ).scale(0.95)
        rate.move_to(BAND_CHART_CENTER + UP * 0.5)
        rate_bg = BackgroundRectangle(rate, color=BLACK, fill_opacity=1, buff=0.25)
        rate_bg.move_to(rate.get_center())
        self.play(FadeIn(rate_bg, run_time=0.5), Write(rate, run_time=2.0))
        self.wait(2.0)

        # Step 2: scale to 11 hours.
        scale = MathTex(
            r"\$30/\text{h} \times 11 \text{ h} \;=\; \$330",
            color=GREEN_OK,
        ).scale(0.95)
        scale.move_to(BAND_CHART_CENTER + DOWN * 0.3)
        scale_bg = BackgroundRectangle(scale, color=BLACK, fill_opacity=1, buff=0.25)
        scale_bg.move_to(scale.get_center())
        self.play(FadeIn(scale_bg, run_time=0.5), Write(scale, run_time=2.0))
        self.wait(2.0)

        # Highlight the answer.
        ans_box = SurroundingRectangle(scale, color=GREEN_OK, buff=0.3, stroke_width=3)
        self.play(Create(ans_box, run_time=1.0))
        self.wait(1.5)

        self.play(
            FadeOut(given, run_time=0.6),
            FadeOut(given_bg, run_time=0.6),
            FadeOut(rate, run_time=0.6),
            FadeOut(rate_bg, run_time=0.6),
            FadeOut(scale, run_time=0.6),
            FadeOut(scale_bg, run_time=0.6),
            FadeOut(ans_box, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise to y = kx (~20 s)
        # ──────────────────────────────────────────────────────────────────
        formula = MathTex(r"y \;=\; k\,x", color=GREEN_OK).scale(1.2)
        formula.move_to(BAND_CHART_CENTER + UP * 1.4)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.25)
        formula_bg.move_to(formula.get_center())
        self.play(FadeIn(formula_bg, run_time=0.5), Write(formula, run_time=1.8))
        self.wait(2.0)

        notes = VGroup(
            Text("k = unit rate  (y per one x)", font_size=22, color=WHITE),
            Text("Scale up:  multiply by k",  font_size=22, color=BLUE_TERM),
            Text("Scale down:  divide by k",  font_size=22, color=TEAL_TERM),
        ).arrange(DOWN, buff=0.4)
        notes.move_to(BAND_CHART_CENTER + DOWN * 0.2)
        for n in notes:
            n_bg = BackgroundRectangle(n, color=BLACK, fill_opacity=0.95, buff=0.15)
            n_bg.move_to(n.get_center())
            self.play(FadeIn(n_bg, run_time=0.4), FadeIn(n, run_time=0.9))
            self.wait(0.8)

        self.wait(2.0)

        self.play(
            FadeOut(formula, run_time=0.6),
            FadeOut(formula_bg, run_time=0.6),
            *[FadeOut(n, run_time=0.6) for n in notes],
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: adding the rate instead of multiplying (~14 s)
        # ──────────────────────────────────────────────────────────────────
        bad = MathTex(
            r"\$180 \;+\; \$30 \times 11 \;=\; ??",
            color=RED_REJECT,
        ).scale(0.95)
        bad.move_to(BAND_CHART_CENTER + UP * 0.5)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.5), Write(bad, run_time=1.8))
        self.wait(1.0)

        bad_note = Text("Don't add the total — scale from the unit rate.",
                        font_size=20, color=RED_REJECT)
        bad_note.next_to(bad, DOWN, buff=0.5)
        bad_note_bg = BackgroundRectangle(bad_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        bad_note_bg.move_to(bad_note.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=1.0))
        self.play(FadeIn(bad_note_bg, run_time=0.4), FadeIn(bad_note, run_time=1.2))
        self.wait(2.5)

        self.play(
            FadeOut(bad, run_time=0.8),
            FadeOut(bad_bg, run_time=0.8),
            FadeOut(cross, run_time=0.8),
            FadeOut(bad_note, run_time=0.8),
            FadeOut(bad_note_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~final_wait = 35 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y \;=\; k\,x \quad (k = \text{unit rate})",
            "Find k from one pair; multiply to scale up, divide to scale down.",
            final_wait=35.0,
        )