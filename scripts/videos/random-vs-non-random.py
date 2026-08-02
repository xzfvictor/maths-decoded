"""
Manim scene for the lesson `random-vs-non-random`
(topic `l8-st-sampling-techniques`).

Random sampling gives every member of the population an equal chance
of being chosen; non-random sampling does not. Random samples tend
to be representative; non-random samples tend to carry bias.

Render target: ~103 s, matched to the audio narration length. The
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


class RandomVsNonRandomScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (CONSTANT header)
        # ──────────────────────────────────────────────────────────────────
        title_group = animate_intro(
            self,
            "Random vs. non-random sampling",
            "Equal chance of selection ⇒ random. Otherwise ⇒ biased.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Random sampling: equal chance, three flavours (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None  # VGroup accumulator for beat 2

        # Random card moved down to UP*0.3 so its top sits clear of the
        # subtitle (~y=2.4) and inside the safe area y ∈ [-1.5, 1.8].
        random_card = make_term_card(r"\text{Random}", "equal chance", GREEN_OK)
        random_card.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(random_card, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        # Fade the parent Random card before showing the flavours so the
        # "equal chance" sublabel does not sit on top of "every kth".
        beat_2 = beat_group(random_card)
        self.play(FadeOut(beat_2, run_time=0.8))
        beat_2 = None

        # Three flavour cards in a row — also moved down to UP*0.6 so the
        # flavour cards and their sublabels stay inside the safe area
        # (sublabels land around y ≈ 0.2, comfortably below subtitle).
        srs = make_term_card(r"\text{Simple}", "hat-draw", BLUE_TERM)
        sys = make_term_card(r"\text{Systematic}", "every kth", TEAL_TERM)
        strat = make_term_card(r"\text{Stratified}", "by group", ORANGE_TERM)
        flavours = VGroup(srs, sys, strat).arrange(RIGHT, buff=0.6)
        flavours.move_to(BAND_CHART_CENTER + UP * 0.6)
        self.play(FadeIn(srs, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)
        self.play(FadeIn(sys, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)
        self.play(FadeIn(strat, shift=UP * 0.2, run_time=1.2))
        self.wait(3.0)

        # Concrete: stratified example (moved further down so it doesn't
        # collide with the flavour-card sublabels).
        strat_ex = MathTex(
            r"40 = 300 \times \tfrac{1}{4} \;\;\Rightarrow\;\; 10 \text{ from each house}",
            color=ORANGE_TERM,
        ).scale(0.85)
        strat_ex_bg = BackgroundRectangle(strat_ex, color=BLACK, fill_opacity=1, buff=0.25)
        strat_ex_bg.move_to(strat_ex.get_center())
        strat_ex.move_to(BAND_CHART_CENTER + DOWN * 1.6)
        self.play(
            FadeIn(strat_ex_bg, run_time=0.5),
            Write(strat_ex, run_time=1.6),
        )
        self.wait(4.0)

        # End of beat 2 — clean FadeOut of the whole beat.
        beat_2 = beat_group(srs, sys, strat, strat_ex, strat_ex_bg)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Non-random sampling: chooser picks (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None  # VGroup accumulator for beat 3

        # Same down-shift as beat 2: Non-random card at UP*0.3 to keep
        # its top below the subtitle line.
        nr_card = make_term_card(r"\text{Non-random}", "chooser picks", RED_REJECT)
        nr_card.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(nr_card, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        # Fade the parent Non-random card before showing the flavours.
        beat_3 = beat_group(nr_card)
        self.play(FadeOut(beat_3, run_time=0.8))
        beat_3 = None

        # Three flavour cards — same safe-area positioning as beat 2.
        conv = make_term_card(r"\text{Convenience}", "easiest to reach", BLUE_TERM)
        quota = make_term_card(r"\text{Quota}", "fill target", TEAL_TERM)
        judge = make_term_card(r"\text{Judgement}", "eye-balled", ORANGE_TERM)
        nrs = VGroup(conv, quota, judge).arrange(RIGHT, buff=0.6)
        nrs.move_to(BAND_CHART_CENTER + UP * 0.6)
        self.play(FadeIn(conv, shift=UP * 0.2, run_time=1.2))
        self.wait(0.8)
        self.play(FadeIn(quota, shift=UP * 0.2, run_time=1.2))
        self.wait(0.8)
        self.play(FadeIn(judge, shift=UP * 0.2, run_time=1.2))
        self.wait(3.0)

        # Concrete: surveying just your own class — further down so it
        # does not collide with the flavour-card sublabels.
        warn = Text(
            "Surveying only your own class? That's convenience — likely biased.",
            font_size=22, color=RED_REJECT,
        )
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.2)
        warn_bg.move_to(warn.get_center())
        warn.move_to(BAND_CHART_CENTER + DOWN * 1.6)
        self.play(
            FadeIn(warn_bg, run_time=0.5),
            FadeIn(warn, run_time=1.4),
        )
        self.wait(4.0)

        # End of beat 3 — clean FadeOut of the whole beat.
        beat_3 = beat_group(conv, quota, judge, warn, warn_bg)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reliability contrast: random ⇒ representative, non-random ⇒ bias
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None  # VGroup accumulator for beat 4

        good = MathTex(
            r"\text{Random} \Rightarrow \text{representative}",
            color=GREEN_OK,
        ).scale(0.95)
        good_bg = BackgroundRectangle(good, color=BLACK, fill_opacity=1, buff=0.28)
        good_bg.move_to(good.get_center())
        good.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(
            FadeIn(good_bg, run_time=0.5),
            Write(good, run_time=1.6),
        )
        self.wait(2.0)
        beat_4 = beat_group(good, good_bg)

        # Fade the first set before showing the second so the two claims
        # do not overlap on screen at once.
        self.play(FadeOut(beat_4, run_time=0.8))
        beat_4 = None

        bad = MathTex(
            r"\text{Non-random} \Rightarrow \text{sampling bias}",
            color=RED_REJECT,
        ).scale(0.95)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.28)
        bad_bg.move_to(bad.get_center())
        bad.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(
            FadeIn(bad_bg, run_time=0.5),
            Write(bad, run_time=1.6),
        )
        self.wait(3.0)
        beat_4 = beat_group(bad, bad_bg)

        # End of beat 4 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Every member has an equal chance} \;\Longleftrightarrow\; \text{Random}",
            "Random samples mirror the population. Non-random samples mirror the chooser.",
            final_wait=40.0,
        )