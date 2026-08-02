"""
Manim scene for the lesson `expand-and-factorise`
(topic `l8-a-linear-expressions`).

The distributive law is the bridge between multiplication and addition.
Expand distributes a factor across every term inside a bracket; factorise
pulls out the greatest common factor to contract a sum back into a
product. The animation walks through one of each direction, then sums up
the rule.

Target duration: ~93 s (matches the audio narration length of 93.85 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ExpandAndFactoriseScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Distributive law: expand and factorise",
            "From product to sum, and back again.",
        )
        # Keep the title visible for the rest of the animation as a
        # constant header — matches the polynomial video's layout.

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Expand 4(x + 3) -> 4x + 12 (~20 s)
        # ──────────────────────────────────────────────────────────────────
        # Show the original product, with the 4 floating above the bracket
        # and an arrow that says "multiply each term".
        expr_left = MathTex(r"4\,(x + 3)").scale(1.4)
        expr_left.move_to(BAND_CHART_CENTER + UP * 1.2)
        expr_left_bg = BackgroundRectangle(expr_left, color=BLACK, fill_opacity=1, buff=0.25)
        expr_left_bg.move_to(expr_left.get_center())

        self.play(FadeIn(expr_left_bg, run_time=0.4), Write(expr_left, run_time=1.5))
        self.wait(2.0)

        # Two arrows fanning out from the 4 to the x and the 3, to
        # make the distribution visually obvious.
        arrow_x = Arrow(
            expr_left.get_left() + UP * 0.45,
            expr_left.get_center() + DOWN * 0.2 + LEFT * 1.4,
            color=BLUE_TERM,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25,
        )
        arrow_3 = Arrow(
            expr_left.get_right() + UP * 0.45,
            expr_left.get_center() + DOWN * 0.2 + RIGHT * 1.4,
            color=BLUE_TERM,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25,
        )
        self.play(Create(arrow_x, run_time=0.8), Create(arrow_3, run_time=0.8))
        self.wait(1.5)

        # Distribute: each term inside the bracket gets multiplied by 4.
        lbl_x = MathTex(r"\times\, 4", color=BLUE_TERM).scale(0.8)
        lbl_x.next_to(arrow_x, DOWN, buff=0.25)
        lbl_3 = MathTex(r"\times\, 4", color=BLUE_TERM).scale(0.8)
        lbl_3.next_to(arrow_3, DOWN, buff=0.25)
        self.play(FadeIn(lbl_x, run_time=0.6), FadeIn(lbl_3, run_time=0.6))
        self.wait(2.0)

        # Replace the product with the expanded sum 4x + 12.
        expr_right = MathTex(r"4x + 12").scale(1.4).set_color_by_tex("4x", BLUE_TERM)
        expr_right.move_to(BAND_CHART_CENTER + UP * 1.2)
        expr_right_bg = BackgroundRectangle(expr_right, color=BLACK, fill_opacity=1, buff=0.25)
        expr_right_bg.move_to(expr_right.get_center())

        self.play(
            FadeOut(VGroup(expr_left, expr_left_bg, arrow_x, arrow_3, lbl_x, lbl_3), run_time=1.0),
        )
        self.play(FadeIn(expr_right_bg, run_time=0.4), Write(expr_right, run_time=1.5))
        self.wait(2.0)

        # Note below: every term gets the 4.
        note1 = Text(
            "Distribute 4 to every term inside the bracket.",
            font_size=22,
            color=BLUE_TERM,
        ).next_to(expr_right, DOWN, buff=0.6)
        note1_bg = BackgroundRectangle(note1, color=BLACK, fill_opacity=0.95, buff=0.18)
        note1_bg.move_to(note1.get_center())
        self.play(FadeIn(note1_bg, run_time=0.5), FadeIn(note1, run_time=1.2))
        self.wait(4.0)
        self.play(
            FadeOut(VGroup(expr_right, expr_right_bg, note1, note1_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Expand 5(2y - 7) -> 10y - 35 (~20 s)
        # ──────────────────────────────────────────────────────────────────
        expr2_left = MathTex(r"5\,(2y - 7)").scale(1.4)
        expr2_left.move_to(BAND_CHART_CENTER + UP * 1.2)
        expr2_left_bg = BackgroundRectangle(expr2_left, color=BLACK, fill_opacity=1, buff=0.25)
        expr2_left_bg.move_to(expr2_left.get_center())

        self.play(FadeIn(expr2_left_bg, run_time=0.4), Write(expr2_left, run_time=1.5))
        self.wait(2.0)

        # Two arrows again, this time with subtraction in mind.
        arrow2_2y = Arrow(
            expr2_left.get_left() + UP * 0.45,
            expr2_left.get_center() + DOWN * 0.2 + LEFT * 1.4,
            color=TEAL_TERM,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25,
        )
        arrow2_7 = Arrow(
            expr2_left.get_right() + UP * 0.45,
            expr2_left.get_center() + DOWN * 0.2 + RIGHT * 1.4,
            color=TEAL_TERM,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25,
        )
        self.play(Create(arrow2_2y, run_time=0.8), Create(arrow2_7, run_time=0.8))
        self.wait(1.5)

        lbl2_2y = MathTex(r"\times\, 5", color=TEAL_TERM).scale(0.8)
        lbl2_2y.next_to(arrow2_2y, DOWN, buff=0.25)
        lbl2_7 = MathTex(r"\times\, 5", color=TEAL_TERM).scale(0.8)
        lbl2_7.next_to(arrow2_7, DOWN, buff=0.25)
        self.play(FadeIn(lbl2_2y, run_time=0.6), FadeIn(lbl2_7, run_time=0.6))
        self.wait(2.0)

        # Result: 10y - 35. Subtraction is preserved.
        expr2_right = MathTex(r"10y - 35").scale(1.4).set_color_by_tex("10y", TEAL_TERM)
        expr2_right.move_to(BAND_CHART_CENTER + UP * 1.2)
        expr2_right_bg = BackgroundRectangle(expr2_right, color=BLACK, fill_opacity=1, buff=0.25)
        expr2_right_bg.move_to(expr2_right.get_center())

        self.play(
            FadeOut(VGroup(expr2_left, expr2_left_bg, arrow2_2y, arrow2_7, lbl2_2y, lbl2_7), run_time=1.0),
        )
        self.play(FadeIn(expr2_right_bg, run_time=0.4), Write(expr2_right, run_time=1.5))
        self.wait(2.0)

        # Note below: subtraction is carried through.
        note2 = Text(
            "Subtraction works the same way: every term gets the 5.",
            font_size=22,
            color=TEAL_TERM,
        ).next_to(expr2_right, DOWN, buff=0.6)
        note2_bg = BackgroundRectangle(note2, color=BLACK, fill_opacity=0.95, buff=0.18)
        note2_bg.move_to(note2.get_center())
        self.play(FadeIn(note2_bg, run_time=0.5), FadeIn(note2, run_time=1.2))
        self.wait(4.0)
        self.play(
            FadeOut(VGroup(expr2_right, expr2_right_bg, note2, note2_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Factorise 6x + 9 -> 3(2x + 3) (~25 s)
        # ──────────────────────────────────────────────────────────────────
        # Show the original sum, then highlight that 6 and 9 share a 3.
        expr3_left = MathTex(r"6x + 9").scale(1.4).set_color_by_tex("6x", ORANGE_TERM).set_color_by_tex("9", ORANGE_TERM)
        expr3_left.move_to(BAND_CHART_CENTER + UP * 1.2)
        expr3_left_bg = BackgroundRectangle(expr3_left, color=BLACK, fill_opacity=1, buff=0.25)
        expr3_left_bg.move_to(expr3_left.get_center())

        self.play(FadeIn(expr3_left_bg, run_time=0.4), Write(expr3_left, run_time=1.5))
        self.wait(2.0)

        # Underline / circle the coefficients and point out the common factor 3.
        coeff_box = SurroundingRectangle(
            MathTex(r"6").set_color_by_tex("6", ORANGE_TERM),
            color=ORANGE_TERM,
            buff=0.12,
            stroke_width=3,
        )
        # Simpler approach: highlight with two small circles.
        circ6 = Circle(radius=0.32, color=ORANGE_TERM, stroke_width=4).move_to(expr3_left.get_center() + LEFT * 1.55 + DOWN * 0.25)
        circ9 = Circle(radius=0.32, color=ORANGE_TERM, stroke_width=4).move_to(expr3_left.get_center() + RIGHT * 1.55 + DOWN * 0.25)
        self.play(Create(circ6, run_time=0.8), Create(circ9, run_time=0.8))
        self.wait(1.5)

        gcd_lbl = MathTex(r"\text{GCD} \;=\; 3", color=GREEN_OK).scale(1.0)
        gcd_lbl.next_to(expr3_left, DOWN, buff=0.7)
        gcd_lbl_bg = BackgroundRectangle(gcd_lbl, color=BLACK, fill_opacity=0.95, buff=0.2)
        gcd_lbl_bg.move_to(gcd_lbl.get_center())
        self.play(FadeIn(gcd_lbl_bg, run_time=0.5), FadeIn(gcd_lbl, run_time=1.2))
        self.wait(3.0)

        # Pull the 3 out and show the factorised form.
        expr3_right = MathTex(r"3\,(2x + 3)").scale(1.4).set_color_by_tex("3\,(2x + 3)", GREEN_OK)
        expr3_right.move_to(BAND_CHART_CENTER + UP * 1.2)
        expr3_right_bg = BackgroundRectangle(expr3_right, color=BLACK, fill_opacity=1, buff=0.25)
        expr3_right_bg.move_to(expr3_right.get_center())

        self.play(
            FadeOut(VGroup(expr3_left, expr3_left_bg, circ6, circ9, gcd_lbl, gcd_lbl_bg), run_time=1.0),
        )
        self.play(FadeIn(expr3_right_bg, run_time=0.4), Write(expr3_right, run_time=1.5))
        self.wait(2.0)

        # Note below.
        note3 = Text(
            "Factorise by pulling out the greatest common factor.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(expr3_right, DOWN, buff=0.6)
        note3_bg = BackgroundRectangle(note3, color=BLACK, fill_opacity=0.95, buff=0.18)
        note3_bg.move_to(note3.get_center())
        self.play(FadeIn(note3_bg, run_time=0.5), FadeIn(note3, run_time=1.2))
        self.wait(5.0)
        self.play(
            FadeOut(VGroup(expr3_right, expr3_right_bg, note3, note3_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~23 s, total ≈ 93 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a\,(b + c) \;=\; ab + ac",
            "Distribute a over every term; factorise by pulling out the GCD.",
            final_wait=24.0,
        )