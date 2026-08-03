"""Manim scene aligned to the simplifying-rational narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    beat_group, make_equation_card, animate_intro,
    animate_final_definition,
)


class SimplifyingRationalScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Simplifying brackets with fraction coefficients",
            "Distribute and collect, or factor first.",
        )

        head = Text("Method 1: distribute and collect", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.48)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        problem = make_equation_card(
            r"\left(x+\frac12\right)\left(x+\frac14\right)",
            color=BLUE_TERM, scale=0.95,
        )
        problem.move_to(BAND_CHART_CENTER + UP * 0.68)
        lines = VGroup(
            MathTex(r"=x^2+\frac14x+\frac12x+\frac18", color=TEAL_TERM).scale(0.78),
            MathTex(r"\frac12+\frac14=\frac34", color=ORANGE_TERM).scale(0.9),
            MathTex(r"=x^2+\frac34x+\frac18", color=GREEN_OK).scale(0.88),
        ).arrange(DOWN, buff=0.22).move_to(BAND_CHART_CENTER + DOWN * 0.52)
        line_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=1, buff=0.11)
            for line in lines
        ])
        beat2 = beat_group(head_bg, head, problem, line_bgs, lines)
        self.play(FadeIn(head_bg), FadeIn(head))
        self.play(FadeIn(problem))
        for bg, line in zip(line_bgs, lines):
            self.play(FadeIn(bg), Write(line), run_time=0.9)
            self.wait(0.45)
        self.wait(2.0)
        self.play(FadeOut(beat2, run_time=0.8))

        head3 = Text("Method 2: factor before multiplying", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.48)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        same = make_equation_card(
            r"\left(x+\frac12\right)\left(x+\frac14\right)",
            color=BLUE_TERM, scale=0.9,
        )
        same.move_to(BAND_CHART_CENTER + UP * 0.72)
        factor_lines = VGroup(
            MathTex(r"=\frac12(2x+1)\cdot\frac14(4x+1)", color=TEAL_TERM).scale(0.82),
            MathTex(r"=\frac18(2x+1)(4x+1)", color=ORANGE_TERM).scale(0.86),
            MathTex(r"=x^2+\frac34x+\frac18", color=GREEN_OK).scale(0.9),
        ).arrange(DOWN, buff=0.24).move_to(BAND_CHART_CENTER + DOWN * 0.48)
        factor_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=1, buff=0.11)
            for line in factor_lines
        ])
        beat3 = beat_group(head3_bg, head3, same, factor_bgs, factor_lines)
        self.play(FadeIn(head3_bg), FadeIn(head3))
        self.play(FadeIn(same))
        for bg, line in zip(factor_bgs, factor_lines):
            self.play(FadeIn(bg), Write(line), run_time=0.9)
            self.wait(0.45)
        self.wait(2.0)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("Two roads, one simplified expression", font_size=25, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.43)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        roads = VGroup(
            Text("Distribute every term, then collect like terms", font_size=21, color=BLUE_TERM),
            Text("or", font_size=19),
            Text("Pull out common factors before multiplying", font_size=21, color=TEAL_TERM),
        ).arrange(DOWN, buff=0.26).move_to(BAND_CHART_CENTER + UP * 0.05)
        roads_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=0.97, buff=0.11)
            for line in roads
        ])
        choose = Text("Pick whichever route makes the fractions easier.", font_size=20, color=ORANGE_TERM)
        choose.move_to(BAND_CHART_CENTER + DOWN * 1.08)
        choose_bg = BackgroundRectangle(choose, color=BLACK, fill_opacity=0.96, buff=0.12)
        beat4 = beat_group(head4_bg, head4, roads_bgs, roads, choose_bg, choose)
        self.play(FadeIn(head4_bg), FadeIn(head4))
        for bg, line in zip(roads_bgs, roads):
            self.play(FadeIn(bg), FadeIn(line), run_time=0.65)
        self.play(FadeIn(choose_bg), FadeIn(choose))
        self.wait(2.5)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"\left(x+\frac12\right)\left(x+\frac14\right)=x^2+\frac34x+\frac18",
            "Distribute and collect, or factor first — both agree.",
            final_wait=39.0,
        )
