"""
Manim scene for the lesson `sampling-variation`
(topic `l8-st-comparing-samples`).

Two random samples from the same population will not give identical
results — that natural difference is called sampling variation. It is
not a mistake; the variation shrinks as the sample size grows.

Render target: ~101 s, matched to the audio narration length. The
title stays at the top of the frame as a constant header.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class SamplingVariationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (CONSTANT header)
        # ──────────────────────────────────────────────────────────────────
        title_group = animate_intro(
            self,
            "Sampling variation",
            "Two samples from one population — different by chance.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: two samples give two different means (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None  # VGroup accumulator for beat 2

        # Sample A (165 cm) — show alone, then fade before showing Sample B.
        sample_a = make_term_card(r"165 \text{ cm}", "Sample A", BLUE_TERM)
        sample_a.move_to(BAND_CHART_CENTER + UP * 1.2)
        self.play(FadeIn(sample_a, shift=UP * 0.3, run_time=1.4))
        self.wait(2.0)
        beat_2 = beat_group(sample_a)
        self.play(FadeOut(beat_2, run_time=0.8))
        beat_2 = None

        # Sample B (163 cm) — show alone.
        sample_b = make_term_card(r"163 \text{ cm}", "Sample B", TEAL_TERM)
        sample_b.move_to(BAND_CHART_CENTER + UP * 1.2)
        self.play(FadeIn(sample_b, shift=UP * 0.3, run_time=1.4))
        self.wait(2.0)
        beat_2 = beat_group(sample_b)
        self.play(FadeOut(beat_2, run_time=0.8))
        beat_2 = None

        # True mean (164 cm).
        truth = MathTex(
            r"\text{True mean} = 164 \text{ cm}",
            color=GREEN_OK,
        ).scale(0.95)
        truth_bg = BackgroundRectangle(truth, color=BLACK, fill_opacity=1, buff=0.25)
        truth_bg.move_to(truth.get_center())
        truth.move_to(BAND_CHART_CENTER + UP * 0.8)
        self.play(
            FadeIn(truth_bg, run_time=0.5),
            Write(truth, run_time=1.4),
        )
        self.wait(3.0)
        beat_2 = beat_group(truth, truth_bg)
        self.play(FadeOut(beat_2, run_time=0.8))
        beat_2 = None

        # Gap (165 - 163 = 2 cm).
        gap = MathTex(
            r"165 - 163 = 2 \text{ cm}",
            color=ORANGE_TERM,
        ).scale(0.9)
        gap_bg = BackgroundRectangle(gap, color=BLACK, fill_opacity=0.95, buff=0.2)
        gap_bg.move_to(gap.get_center())
        gap.move_to(BAND_CHART_CENTER + UP * 0.8)
        self.play(
            FadeIn(gap_bg, run_time=0.5),
            Write(gap, run_time=1.4),
        )
        self.wait(3.0)
        beat_2 = beat_group(gap, gap_bg)

        # End of beat 2 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalisation: variations across many samples (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None  # VGroup accumulator for beat 3

        # Spread of sample means visualisation with 8 dots spread around truth.
        spread = MathTex(
            r"\bar{x}_1,\; \bar{x}_2,\; \ldots,\; \bar{x}_{10}",
            color=BLUE_TERM,
        ).scale(1.1)
        spread.move_to(BAND_CHART_CENTER + UP * 1.2)
        spread_bg = BackgroundRectangle(spread, color=BLACK, fill_opacity=1, buff=0.28)
        spread_bg.move_to(spread.get_center())
        self.play(
            FadeIn(spread_bg, run_time=0.5),
            Write(spread, run_time=1.6),
        )
        self.wait(2.0)
        beat_3 = beat_group(spread, spread_bg)
        self.play(FadeOut(beat_3, run_time=0.8))
        beat_3 = None

        truth2 = MathTex(
            r"\mu \;(\text{true population mean})",
            color=GREEN_OK,
        ).scale(0.95)
        truth2.move_to(BAND_CHART_CENTER + UP * 0.8)
        truth2_bg = BackgroundRectangle(truth2, color=BLACK, fill_opacity=1, buff=0.25)
        truth2_bg.move_to(truth2.get_center())
        self.play(
            FadeIn(truth2_bg, run_time=0.5),
            Write(truth2, run_time=1.4),
        )
        self.wait(2.0)
        beat_3 = beat_group(truth2, truth2_bg)
        self.play(FadeOut(beat_3, run_time=0.8))
        beat_3 = None

        # Key claim: each sample mean is just an estimate
        claim = MathTex(
            r"\text{Sample mean} \;\; \neq \;\; \text{population mean}",
            color=ORANGE_TERM,
        ).scale(0.95)
        claim.move_to(BAND_CHART_CENTER + UP * 0.8)
        claim_bg = BackgroundRectangle(claim, color=BLACK, fill_opacity=1, buff=0.25)
        claim_bg.move_to(claim.get_center())
        self.play(
            FadeIn(claim_bg, run_time=0.5),
            Write(claim, run_time=1.4),
        )
        self.wait(3.0)
        beat_3 = beat_group(claim, claim_bg)

        # End of beat 3 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: don't conclude a real population difference from
        # one sample comparison (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None  # VGroup accumulator for beat 4

        bad = Text(
            "Two samples disagree?",
            font_size=28, color=RED_REJECT,
        )
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        bad.move_to(BAND_CHART_CENTER + UP * 1.2)
        self.play(
            FadeIn(bad_bg, run_time=0.5),
            FadeIn(bad, run_time=1.2),
        )
        self.wait(1.5)
        beat_4 = beat_group(bad, bad_bg)
        self.play(FadeOut(beat_4, run_time=0.8))
        beat_4 = None

        conclusion = MathTex(
            r"\text{Therefore they came from different populations?}",
            color=RED_REJECT,
        ).scale(0.85)
        conclusion_bg = BackgroundRectangle(conclusion, color=BLACK, fill_opacity=1, buff=0.25)
        conclusion_bg.move_to(conclusion.get_center())
        conclusion.move_to(BAND_CHART_CENTER + UP * 0.8)
        self.play(
            FadeIn(conclusion_bg, run_time=0.5),
            Write(conclusion, run_time=1.4),
        )
        self.wait(2.0)
        beat_4 = beat_group(conclusion, conclusion_bg)

        cross = Cross(conclusion, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=1.0))
        self.wait(1.5)
        beat_4 = beat_group(conclusion, conclusion_bg, cross)

        # Fade the crossed-out conclusion before showing the fix.
        self.play(FadeOut(beat_4, run_time=0.8))
        beat_4 = None

        fix = MathTex(
            r"\text{Likely just sampling variation.}",
            color=GREEN_OK,
        ).scale(1.0)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=1, buff=0.28)
        fix_bg.move_to(fix.get_center())
        fix.move_to(BAND_CHART_CENTER + UP * 0.8)
        self.play(
            FadeIn(fix_bg, run_time=0.5),
            Write(fix, run_time=1.6),
        )
        self.wait(4.0)
        beat_4 = beat_group(fix, fix_bg)

        # End of beat 4 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\begin{gathered}\text{Sampling\;variation}\\[2pt]=\\[2pt]\text{by-chance\;difference\;between\;samples}\end{gathered}",
            "Always quote n with any sample statistic — variation shrinks as n grows.",
            final_wait=39.0,
        )