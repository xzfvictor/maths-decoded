"""
Manim scene for the lesson `writing-scientific-notation`
(topic `l9-m-scientific-notation`).

A number is in scientific notation when written as a × 10ⁿ with
1 ≤ a < 10 and n an integer. The scene walks through converting
4500 = 4.5 × 10³, generalises the rule, and rejects the common
mistake of writing 45 × 10² (the coefficient 45 is too big).

Target duration: ~84 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class WritingScientificNotationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Writing numbers in scientific notation",
            "Move the decimal so one non-zero digit sits to its left.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: 4500 → 4.5 × 10³ (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Start with the original number.
        original = MathTex(r"4500", color=BLUE_TERM).scale(2.0)
        original.move_to(BAND_CHART_CENTER + UP * 0.9)
        original_bg = BackgroundRectangle(original, color=BLACK, fill_opacity=1, buff=0.25)
        original_bg.move_to(original.get_center())
        self.play(FadeIn(original_bg, run_time=0.4), Write(original, run_time=1.4))
        self.wait(1.5)

        # Move the decimal arrow (visual cue).
        arrow = Arrow(UP * 0.0, DOWN * 0.5, color=WHITE, stroke_width=3)
        move_note = Text("shift the decimal 3 places left",
                         font_size=22, color=BLUE_TERM)
        move_note.move_to(BAND_CHART_CENTER + DOWN * 0.2)
        move_bg = BackgroundRectangle(move_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        move_bg.move_to(move_note.get_center())
        self.play(
            FadeIn(move_bg, run_time=0.4),
            FadeIn(move_note, run_time=1.0),
        )
        self.wait(2.0)

        # The scientific-notation result.
        result = MathTex(r"4500 \;=\; 4.5 \times 10^{3}", color=GREEN_OK).scale(1.2)
        result.move_to(BAND_CHART_CENTER + DOWN * 1.3)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=1, buff=0.25)
        result_bg.move_to(result.get_center())
        self.play(FadeIn(result_bg, run_time=0.4), Write(result, run_time=1.6))
        self.wait(2.5)
        self.play(
            FadeOut(original, run_time=0.6),
            FadeOut(original_bg, run_time=0.6),
            FadeOut(move_note, run_time=0.6),
            FadeOut(move_bg, run_time=0.6),
            FadeOut(result, run_time=0.6),
            FadeOut(result_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: a × 10ⁿ where 1 ≤ a < 10 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(
            r"a \times 10^{n}, \quad 1 \le a < 10",
            color=BLUE_TERM, scale=1.2,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        lbl_a = Text("a has one non-zero digit in front of the decimal",
                     font_size=22, color=BLUE_TERM)
        lbl_a.next_to(general, DOWN, buff=0.5)
        lbl_a_bg = BackgroundRectangle(lbl_a, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl_a_bg.move_to(lbl_a.get_center())

        lbl_n = Text("n is an integer (positive, negative, or zero)",
                     font_size=22, color=BLUE_TERM)
        lbl_n.next_to(lbl_a, DOWN, buff=0.3)
        lbl_n_bg = BackgroundRectangle(lbl_n, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl_n_bg.move_to(lbl_n.get_center())

        self.play(FadeIn(lbl_a_bg, run_time=0.4), FadeIn(lbl_a, run_time=1.1))
        self.wait(1.2)
        self.play(FadeIn(lbl_n_bg, run_time=0.4), FadeIn(lbl_n, run_time=1.1))
        self.wait(2.0)
        self.play(
            FadeOut(general, run_time=0.7),
            FadeOut(lbl_a, run_time=0.7),
            FadeOut(lbl_a_bg, run_time=0.7),
            FadeOut(lbl_n, run_time=0.7),
            FadeOut(lbl_n_bg, run_time=0.7),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: 45 × 10² (a is too big) (~12 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(r"4500 = 45 \times 10^{2}\text{ ?}", color=RED_REJECT).scale(1.1)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.4)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.22)
        wrong_bg.move_to(wrong.get_center())
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.4))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.7))
        self.wait(1.2)

        fix = Text("a = 45 is NOT in [1, 10).", font_size=22, color=GREEN_OK)
        fix.next_to(wrong, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.15)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.2))
        self.wait(1.5)
        self.play(
            FadeOut(wrong, run_time=0.6),
            FadeOut(wrong_bg, run_time=0.6),
            FadeOut(cross, run_time=0.6),
            FadeOut(fix, run_time=0.6),
            FadeOut(fix_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~23 s, total ≈ 84 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a \times 10^{n}, \quad 1 \le a < 10",
            "One non-zero digit left of the decimal — count shifts for n.",
            final_wait=23.0,
        )
