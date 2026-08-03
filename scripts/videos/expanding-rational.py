"""
Manim scene for the lesson `expanding-rational`
(topic `l10a-aa-linear-rational`).

A rational expression is a(x)/b(x) where both are polynomials. The
animation builds a concrete example, shows that it is a single fraction,
and contrasts it with the "polynomial" case where the denominator is 1.

Target duration: ~106.0 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class ExpandingRationalScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Expanding a rational expression",
            "Polynomial over polynomial — keep as one fraction.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — What is a rational expression? (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("The shape", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.45)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        form = make_equation_card(
            r"\dfrac{a(x)}{b(x)}",
            color=BLUE_TERM, scale=1.0,
        )
        form.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(form, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        lbl1 = Text("a(x) is a polynomial (top)",
                    font_size=20, color=BLUE_TERM)
        lbl1.next_to(form, DOWN, buff=0.55)
        lbl1_bg = BackgroundRectangle(lbl1, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        lbl1_bg.move_to(lbl1.get_center())
        self.play(FadeIn(lbl1_bg, run_time=0.4), FadeIn(lbl1, run_time=1.0))
        self.wait(0.8)

        lbl2 = Text("b(x) is a polynomial (bottom)",
                    font_size=20, color=TEAL_TERM)
        lbl2.next_to(lbl1, DOWN, buff=0.25)
        lbl2_bg = BackgroundRectangle(lbl2, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        lbl2_bg.move_to(lbl2.get_center())
        self.play(FadeIn(lbl2_bg, run_time=0.4), FadeIn(lbl2, run_time=1.0))
        self.wait(1.5)

        beat2 = beat_group(head, head_bg, form, lbl1, lbl1_bg, lbl2, lbl2_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — A concrete example (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Worked example", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.5)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        top = make_equation_card(
            r"a(x) \;=\; 2x^{2} + 3x",
            color=BLUE_TERM, scale=1.0,
        )
        top.move_to(BAND_CHART_CENTER + UP * 0.7)
        self.play(FadeIn(top, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        bot = make_equation_card(
            r"b(x) \;=\; x - 1",
            color=TEAL_TERM, scale=1.0,
        )
        bot.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        self.play(FadeIn(bot, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        full = MathTex(
            r"\dfrac{2x^{2}+3x}{x-1}",
            color=GREEN_OK,
        ).scale(0.7)
        full.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        full_bg = BackgroundRectangle(full, color=BLACK,
                                       fill_opacity=1, buff=0.18)
        full_bg.move_to(full.get_center())
        self.play(FadeIn(full_bg, run_time=0.3),
                  FadeIn(full, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        beat3 = beat_group(head3, head3_bg, top, bot, full, full_bg)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Expand: each term of a(x) divided by b(x) (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Expand", font_size=26, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        expanded = make_equation_card(
            r"\dfrac{2x^{2}+3x}{x-1} \;=\; "
            r"\dfrac{2x^{2}}{x-1} + \dfrac{3x}{x-1}",
            color=ORANGE_TERM, scale=0.9,
        )
        expanded.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(expanded, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        tip = Text(
            "Split numerator term-by-term; keep denominator the same.",
            font_size=20, color=WHITE,
        ).next_to(expanded, DOWN, buff=0.4)
        tip_bg = BackgroundRectangle(tip, color=BLACK,
                                     fill_opacity=0.95, buff=0.15)
        tip_bg.move_to(tip.get_center())
        self.play(FadeIn(tip_bg, run_time=0.4),
                  FadeIn(tip, run_time=1.0))
        self.wait(2.0)

        beat4 = beat_group(head4, head4_bg, expanded, tip, tip_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 106.0 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\dfrac{a(x)}{b(x)} = \dfrac{a_1(x)}{b(x)} + \dfrac{a_2(x)}{b(x)}"
            r" + \cdots",
            "Split the numerator term by term; denominator stays put.",
            final_wait=48.0,
        )