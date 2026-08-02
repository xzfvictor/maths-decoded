"""
Manim scene for the lesson `financial-modelling`
(topic `l8-m-modelling-ratios-rates`).

Ratios and rates show up everywhere money is involved — best-buy
comparison, wages, and fuel cost. The trick in all three is spotting
the rate (per unit, per hour, per litre) and multiplying or dividing.

Target duration: ~79 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


def text_card(text_str: str, color, scale: float = 1.0) -> VGroup:
    """A bordered text card with an opaque background."""
    t = Text(text_str, font_size=28, color=color).scale(scale)
    bg = BackgroundRectangle(t, color=BLACK, fill_opacity=0.9, buff=0.18)
    box = SurroundingRectangle(t, color=color, buff=0.18, stroke_width=2)
    return VGroup(bg, box, t)


class FinancialModellingScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Financial modelling with ratios and rates",
            "Best buy · wages · fuel cost — all about spotting the rate.",
            hold=1.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Best buy: find the cheaper unit rate (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat1 = VGroup(title[0], title[1], title[2], title[3])

        # Two options: small pack vs big pack.
        small = text_card("$3.50 for 500 g", BLUE_TERM)
        big   = text_card("$6.00 for 1 kg", ORANGE_TERM)
        row = VGroup(small, big).arrange(RIGHT, buff=1.2)
        row.move_to(BAND_CHART_CENTER + UP * 0.8)
        for m in row:
            m.set_z_index(2)

        self.play(FadeIn(small, shift=UP * 0.2, run_time=1.2))
        self.wait(0.5)
        self.play(FadeIn(big, shift=UP * 0.2, run_time=1.2))
        self.wait(2.0)

        # Convert to unit price (per 100 g) for an apples-to-apples comparison.
        unit1 = text_card("$0.70 per 100 g", BLUE_TERM, scale=0.85)
        unit2 = text_card("$0.60 per 100 g", ORANGE_TERM, scale=0.85)
        unit1.next_to(small, DOWN, buff=0.6)
        unit2.next_to(big, DOWN, buff=0.6)
        for m in unit1:
            m.set_z_index(2)
        for m in unit2:
            m.set_z_index(2)
        self.play(FadeIn(unit1, run_time=1.0), FadeIn(unit2, run_time=1.0))
        self.wait(2.5)

        verdict = Text("Big pack wins", font_size=24, color=GREEN_OK)
        verdict.next_to(VGroup(unit1, unit2), DOWN, buff=0.6)
        verdict_bg = BackgroundRectangle(verdict, color=BLACK, fill_opacity=0.95, buff=0.15)
        verdict_bg.move_to(verdict.get_center())
        self.play(FadeIn(verdict_bg, run_time=0.4), FadeIn(verdict, run_time=1.0))
        self.wait(3.0)

        # Clean up beat 2 before beat 3.
        beat2 = VGroup(small, big, unit1, unit2, verdict, verdict_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Wages: rate × hours = pay (~14 s)
        # ──────────────────────────────────────────────────────────────────
        rate = text_card("$22 per hour", BLUE_TERM, scale=0.95)
        times = text_card("× 8 hours", TEAL_TERM, scale=0.95)
        wages = VGroup(rate, times).arrange(RIGHT, buff=0.4)
        wages.move_to(BAND_CHART_CENTER + UP * 0.7)
        for m in wages:
            m.set_z_index(2)
        self.play(
            FadeIn(rate, shift=UP * 0.2, run_time=1.0),
            FadeIn(times, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(2.5)

        pay = text_card("$176", GREEN_OK, scale=1.6)
        pay.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        for m in pay:
            m.set_z_index(2)
        self.play(FadeOut(wages, run_time=0.9))
        self.play(FadeIn(pay, run_time=1.4))
        self.wait(3.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Fuel cost: price × litres = trip cost (~14 s)
        # ──────────────────────────────────────────────────────────────────
        beat3 = VGroup(pay)
        self.play(FadeOut(beat3, run_time=0.8))

        price = text_card("$1.40 per litre", BLUE_TERM, scale=0.95)
        litres = text_card("× 10 litres", TEAL_TERM, scale=0.95)
        trip = VGroup(price, litres).arrange(RIGHT, buff=0.4)
        trip.move_to(BAND_CHART_CENTER + UP * 0.7)
        for m in trip:
            m.set_z_index(2)
        self.play(
            FadeIn(price, shift=UP * 0.2, run_time=1.0),
            FadeIn(litres, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(2.5)

        cost = text_card("$14", GREEN_OK, scale=1.6)
        cost.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        for m in cost:
            m.set_z_index(2)
        self.play(FadeOut(trip, run_time=0.9))
        self.play(FadeIn(cost, run_time=1.4))
        self.wait(3.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~28 s, total ≈ 79 s)
        # ──────────────────────────────────────────────────────────────────
        beat4 = VGroup(cost)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"\text{Cost} \;=\; \text{rate} \times \text{quantity}",
            "Spot the rate, then multiply (or divide) to get what you need.",
            final_wait=28.0,
        )