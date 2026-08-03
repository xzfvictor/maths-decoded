"""Manim scene aligned to the modelling-with-notation narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    beat_group, animate_intro, animate_final_definition,
)


class ModellingWithNotationScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Modelling with function notation",
            "Let each variable name hint at the quantity it represents.",
        )

        head = Text("Names that explain the model", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.48)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        examples = VGroup(
            MathTex(r"V(r)=\frac{4}{3}\pi r^3\quad\text{sphere volume}", color=BLUE_TERM).scale(0.78),
            MathTex(r"A(w)\quad\text{path area with width }w", color=TEAL_TERM).scale(0.78),
            MathTex(r"P(t)=P_0(1.05)^t\quad\text{population: 5\% growth each year}", color=GREEN_OK).scale(0.72),
            MathTex(r"C(n)\quad\text{cost for }n\text{ hours worked}", color=ORANGE_TERM).scale(0.78),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        example_bgs = VGroup(*[
            BackgroundRectangle(row, color=BLACK, fill_opacity=0.96, buff=0.11)
            for row in examples
        ])
        beat2 = beat_group(head_bg, head, example_bgs, examples)
        self.play(FadeIn(head_bg), FadeIn(head))
        for bg, row in zip(example_bgs, examples):
            self.play(FadeIn(bg, run_time=0.2), FadeIn(row, shift=RIGHT * 0.12, run_time=0.8))
            self.wait(0.6)
        self.wait(2.0)
        self.play(FadeOut(beat2, run_time=0.8))

        head3 = Text("A repeatable modelling recipe", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.48)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        recipe = VGroup(
            Text("1. Identify what goes in: the independent variable", font_size=19),
            Text("2. Give that input a meaningful letter", font_size=19),
            Text("3. Decide what comes out: the dependent variable", font_size=19),
            Text("4. Write the output as a function of the input", font_size=19),
            Text("5. Translate the relationship into a formula", font_size=19),
            Text("6. Plug in values to answer the question", font_size=19),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to(BAND_CHART_CENTER + DOWN * 0.02)
        recipe_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=0.96, buff=0.09)
            for line in recipe
        ])
        for i, line in enumerate(recipe):
            line.set_color([BLUE_TERM, BLUE_TERM, TEAL_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK][i])
        beat3 = beat_group(head3_bg, head3, recipe_bgs, recipe)
        self.play(FadeIn(head3_bg), FadeIn(head3))
        for bg, line in zip(recipe_bgs, recipe):
            self.play(FadeIn(bg, run_time=0.15), FadeIn(line, run_time=0.55))
        self.wait(2.5)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("Independent in — dependent out", font_size=26, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.42)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        left = VGroup(
            Text("INPUT", font_size=24, color=BLUE_TERM),
            Text("independent", font_size=20, color=BLUE_TERM),
            Text("you choose it", font_size=18),
        ).arrange(DOWN, buff=0.18).move_to(LEFT * 3 + DOWN * 0.1)
        right = VGroup(
            Text("OUTPUT", font_size=24, color=GREEN_OK),
            Text("dependent", font_size=20, color=GREEN_OK),
            Text("depends on the input", font_size=18),
        ).arrange(DOWN, buff=0.18).move_to(RIGHT * 3 + DOWN * 0.1)
        left_box = SurroundingRectangle(left, color=BLUE_TERM, buff=0.25)
        right_box = SurroundingRectangle(right, color=GREEN_OK, buff=0.25)
        arrow = Arrow(left_box.get_right(), right_box.get_left(), buff=0.25, color=ORANGE_TERM)
        f_label = MathTex(r"F(\,\cdot\,)", color=ORANGE_TERM).scale(0.85).next_to(arrow, UP, buff=0.18)
        beat4 = beat_group(head4_bg, head4, left, right, left_box, right_box, arrow, f_label)
        self.play(FadeIn(head4_bg), FadeIn(head4))
        self.play(FadeIn(left), Create(left_box))
        self.play(GrowArrow(arrow), FadeIn(f_label))
        self.play(FadeIn(right), Create(right_box))
        self.wait(3.0)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"x\ \text{independent}\quad\longrightarrow\quad F(x)\ \text{dependent}",
            "Choose the input; the model determines the output.",
            final_wait=56.0,
        )
