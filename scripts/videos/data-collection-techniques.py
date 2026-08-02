"""
Manim scene for the lesson `data-collection-techniques`
(topic `l8-st-population-sample`).

Statisticians collect data in four main ways: census, sample,
experiment, observation. Each has trade-offs in cost, time, and what
it can claim (parameters vs. estimates, association vs. cause).

Render target: ~96 s, matched to the audio narration length. The
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


class DataCollectionTechniquesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (CONSTANT header)
        # ──────────────────────────────────────────────────────────────────
        title_group = animate_intro(
            self,
            "Four ways to collect data",
            "Census · Sample · Experiment · Observation",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete pairing: census vs. sample (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Wait for the previous beat to fully clear before showing the next
        # pair of cards, so the two pairs never share the screen.
        self.wait(0.6)
        # Two cards side by side.
        census_card = make_term_card(r"\text{Census}", "everyone", BLUE_TERM)
        sample_card = make_term_card(r"\text{Sample}", "a subset", TEAL_TERM)
        pair = VGroup(census_card, sample_card).arrange(RIGHT, buff=1.2)
        pair.move_to(BAND_CHART_CENTER + UP * 0.4)

        self.play(FadeIn(census_card, shift=UP * 0.3, run_time=1.4))
        self.wait(1.0)
        self.play(FadeIn(sample_card, shift=UP * 0.3, run_time=1.4))
        self.wait(2.5)

        # Cost annotation: census is slow + expensive.
        census_note = Text(
            "Slow + expensive, but exact",
            font_size=22, color=BLUE_TERM,
        )
        census_note.next_to(census_card, DOWN, buff=0.5)
        census_note_bg = BackgroundRectangle(census_note, color=BLACK, fill_opacity=0.95, buff=0.18)
        census_note_bg.move_to(census_note.get_center())
        sample_note = Text(
            "Cheap + quick, but uncertain",
            font_size=22, color=TEAL_TERM,
        )
        sample_note.next_to(sample_card, DOWN, buff=0.5)
        sample_note_bg = BackgroundRectangle(sample_note, color=BLACK, fill_opacity=0.95, buff=0.18)
        sample_note_bg.move_to(sample_note.get_center())

        self.play(
            FadeIn(census_note_bg, run_time=0.5),
            FadeIn(census_note, run_time=1.0),
            FadeIn(sample_note_bg, run_time=0.5),
            FadeIn(sample_note, run_time=1.0),
        )
        self.wait(3.0)

        # Concrete example: 25 million Australians.
        example = Text(
            "Australian census: every 5 years, ~25 million people.",
            font_size=22, color=WHITE,
        )
        example_bg = BackgroundRectangle(example, color=BLACK, fill_opacity=1, buff=0.2)
        example_bg.move_to(example.get_center())
        example.move_to(BAND_CHART_CENTER + DOWN * 2.2)
        self.play(
            FadeIn(example_bg, run_time=0.5),
            FadeIn(example, run_time=1.2),
        )
        self.wait(5.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The other two: experiment vs. observation (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat2_group = VGroup(
            census_card, sample_card, census_note, census_note_bg,
            sample_note, sample_note_bg, example, example_bg,
        )
        self.play(FadeOut(beat2_group, run_time=1.5))
        # Let the previous cards fully clear before the next pair appears.
        self.wait(0.5)

        # Experiment card — applies a treatment.
        exp_card = make_term_card(r"\text{Experiment}", "treatment + control", ORANGE_TERM)
        exp_card.move_to(BAND_CHART_CENTER + UP * 0.6)

        # Observation card — just watches.
        obs_card = make_term_card(r"\text{Observation}", "no intervention", PURPLE_C)
        obs_card.move_to(BAND_CHART_CENTER + DOWN * 1.4)

        self.play(FadeIn(exp_card, shift=UP * 0.3, run_time=1.4))
        self.wait(1.0)
        self.play(FadeIn(obs_card, shift=UP * 0.3, run_time=1.4))
        self.wait(2.0)

        # Claim ladder: experiment → cause, observation → association.
        cause = MathTex(r"\text{Experiment} \Rightarrow \text{cause}", color=GREEN_OK).scale(0.9)
        cause_bg = BackgroundRectangle(cause, color=BLACK, fill_opacity=1, buff=0.25)
        cause_bg.move_to(cause.get_center())
        cause.move_to(BAND_CHART_CENTER + UP * 1.6)
        self.play(
            FadeIn(cause_bg, run_time=0.5),
            Write(cause, run_time=1.6),
        )

        assoc = MathTex(
            r"\text{Observation} \Rightarrow \text{association only}",
            color=RED_REJECT,
        ).scale(0.9)
        assoc_bg = BackgroundRectangle(assoc, color=BLACK, fill_opacity=1, buff=0.25)
        assoc_bg.move_to(assoc.get_center())
        # Stay inside the safe chart band (y < 1.8). The cause label sits
        # at UP*1.6 above; place assoc below the obs_card, not above.
        assoc.move_to(BAND_CHART_CENTER + DOWN * 0.5)
        self.play(
            FadeIn(assoc_bg, run_time=0.5),
            Write(assoc, run_time=1.6),
        )
        self.wait(3.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Bias can sneak into every technique (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat3_group = VGroup(exp_card, obs_card, cause, cause_bg, assoc, assoc_bg)
        self.play(FadeOut(beat3_group, run_time=1.5))

        # Bias banner — fade in, then fade out before the next example so
        # the screen never stacks banner + sampling + response all at once.
        bias = Text("Watch out: BIAS can sneak into any method", font_size=28, color=RED_REJECT)
        bias_bg = BackgroundRectangle(bias, color=BLACK, fill_opacity=1, buff=0.25)
        bias_bg.move_to(bias.get_center())
        bias.move_to(BAND_CHART_CENTER + UP * 1.6)
        bias_grp = beat_group(bias, bias_bg)
        self.play(
            FadeIn(bias_bg, run_time=0.5),
            FadeIn(bias, run_time=1.4),
        )
        self.wait(1.5)
        self.play(FadeOut(bias_grp, run_time=0.8))

        # Sampling-bias example
        sb = Text(
            "Sampling bias: surveying one shopping centre misses the rest.",
            font_size=22, color=WHITE,
        )
        sb_bg = BackgroundRectangle(sb, color=BLACK, fill_opacity=0.95, buff=0.2)
        sb_bg.move_to(sb.get_center())
        sb.move_to(BAND_CHART_CENTER + UP * 0.6)
        sb_grp = beat_group(sb, sb_bg)
        self.play(
            FadeIn(sb_bg, run_time=0.5),
            FadeIn(sb, run_time=1.2),
        )
        self.wait(2.0)
        self.play(FadeOut(sb_grp, run_time=0.8))

        rb = Text(
            "Response bias: leading questions nudge a particular answer.",
            font_size=22, color=WHITE,
        )
        rb_bg = BackgroundRectangle(rb, color=BLACK, fill_opacity=0.95, buff=0.2)
        rb_bg.move_to(rb.get_center())
        rb.move_to(BAND_CHART_CENTER + UP * 0.6)
        self.play(
            FadeIn(rb_bg, run_time=0.5),
            FadeIn(rb, run_time=1.2),
        )
        self.wait(4.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        beat4_group = VGroup(rb, rb_bg)
        self.play(FadeOut(beat4_group, run_time=1.5))

        animate_final_definition(
            self,
            r"\text{Pick the method that fits the question}",
            "Census → exact. Experiment → cause. Observation → association.",
            final_wait=37.0,
        )
