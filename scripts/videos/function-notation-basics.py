"""Manim scene aligned to the function-notation-basics narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    beat_group, make_equation_card, animate_intro,
    animate_final_definition,
)


class FunctionNotationBasicsScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Function notation",
            'Read f(x) as "f of x" — the output at input x.',
        )

        # The exact rule and three evaluations from the narration.
        head = Text("Substitute the input for x", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.45)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        rule = make_equation_card(r"f(x)=3x+1", color=BLUE_TERM, scale=1.15)
        rule.move_to(BAND_CHART_CENTER + UP * 0.72)

        evaluations = VGroup(
            MathTex(r"f(2)=3(2)+1=7", color=GREEN_OK).scale(0.82),
            MathTex(r"f(-1)=3(-1)+1=-2", color=ORANGE_TERM).scale(0.82),
            MathTex(r"f(0)=3(0)+1=1\quad\text{(y-intercept)}", color=TEAL_TERM).scale(0.78),
        ).arrange(DOWN, buff=0.18).move_to(BAND_CHART_CENTER + DOWN * 0.48)
        eval_bgs = VGroup(*[
            BackgroundRectangle(eq, color=BLACK, fill_opacity=0.96, buff=0.12)
            for eq in evaluations
        ])
        beat2 = beat_group(head_bg, head, rule, eval_bgs, evaluations)

        self.play(FadeIn(head_bg), FadeIn(head))
        self.play(FadeIn(rule, shift=UP * 0.15), run_time=1.4)
        for bg, eq in zip(eval_bgs, evaluations):
            self.play(FadeIn(bg, run_time=0.25), Write(eq, run_time=1.0))
            self.wait(0.7)
        self.wait(2.0)
        self.play(FadeOut(beat2, run_time=0.8))

        # Function and input letters are conventions, not fixed rules.
        head3 = Text("Friendly naming conventions", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.42)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        names = MathTex(r"f,\ g,\ h,\ V,\ A,\ P", color=BLUE_TERM).scale(1.05)
        names.move_to(BAND_CHART_CENTER + UP * 0.55)
        names_bg = BackgroundRectangle(names, color=BLACK, fill_opacity=1, buff=0.18)
        meanings = Text("V for volume • A for area • P for price", font_size=21, color=GREEN_OK)
        meanings.move_to(BAND_CHART_CENTER + DOWN * 0.08)
        meanings_bg = BackgroundRectangle(meanings, color=BLACK, fill_opacity=0.96, buff=0.13)
        inputs = MathTex(r"\text{inputs can be }x,\ t,\ r,\ldots", color=ORANGE_TERM).scale(0.88)
        inputs.move_to(BAND_CHART_CENTER + DOWN * 0.78)
        inputs_bg = BackgroundRectangle(inputs, color=BLACK, fill_opacity=1, buff=0.15)
        tidy = Text("Choose letters that keep the model tidy.", font_size=20)
        tidy.move_to(BAND_CHART_CENTER + DOWN * 1.25)
        tidy_bg = BackgroundRectangle(tidy, color=BLACK, fill_opacity=0.95, buff=0.12)
        beat3 = beat_group(
            head3_bg, head3, names_bg, names, meanings_bg, meanings,
            inputs_bg, inputs, tidy_bg, tidy,
        )

        self.play(FadeIn(head3_bg), FadeIn(head3))
        self.play(FadeIn(names_bg), Write(names))
        self.play(FadeIn(meanings_bg), FadeIn(meanings))
        self.play(FadeIn(inputs_bg), Write(inputs))
        self.play(FadeIn(tidy_bg), FadeIn(tidy))
        self.wait(3.0)
        self.play(FadeOut(beat3, run_time=0.8))

        animate_final_definition(
            self,
            r"f(2)=7,\qquad f(-1)=-2,\qquad f(0)=1",
            "Function notation asks for the output at a chosen input.",
            final_wait=86.0,
        )
