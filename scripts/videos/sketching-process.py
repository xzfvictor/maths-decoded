"""Manim scene aligned to the sketching-process narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    beat_group, make_equation_card, animate_intro,
    animate_final_definition,
)


class SketchingProcessScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "A reliable polynomial sketching process",
            "Build a feature summary, choose a scale, then draw smoothly.",
        )

        head = Text("Use this order", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.48)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        steps = VGroup(
            Text("1. End behaviour (odd + positive: left ↓, right ↑)", font_size=18, color=BLUE_TERM),
            Text("2. y-intercept: set x = 0", font_size=18, color=TEAL_TERM),
            Text("3. x-intercepts: factor or use the factor theorem", font_size=18, color=GREEN_OK),
            Text("4. Turning points (for cubics, roughly between roots)", font_size=18, color=ORANGE_TERM),
            Text("5. Choose a scale that fits every key point", font_size=18),
            Text("6. Draw one smooth curve with the right end behaviour", font_size=18, color=BLUE_TERM),
            Text("7. Label the intercepts", font_size=18, color=GREEN_OK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.13).move_to(BAND_CHART_CENTER + DOWN * 0.02)
        step_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=0.97, buff=0.08)
            for line in steps
        ])
        beat2 = beat_group(head_bg, head, step_bgs, steps)
        self.play(FadeIn(head_bg), FadeIn(head))
        for bg, line in zip(step_bgs, steps):
            self.play(FadeIn(bg, run_time=0.12), FadeIn(line, run_time=0.45))
        self.wait(2.5)
        self.play(FadeOut(beat2, run_time=0.8))

        head3 = Text("Feature summary before drawing", font_size=25, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.48)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        equation = make_equation_card(
            r"p(x)=(x+1)(x-2)=x^2-x-2", color=BLUE_TERM, scale=0.92,
        )
        equation.move_to(BAND_CHART_CENTER + UP * 0.72)
        facts = VGroup(
            Text("Even degree, positive leading term → both ends rise", font_size=19, color=BLUE_TERM),
            MathTex(r"p(0)=-2\quad\Rightarrow\quad y\text{-intercept }(0,-2)", color=TEAL_TERM).scale(0.72),
            MathTex(r"x\text{-intercepts}:\ (-1,0),\ (2,0)", color=GREEN_OK).scale(0.76),
            MathTex(r"\text{turning point}:\ \left(\frac12,-\frac94\right)", color=ORANGE_TERM).scale(0.76),
        ).arrange(DOWN, buff=0.18).move_to(BAND_CHART_CENTER + DOWN * 0.5)
        fact_bgs = VGroup(*[
            BackgroundRectangle(item, color=BLACK, fill_opacity=0.97, buff=0.09)
            for item in facts
        ])
        beat3 = beat_group(head3_bg, head3, equation, fact_bgs, facts)
        self.play(FadeIn(head3_bg), FadeIn(head3))
        self.play(FadeIn(equation))
        for bg, item in zip(fact_bgs, facts):
            self.play(FadeIn(bg), FadeIn(item), run_time=0.65)
        self.wait(2.5)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("Choose the scale, plot, smooth, and label", font_size=24, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.48)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        ax = Axes(
            x_range=[-2, 3, 1], y_range=[-3, 1.4, 1],
            x_length=6.4, y_length=2.5, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.12)
        curve = ax.plot(
            lambda x: x * x - x - 2,
            x_range=[-1.35, 2.35], color=BLUE_TERM, stroke_width=4,
        )
        points = VGroup(
            Dot(ax.c2p(-1, 0), color=GREEN_OK, radius=0.075),
            Dot(ax.c2p(2, 0), color=GREEN_OK, radius=0.075),
            Dot(ax.c2p(0, -2), color=TEAL_TERM, radius=0.075),
            Dot(ax.c2p(0.5, -2.25), color=ORANGE_TERM, radius=0.075),
        )
        labels = VGroup(
            MathTex(r"(-1,0)", color=GREEN_OK).scale(0.63).move_to(ax.c2p(-1.38, 0.48)),
            MathTex(r"(2,0)", color=GREEN_OK).scale(0.63).move_to(ax.c2p(2.34, 0.48)),
            MathTex(r"(0,-2)", color=TEAL_TERM).scale(0.63).move_to(ax.c2p(-0.52, -1.62)),
            MathTex(r"\left(\frac12,-\frac94\right)", color=ORANGE_TERM).scale(0.62).move_to(ax.c2p(1.25, -2.48)),
        )
        label_bgs = VGroup(*[
            BackgroundRectangle(label, color=BLACK, fill_opacity=0.96, buff=0.07)
            for label in labels
        ])
        beat4 = beat_group(head4_bg, head4, ax, curve, points, label_bgs, labels)
        self.play(FadeIn(head4_bg), FadeIn(head4))
        self.play(Create(ax), run_time=1.0)
        self.play(FadeIn(points), run_time=0.8)
        self.play(Create(curve), run_time=1.8)
        for bg, label in zip(label_bgs, labels):
            self.play(FadeIn(bg), FadeIn(label), run_time=0.4)
        self.wait(3.0)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"\text{end}\to y\text{-int}\to x\text{-ints}\to\text{turns}\to\text{scale}\to\text{curve}",
            "Plot the key features and label the intercepts.",
            final_wait=35.0,
        )

