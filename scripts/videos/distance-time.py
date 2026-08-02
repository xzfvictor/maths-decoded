"""
Manim scene for the lesson `distance-time`
(topic `l8-m-modelling-ratios-rates`).

Distance = speed × time. The scene works a concrete 60 km/h × 2.5 h
= 150 km example, generalises the triangle of formulas, and rejects
the common mistake of mixing units (e.g. multiplying km/h by seconds).

Target duration: ~87 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class DistanceTimeScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Distance, time and speed",
            "distance = speed × time",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: 60 km/h × 2.5 h = 150 km (~18 s)
        # ──────────────────────────────────────────────────────────────────
        # Build the calculation left to right.
        s = MathTex(r"60\ \text{km/h}", color=BLUE_TERM).scale(1.2)
        x1 = MathTex(r"\times", color=WHITE).scale(1.2)
        t = MathTex(r"2.5\ \text{h}", color=ORANGE_TERM).scale(1.2)
        eq = MathTex(r"=", color=WHITE).scale(1.2)
        d = MathTex(r"150\ \text{km}", color=GREEN_OK).scale(1.2)

        row = VGroup(s, x1, t, eq, d).arrange(RIGHT, buff=0.35)
        row.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in row:
            bg = BackgroundRectangle(m, color=BLACK, fill_opacity=0.85, buff=0.15)
            bg.move_to(m.get_center())
            m.bg = bg
        bgs = VGroup(*[m.bg for m in row])

        self.play(FadeIn(bgs, run_time=0.4), FadeIn(row, run_time=1.6))
        self.wait(3.0)

        check = Text("Speed × time gives distance.", font_size=22, color=GREEN_OK)
        check.next_to(row, DOWN, buff=0.5)
        check_bg = BackgroundRectangle(check, color=BLACK, fill_opacity=0.95, buff=0.15)
        check_bg.move_to(check.get_center())
        self.play(FadeIn(check_bg, run_time=0.4), FadeIn(check, run_time=1.2))
        self.wait(3.0)
        self.play(
            FadeOut(row, run_time=0.8),
            FadeOut(bgs, run_time=0.8),
            FadeOut(check, run_time=0.8),
            FadeOut(check_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Triangle of formulas: d = s × t, s = d / t, t = d / s
        # (~18 s)
        # ──────────────────────────────────────────────────────────────────
        eq1 = make_equation_card(r"d = s \times t", color=BLUE_TERM, scale=1.2)
        eq1.move_to(BAND_CHART_CENTER + UP * 0.9)
        for m in eq1:
            m.set_z_index(2)

        eq2 = make_equation_card(r"s = d / t", color=TEAL_TERM, scale=1.2)
        eq2.next_to(eq1, DOWN, buff=0.4)
        for m in eq2:
            m.set_z_index(2)

        eq3 = make_equation_card(r"t = d / s", color=ORANGE_TERM, scale=1.2)
        eq3.next_to(eq2, DOWN, buff=0.4)
        for m in eq3:
            m.set_z_index(2)

        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(eq2, shift=UP * 0.2, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(eq3, shift=UP * 0.2, run_time=1.0))
        self.wait(2.0)

        # Sanity-check callout.
        sanity = Text(
            "Convert units so they match before you multiply.",
            font_size=22, color=GREEN_OK,
        )
        sanity.next_to(eq3, DOWN, buff=0.45)
        sanity_bg = BackgroundRectangle(sanity, color=BLACK, fill_opacity=0.95, buff=0.15)
        sanity_bg.move_to(sanity.get_center())
        self.play(FadeIn(sanity_bg, run_time=0.4), FadeIn(sanity, run_time=1.2))
        self.wait(3.0)
        self.play(
            FadeOut(eq1, run_time=0.8),
            FadeOut(eq2, run_time=0.8),
            FadeOut(eq3, run_time=0.8),
            FadeOut(sanity, run_time=0.8),
            FadeOut(sanity_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: 60 km/h × 30 s ≠ 150 km (~8 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(
            r"60\ \text{km/h} \times 30\ \text{s} = 30\ \text{?}",
            color=RED_REJECT,
        ).scale(0.95)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.5)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.4))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.8))
        self.wait(0.8)

        right = MathTex(
            r"30\ \text{s} = \tfrac{1}{120}\ \text{h},\ \text{so } d = 0.5\ \text{km}",
            color=GREEN_OK,
        ).scale(0.95)
        right.next_to(wrong, DOWN, buff=0.5)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=1, buff=0.25)
        right_bg.move_to(right.get_center())
        self.play(
            FadeOut(wrong, run_time=0.6),
            FadeOut(wrong_bg, run_time=0.6),
            FadeOut(cross, run_time=0.6),
            FadeIn(right_bg, run_time=0.4),
            Write(right, run_time=1.4),
        )
        self.wait(2.5)
        self.play(
            FadeOut(right, run_time=0.8),
            FadeOut(right_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~32 s, total ≈ 87 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"d = s \times t",
            "Match the units first, then pick the form that isolates the unknown.",
            final_wait=32.0,
        )
