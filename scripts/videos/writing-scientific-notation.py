"""
Manim scene for the lesson `writing-scientific-notation`
(topic `l9-m-scientific-notation`).

A number is in scientific notation when written as a × 10ⁿ with
1 ≤ a < 10 and n an integer. The scene walks through converting
4500 = 4.5 × 10³ and 0.0032 = 3.2 × 10⁻³, generalises the rule,
and rejects the mistake of writing 45 × 10² (a is too big).

Render target: ~25 s audio + 20 s final wait.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class WritingScientificNotationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Writing numbers in scientific notation",
            "Move the decimal so exactly one non-zero digit sits to its left.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: 4500 → 4.5 × 10³
        # ──────────────────────────────────────────────────────────────────
        original = MathTex(r"4500", color=BLUE_TERM).scale(1.6)
        original.move_to(BAND_CHART_CENTER + UP * 0.9)
        original_bg = BackgroundRectangle(original, color=BLACK, fill_opacity=1, buff=0.22)
        original_bg.move_to(original.get_center())
        self.play(FadeIn(original_bg, run_time=0.4), Write(original, run_time=1.2))
        self.wait(0.6)

        # The shift note.
        move_note = Text("shift the decimal 3 places LEFT",
                         font_size=22, color=BLUE_TERM)
        move_note.move_to(BAND_CHART_CENTER + UP * 0.0)
        move_bg = BackgroundRectangle(move_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        move_bg.move_to(move_note.get_center())
        self.play(FadeIn(move_bg, run_time=0.3), FadeIn(move_note, run_time=0.8))
        self.wait(0.8)

        # The scientific-notation result.
        result = MathTex(r"4500 = 4.5 \times 10^{3}", color=GREEN_OK).scale(1.1)
        result.move_to(BAND_CHART_CENTER + DOWN * 0.9)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=1, buff=0.22)
        result_bg.move_to(result.get_center())
        self.play(FadeIn(result_bg, run_time=0.4), Write(result, run_time=1.3))
        self.wait(0.8)

        # Concrete #2: 0.0032 → 3.2 × 10⁻³
        orig2 = MathTex(r"0.0032", color=BLUE_TERM).scale(1.6)
        orig2.move_to(BAND_CHART_CENTER + UP * 0.9)
        orig2_bg = BackgroundRectangle(orig2, color=BLACK, fill_opacity=1, buff=0.22)
        orig2_bg.move_to(orig2.get_center())

        # Transform: shift up the first example, bring in the second.
        beat2a = beat_group(original, original_bg, move_note, move_bg,
                            result, result_bg)
        self.play(FadeOut(beat2a, run_time=0.6))

        orig2.move_to(BAND_CHART_CENTER + UP * 0.9)
        self.play(FadeIn(orig2_bg, run_time=0.4), Write(orig2, run_time=1.0))
        self.wait(0.4)

        move_note2 = Text("shift the decimal 3 places RIGHT",
                          font_size=22, color=BLUE_TERM)
        move_note2.move_to(BAND_CHART_CENTER + UP * 0.0)
        move_bg2 = BackgroundRectangle(move_note2, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        move_bg2.move_to(move_note2.get_center())
        self.play(FadeIn(move_bg2, run_time=0.3), FadeIn(move_note2, run_time=0.7))
        self.wait(0.5)

        result2 = MathTex(r"0.0032 = 3.2 \times 10^{-3}", color=GREEN_OK).scale(1.1)
        result2.move_to(BAND_CHART_CENTER + DOWN * 0.9)
        result2_bg = BackgroundRectangle(result2, color=BLACK, fill_opacity=1, buff=0.22)
        result2_bg.move_to(result2.get_center())
        self.play(FadeIn(result2_bg, run_time=0.4), Write(result2, run_time=1.3))
        self.wait(0.6)

        beat2b = beat_group(orig2, orig2_bg, move_note2, move_bg2,
                            result2, result2_bg)
        self.play(FadeOut(beat2b, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: a × 10ⁿ where 1 ≤ a < 10
        # ──────────────────────────────────────────────────────────────────
        general = MathTex(
            r"a \times 10^{n}, \quad 1 \le a < 10",
            color=BLUE_TERM,
        ).scale(1.15)
        general.move_to(BAND_CHART_CENTER + UP * 0.5)
        general_bg = BackgroundRectangle(general, color=BLACK, fill_opacity=1, buff=0.25)
        general_bg.move_to(general.get_center())
        self.play(FadeIn(general_bg, run_time=0.4), Write(general, run_time=1.2))
        self.wait(0.6)

        lbl_a = Text("a has exactly one non-zero digit in front of the decimal",
                     font_size=20, color=BLUE_TERM)
        lbl_a.next_to(general, DOWN, buff=0.4)
        lbl_a_bg = BackgroundRectangle(lbl_a, color=BLACK, fill_opacity=0.95, buff=0.13)
        lbl_a_bg.move_to(lbl_a.get_center())

        lbl_n = Text("n is an integer (positive, negative, or zero)",
                     font_size=20, color=BLUE_TERM)
        lbl_n.next_to(lbl_a, DOWN, buff=0.25)
        lbl_n_bg = BackgroundRectangle(lbl_n, color=BLACK, fill_opacity=0.95, buff=0.13)
        lbl_n_bg.move_to(lbl_n.get_center())

        self.play(FadeIn(lbl_a_bg, run_time=0.3), FadeIn(lbl_a, run_time=0.7))
        self.wait(0.4)
        self.play(FadeIn(lbl_n_bg, run_time=0.3), FadeIn(lbl_n, run_time=0.7))
        self.wait(0.8)

        beat3 = beat_group(general, general_bg, lbl_a, lbl_a_bg, lbl_n, lbl_n_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: 45 × 10² (a is too big)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(r"4500 = 45 \times 10^{2} \;\;?", color=RED_REJECT).scale(1.0)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.4)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.22)
        wrong_bg.move_to(wrong.get_center())
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.2))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.6))
        self.wait(0.5)

        fix = Text("a = 45 is NOT in [1, 10).", font_size=22, color=GREEN_OK)
        fix.next_to(wrong, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.15)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.3), FadeIn(fix, run_time=0.8))
        self.wait(0.6)

        beat4 = beat_group(wrong, wrong_bg, cross, fix, fix_bg)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a \times 10^{n}, \quad 1 \le a < 10",
            "One non-zero digit left of the decimal — count shifts for n.",
            final_wait=20.0,
        )
