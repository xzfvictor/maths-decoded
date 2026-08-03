"""Manim scene aligned to the solving-rational narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    beat_group, make_equation_card, animate_intro,
    animate_final_definition,
)


class SolvingRationalScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Solving equations with fractional coefficients",
            "Clear the fractions, then solve a whole-number equation.",
        )

        head = Text("Recommended method", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.46)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        method = VGroup(
            Text("1. Find the lowest common denominator (LCD)", font_size=21, color=BLUE_TERM),
            Text("2. Multiply every term on both sides by the LCD", font_size=21, color=TEAL_TERM),
            Text("3. Solve the resulting linear equation", font_size=21, color=GREEN_OK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(BAND_CHART_CENTER + UP * 0.02)
        method_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=0.97, buff=0.11)
            for line in method
        ])
        equality = Text("Multiplying both sides by the same number preserves equality.", font_size=19, color=ORANGE_TERM)
        equality.move_to(BAND_CHART_CENTER + DOWN * 1.12)
        equality_bg = BackgroundRectangle(equality, color=BLACK, fill_opacity=0.96, buff=0.11)
        beat2 = beat_group(head_bg, head, method_bgs, method, equality_bg, equality)
        self.play(FadeIn(head_bg), FadeIn(head))
        for bg, line in zip(method_bgs, method):
            self.play(FadeIn(bg), FadeIn(line), run_time=0.75)
        self.play(FadeIn(equality_bg), FadeIn(equality))
        self.wait(2.5)
        self.play(FadeOut(beat2, run_time=0.8))

        head3 = Text("Worked example: LCD = 6", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.48)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        equation = make_equation_card(r"\frac{x}{2}+\frac{x}{3}=5", color=BLUE_TERM, scale=1.0)
        equation.move_to(BAND_CHART_CENTER + UP * 0.72)
        lines = VGroup(
            MathTex(r"6\left(\frac{x}{2}\right)+6\left(\frac{x}{3}\right)=6(5)", color=ORANGE_TERM).scale(0.78),
            MathTex(r"3x+2x=30", color=TEAL_TERM).scale(0.9),
            MathTex(r"5x=30", color=TEAL_TERM).scale(0.9),
            MathTex(r"x=6", color=GREEN_OK).scale(1.05),
        ).arrange(DOWN, buff=0.17).move_to(BAND_CHART_CENTER + DOWN * 0.48)
        line_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=1, buff=0.1)
            for line in lines
        ])
        beat3 = beat_group(head3_bg, head3, equation, line_bgs, lines)
        self.play(FadeIn(head3_bg), FadeIn(head3))
        self.play(FadeIn(equation))
        for bg, line in zip(line_bgs, lines):
            self.play(FadeIn(bg), Write(line), run_time=0.8)
            self.wait(0.35)
        self.play(Indicate(lines[-1], color=GREEN_OK))
        self.wait(2.0)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("Why clearing first is safer", font_size=25, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.42)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        compare = VGroup(
            Text("Fractions disappear in one step", font_size=22, color=BLUE_TERM),
            Text("Then ordinary inverse operations take over", font_size=22, color=TEAL_TERM),
            Text("Keeping fractions works — but invites small slip-ups", font_size=20, color=ORANGE_TERM),
        ).arrange(DOWN, buff=0.32).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        compare_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=0.97, buff=0.11)
            for line in compare
        ])
        beat4 = beat_group(head4_bg, head4, compare_bgs, compare)
        self.play(FadeIn(head4_bg), FadeIn(head4))
        for bg, line in zip(compare_bgs, compare):
            self.play(FadeIn(bg), FadeIn(line), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"\frac{x}{2}+\frac{x}{3}=5\ \xrightarrow{\times 6}\ 3x+2x=30\ \Rightarrow\ x=6",
            "Multiply every term by the LCD, then solve normally.",
            final_wait=48.0,
        )
