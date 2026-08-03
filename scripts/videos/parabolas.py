"""Manim scene aligned to the parabolas narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    PURPLE_ACCENT, beat_group, animate_intro, animate_final_definition,
)


class ParabolasScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Parabolas",
            "Begin with y = x², then use a to control opening and width.",
        )

        head = MathTex(r"y=x^2", color=BLUE_TERM).scale(1.0)
        head.move_to(BAND_CHART_CENTER + UP * 1.48)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=1, buff=0.14)
        ax = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-0.5, 4.5, 1],
            x_length=7.0, y_length=2.45, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.15)
        base = ax.plot(lambda x: x * x, x_range=[-2.1, 2.1], color=BLUE_TERM, stroke_width=4)
        vertex = Dot(ax.c2p(0, 0), color=GREEN_OK, radius=0.08)
        vertex_label = Text("vertex at the origin", font_size=19, color=GREEN_OK)
        vertex_label.move_to(RIGHT * 3.9 + DOWN * 0.28)
        vertex_bg = BackgroundRectangle(vertex_label, color=BLACK, fill_opacity=0.96, buff=0.1)
        symmetry = DashedLine(ax.c2p(0, -0.4), ax.c2p(0, 4.35), color=TEAL_TERM, stroke_width=3)
        symmetry_label = MathTex(r"x=0\ \text{axis of symmetry}", color=TEAL_TERM).scale(0.68)
        symmetry_label.move_to(LEFT * 3.9 + UP * 0.58)
        symmetry_bg = BackgroundRectangle(symmetry_label, color=BLACK, fill_opacity=0.96, buff=0.1)
        beat2 = beat_group(
            head_bg, head, ax, base, vertex, vertex_bg, vertex_label,
            symmetry, symmetry_bg, symmetry_label,
        )
        self.play(FadeIn(head_bg), Write(head))
        self.play(Create(ax), Create(base), run_time=1.6)
        self.play(FadeIn(vertex), FadeIn(vertex_bg), FadeIn(vertex_label))
        self.play(Create(symmetry), FadeIn(symmetry_bg), FadeIn(symmetry_label))
        self.wait(3.0)
        self.play(FadeOut(beat2, run_time=0.8))

        head3 = Text("The sign and size of a", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.48)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        ax2 = Axes(
            x_range=[-2.4, 2.4, 1], y_range=[-4.2, 4.2, 2],
            x_length=6.1, y_length=2.4, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(LEFT * 2.0 + DOWN * 0.16)
        curves = VGroup(
            ax2.plot(lambda x: x * x, x_range=[-2.0, 2.0], color=BLUE_TERM, stroke_width=4),
            ax2.plot(lambda x: 2 * x * x, x_range=[-1.42, 1.42], color=GREEN_OK, stroke_width=4),
            ax2.plot(lambda x: 0.5 * x * x, x_range=[-2.35, 2.35], color=ORANGE_TERM, stroke_width=4),
            ax2.plot(lambda x: -x * x, x_range=[-2.0, 2.0], color=PURPLE_ACCENT, stroke_width=4),
        )
        legend = VGroup(
            MathTex(r"y=x^2", color=BLUE_TERM).scale(0.72),
            MathTex(r"y=2x^2\quad\text{narrower}", color=GREEN_OK).scale(0.72),
            MathTex(r"y=\frac12x^2\quad\text{wider}", color=ORANGE_TERM).scale(0.72),
            MathTex(r"y=-x^2\quad\text{opens down}", color=PURPLE_ACCENT).scale(0.72),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24).move_to(RIGHT * 3.75 + DOWN * 0.12)
        legend_bgs = VGroup(*[
            BackgroundRectangle(item, color=BLACK, fill_opacity=0.97, buff=0.09)
            for item in legend
        ])
        beat3 = beat_group(head3_bg, head3, ax2, curves, legend_bgs, legend)
        self.play(FadeIn(head3_bg), FadeIn(head3))
        self.play(Create(ax2))
        for curve, bg, label in zip(curves, legend_bgs, legend):
            self.play(Create(curve), FadeIn(bg), FadeIn(label), run_time=1.0)
        self.wait(3.0)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("Read these features from the graph", font_size=25, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.44)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        facts = VGroup(
            MathTex(r"a>0:\ \text{opens up}\qquad a<0:\ \text{opens down}", color=BLUE_TERM).scale(0.78),
            MathTex(r"|a|\ \text{larger}:\ \text{narrower}\qquad |a|\ \text{smaller}:\ \text{wider}", color=ORANGE_TERM).scale(0.72),
            Text("Vertex = turning point", font_size=21, color=GREEN_OK),
            Text("Axis of symmetry = vertical line through the vertex", font_size=20, color=TEAL_TERM),
            Text("Intercepts = where the curve crosses the axes", font_size=20),
        ).arrange(DOWN, buff=0.2).move_to(BAND_CHART_CENTER + DOWN * 0.1)
        fact_bgs = VGroup(*[
            BackgroundRectangle(item, color=BLACK, fill_opacity=0.97, buff=0.1)
            for item in facts
        ])
        beat4 = beat_group(head4_bg, head4, fact_bgs, facts)
        self.play(FadeIn(head4_bg), FadeIn(head4))
        for bg, item in zip(fact_bgs, facts):
            self.play(FadeIn(bg), FadeIn(item), run_time=0.65)
        self.wait(2.5)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"y=ax^2:\quad \operatorname{sign}(a)\text{ sets direction, }|a|\text{ sets width}",
            "Find the vertex, intercepts, and vertical axis of symmetry.",
            final_wait=39.0,
        )
