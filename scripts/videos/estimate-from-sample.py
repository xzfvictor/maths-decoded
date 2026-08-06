"""
Manim scene for the lesson `estimate-from-sample`
(topic `l9-st-survey-reports`).

Use the sample mean / median / proportion as point estimates for the
population values. Bigger samples are more precise; bias cannot be
fixed with more data.

Render target: ~50-60 s, final_wait=48.3 s.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class EstimateFromSampleScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Estimating from a sample",
            "Sample summary  ⇒  best guess for the population.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Sample mean estimates the population mean
        # ──────────────────────────────────────────────────────────────────
        data = Text(
            "{18, 22, 25, 30, 35}",
            font_size=24,
        ).move_to(BAND_CHART_CENTER + UP * 1.5)
        data_bg = BackgroundRectangle(data, color=BLACK, fill_opacity=1, buff=0.2)
        data_bg.move_to(data.get_center())

        self.play(FadeIn(data_bg, run_time=0.5), FadeIn(data, run_time=1.0))
        self.wait(0.5)

        mean_card = make_term_card(
            r"\bar{x} = 26",
            "sample mean = estimate of population mean",
            GREEN_OK,
        )
        mean_card.move_to(BAND_CHART_CENTER + UP * 0.1)
        mean_card.set_z_index(2)

        self.play(FadeIn(mean_card, shift=UP * 0.2, run_time=1.0))
        self.wait(1.0)

        arrow_lbl = Text(
            r"x̄ estimates μ (population mean)",
            font_size=22,
            color=BLUE_TERM,
        ).next_to(mean_card, DOWN, buff=0.5)
        arrow_bg = BackgroundRectangle(arrow_lbl, color=BLACK, fill_opacity=0.95, buff=0.18)
        arrow_bg.move_to(arrow_lbl.get_center())
        self.play(FadeIn(arrow_bg, run_time=0.5), FadeIn(arrow_lbl, run_time=1.0))
        self.wait(1.0)
        self.play(FadeOut(
            beat_group(data, data_bg, mean_card, arrow_lbl, arrow_bg),
            run_time=0.8,
        ))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Sample proportion estimates population proportion
        # ──────────────────────────────────────────────────────────────────
        prop_eq = make_equation_card(
            r"\hat{p} \;=\; \dfrac{220}{400} \;=\; 0.55",
            color=GREEN_OK,
            scale=1.0,
        )
        prop_eq.move_to(BAND_CHART_CENTER + UP * 0.4)

        self.play(FadeIn(prop_eq, run_time=1.2))
        self.wait(0.8)

        prop_note = Text(
            "p̂ (55%) estimates the population proportion.",
            font_size=22,
            color=ORANGE_TERM,
        ).next_to(prop_eq, DOWN, buff=0.5)
        prop_bg = BackgroundRectangle(prop_note, color=BLACK, fill_opacity=0.95, buff=0.18)
        prop_bg.move_to(prop_note.get_center())
        self.play(FadeIn(prop_bg, run_time=0.5), FadeIn(prop_note, run_time=1.0))
        self.wait(1.5)
        self.play(FadeOut(beat_group(prop_eq, prop_note, prop_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Bias warning: more data can't fix it
        # ──────────────────────────────────────────────────────────────────
        bias_eq = make_equation_card(
            r"\text{biased method} \;\not\Rightarrow\; \text{fixed by more data}",
            color=RED_REJECT,
            scale=0.85,
        )
        bias_eq.move_to(BAND_CHART_CENTER + UP * 0.5)

        self.play(FadeIn(bias_eq, run_time=1.2))
        self.wait(0.8)

        warn = Text(
            "Bias stays biased — collect the right way first.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(bias_eq, DOWN, buff=0.5)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.18)
        warn_bg.move_to(warn.get_center())
        self.play(FadeIn(warn_bg, run_time=0.5), FadeIn(warn, run_time=1.0))
        self.wait(1.5)
        self.play(FadeOut(beat_group(bias_eq, warn, warn_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"\bar{x} \approx \mu,\quad \hat{p} \approx p",
            "Sample summary  ⇒  point estimate of the population value.",
            final_wait=48.3,
        )
