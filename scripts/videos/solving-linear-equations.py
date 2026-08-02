"""
Manim scene for the lesson `solving-linear-equations`
(topic `l9-a-linear-graphs-equations`).

A linear equation has x raised only to the first power. Solve by undoing
operations one at a time: subtract the constant, then divide by the
coefficient. The animation walks through 3x + 5 = 17 step by step,
generalises to ax + b = c, and rejects the common mistake of dividing
before subtracting.

Target duration: ~77 s (matches the audio narration length of 77.15 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SolvingLinearEquationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Solving linear equations",
            "Subtract the constant, then divide by the coefficient.",
            hold=2.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: 3x + 5 = 17 → x = 4 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Show the starting equation.
        eq1 = make_equation_card(r"3x + 5 = 17", color=BLUE_TERM, scale=1.4)
        eq1.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in eq1:
            m.set_z_index(2)
        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.5))
        self.wait(2.5)

        # Goal call-out.
        goal = Text(
            "Find the x that makes this true.",
            font_size=22,
            color=BLUE_TERM,
        ).next_to(eq1, DOWN, buff=0.7)
        goal_bg = BackgroundRectangle(goal, color=BLACK, fill_opacity=0.95, buff=0.18)
        goal_bg.move_to(goal.get_center())
        self.play(FadeIn(goal_bg, run_time=0.5), FadeIn(goal, run_time=1.2))
        self.wait(2.0)

        # Step 1: subtract 5 from both sides → 3x = 12.
        step1 = Text("step 1: subtract 5 from both sides",
                     font_size=22, color=GREEN_OK)
        step1.next_to(goal, DOWN, buff=0.4)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=0.95, buff=0.15)
        step1_bg.move_to(step1.get_center())
        self.play(FadeIn(step1_bg, run_time=0.4), FadeIn(step1, run_time=1.0))
        self.wait(1.8)

        eq2 = make_equation_card(r"3x = 12", color=GREEN_OK, scale=1.4)
        eq2.move_to(eq1.get_center())
        for m in eq2:
            m.set_z_index(2)
        self.play(Transform(eq1, eq2, run_time=1.4))
        self.wait(1.0)

        # Step 2: divide both sides by 3 → x = 4.
        step2 = Text("step 2: divide both sides by 3",
                     font_size=22, color=GREEN_OK)
        step2.next_to(step1, DOWN, buff=0.3)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=0.95, buff=0.15)
        step2_bg.move_to(step2.get_center())
        self.play(FadeIn(step2_bg, run_time=0.4), FadeIn(step2, run_time=1.0))
        self.wait(1.5)

        eq3 = make_equation_card(r"x = 4", color=GREEN_OK, scale=1.7)
        eq3.move_to(eq1.get_center())
        for m in eq3:
            m.set_z_index(2)
        self.play(Transform(eq1, eq3, run_time=1.4))
        self.wait(1.0)

        # Check: 3(4) + 5 = 12 + 5 = 17.
        check = MathTex(
            r"3(4) + 5 \;=\; 12 + 5 \;=\; 17",
            color=GREEN_OK,
        ).scale(1.0)
        check.next_to(eq1, DOWN, buff=2.0)
        check_bg = BackgroundRectangle(check, color=BLACK, fill_opacity=1, buff=0.25)
        check_bg.move_to(check.get_center())
        self.play(FadeIn(check_bg, run_time=0.5), Write(check, run_time=1.8))
        self.wait(1.5)
        self.play(Indicate(eq1, color=GREEN_OK, scale_factor=1.06), run_time=1.2)

        # Clear beat 2 to make room for the general rule.
        beat2_group = VGroup(eq1, goal, goal_bg, step1, step1_bg,
                             step2, step2_bg, check, check_bg)
        self.play(FadeOut(beat2_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise to the recipe ax + b = c → x = (c - b)/a (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Recipe for ax + b = c", font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 2.2)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        general = make_equation_card(
            r"x \;=\; \dfrac{c - b}{a}",
            color=BLUE_TERM,
            scale=1.4,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in general:
            m.set_z_index(2)

        self.play(FadeIn(head_bg, run_time=0.5), FadeIn(head, run_time=1.0))
        self.wait(1.5)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.5))
        self.wait(2.0)

        # Two-line recipe.
        line1 = MathTex(r"1.\; \text{Subtract } b", color=GREEN_OK).scale(0.95)
        line2 = MathTex(r"2.\; \text{Divide by } a", color=GREEN_OK).scale(0.95)
        line1.next_to(general, DOWN, buff=0.5)
        line2.next_to(line1, DOWN, buff=0.3)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=0.9, buff=0.18)
        line1_bg.move_to(line1.get_center())
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=0.9, buff=0.18)
        line2_bg.move_to(line2.get_center())
        self.play(FadeIn(line1_bg, run_time=0.4), FadeIn(line1, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(line2_bg, run_time=0.4), FadeIn(line2, run_time=1.0))
        self.wait(2.5)

        # Clean up beat 3.
        beat3_group = VGroup(head, head_bg, general,
                             line1, line1_bg, line2, line2_bg)
        self.play(FadeOut(beat3_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: divide first when a constant is added (~12 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(
            r"\dfrac{3x + 5}{3} \;=\; \dfrac{17}{3}",
            color=RED_REJECT,
        ).scale(1.1)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.8)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())

        self.play(FadeIn(wrong_bg, run_time=0.5), Write(wrong, run_time=1.4))
        self.wait(1.0)

        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.0)

        note = Text(
            "Divide BEFORE subtracting → the 5 doesn't cancel.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.5), FadeIn(note, run_time=1.2))
        self.wait(2.0)
        self.play(
            FadeOut(VGroup(wrong, wrong_bg, cross, note, note_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=28 s, total ≈ 77 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"x \;=\; \dfrac{c - b}{a}",
            "Subtract the constant first, then divide by the coefficient.",
            final_wait=28.0,
        )