"""
Manim scene for the lesson `solving-equations`
(topic `l8-a-linear-equations-inequalities`).

Solving a linear equation means finding the value of the variable that
makes the equation true. The technique is to apply inverse operations
to both sides — undo addition/subtraction first, then undo
multiplication/division. The scene walks through 3x + 5 = 17 step by
step and closes with the general two-step recipe.

Target duration: ~87 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, YELLOW_HIGHLIGHT, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SolvingEquationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Solving linear equations",
            "Undo addition, then multiplication — both sides at once.",
            hold=2.5,
        )
        # Keep the title visible for the rest of the animation as a
        # constant header — matches the polynomial video's layout.

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Show the equation 3x + 5 = 17 (~14 s)
        # ──────────────────────────────────────────────────────────────────
        eq1 = make_equation_card(r"3x + 5 = 17", color=BLUE_TERM, scale=1.4)
        eq1.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in eq1:
            m.set_z_index(2)
        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.5))
        self.wait(3.0)

        # Goal: find the x that makes this true.
        goal = Text(
            "Find the value of x that makes this true.",
            font_size=22,
            color=BLUE_TERM,
        ).next_to(eq1, DOWN, buff=0.7)
        goal_bg = BackgroundRectangle(goal, color=BLACK, fill_opacity=0.95, buff=0.18)
        goal_bg.move_to(goal.get_center())
        self.play(FadeIn(goal_bg, run_time=0.5), FadeIn(goal, run_time=1.2))
        self.wait(4.0)
        self.play(
            FadeOut(goal, run_time=0.8),
            FadeOut(goal_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Step 1: subtract 5 → 3x = 12 (~17 s)
        # ──────────────────────────────────────────────────────────────────
        # Down arrow + label below the equation.
        arrow1 = Arrow(
            start=eq1.get_bottom() + DOWN * 0.3,
            end=eq1.get_bottom() + DOWN * 1.0,
            color=GREEN_OK,
            buff=0,
            stroke_width=6,
        )
        lbl1 = Text("subtract 5 from both sides", font_size=22, color=GREEN_OK)
        lbl1.next_to(arrow1, DOWN, buff=0.3)
        lbl1_bg = BackgroundRectangle(lbl1, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl1_bg.move_to(lbl1.get_center())

        self.play(Create(arrow1, run_time=1.0))
        self.play(FadeIn(lbl1_bg, run_time=0.4), FadeIn(lbl1, run_time=1.0))
        self.wait(2.0)

        # Transform the equation in place.
        eq2 = make_equation_card(r"3x = 12", color=GREEN_OK, scale=1.4)
        eq2.move_to(eq1.get_center())
        for m in eq2:
            m.set_z_index(2)
        self.play(Transform(eq1, eq2, run_time=1.6))
        self.wait(1.5)
        self.play(
            FadeOut(arrow1, run_time=0.8),
            FadeOut(lbl1, run_time=0.8),
            FadeOut(lbl1_bg, run_time=0.8),
        )
        self.wait(3.0)
        self.play(Indicate(eq1, color=GREEN_OK, scale_factor=1.06), run_time=1.2)

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Step 2: divide by 3 → x = 4 (~17 s)
        # ──────────────────────────────────────────────────────────────────
        arrow2 = Arrow(
            start=eq1.get_bottom() + DOWN * 0.3,
            end=eq1.get_bottom() + DOWN * 1.0,
            color=GREEN_OK,
            buff=0,
            stroke_width=6,
        )
        lbl2 = Text("divide both sides by 3", font_size=22, color=GREEN_OK)
        lbl2.next_to(arrow2, DOWN, buff=0.3)
        lbl2_bg = BackgroundRectangle(lbl2, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl2_bg.move_to(lbl2.get_center())

        self.play(Create(arrow2, run_time=1.0))
        self.play(FadeIn(lbl2_bg, run_time=0.4), FadeIn(lbl2, run_time=1.0))
        self.wait(2.0)

        eq3 = make_equation_card(r"x = 4", color=GREEN_OK, scale=1.7)
        eq3.move_to(eq1.get_center())
        for m in eq3:
            m.set_z_index(2)
        self.play(Transform(eq1, eq3, run_time=1.6))
        self.wait(1.5)
        self.play(
            FadeOut(arrow2, run_time=0.8),
            FadeOut(lbl2, run_time=0.8),
            FadeOut(lbl2_bg, run_time=0.8),
        )
        self.wait(3.0)
        self.play(Indicate(eq1, color=GREEN_OK, scale_factor=1.08), run_time=1.2)

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Substitute back to verify (~12 s)
        # ──────────────────────────────────────────────────────────────────
        check = MathTex(
            r"3(4) + 5 \;=\; 12 + 5 \;=\; 17",
            color=GREEN_OK,
        ).scale(1.2)
        check.next_to(eq1, DOWN, buff=0.8)
        check_bg = BackgroundRectangle(check, color=BLACK, fill_opacity=1, buff=0.25)
        check_bg.move_to(check.get_center())

        tick = Text("✓", font_size=40, color=GREEN_OK)
        tick.next_to(check, RIGHT, buff=0.4)
        tick_bg = BackgroundRectangle(tick, color=BLACK, fill_opacity=0.95, buff=0.18)
        tick_bg.move_to(tick.get_center())

        self.play(FadeIn(check_bg, run_time=0.5), Write(check, run_time=2.0))
        self.wait(1.0)
        self.play(FadeIn(tick_bg, run_time=0.4), FadeIn(tick, run_time=0.8))
        self.wait(3.0)
        self.play(
            FadeOut(eq1, run_time=1.0),
            FadeOut(check, run_time=1.0),
            FadeOut(check_bg, run_time=1.0),
            FadeOut(tick, run_time=1.0),
            FadeOut(tick_bg, run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (~20 s with final_wait = 14, total ≈ 87 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"x \;=\; \dfrac{b - c}{a}",
            "Subtract the constant, then divide by the coefficient.",
            final_wait=34.0,
        )