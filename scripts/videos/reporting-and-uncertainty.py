"""
Manim scene for the lesson `reporting-and-uncertainty`
(topic `l8-st-statistical-investigations`).

A statistical report tells a story about what the numbers mean and how
much we should trust them: state the question, the sample, the method,
and acknowledge uncertainty. Reject over-claiming from a small sample.

Target duration: ~77.8 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, PURPLE_ACCENT, YELLOW_HIGHLIGHT, make_term_card,
    make_equation_card, animate_intro, animate_final_definition,
    beat_group,
)
from manim import *


class ReportingAndUncertaintyScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Reporting findings + acknowledging uncertainty",
            "State the sample, the method, and how much we trust the answer.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete report snippet (~17 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None
        # Pretend report line: "We surveyed 60 random Year 8 students..."
        line = MathTex(
            r"\text{``Based on a random sample of } n = 60 \text{ Year 8 students, }"
            r"\ldots\text{''}"
        ).scale(0.85)
        line.move_to(BAND_CHART_CENTER + UP * 0.9)
        line_bg = BackgroundRectangle(line, color=BLACK, fill_opacity=1, buff=0.25)
        line_bg.move_to(line.get_center())
        beat_2 = beat_group(beat_2, line_bg, line)

        self.play(
            FadeIn(line_bg, run_time=0.4),
            Write(line, run_time=2.4),
        )
        self.wait(3.0)

        # Estimate line: 8.1 hours sleep.
        est = MathTex(
            r"\text{we estimate } \bar{x} \approx 8.1 \text{ hours per school night.}",
            color=GREEN_OK,
        ).scale(0.85)
        est.next_to(line, DOWN, buff=0.5)
        est_bg = BackgroundRectangle(est, color=BLACK, fill_opacity=1, buff=0.25)
        est_bg.move_to(est.get_center())
        beat_2 = beat_group(beat_2, est_bg, est)
        self.play(FadeIn(est_bg, run_time=0.4), FadeIn(est, run_time=2.0))
        self.wait(3.0)

        # Uncertainty line.
        unc = MathTex(
            r"\text{...with uncertainty due to sampling variation.}",
            color=ORANGE_TERM,
        ).scale(0.85)
        unc.next_to(est, DOWN, buff=0.4)
        unc_bg = BackgroundRectangle(unc, color=BLACK, fill_opacity=1, buff=0.25)
        unc_bg.move_to(unc.get_center())
        beat_2 = beat_group(beat_2, unc_bg, unc)
        self.play(FadeIn(unc_bg, run_time=0.4), FadeIn(unc, run_time=2.0))
        self.wait(4.0)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — What to include in a report (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None
        items_left = [
            ("\text{Question}",     "what was investigated",     BLUE_TERM),
            ("\text{Population}",   "who it applies to",          TEAL_TERM),
            ("\text{Sample size } n", "how many responded",       ORANGE_TERM),
        ]
        items_right = [
            ("\text{Method}",       "random / stratified / ...",  PURPLE_ACCENT),
            ("\text{Statistic}",    "mean / proportion",          GREEN_OK),
            ("\text{Uncertainty}",  "how much we trust it",       YELLOW_HIGHLIGHT),
        ]
        left_col = VGroup(*[
            make_term_card(tex, lbl, color).scale(0.4)
            for tex, lbl, color in items_left
        ]).arrange(DOWN, buff=0.18)
        right_col = VGroup(*[
            make_term_card(tex, lbl, color).scale(0.4)
            for tex, lbl, color in items_right
        ]).arrange(DOWN, buff=0.18)
        cards = VGroup(left_col, right_col).arrange(RIGHT, buff=0.8)
        # Place the top of the stack safely below the subtitle at y = 2.4.
        # Aim for top at y ≈ 0.9 so the cards sit inside y ∈ [-1.0, 1.0].
        cards.move_to(BAND_CHART_CENTER)
        cards.shift(DOWN * (cards.get_top()[1] - 0.9))

        for c in cards:
            beat_3 = beat_group(beat_3, c)
            self.play(FadeIn(c, shift=RIGHT * 0.15, run_time=0.6))
            self.wait(0.6)

        self.wait(5.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: over-claiming from n = 20 (~9 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None
        bad = Text(
            '"The mean sleep at our school is exactly 9.5 hours."',
            font_size=24, color=WHITE,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.4)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        beat_4 = beat_group(beat_4, bad_bg, bad)
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(1.5)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        beat_4 = beat_group(beat_4, cross)
        self.play(Create(cross, run_time=1.0))

        why = MathTex(
            r"\text{Too strong a claim for } n = 20.",
            color=RED_REJECT,
        ).scale(0.9)
        why.next_to(bad, DOWN, buff=0.5)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=1, buff=0.22)
        why_bg.move_to(why.get_center())
        beat_4 = beat_group(beat_4, why_bg, why)
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.4))
        self.wait(2.5)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 77.8 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Honest report} = \text{source, size, method, uncertainty}",
            "Say 'we estimate ...' rather than 'it is exactly ...'.",
            final_wait=28.0,
        )
