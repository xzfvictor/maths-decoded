"""
Manim scene for the lesson `design-test-refine`
(topic `l10a-asp-spatial-algorithms`).

Cycles for a spatial algorithm: design a pseudocode plan for the
typical case; test by tracing edge cases like equal points, horizontal
or vertical pairs, right angles, collinear (degenerate) cases; refine
failing steps; implement; and justify every step. Worked example:
distance algorithm — same point gives 0, far pair gives the expected
length.

Target duration: ~95 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class DesignTestRefineScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Design, test, refine",
            "Iterate the algorithm until every edge case works.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Design: pseudocode for the typical case (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Step 1: Design", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.1)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        # Show three sample pseudocode lines.
        lines = VGroup(
            Text("read x1, y1, x2, y2", font_size=22, color=BLUE_TERM),
            Text("dx := x2 - x1", font_size=22, color=BLUE_TERM),
            Text("dy := y2 - y1", font_size=22, color=BLUE_TERM),
            Text("d := sqrt(dx^2 + dy^2)", font_size=22, color=BLUE_TERM),
            Text("output d", font_size=22, color=BLUE_TERM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        lines.move_to(BAND_CHART_CENTER + DOWN * 0.35)

        lines_bg = BackgroundRectangle(lines, color=BLACK, fill_opacity=0.85, buff=0.18)
        lines_bg.move_to(lines.get_center())
        beat_2 = beat_group(beat_2, lines, lines_bg)

        self.play(FadeIn(lines_bg, run_time=0.4), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(l, run_time=0.6) for l in lines],
                             lag_ratio=0.18), run_time=2.2)
        self.wait(5.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Test edge cases (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head3 = Text("Step 2: Test edge cases", font_size=26, color=ORANGE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.15)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        beat_3 = beat_group(beat_3, head3, head3_bg)
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        # Three test-case cards.
        c1 = make_equation_card(
            r"\text{Equal points: } (1,1),(1,1) \;\Rightarrow\; d = 0",
            color=GREEN_OK, scale=0.62,
        )
        c1.move_to(BAND_CHART_CENTER + UP * 0.3 + LEFT * 3.0)
        c2 = make_equation_card(
            r"\text{Horizontal: } (1,1),(5,1) \;\Rightarrow\; d = 4",
            color=GREEN_OK, scale=0.62,
        )
        c2.move_to(BAND_CHART_CENTER + UP * 0.3)
        c3 = make_equation_card(
            r"\text{Vertical: } (2,1),(2,4) \;\Rightarrow\; d = 3",
            color=GREEN_OK, scale=0.62,
        )
        c3.move_to(BAND_CHART_CENTER + UP * 0.3 + RIGHT * 3.0)
        grp = VGroup(c1, c2, c3)
        beat_3 = beat_group(beat_3, c1, c2, c3)
        self.play(FadeIn(c1, shift=UP * 0.2, run_time=1.0))
        self.wait(0.4)
        self.play(FadeIn(c2, shift=UP * 0.2, run_time=1.0))
        self.wait(0.4)
        self.play(FadeIn(c3, shift=UP * 0.2, run_time=1.0))
        self.wait(2.0)

        # Triangle classifier card covering all four cases.
        c4 = make_equation_card(
            r"\text{Triangle: equilateral, isosceles, scalene, degenerate}",
            color=ORANGE_TERM, scale=0.6,
        )
        c4.move_to(BAND_CHART_CENTER + DOWN * 0.55)
        beat_3 = beat_group(beat_3, c4)
        self.play(FadeIn(c4, shift=UP * 0.2, run_time=1.2))
        self.wait(5.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Justify: every step needs a reason (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        head4 = Text("Step 3: Justify",
                     font_size=26, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.15)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        beat_4 = beat_group(beat_4, head4, head4_bg)
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        claim = MathTex(
            r"\text{midpoint} \;=\; \left(\dfrac{x_1+x_2}{2},\;\dfrac{y_1+y_2}{2}\right)",
            color=BLUE_TERM,
        ).scale(1.0)
        claim.move_to(BAND_CHART_CENTER + UP * 0.4)
        claim_bg = BackgroundRectangle(claim, color=BLACK, fill_opacity=1, buff=0.22)
        claim_bg.move_to(claim.get_center())
        beat_4 = beat_group(beat_4, claim, claim_bg)
        self.play(FadeIn(claim_bg, run_time=0.4), Write(claim, run_time=2.0))
        self.wait(2.0)

        reason = Text(
            "Average the x-coords — because the midpoint's x is\nhalfway between the two endpoints.",
            font_size=22, color=GREEN_OK,
        )
        reason.next_to(claim, DOWN, buff=0.5)
        reason_bg = BackgroundRectangle(reason, color=BLACK, fill_opacity=0.95, buff=0.15)
        reason_bg.move_to(reason.get_center())
        beat_4 = beat_group(beat_4, reason, reason_bg)
        self.play(FadeIn(reason_bg, run_time=0.4), FadeIn(reason, run_time=2.0))
        self.wait(8.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~38 s, total ≈ 95 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Design}\;\to\;\text{Test}\;\to\;\text{Refine}\;\to\;\text{Justify}",
            "Every step needs a reason, every edge case a test.",
            final_wait=38.0,
        )
