"""Manim scene aligned to the investigate-variation narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    beat_group, make_equation_card, animate_intro,
    animate_final_definition,
)


class InvestigateVariationScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Investigating variation",
            "Change one parameter and watch the graph respond.",
        )

        head = Text("Use a slider like a mathematical detective", font_size=25, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.46)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        family = make_equation_card(r"y=a(x-h)^2+k", color=BLUE_TERM, scale=1.08)
        family.move_to(BAND_CHART_CENTER + UP * 0.5)
        method = VGroup(
            Text("Hold every other parameter fixed", font_size=21, color=TEAL_TERM),
            Text("Slide one parameter slowly", font_size=21, color=ORANGE_TERM),
            Text("Ask: shape, position, or both?", font_size=21, color=GREEN_OK),
        ).arrange(DOWN, buff=0.22).move_to(BAND_CHART_CENTER + DOWN * 0.65)
        method_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=0.96, buff=0.1)
            for line in method
        ])
        beat2 = beat_group(head_bg, head, family, method_bgs, method)
        self.play(FadeIn(head_bg), FadeIn(head))
        self.play(FadeIn(family, shift=UP * 0.15), run_time=1.3)
        for bg, line in zip(method_bgs, method):
            self.play(FadeIn(bg), FadeIn(line), run_time=0.65)
        self.wait(2.5)
        self.play(FadeOut(beat2, run_time=0.8))

        # Width is controlled by a. Numerical values are used only to draw
        # representative curves; the visible statement stays general.
        head3 = Text("a stretches or squashes the width", font_size=25, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.5)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        ax = Axes(
            x_range=[-3.2, 3.2, 1], y_range=[-0.5, 5, 1],
            x_length=7.2, y_length=2.35, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.12)
        wide = ax.plot(lambda x: 0.5 * x * x, x_range=[-3.0, 3.0], color=BLUE_TERM, stroke_width=4)
        narrow = ax.plot(lambda x: 2 * x * x, x_range=[-1.55, 1.55], color=ORANGE_TERM, stroke_width=4)
        wide_label = Text("smaller |a| → wider", font_size=18, color=BLUE_TERM).move_to(LEFT * 3.7 + UP * 0.9)
        narrow_label = Text("larger |a| → narrower", font_size=18, color=ORANGE_TERM).move_to(RIGHT * 3.7 + UP * 0.9)
        wide_bg = BackgroundRectangle(wide_label, color=BLACK, fill_opacity=0.95, buff=0.1)
        narrow_bg = BackgroundRectangle(narrow_label, color=BLACK, fill_opacity=0.95, buff=0.1)
        beat3 = beat_group(head3_bg, head3, ax, wide, narrow, wide_bg, wide_label, narrow_bg, narrow_label)
        self.play(FadeIn(head3_bg), FadeIn(head3))
        self.play(Create(ax), Create(wide), run_time=1.5)
        self.play(FadeIn(wide_bg), FadeIn(wide_label))
        self.play(Create(narrow), run_time=1.5)
        self.play(FadeIn(narrow_bg), FadeIn(narrow_label))
        self.wait(2.5)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("h moves sideways; k moves vertically", font_size=25, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.46)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        form = make_equation_card(r"y=a(x-h)^2+k", color=GREEN_OK, scale=1.05)
        form.move_to(BAND_CHART_CENTER + UP * 0.55)
        effects = VGroup(
            MathTex(r"h:\quad\text{slide left or right}", color=BLUE_TERM).scale(0.86),
            MathTex(r"k:\quad\text{lift up or down}", color=ORANGE_TERM).scale(0.86),
            Text("Change one at a time, test several values, then state a rule.", font_size=19, color=TEAL_TERM),
        ).arrange(DOWN, buff=0.28).move_to(BAND_CHART_CENTER + DOWN * 0.52)
        effects_bgs = VGroup(*[
            BackgroundRectangle(item, color=BLACK, fill_opacity=0.97, buff=0.11)
            for item in effects
        ])
        beat4 = beat_group(head4_bg, head4, form, effects_bgs, effects)
        self.play(FadeIn(head4_bg), FadeIn(head4))
        self.play(FadeIn(form))
        for bg, item in zip(effects_bgs, effects):
            self.play(FadeIn(bg), FadeIn(item), run_time=0.7)
        self.wait(3.0)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"y=a(x-h)^2+k",
            "a controls width; h shifts left/right; k shifts up/down.",
            final_wait=48.0,
        )
