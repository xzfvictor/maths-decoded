"""
Manim scene for the lesson `quadratic-and-other-modelling`
(topic `l9-a-modelling-change`).

When the rate of change itself changes, the model is quadratic: constant
second differences. The animation walks through the sequence
{0, 3, 12, 27, 48, ...}, shows the first and second differences,
generalises to y = ax² + bx + c, and rejects the common confusion of
calling a quadratic sequence exponential.

Target duration: ~99 s (matches the audio narration length of 99.25 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class QuadraticAndOtherModellingScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Quadratic and other models",
            "Constant second differences → quadratic.",
            hold=2.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Sequence {0, 3, 12, 27, 48, ...} + differences (~25 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Sequence: 0, 3, 12, 27, 48, ...",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.3)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.5)

        # First differences row.
        first_lbl = Text("1st differences:", font_size=20, color=ORANGE_TERM)
        first_row = MathTex(r"3,\ 9,\ 15,\ 21", color=ORANGE_TERM).scale(0.95)
        first_lbl.next_to(head, DOWN, buff=0.5)
        first_row.next_to(first_lbl, RIGHT, buff=0.4)
        first_lbl_bg = BackgroundRectangle(first_lbl, color=BLACK,
                                            fill_opacity=0.9, buff=0.12)
        first_lbl_bg.move_to(first_lbl.get_center())
        first_bg = BackgroundRectangle(first_row, color=BLACK,
                                       fill_opacity=0.9, buff=0.15)
        first_bg.move_to(first_row.get_center())

        self.play(
            FadeIn(first_lbl_bg, run_time=0.4),
            FadeIn(first_lbl, run_time=0.8),
            FadeIn(first_bg, run_time=0.4),
            FadeIn(first_row, run_time=1.0),
        )
        self.wait(2.0)

        # Second differences row.
        second_lbl = Text("2nd differences:", font_size=20, color=GREEN_OK)
        second_row = MathTex(r"6,\ 6,\ 6", color=GREEN_OK).scale(0.95)
        second_lbl.next_to(first_lbl, DOWN, buff=0.35)
        second_row.next_to(second_lbl, RIGHT, buff=0.4)
        second_lbl_bg = BackgroundRectangle(second_lbl, color=BLACK,
                                             fill_opacity=0.9, buff=0.12)
        second_lbl_bg.move_to(second_lbl.get_center())
        second_bg = BackgroundRectangle(second_row, color=BLACK,
                                        fill_opacity=0.9, buff=0.15)
        second_bg.move_to(second_row.get_center())

        self.play(
            FadeIn(second_lbl_bg, run_time=0.4),
            FadeIn(second_lbl, run_time=0.8),
            FadeIn(second_bg, run_time=0.4),
            FadeIn(second_row, run_time=1.0),
        )
        self.wait(2.0)

        # Highlight "constant".
        const = Text("constant  →  quadratic", font_size=22, color=GREEN_OK)
        const.next_to(second_lbl, DOWN, buff=0.5)
        const_bg = BackgroundRectangle(const, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        const_bg.move_to(const.get_center())
        self.play(FadeIn(const_bg, run_time=0.4), FadeIn(const, run_time=1.2))
        self.wait(2.5)

        beat2_group = VGroup(
            head, head_bg, first_lbl, first_lbl_bg, first_row, first_bg,
            second_lbl, second_lbl_bg, second_row, second_bg, const, const_bg,
        )
        self.play(FadeOut(beat2_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — General quadratic form y = ax² + bx + c (~18 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(r"y \;=\; a\,x^{2} + b\,x + c",
                                      color=BLUE_TERM, scale=1.4)
        general.move_to(BAND_CHART_CENTER + UP * 0.7)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        # Label each coefficient.
        line1 = MathTex(r"\text{leading coefficient } a \;\Rightarrow\; \text{shape}",
                        color=GREEN_OK).scale(0.85)
        line2 = MathTex(r"a, b, c \;=\; \text{constants}",
                        color=ORANGE_TERM).scale(0.85)
        line1.next_to(general, DOWN, buff=0.55)
        line2.next_to(line1, DOWN, buff=0.35)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=0.95, buff=0.18)
        line1_bg.move_to(line1.get_center())
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=0.95, buff=0.18)
        line2_bg.move_to(line2.get_center())
        self.play(FadeIn(line1_bg, run_time=0.4), FadeIn(line1, run_time=1.0))
        self.wait(0.6)
        self.play(FadeIn(line2_bg, run_time=0.4), FadeIn(line2, run_time=1.0))
        self.wait(2.5)

        beat3_group = VGroup(general, line1, line1_bg, line2, line2_bg)
        self.play(FadeOut(beat3_group, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: calling a quadratic "exponential" (~10 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(
            r"y = a \cdot b^{x}",
            color=RED_REJECT,
        ).scale(1.3)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.7)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())

        self.play(FadeIn(wrong_bg, run_time=0.5), Write(wrong, run_time=1.4))
        self.wait(1.0)

        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.7))
        self.wait(0.8)

        # Reason: constant RATIO ≠ constant 2nd differences.
        reason = MathTex(
            r"\text{exponential: constant RATIO}",
            color=ORANGE_TERM,
        ).scale(0.9)
        reason.next_to(wrong, DOWN, buff=0.5)
        reason_bg = BackgroundRectangle(reason, color=BLACK, fill_opacity=0.95, buff=0.18)
        reason_bg.move_to(reason.get_center())
        self.play(FadeIn(reason_bg, run_time=0.4), FadeIn(reason, run_time=1.2))
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(wrong, wrong_bg, cross, reason, reason_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=38 s, total ≈ 99 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y \;=\; a\,x^{2} + b\,x + c",
            "Constant second differences → quadratic model.",
            final_wait=38.0,
        )