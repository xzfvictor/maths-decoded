"""
Manim scene for the lesson `sampling-methods`
(topic `l9-st-sampling-methods`).

Random sampling aims to be unbiased; convenience, voluntary and quota
samples trade some bias for ease.

Render target: ~70-80 s, final_wait=20 s.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class SamplingMethodsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Sampling methods",
            "How you pick the sample shapes what you can conclude.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Simple random sampling: the gold standard
        # ──────────────────────────────────────────────────────────────────
        srs = make_term_card(
            r"\text{Simple random}",
            "every individual has equal chance",
            GREEN_OK,
        )
        srs.move_to(BAND_CHART_CENTER + UP * 0.6)
        srs.set_z_index(2)

        self.play(FadeIn(srs, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)

        gold = Text("gold standard", font_size=22, color=GREEN_OK)
        gold.next_to(srs, DOWN, buff=0.4)
        gold_bg = BackgroundRectangle(gold, color=BLACK, fill_opacity=0.95, buff=0.18)
        gold_bg.move_to(gold.get_center())
        self.play(FadeIn(gold_bg, run_time=0.5), FadeIn(gold, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(beat_group(srs, gold, gold_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Systematic, stratified, cluster
        # ──────────────────────────────────────────────────────────────────
        sys_card = make_term_card(
            r"\text{Systematic}",
            "every k-th item",
            BLUE_TERM,
        )
        strat_card = make_term_card(
            r"\text{Stratified}",
            "random sample per stratum",
            TEAL_TERM,
        )
        clus_card = make_term_card(
            r"\text{Cluster}",
            "whole groups chosen at random",
            ORANGE_TERM,
        )
        row = VGroup(sys_card, strat_card, clus_card).arrange(RIGHT, buff=0.4)
        row.move_to(BAND_CHART_CENTER + UP * 0.4)
        for c in row:
            c.set_z_index(2)

        self.play(FadeIn(sys_card, shift=UP * 0.2, run_time=0.8))
        self.play(FadeIn(strat_card, shift=UP * 0.2, run_time=0.8))
        self.play(FadeIn(clus_card, shift=UP * 0.2, run_time=0.8))
        self.wait(1.0)

        when = Text(
            "Stratify when the answer differs by group.",
            font_size=22,
            color=TEAL_TERM,
        ).next_to(row, DOWN, buff=0.5)
        when_bg = BackgroundRectangle(when, color=BLACK, fill_opacity=0.95, buff=0.18)
        when_bg.move_to(when.get_center())
        self.play(FadeIn(when_bg, run_time=0.5), FadeIn(when, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(beat_group(row, when, when_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Convenience / voluntary: bias trade-off
        # ──────────────────────────────────────────────────────────────────
        bias_card = make_term_card(
            r"\text{Convenience / Voluntary}",
            "whoever is easiest to reach",
            RED_REJECT,
        )
        bias_card.move_to(BAND_CHART_CENTER + UP * 0.6)
        bias_card.set_z_index(2)

        self.play(FadeIn(bias_card, shift=UP * 0.2, run_time=1.0))
        self.wait(1.0)

        cross = Cross(bias_card, color=RED_REJECT, stroke_width=5)
        warn = Text(
            "often biased — trade ease for accuracy",
            font_size=22,
            color=RED_REJECT,
        ).next_to(bias_card, DOWN, buff=0.5)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.18)
        warn_bg.move_to(warn.get_center())
        self.play(Create(cross, run_time=0.8))
        self.play(FadeIn(warn_bg, run_time=0.5), FadeIn(warn, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(
            beat_group(bias_card, cross, warn, warn_bg),
            run_time=0.8,
        ))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Random} \;=\; \text{unbiased by design}",
            "Convenience and voluntary samples trade bias for ease.",
            final_wait=20,
        )
