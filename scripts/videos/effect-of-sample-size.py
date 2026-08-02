"""
Manim scene for the lesson `effect-of-sample-size`
(topic `l8-st-comparing-samples`).

Bigger samples have less sampling variation — their statistics sit
closer to the population parameter. Doubling n divides the spread by
about √2. A bigger sample fixes variation, not bias.

Render target: ~110 s, matched to the audio narration length. The
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


class EffectOfSampleSizeScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (CONSTANT header)
        # ──────────────────────────────────────────────────────────────────
        title_group = animate_intro(
            self,
            "Effect of sample size",
            "Larger n → tighter sampling distribution → closer to truth.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete visual: spread of sample means shrinks with n (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None  # VGroup accumulator for beat 2

        # Wide distribution for n=5 (dots scattered vertically along a centerline).
        wide_dots = VGroup(*[
            Dot(radius=0.06, color=BLUE_TERM).move_to(
                LEFT * 3 + UP * (1.2 * y)  # y ∈ {-1, 0, 1}, scaled
            ) for y in [-1.0, 0.5, -0.4, 0.9, -0.7, 0.2, -0.3, 0.6, -0.1, 0.4]
        ])
        wide_dots.arrange(DOWN, buff=0.18)
        wide_dots.move_to(LEFT * 3.2 + UP * 0.4)
        wide_lbl = MathTex(r"n = 5", color=BLUE_TERM).scale(1.0)
        wide_lbl.next_to(wide_dots, DOWN, buff=0.5)
        wide_lbl_bg = BackgroundRectangle(wide_lbl, color=BLACK, fill_opacity=1, buff=0.2)
        wide_lbl_bg.move_to(wide_lbl.get_center())
        wide_caption = Text("spread: 148 – 180 cm", font_size=20, color=BLUE_TERM)
        wide_caption.next_to(wide_lbl, DOWN, buff=0.35)
        wide_caption_bg = BackgroundRectangle(wide_caption, color=BLACK, fill_opacity=0.9, buff=0.15)
        wide_caption_bg.move_to(wide_caption.get_center())

        self.play(
            FadeIn(wide_dots, run_time=1.4),
            FadeIn(wide_lbl_bg, run_time=0.4),
            FadeIn(wide_lbl, run_time=1.0),
        )
        self.wait(2.0)
        self.play(
            FadeIn(wide_caption_bg, run_time=0.4),
            FadeIn(wide_caption, run_time=1.0),
        )
        self.wait(3.0)
        beat_2 = beat_group(
            wide_dots, wide_lbl, wide_lbl_bg, wide_caption, wide_caption_bg,
        )

        # Fade the wide column before showing the narrow one.
        self.play(FadeOut(beat_2, run_time=0.8))
        beat_2 = None

        # Narrow distribution for n=50 (dots clustered tightly).
        narrow_dots = VGroup(*[
            Dot(radius=0.06, color=GREEN_OK) for _ in range(10)
        ])
        narrow_y = [-0.2, 0.1, -0.05, 0.15, -0.1, 0.05, -0.15, 0.0, -0.08, 0.12]
        for d, y in zip(narrow_dots, narrow_y):
            d.move_to(RIGHT * 3.2 + UP * y)
        narrow_lbl = MathTex(r"n = 50", color=GREEN_OK).scale(1.0)
        narrow_lbl.next_to(narrow_dots, DOWN, buff=0.5)
        narrow_lbl_bg = BackgroundRectangle(narrow_lbl, color=BLACK, fill_opacity=1, buff=0.2)
        narrow_lbl_bg.move_to(narrow_lbl.get_center())
        narrow_caption = Text("clustered near 164 cm", font_size=20, color=GREEN_OK)
        narrow_caption.next_to(narrow_lbl, DOWN, buff=0.35)
        narrow_caption_bg = BackgroundRectangle(narrow_caption, color=BLACK, fill_opacity=0.9, buff=0.15)
        narrow_caption_bg.move_to(narrow_caption.get_center())

        self.play(
            FadeIn(narrow_dots, run_time=1.4),
            FadeIn(narrow_lbl_bg, run_time=0.4),
            FadeIn(narrow_lbl, run_time=1.0),
        )
        self.wait(2.0)
        self.play(
            FadeIn(narrow_caption_bg, run_time=0.4),
            FadeIn(narrow_caption, run_time=1.0),
        )
        self.wait(3.0)
        beat_2 = beat_group(
            narrow_dots, narrow_lbl, narrow_lbl_bg, narrow_caption, narrow_caption_bg,
        )

        # End of beat 2 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalisation: doubling n halves the spread (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None  # VGroup accumulator for beat 3

        # Show one equation/claim at a time so they don't all stack.
        rule = MathTex(
            r"\text{spread} \propto \dfrac{1}{\sqrt{n}}",
            color=GREEN_OK,
        ).scale(1.2)
        rule.move_to(BAND_CHART_CENTER + UP * 1.0)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.28)
        rule_bg.move_to(rule.get_center())
        self.play(
            FadeIn(rule_bg, run_time=0.5),
            Write(rule, run_time=1.8),
        )
        self.wait(2.0)
        beat_3 = beat_group(rule, rule_bg)
        self.play(FadeOut(beat_3, run_time=0.8))
        beat_3 = None

        # Concrete: doubling n halves the spread.
        doubling = MathTex(
            r"n \;\rightarrow\; 4n \quad\Rightarrow\quad \text{spread} \;\rightarrow\; \tfrac{1}{2} \,\text{spread}",
            color=ORANGE_TERM,
        ).scale(0.85)
        doubling.move_to(BAND_CHART_CENTER + UP * 0.6)
        doubling_bg = BackgroundRectangle(doubling, color=BLACK, fill_opacity=1, buff=0.25)
        doubling_bg.move_to(doubling.get_center())
        self.play(
            FadeIn(doubling_bg, run_time=0.5),
            Write(doubling, run_time=1.8),
        )
        self.wait(3.0)
        beat_3 = beat_group(doubling, doubling_bg)
        self.play(FadeOut(beat_3, run_time=0.8))
        beat_3 = None

        # Implication
        impl = Text(
            "Bigger n → more precise estimate, narrower prediction interval.",
            font_size=22, color=WHITE,
        )
        impl_bg = BackgroundRectangle(impl, color=BLACK, fill_opacity=1, buff=0.2)
        impl_bg.move_to(impl.get_center())
        impl.move_to(BAND_CHART_CENTER + UP * 0.6)
        self.play(
            FadeIn(impl_bg, run_time=0.5),
            FadeIn(impl, run_time=1.2),
        )
        self.wait(4.0)
        beat_3 = beat_group(impl, impl_bg)

        # End of beat 3 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Warn: bigger n does NOT fix bias (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None  # VGroup accumulator for beat 4

        warn = Text(
            "WARNING: bigger n fixes variation — not bias.",
            font_size=26, color=RED_REJECT,
        )
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=1, buff=0.28)
        warn_bg.move_to(warn.get_center())
        warn.move_to(BAND_CHART_CENTER + UP * 1.0)
        self.play(
            FadeIn(warn_bg, run_time=0.5),
            FadeIn(warn, run_time=1.4),
        )
        self.wait(2.0)
        beat_4 = beat_group(warn, warn_bg)
        self.play(FadeOut(beat_4, run_time=0.8))
        beat_4 = None

        example = Text(
            "Survey only one suburb → still biased — even with n = 5000.",
            font_size=22, color=WHITE,
        )
        example_bg = BackgroundRectangle(example, color=BLACK, fill_opacity=0.95, buff=0.2)
        example_bg.move_to(example.get_center())
        example.move_to(BAND_CHART_CENTER + UP * 0.8)
        self.play(
            FadeIn(example_bg, run_time=0.5),
            FadeIn(example, run_time=1.4),
        )
        self.wait(2.5)
        beat_4 = beat_group(example, example_bg)
        self.play(FadeOut(beat_4, run_time=0.8))
        beat_4 = None

        precision = MathTex(
            r"\text{Precise but wrong} = \text{reliable answer to the wrong question}",
            color=RED_REJECT,
        ).scale(0.85)
        precision_bg = BackgroundRectangle(precision, color=BLACK, fill_opacity=1, buff=0.25)
        precision_bg.move_to(precision.get_center())
        precision.move_to(BAND_CHART_CENTER + UP * 0.8)
        self.play(
            FadeIn(precision_bg, run_time=0.5),
            Write(precision, run_time=1.6),
        )
        self.wait(4.0)
        beat_4 = beat_group(precision, precision_bg)

        # End of beat 4 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Sample size} \uparrow \;\;\Rightarrow\;\; \text{variation} \downarrow",
            "Bigger n ⇒ tighter estimates. But only a fair method removes bias.",
            final_wait=43.0,
        )