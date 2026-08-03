"""
Manim scene for the lesson `circles-and-exponentials`
(topic `l10a-aa-parabolas-curves`).

Two non-linear families: the unit circle (top/bottom halves as functions
y = ±√(1-x²)) and the exponential y = 2^x. The animation shows the
shape of each side-by-side with the formula.

Target duration: ~73.8 s (matches the audio narration length).
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


class CirclesAndExponentialsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Circles and exponentials",
            "Two non-linear shapes — circle and exponential growth.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The unit circle (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Unit circle", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        circle = Circle(radius=1.4, color=BLUE_TERM, stroke_width=4)
        circle.move_to(BAND_CHART_CENTER + DOWN * 0.3)
        eq = make_equation_card(
            r"x^{2} + y^{2} = 1",
            color=BLUE_TERM, scale=1.1,
        )
        eq.move_to(circle.get_center())
        self.play(Create(circle, run_time=1.4))
        self.play(FadeIn(eq, run_time=1.2))
        self.wait(1.5)

        beat2 = beat_group(head, head_bg, circle, eq)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Two halves as functions y = ±√(1-x²) (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Two halves", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        top = make_equation_card(
            r"y = +\sqrt{1-x^{2}}",
            color=GREEN_OK, scale=1.1,
        )
        top.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(top, shift=UP * 0.2, run_time=1.4))
        self.wait(0.8)

        bot = make_equation_card(
            r"y = -\sqrt{1-x^{2}}",
            color=ORANGE_TERM, scale=1.1,
        )
        bot.move_to(BAND_CHART_CENTER + DOWN * 0.5)
        self.play(FadeIn(bot, shift=UP * 0.2, run_time=1.4))
        self.wait(0.8)

        note = Text(
            "Each half is a function — top, then bottom.",
            font_size=20, color=WHITE,
        ).next_to(bot, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4),
                  FadeIn(note, run_time=1.0))
        self.wait(1.5)

        beat3 = beat_group(head3, head3_bg, top, bot, note, note_bg)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Exponential growth y = 2^x (~8 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Exponential", font_size=26, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        ax = Axes(
            x_range=[-2, 4, 1], y_range=[-0.5, 5, 1],
            x_length=6, y_length=3,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
            color=WHITE,
        ).move_to(BAND_CHART_CENTER + DOWN * 0.3)

        exp_curve = ax.plot(lambda x: 2 ** x if x >= -2 else 0.25,
                            x_range=[-2, 2.3], color=GREEN_OK, stroke_width=4)
        exp_eq = MathTex("y = 2^{x}", color=GREEN_OK).scale(0.95)
        exp_eq.move_to(ax.c2p(-1.5, 3.0))
        exp_eq_bg = BackgroundRectangle(exp_eq, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        exp_eq_bg.move_to(exp_eq.get_center())

        self.play(Create(ax, run_time=1.0), Create(exp_curve, run_time=1.5))
        self.play(FadeIn(exp_eq_bg, run_time=0.4), FadeIn(exp_eq, run_time=1.0))
        self.wait(1.5)

        beat4 = beat_group(head4, head4_bg, ax, exp_curve, exp_eq, exp_eq_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 73.8 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"x^{2}+y^{2}=1,\quad y=2^{x}",
            "Circles are bounded; exponentials grow fast.",
            final_wait=32.0,
        )