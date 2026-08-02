"""
Manim scene for the lesson `financial-contexts`
(topic `l8-n-modelling-rationals-percentages`).

Financial problems reduce to a small set of patterns. The most
common trap is order: a discount then a tax is not the same as
a tax then a discount.

Target duration: ~92 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class FinancialContextsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Financial contexts",
            "One multiplier, one calculation",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Discount then tax: $200 → $150 → $165 (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("$200  →  -25%  →  +10% tax",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.9)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        # Discount step
        s1 = MathTex(r"200 \times 0.75 = 150", color=BLUE_TERM).scale(1.1)
        s1.move_to(BAND_CHART_CENTER + UP * 0.4)
        s1_bg = BackgroundRectangle(s1, color=BLACK, fill_opacity=1, buff=0.25)
        s1_bg.move_to(s1.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
            FadeIn(s1_bg, run_time=0.4),
            Write(s1, run_time=1.6),
        )
        self.wait(2.5)

        # Tax step
        s2 = MathTex(
            r"150 \times 1.10 = 165",
            color=GREEN_OK,
        ).scale(1.15)
        s2.next_to(s1, DOWN, buff=0.5)
        s2_bg = BackgroundRectangle(s2, color=BLACK, fill_opacity=1, buff=0.25)
        s2_bg.move_to(s2.get_center())

        self.play(
            FadeIn(s2_bg, run_time=0.4),
            Write(s2, run_time=1.6),
        )
        self.wait(5.0)

        beat2_group = VGroup(head, head_bg, s1, s1_bg, s2, s2_bg)
        self.play(FadeOut(beat2_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Wage example: $18.50 × 12 = $222 (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("Wage:  $18.50/h  ×  12 h",
                     font_size=24, color=TEAL_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.9)
        head2_bg = BackgroundRectangle(head2, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        w = MathTex(
            r"\text{earnings} = \text{rate} \times \text{hours}",
            color=TEAL_TERM,
        ).scale(1.0)
        w.move_to(BAND_CHART_CENTER + UP * 0.4)
        w_bg = BackgroundRectangle(w, color=BLACK, fill_opacity=1, buff=0.25)
        w_bg.move_to(w.get_center())

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
            FadeIn(w_bg, run_time=0.4),
            Write(w, run_time=1.6),
        )
        self.wait(2.0)

        wnum = MathTex(
            r"18.50 \times 12 = 222",
            color=GREEN_OK,
        ).scale(1.15)
        wnum.next_to(w, DOWN, buff=0.5)
        wnum_bg = BackgroundRectangle(wnum, color=BLACK, fill_opacity=1, buff=0.25)
        wnum_bg.move_to(wnum.get_center())

        self.play(
            FadeIn(wnum_bg, run_time=0.4),
            Write(wnum, run_time=1.4),
        )
        self.wait(4.0)

        # Unit rate reminder
        rate = Text(
            "Best buy: divide price by quantity → unit rate.",
            font_size=20,
            color=GREEN_OK,
        ).next_to(wnum, DOWN, buff=0.5)
        rate_bg = BackgroundRectangle(rate, color=BLACK, fill_opacity=0.95, buff=0.18)
        rate_bg.move_to(rate.get_center())

        self.play(
            FadeIn(rate_bg, run_time=0.4),
            FadeIn(rate, run_time=1.0),
        )
        self.wait(3.0)

        beat3_group = VGroup(head2, head2_bg, w, w_bg, wnum, wnum_bg, rate, rate_bg)
        self.play(FadeOut(beat3_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Warning: order matters; $100 -10% then +10% ≠ $100 (~17 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Order matters", font_size=24, color=RED_REJECT)
        head3.move_to(BAND_CHART_CENTER + UP * 1.9)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())

        walk = MathTex(
            r"100 \;\to\; 90 \;\to\; 99",
            color=RED_REJECT,
        ).scale(1.15)
        walk.move_to(BAND_CHART_CENTER + UP * 0.4)
        walk_bg = BackgroundRectangle(walk, color=BLACK, fill_opacity=1, buff=0.25)
        walk_bg.move_to(walk.get_center())

        self.play(
            FadeIn(head3_bg, run_time=0.4),
            FadeIn(head3, run_time=0.9),
            FadeIn(walk_bg, run_time=0.4),
            Write(walk, run_time=1.6),
        )
        self.wait(2.0)

        # Note
        note = Text(
            "10% off then 10% on  ≠  back to the original.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(walk, DOWN, buff=0.6)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())

        self.play(
            FadeIn(note_bg, run_time=0.4),
            FadeIn(note, run_time=1.0),
        )
        self.wait(3.0)

        beat4_group = VGroup(head3, head3_bg, walk, walk_bg, note, note_bg)
        self.play(FadeOut(beat4_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~35 s, total ≈ 92 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Identify } \text{givens, find unknowns, pick one multiplier}",
            "Discounts and taxes use the new amount as the base.",
            final_wait=35.0,
        )
