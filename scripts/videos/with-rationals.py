"""
Manim scene for the lesson `with-rationals`
(topic `l8-n-four-operations`).

A rational number is anything of the form p/q with q != 0. The trick is
to convert to one form first, then apply the integer strategy. The
animation shows 3/4 -> 0.75, then 0.75 + 0.5 = 1.25, and finally adds
a PEMDAS reminder.

Target duration: ~105 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, beat_group,
    animate_intro, animate_final_definition,
)
from manim import *


class WithRationalsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Efficient strategies with rationals",
            "Convert to one form, then use the integer strategy",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Convert 3/4 to 0.75 (concrete example, ~25 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("1. Convert fraction to decimal", font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.3)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        # Card for 3/4
        frac_card = make_term_card(r"\dfrac{3}{4}", "power-of-10 denominator", BLUE_TERM)
        frac_card.move_to(BAND_CHART_CENTER + UP * 0.4)
        frac_card.set_z_index(2)

        # Conversion result
        dec_card = make_term_card(r"0.75", "decimal form", GREEN_OK)
        dec_card.move_to(BAND_CHART_CENTER + UP * 0.4)
        dec_card.set_z_index(2)

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
            FadeIn(frac_card, shift=UP * 0.2, run_time=1.2),
        )
        self.wait(2.5)

        # Arrow showing the conversion
        arrow = Arrow(frac_card.get_right(), dec_card.get_left(),
                      color=BLUE_TERM, buff=0.2, stroke_width=3)
        arrow.next_to(frac_card, RIGHT, buff=0.6)
        # Recompute arrow target because we put both cards at same anchor
        arrow = Arrow(frac_card.get_right(), frac_card.get_right() + RIGHT * 0.8,
                      color=BLUE_TERM, buff=0.0, stroke_width=3)

        # Simpler: just transform the card to the decimal
        self.play(
            FadeOut(frac_card, run_time=0.8),
        )
        self.play(FadeIn(dec_card, shift=UP * 0.2, run_time=1.2))
        self.wait(2.0)

        # Quick check note: 75 / 100 = 0.75
        check = MathTex(
            r"\dfrac{3}{4} = \dfrac{75}{100} = 0.75",
            color=GREEN_OK,
        ).scale(0.9)
        check.next_to(dec_card, DOWN, buff=0.6)
        check_bg = BackgroundRectangle(check, color=BLACK, fill_opacity=1, buff=0.2)
        check_bg.move_to(check.get_center())

        self.play(
            FadeIn(check_bg, run_time=0.4),
            Write(check, run_time=1.6),
        )
        self.wait(4.0)

        beat2 = beat_group(head, head_bg, dec_card, check, check_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Add 0.75 + 0.5 = 1.25 with PEMDAS (~25 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("2. Now add:  0.75 + 0.5",
                     font_size=24, color=TEAL_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        lhs = MathTex(r"0.75 + 0.5", color=TEAL_TERM).scale(1.1)
        lhs.move_to(BAND_CHART_CENTER + UP * 0.4)
        lhs_bg = BackgroundRectangle(lhs, color=BLACK, fill_opacity=1, buff=0.22)
        lhs_bg.move_to(lhs.get_center())

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
            FadeIn(lhs_bg, run_time=0.4),
            Write(lhs, run_time=1.4),
        )
        self.wait(2.5)

        result = MathTex(r"= 1.25", color=GREEN_OK).scale(1.2)
        result.next_to(lhs, DOWN, buff=0.5)
        result_bg = BackgroundRectangle(result, color=BLACK,
                                        fill_opacity=1, buff=0.25)
        result_bg.move_to(result.get_center())

        self.play(
            FadeIn(result_bg, run_time=0.4),
            Write(result, run_time=1.4),
        )
        self.wait(2.5)

        # PEMDAS reminder note
        pemdas = Text(
            "PEMDAS still applies — addition last, after any × or ÷",
            font_size=20,
            color=GREEN_OK,
        ).next_to(result, DOWN, buff=0.6)
        pemdas_bg = BackgroundRectangle(pemdas, color=BLACK, fill_opacity=0.95, buff=0.18)
        pemdas_bg.move_to(pemdas.get_center())

        self.play(
            FadeIn(pemdas_bg, run_time=0.4),
            FadeIn(pemdas, run_time=1.0),
        )
        self.wait(5.0)

        beat3 = beat_group(head2, head2_bg, lhs, lhs_bg, result, result_bg,
                           pemdas, pemdas_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Contrast: try to add 3/4 + 1/2 without converting (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Without converting…", font_size=24, color=RED_REJECT)
        head3.move_to(BAND_CHART_CENTER + UP * 1.3)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())

        raw = MathTex(
            r"\dfrac{3}{4} + \dfrac{1}{2} \;=\; \text{?}",
            color=RED_REJECT,
        ).scale(1.1)
        raw.move_to(BAND_CHART_CENTER + UP * 0.4)
        raw_bg = BackgroundRectangle(raw, color=BLACK, fill_opacity=1, buff=0.25)
        raw_bg.move_to(raw.get_center())

        self.play(
            FadeIn(head3_bg, run_time=0.4),
            FadeIn(head3, run_time=0.9),
            FadeIn(raw_bg, run_time=0.4),
            Write(raw, run_time=1.4),
        )
        self.wait(1.5)

        # Cross through
        cross = Cross(raw, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.0)

        # Explanation
        note = Text(
            "Different denominators — convert first, then add.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(raw, DOWN, buff=0.6)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())

        self.play(
            FadeIn(note_bg, run_time=0.4),
            FadeIn(note, run_time=1.0),
        )
        self.wait(4.5)

        beat4 = beat_group(head3, head3_bg, raw, raw_bg, cross, note, note_bg)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~40 s, total ≈ 105 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Rationals} \;\Rightarrow\; \text{convert, then compute}",
            "PEMDAS still applies. Estimate first to catch slips.",
            final_wait=40.0,
        )
