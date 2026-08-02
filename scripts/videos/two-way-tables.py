"""
Manim scene for the lesson `two-way-tables`
(topic `l8-p-two-event-outcomes`).

A two-way table cross-tabulates two categorical events A and B. The
four cells cover every combination; their probabilities sum to 1.
Show a class-of-30 example, then read off the marginal rule.

Target duration: ~86.0 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, PURPLE_ACCENT, YELLOW_HIGHLIGHT, make_term_card,
    make_equation_card, animate_intro, animate_final_definition,
    beat_group,
)
from manim import *


class TwoWayTablesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Two-way tables for two events",
            "A grid whose four cells cover every combination.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: class of 30 (~24 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None

        # Populate the cells with the values from the worked example.
        # In class of 30: 12 play sport, 8 play music, 4 do both.
        # Sport only: 12 - 4 = 8. Music only: 8 - 4 = 4. Neither: 30-16=14.
        # Smaller font (22 instead of 28) so the highlight box fits inside
        # the cell without overlapping the grid lines.
        # Cell width widened from 1.5 to 1.8 and header scale reduced from
        # 0.8 to 0.6 so the long "Total S / Total M" labels stay inside
        # their cells and don't bleed into the next column.
        vals = [
            [Text("4",  font_size=22, color=WHITE), Text("8",  font_size=22, color=WHITE), Text("12", font_size=22, color=YELLOW_HIGHLIGHT)],
            [Text("4",  font_size=22, color=WHITE), Text("14", font_size=22, color=WHITE), Text("18", font_size=22, color=YELLOW_HIGHLIGHT)],
            [Text("8",  font_size=22, color=YELLOW_HIGHLIGHT), Text("22", font_size=22, color=YELLOW_HIGHLIGHT), Text("30", font_size=22, color=GREEN_OK)],
        ]
        headers = [
            [MathTex("S \cap M",   color=BLUE_TERM).scale(0.6), MathTex("S \cap M'",  color=TEAL_TERM).scale(0.6), MathTex("S", color=YELLOW_HIGHLIGHT).scale(0.6)],
            [MathTex("S' \cap M",  color=TEAL_TERM).scale(0.6), MathTex("S' \cap M'", color=ORANGE_TERM).scale(0.6), MathTex("S'", color=YELLOW_HIGHLIGHT).scale(0.6)],
            [MathTex("M", color=YELLOW_HIGHLIGHT).scale(0.6), MathTex("M'", color=YELLOW_HIGHLIGHT).scale(0.6), MathTex(r"\sum", color=GREEN_OK).scale(0.6)],
        ]

        # Make a manual grid using rectangles and inline text.
        cell_w, cell_h = 1.8, 0.95
        grid = VGroup()
        # header rows
        for c in range(3):
            x = (c - 1) * cell_w
            head = headers[0][c].move_to(UP * 0.7 + RIGHT * x)
            grid.add(head)
            beat_2 = VGroup(beat_2, head) if beat_2 is not None else VGroup(head)
        # data rows 1 and 2
        for r, y in enumerate([UP * 0.0, DOWN * 0.95]):
            for c in range(3):
                x = (c - 1) * cell_w
                head = headers[r+1][c].move_to(y + RIGHT * x)
                grid.add(head)
                beat_2 = VGroup(beat_2, head)
                val = vals[r+1][c].move_to(y + RIGHT * x + DOWN * 0.45)
                grid.add(val)
                beat_2 = VGroup(beat_2, val)

        # Grid lines for clarity (kept inside y ∈ [-1.5, 1.8] safe area).
        h_lines = VGroup()
        # horizontal
        for y in [UP * 0.35, DOWN * 0.5, DOWN * 1.4]:
            line = Line(LEFT * 3.0, RIGHT * 3.0, color=WHITE, stroke_width=1).move_to(y)
            h_lines.add(line)
            beat_2 = VGroup(beat_2, line)
        v_lines = VGroup()
        # vertical — endpoints stay inside the safe area
        for x in [LEFT * 0.95, RIGHT * 0.95]:
            line = Line(UP * 0.95, DOWN * 1.45, color=WHITE, stroke_width=1).move_to(x)
            v_lines.add(line)
            beat_2 = VGroup(beat_2, line)

        # Background panel.
        bg = BackgroundRectangle(
            VGroup(grid, h_lines, v_lines),
            color=BLACK, fill_opacity=1, buff=0.25,
        )
        beat_2 = VGroup(beat_2, bg)

        self.play(FadeIn(bg, run_time=0.5))
        self.play(
            Create(h_lines, run_time=0.7),
            Create(v_lines, run_time=0.7),
        )
        self.play(FadeIn(grid, run_time=1.6))
        self.wait(3.0)

        # Highlight the "22" cell with a small, tight callout box that
        # stays within the cell — no overlap with the table grid.
        hl = SurroundingRectangle(
            vals[2][1], color=GREEN_OK, buff=0.10, stroke_width=3,
        )
        self.play(Create(hl, run_time=1.0))
        self.wait(3.0)
        self.play(FadeOut(hl, run_time=0.4))

        cap = Text(
            "The four cells cover every student in the class.",
            font_size=20, color=GREEN_OK,
        ).move_to(DOWN * 1.4)
        cap_bg = BackgroundRectangle(cap, color=BLACK, fill_opacity=0.95, buff=0.18)
        cap_bg.move_to(cap.get_center())
        beat_2 = VGroup(beat_2, cap_bg, cap)
        self.play(FadeIn(cap_bg, run_time=0.4), FadeIn(cap, run_time=1.4))
        self.wait(4.0)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Reading probabilities from the cells (~17 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None
        row_sum = MathTex(
            r"\Pr(A) = \Pr(A \cap B) + \Pr(A \cap B')",
            color=BLUE_TERM,
        ).scale(1.0)
        row_sum.move_to(BAND_CHART_CENTER + UP * 1.4)
        row_bg = BackgroundRectangle(row_sum, color=BLACK, fill_opacity=1, buff=0.25)
        row_bg.move_to(row_sum.get_center())
        beat_3 = VGroup(row_bg, row_sum)
        self.play(FadeIn(row_bg, run_time=0.4), FadeIn(row_sum, run_time=2.0))
        self.wait(3.0)

        all_sum = MathTex(
            r"\Pr(A \cap B) + \Pr(A \cap B') + \Pr(A' \cap B) + \Pr(A' \cap B') = 1",
            color=GREEN_OK,
        ).scale(0.75)
        all_sum.next_to(row_sum, DOWN, buff=0.55)
        all_bg = BackgroundRectangle(all_sum, color=BLACK, fill_opacity=1, buff=0.25)
        all_bg.move_to(all_sum.get_center())
        beat_3 = VGroup(beat_3, all_bg, all_sum)
        self.play(FadeIn(all_bg, run_time=0.4), FadeIn(all_sum, run_time=2.4))
        self.wait(5.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject forgetting one cell (~9 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None
        bad = MathTex(
            r"\Pr(A \cap B) + \Pr(A \cap B') + \Pr(A' \cap B) = 1",
            color=RED_REJECT,
        ).scale(0.95)
        bad.move_to(BAND_CHART_CENTER + UP * 0.4)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        beat_4 = VGroup(bad_bg, bad)
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=2.0))
        self.wait(2.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        beat_4 = VGroup(beat_4, cross)
        self.play(Create(cross, run_time=1.0))

        why = Text(
            "Missing 'neither' — sum will not reach 1.",
            font_size=22, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        beat_4 = VGroup(beat_4, why_bg, why)
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.4))
        self.wait(2.5)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 86.0 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\Pr(A \cap B) + \Pr(A \cap B') + \Pr(A' \cap B) + \Pr(A' \cap B') = 1",
            "Sum all four cells — they cover every outcome.",
            final_wait=32.0,
        )
