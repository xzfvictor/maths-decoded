"""Manim scene aligned to the reading-features narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    beat_group, make_equation_card, animate_intro,
    animate_final_definition,
)


class ReadingFeaturesScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Read polynomial features from the equation",
            "Build the curve's summary before graphing.",
        )

        polynomial = make_equation_card(
            r"p(x)=x^3-2x^2-x+2", color=BLUE_TERM, scale=1.05,
        )
        polynomial.move_to(BAND_CHART_CENTER + UP * 1.16)
        features = VGroup(
            MathTex(r"\text{degree}=3\quad\Rightarrow\quad\text{cubic shape}", color=TEAL_TERM).scale(0.82),
            MathTex(r"\text{leading coefficient}=+1", color=GREEN_OK).scale(0.84),
            Text("Positive odd degree: left end down, right end up", font_size=20, color=ORANGE_TERM),
        ).arrange(DOWN, buff=0.25).move_to(BAND_CHART_CENTER + DOWN * 0.28)
        feature_bgs = VGroup(*[
            BackgroundRectangle(item, color=BLACK, fill_opacity=0.97, buff=0.11)
            for item in features
        ])
        beat2 = beat_group(polynomial, feature_bgs, features)
        self.play(FadeIn(polynomial))
        for bg, item in zip(feature_bgs, features):
            self.play(FadeIn(bg), FadeIn(item), run_time=0.75)
        self.wait(2.5)
        self.play(FadeOut(beat2, run_time=0.8))

        head3 = Text("Set x = 0 for the y-intercept", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.45)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        substitute = MathTex(
            r"p(0)=0^3-2(0)^2-0+2=2", color=BLUE_TERM
        ).scale(0.9).move_to(BAND_CHART_CENTER + UP * 0.35)
        substitute_bg = BackgroundRectangle(substitute, color=BLACK, fill_opacity=1, buff=0.17)
        intercept = make_equation_card(r"y\text{-intercept }(0,2)", color=GREEN_OK, scale=0.95)
        intercept.move_to(BAND_CHART_CENTER + DOWN * 0.68)
        constant = Text("For a polynomial, this is the constant term.", font_size=20, color=ORANGE_TERM)
        constant.move_to(BAND_CHART_CENTER + DOWN * 1.25)
        constant_bg = BackgroundRectangle(constant, color=BLACK, fill_opacity=0.96, buff=0.1)
        beat3 = beat_group(head3_bg, head3, substitute_bg, substitute, intercept, constant_bg, constant)
        self.play(FadeIn(head3_bg), FadeIn(head3))
        self.play(FadeIn(substitute_bg), Write(substitute))
        self.play(FadeIn(intercept))
        self.play(FadeIn(constant_bg), FadeIn(constant))
        self.wait(2.5)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("Use the factor theorem for candidate roots", font_size=25, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.47)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        tests = VGroup(
            MathTex(r"p(1)=0", color=BLUE_TERM).scale(0.88),
            MathTex(r"p(-1)=0", color=TEAL_TERM).scale(0.88),
            MathTex(r"p(2)=0", color=ORANGE_TERM).scale(0.88),
        ).arrange(RIGHT, buff=0.85).move_to(BAND_CHART_CENTER + UP * 0.52)
        test_bgs = VGroup(*[
            BackgroundRectangle(test, color=BLACK, fill_opacity=1, buff=0.12)
            for test in tests
        ])
        factor = MathTex(r"p(x)=(x+1)(x-1)(x-2)", color=GREEN_OK).scale(0.9)
        factor.move_to(BAND_CHART_CENTER + DOWN * 0.24)
        factor_bg = BackgroundRectangle(factor, color=BLACK, fill_opacity=1, buff=0.15)
        roots = MathTex(r"x=-1,\ 1,\ 2\quad\text{are the x-intercepts}", color=GREEN_OK).scale(0.82)
        roots.move_to(BAND_CHART_CENTER + DOWN * 0.93)
        roots_bg = BackgroundRectangle(roots, color=BLACK, fill_opacity=1, buff=0.13)
        turn = Text("Sign changes help locate possible turning points.", font_size=19, color=ORANGE_TERM)
        turn.move_to(BAND_CHART_CENTER + DOWN * 1.32)
        turn_bg = BackgroundRectangle(turn, color=BLACK, fill_opacity=0.96, buff=0.09)
        beat4 = beat_group(
            head4_bg, head4, test_bgs, tests, factor_bg, factor,
            roots_bg, roots, turn_bg, turn,
        )
        self.play(FadeIn(head4_bg), FadeIn(head4))
        for bg, test in zip(test_bgs, tests):
            self.play(FadeIn(bg), Write(test), run_time=0.65)
        self.play(FadeIn(factor_bg), Write(factor))
        self.play(FadeIn(roots_bg), FadeIn(roots))
        self.play(FadeIn(turn_bg), FadeIn(turn))
        self.wait(3.0)
        self.play(FadeOut(beat4, run_time=0.8))

        head5 = Text("Equation-first summary", font_size=26, color=BLUE_TERM)
        head5.move_to(BAND_CHART_CENTER + UP * 1.42)
        head5_bg = BackgroundRectangle(head5, color=BLACK, fill_opacity=0.95, buff=0.15)
        summary = VGroup(
            Text("Degree → curve family", font_size=21, color=BLUE_TERM),
            Text("Leading sign → end behaviour", font_size=21, color=TEAL_TERM),
            Text("Set x = 0 → y-intercept", font_size=21, color=ORANGE_TERM),
            Text("Factor theorem → candidate roots", font_size=21, color=GREEN_OK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(BAND_CHART_CENTER + DOWN * 0.08)
        summary_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=0.97, buff=0.1)
            for line in summary
        ])
        beat5 = beat_group(head5_bg, head5, summary_bgs, summary)
        self.play(FadeIn(head5_bg), FadeIn(head5))
        for bg, line in zip(summary_bgs, summary):
            self.play(FadeIn(bg), FadeIn(line), run_time=0.65)
        self.wait(2.5)
        self.play(FadeOut(beat5, run_time=0.8))

        animate_final_definition(
            self,
            r"p(x)=x^3-2x^2-x+2=(x+1)(x-1)(x-2)",
            "Read degree, leading sign, y-intercept, and roots before graphing.",
            final_wait=47.0,
        )
