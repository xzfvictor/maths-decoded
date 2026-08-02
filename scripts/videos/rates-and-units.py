"""
Manim scene for the lesson `rates-and-units`
(topic `l8-m-rates`).

A rate compares two quantities of different units; the unit rate
answers "how much of A per one of B". The scene works a concrete
240 km / 4 h = 60 km/h example, generalises to the triangle of
formulas, and rejects the confusion between rate and ratio.

Target duration: ~69 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class RatesAndUnitsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Rates and unit rates",
            "Rate = quantity / time  (units stay attached)",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: 240 km / 4 h = 60 km/h (~18 s)
        # ──────────────────────────────────────────────────────────────────
        frac_tex = MathTex(
            r"\dfrac{240\ \text{km}}{4\ \text{h}} = 60\ \text{km/h}",
            color=BLUE_TERM,
        ).scale(1.4)
        frac_tex.move_to(BAND_CHART_CENTER + UP * 0.6)
        frac_bg = BackgroundRectangle(frac_tex, color=BLACK, fill_opacity=1, buff=0.25)
        frac_bg.move_to(frac_tex.get_center())
        self.play(FadeIn(frac_bg, run_time=0.5), Write(frac_tex, run_time=2.0))
        self.wait(3.0)

        unit = Text("60 km per hour — a unit rate", font_size=22, color=GREEN_OK)
        unit.next_to(frac_tex, DOWN, buff=0.5)
        unit_bg = BackgroundRectangle(unit, color=BLACK, fill_opacity=0.95, buff=0.15)
        unit_bg.move_to(unit.get_center())
        self.play(FadeIn(unit_bg, run_time=0.4), FadeIn(unit, run_time=1.2))
        self.wait(3.0)
        self.play(
            FadeOut(frac_tex, run_time=0.8),
            FadeOut(frac_bg, run_time=0.8),
            FadeOut(unit, run_time=0.8),
            FadeOut(unit_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Triangle of formulas: A = r × B, B = A / r, r = A / B
        # (~18 s)
        # ──────────────────────────────────────────────────────────────────
        eq1 = make_equation_card(r"A = r \times B", color=BLUE_TERM, scale=1.2)
        eq1.move_to(BAND_CHART_CENTER + UP * 0.9)
        for m in eq1:
            m.set_z_index(2)

        eq2 = make_equation_card(r"B = A / r", color=TEAL_TERM, scale=1.2)
        eq2.next_to(eq1, DOWN, buff=0.4)
        for m in eq2:
            m.set_z_index(2)

        eq3 = make_equation_card(r"r = A / B", color=ORANGE_TERM, scale=1.2)
        eq3.next_to(eq2, DOWN, buff=0.4)
        for m in eq3:
            m.set_z_index(2)

        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(eq2, shift=UP * 0.2, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(eq3, shift=UP * 0.2, run_time=1.0))
        self.wait(2.0)

        # Cover the unknown, the rest is the formula.
        rule = Text("Pick the form that puts the unknown on its own.", font_size=22, color=GREEN_OK)
        rule.next_to(eq3, DOWN, buff=0.45)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=0.95, buff=0.15)
        rule_bg.move_to(rule.get_center())
        self.play(FadeIn(rule_bg, run_time=0.4), FadeIn(rule, run_time=1.2))
        self.wait(3.5)
        self.play(
            FadeOut(eq1, run_time=0.8),
            FadeOut(eq2, run_time=0.8),
            FadeOut(eq3, run_time=0.8),
            FadeOut(rule, run_time=0.8),
            FadeOut(rule_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: dropping the units makes it a ratio, not a rate
        # (~6 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(
            r"240 : 4 = 60 : 1\ \text{?}",
            color=RED_REJECT,
        ).scale(1.1)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.5)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.4))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.5)
        self.play(
            FadeOut(wrong, run_time=0.6),
            FadeOut(wrong_bg, run_time=0.6),
            FadeOut(cross, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~25 s, total ≈ 69 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{rate} = \dfrac{\text{quantity A}}{\text{quantity B}}",
            "Keep the units attached — they tell you what the rate means.",
            final_wait=25.0,
        )
