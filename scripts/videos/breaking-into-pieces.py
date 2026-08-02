"""
Manim scene for the lesson `breaking-into-pieces`
(topic `l8-m-composite-shapes`).

A composite shape is two or more simple shapes joined together. Find
its area by splitting into familiar shapes and adding (or by
subtracting a gap from a bounding rectangle).

Target duration: ~96 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class BreakingIntoPiecesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Breaking composite shapes into pieces",
            "Split, calculate each piece, combine",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — L-shape: 6×4 minus 3×2 = 18 m²  (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("1. L-shape:  subtract the missing corner",
                    font_size=24, color=BLUE_TERM)
        # Title at UP*1.9 collided with the subtitle (y ≈ 2.3). Move
        # down to UP*1.3 so it sits cleanly inside the chart band.
        head.move_to(BAND_CHART_CENTER + UP * 1.3)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        # Full rectangle
        full = MathTex(
            r"\text{full rectangle} = 6 \times 4 = 24 \text{ m}^2",
            color=BLUE_TERM,
        ).scale(1.0)
        full.move_to(BAND_CHART_CENTER + UP * 0.5)
        full_bg = BackgroundRectangle(full, color=BLACK, fill_opacity=1, buff=0.25)
        full_bg.move_to(full.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
            FadeIn(full_bg, run_time=0.4),
            Write(full, run_time=1.6),
        )
        self.wait(2.5)

        # Missing piece
        miss = MathTex(
            r"\text{missing} = 3 \times 2 = 6 \text{ m}^2",
            color=ORANGE_TERM,
        ).scale(1.0)
        miss.next_to(full, DOWN, buff=0.45)
        miss_bg = BackgroundRectangle(miss, color=BLACK, fill_opacity=1, buff=0.25)
        miss_bg.move_to(miss.get_center())

        self.play(
            FadeIn(miss_bg, run_time=0.4),
            Write(miss, run_time=1.4),
        )
        self.wait(2.0)

        # Result
        result = MathTex(
            r"\text{L-shape} = 24 - 6 = 18 \text{ m}^2",
            color=GREEN_OK,
        ).scale(1.1)
        result.next_to(miss, DOWN, buff=0.5)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=1, buff=0.25)
        result_bg.move_to(result.get_center())

        self.play(
            FadeIn(result_bg, run_time=0.4),
            Write(result, run_time=1.4),
        )
        self.wait(3.0)

        beat2_group = VGroup(head, head_bg, full, full_bg, miss, miss_bg,
                             result, result_bg)
        self.play(FadeOut(beat2_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Add pieces: rectangle 5×3 + square 2×2 = 19 m²  (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("2. Add pieces:  two simple shapes",
                     font_size=24, color=TEAL_TERM)
        # Same fix as head — keep below the subtitle band.
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        rect = MathTex(
            r"\text{rectangle} = 5 \times 3 = 15 \text{ m}^2",
            color=TEAL_TERM,
        ).scale(1.0)
        rect.move_to(BAND_CHART_CENTER + UP * 0.5)
        rect_bg = BackgroundRectangle(rect, color=BLACK, fill_opacity=1, buff=0.25)
        rect_bg.move_to(rect.get_center())

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
            FadeIn(rect_bg, run_time=0.4),
            Write(rect, run_time=1.4),
        )
        self.wait(2.0)

        sq = MathTex(
            r"\text{square} = 2 \times 2 = 4 \text{ m}^2",
            color=ORANGE_TERM,
        ).scale(1.0)
        sq.next_to(rect, DOWN, buff=0.45)
        sq_bg = BackgroundRectangle(sq, color=BLACK, fill_opacity=1, buff=0.25)
        sq_bg.move_to(sq.get_center())

        self.play(
            FadeIn(sq_bg, run_time=0.4),
            Write(sq, run_time=1.4),
        )
        self.wait(2.0)

        total = MathTex(
            r"\text{total} = 15 + 4 = 19 \text{ m}^2",
            color=GREEN_OK,
        ).scale(1.1)
        total.next_to(sq, DOWN, buff=0.5)
        total_bg = BackgroundRectangle(total, color=BLACK, fill_opacity=1, buff=0.25)
        total_bg.move_to(total.get_center())

        self.play(
            FadeIn(total_bg, run_time=0.4),
            Write(total, run_time=1.4),
        )
        self.wait(3.0)

        # Perimeter note
        perim = Text(
            "Perimeter: walk around the outside — add every edge length.",
            font_size=20,
            color=GREEN_OK,
        ).next_to(total, DOWN, buff=0.5)
        perim_bg = BackgroundRectangle(perim, color=BLACK, fill_opacity=0.95, buff=0.18)
        perim_bg.move_to(perim.get_center())

        self.play(
            FadeIn(perim_bg, run_time=0.4),
            FadeIn(perim, run_time=1.0),
        )
        self.wait(3.0)

        beat3_group = VGroup(head2, head2_bg, rect, rect_bg, sq, sq_bg,
                             total, total_bg, perim, perim_bg)
        self.play(FadeOut(beat3_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Both strategies give the same answer (~16 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Both strategies:  same answer",
                     font_size=24, color=ORANGE_TERM)
        # Same fix as head — keep below the subtitle band.
        head3.move_to(BAND_CHART_CENTER + UP * 1.3)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())

        compare = MathTex(
            r"\text{add pieces} \;=\; \text{subtract the gap}",
            color=GREEN_OK,
        ).scale(1.05)
        compare.move_to(BAND_CHART_CENTER + UP * 0.3)
        compare_bg = BackgroundRectangle(compare, color=BLACK, fill_opacity=1, buff=0.25)
        compare_bg.move_to(compare.get_center())

        self.play(
            FadeIn(head3_bg, run_time=0.4),
            FadeIn(head3, run_time=0.9),
            FadeIn(compare_bg, run_time=0.4),
            Write(compare, run_time=1.6),
        )
        self.wait(2.5)

        # Pick the simpler one
        tip = Text(
            "Pick whichever has fewer, simpler pieces.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(compare, DOWN, buff=0.6)
        tip_bg = BackgroundRectangle(tip, color=BLACK, fill_opacity=0.95, buff=0.18)
        tip_bg.move_to(tip.get_center())

        self.play(
            FadeIn(tip_bg, run_time=0.4),
            FadeIn(tip, run_time=1.0),
        )
        self.wait(3.0)

        beat4_group = VGroup(head3, head3_bg, compare, compare_bg, tip, tip_bg)
        self.play(FadeOut(beat4_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~38 s, total ≈ 96 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Area} \;=\; \text{sum of simple-shape areas}",
            "Split, calculate each piece, then add. Or subtract the gap.",
            final_wait=38.0,
        )
