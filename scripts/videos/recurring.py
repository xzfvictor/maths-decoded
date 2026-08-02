"""
Manim scene for the lesson `recurring`
(topic `l8-n-fractions-decimals`).

Convert a recurring decimal back to a fraction with the multiply-and-subtract
trick: let x = the decimal, multiply by 10^k where k is the block length,
subtract the original equation to clear the block, then solve for x.

Target duration: ~92 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, beat_group,
    animate_intro, animate_final_definition,
)
from manim import *


class RecurringScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Recurring decimals back to fractions",
            "Multiply by 10^k, subtract, solve for x",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Set up: x = 0.overline{6}, then 10x = 6.overline{6} (~16 s)
        # ──────────────────────────────────────────────────────────────────
        # Step 1: let x = 0.overline{6}.
        # Place the "Step 1" label at a fixed y (UP*1.0) so it doesn't
        # collide with the subtitle; place the equation below it (UP*0.3).
        x_def = MathTex(r"x \;=\; 0.\overline{6}", color=BLUE_TERM).scale(1.2)
        x_def.move_to(BAND_CHART_CENTER + UP * 0.3)
        x_def_bg = BackgroundRectangle(x_def, color=BLACK,
                                       fill_opacity=1, buff=0.28)
        x_def_bg.move_to(x_def.get_center())

        lbl1 = Text("Step 1: let x equal the decimal",
                    font_size=22, color=BLUE_TERM)
        lbl1.move_to(BAND_CHART_CENTER + UP * 1.0)
        lbl1_bg = BackgroundRectangle(lbl1, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        lbl1_bg.move_to(lbl1.get_center())

        self.play(
            FadeIn(lbl1_bg, run_time=0.4),
            FadeIn(lbl1, run_time=0.9),
        )
        self.play(
            FadeIn(x_def_bg, run_time=0.4),
            Write(x_def, run_time=1.5),
        )
        self.wait(3.0)

        # Step 2: multiply by 10 because the block has length 1.
        ten_x = MathTex(r"10x \;=\; 6.\overline{6}", color=TEAL_TERM).scale(1.2)
        ten_x.next_to(x_def, DOWN, buff=0.55)
        ten_x_bg = BackgroundRectangle(ten_x, color=BLACK,
                                       fill_opacity=1, buff=0.28)
        ten_x_bg.move_to(ten_x.get_center())

        lbl2 = Text(
            "Step 2: multiply by 10 (block length is 1)",
            font_size=22, color=TEAL_TERM,
        )
        lbl2.next_to(ten_x, DOWN, buff=0.3)
        lbl2_bg = BackgroundRectangle(lbl2, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        lbl2_bg.move_to(lbl2.get_center())

        self.play(
            FadeIn(ten_x_bg, run_time=0.4),
            Write(ten_x, run_time=1.5),
        )
        self.play(
            FadeIn(lbl2_bg, run_time=0.4),
            FadeIn(lbl2, run_time=0.9),
        )
        self.wait(3.5)

        # Beat 2 group — fade out everything before beat 3 starts.
        beat2 = beat_group(lbl1, lbl1_bg, x_def, x_def_bg,
                           ten_x, ten_x_bg, lbl2, lbl2_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Subtract and solve: 9x = 6 ⇒ x = 6/9 = 2/3 (~16 s)
        # ──────────────────────────────────────────────────────────────────
        sub = MathTex(
            r"10x - x \;=\; 6.\overline{6} - 0.\overline{6}",
            color=ORANGE_TERM,
        ).scale(1.1)
        sub.move_to(BAND_CHART_CENTER + UP * 1.0)
        sub_bg = BackgroundRectangle(sub, color=BLACK,
                                     fill_opacity=1, buff=0.25)
        sub_bg.move_to(sub.get_center())

        self.play(
            FadeIn(sub_bg, run_time=0.4),
            Write(sub, run_time=1.6),
        )
        self.wait(2.5)

        nine = MathTex(r"9x \;=\; 6", color=ORANGE_TERM).scale(1.3)
        nine.next_to(sub, DOWN, buff=0.5)
        nine_bg = BackgroundRectangle(nine, color=BLACK,
                                      fill_opacity=1, buff=0.28)
        nine_bg.move_to(nine.get_center())

        self.play(
            FadeIn(nine_bg, run_time=0.4),
            Write(nine, run_time=1.4),
        )
        self.wait(2.5)

        six_nine = MathTex(r"x \;=\; \dfrac{6}{9}", color=GREEN_OK).scale(1.3)
        six_nine.next_to(nine, DOWN, buff=0.5)
        six_nine_bg = BackgroundRectangle(six_nine, color=BLACK,
                                         fill_opacity=1, buff=0.28)
        six_nine_bg.move_to(six_nine.get_center())

        self.play(
            FadeIn(six_nine_bg, run_time=0.4),
            Write(six_nine, run_time=1.4),
        )
        self.wait(2.0)

        # Fade out the work (sub, nine, six_nine) before showing the answer.
        beat3_work = beat_group(sub, sub_bg, nine, nine_bg,
                                six_nine, six_nine_bg)
        self.play(FadeOut(beat3_work, run_time=0.8))

        # Show the final reduced answer at a fresh position.
        reduced = MathTex(
            r"x \;=\; \dfrac{6}{9} \;=\; \dfrac{2}{3}",
            color=GREEN_OK,
        ).scale(1.3)
        reduced.move_to(BAND_CHART_CENTER + UP * 0.3)
        reduced_bg = BackgroundRectangle(reduced, color=BLACK,
                                         fill_opacity=1, buff=0.3)
        reduced_bg.move_to(reduced.get_center())

        self.play(
            FadeIn(reduced_bg, run_time=0.5),
            Write(reduced, run_time=1.6),
        )
        self.wait(3.5)

        beat3_answer = beat_group(reduced, reduced_bg)
        self.play(FadeOut(beat3_answer, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Quick second example: 0.overline{3} = 1/3 (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Quick check: 0.overline{3}",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.6)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        eq1 = MathTex(r"10x - x = 3", color=BLUE_TERM).scale(1.1)
        eq1.next_to(head, DOWN, buff=0.5)
        eq1_bg = BackgroundRectangle(eq1, color=BLACK,
                                     fill_opacity=1, buff=0.25)
        eq1_bg.move_to(eq1.get_center())

        eq2 = MathTex(r"9x = 3", color=BLUE_TERM).scale(1.1)
        eq2.next_to(eq1, DOWN, buff=0.4)
        eq2_bg = BackgroundRectangle(eq2, color=BLACK,
                                     fill_opacity=1, buff=0.25)
        eq2_bg.move_to(eq2.get_center())

        eq3 = MathTex(r"x = \dfrac{3}{9} = \dfrac{1}{3}",
                      color=GREEN_OK).scale(1.1)
        eq3.next_to(eq2, DOWN, buff=0.4)
        eq3_bg = BackgroundRectangle(eq3, color=BLACK,
                                     fill_opacity=1, buff=0.28)
        eq3_bg.move_to(eq3.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
        )
        self.wait(1.0)
        self.play(FadeIn(eq1_bg, run_time=0.4), Write(eq1, run_time=1.0))
        self.wait(1.5)
        self.play(FadeIn(eq2_bg, run_time=0.4), Write(eq2, run_time=1.0))
        self.wait(2.0)
        self.play(FadeIn(eq3_bg, run_time=0.4), Write(eq3, run_time=1.2))
        self.wait(3.5)

        beat4 = beat_group(head, head_bg, eq1, eq1_bg, eq2, eq2_bg,
                           eq3, eq3_bg)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (total ≈ 92 s; final_wait = 35 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Let } x = 0.\overline{a}; \quad 10x - x = a;\;"
            r"x = \dfrac{a}{9}",
            "Multiply by 10^k (block length), subtract, solve.",
            final_wait=35.0,
        )
