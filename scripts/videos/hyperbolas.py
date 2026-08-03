"""Manim scene aligned to the hyperbolas narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    beat_group, animate_intro, animate_final_definition,
)


class HyperbolasScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Hyperbolas",
            "Reciprocal curves, quadrant flips, and translations.",
        )

        formula = MathTex(r"y=\frac{k}{x}", color=BLUE_TERM).scale(0.95)
        formula.move_to(BAND_CHART_CENTER + UP * 1.5)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.14)
        pos_label = MathTex(r"k>0:\ \text{quadrants I and III}", color=GREEN_OK).scale(0.7)
        pos_label.move_to(LEFT * 3.25 + UP * 0.92)
        neg_label = MathTex(r"k<0:\ \text{quadrants II and IV}", color=ORANGE_TERM).scale(0.7)
        neg_label.move_to(RIGHT * 3.25 + UP * 0.92)
        pos_bg = BackgroundRectangle(pos_label, color=BLACK, fill_opacity=0.95, buff=0.09)
        neg_bg = BackgroundRectangle(neg_label, color=BLACK, fill_opacity=0.95, buff=0.09)
        left_ax = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=4.7, y_length=2.15, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(LEFT * 3.25 + DOWN * 0.22)
        right_ax = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=4.7, y_length=2.15, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(RIGHT * 3.25 + DOWN * 0.22)
        positive = VGroup(
            left_ax.plot(lambda x: 1 / x, x_range=[0.36, 2.85], color=GREEN_OK, stroke_width=4),
            left_ax.plot(lambda x: 1 / x, x_range=[-2.85, -0.36], color=GREEN_OK, stroke_width=4),
        )
        negative = VGroup(
            right_ax.plot(lambda x: -1 / x, x_range=[0.36, 2.85], color=ORANGE_TERM, stroke_width=4),
            right_ax.plot(lambda x: -1 / x, x_range=[-2.85, -0.36], color=ORANGE_TERM, stroke_width=4),
        )
        axes_note = MathTex(r"x=0\ \text{and}\ y=0\ \text{are asymptotes}", color=TEAL_TERM).scale(0.72)
        axes_note.move_to(BAND_CHART_CENTER + DOWN * 1.36)
        axes_note_bg = BackgroundRectangle(axes_note, color=BLACK, fill_opacity=1, buff=0.1)
        beat2 = beat_group(
            formula_bg, formula, pos_bg, pos_label, neg_bg, neg_label,
            left_ax, right_ax, positive, negative, axes_note_bg, axes_note,
        )
        self.play(FadeIn(formula_bg), Write(formula))
        self.play(Create(left_ax), Create(right_ax), run_time=1.2)
        self.play(Create(positive), FadeIn(pos_bg), FadeIn(pos_label), run_time=1.5)
        self.play(Create(negative), FadeIn(neg_bg), FadeIn(neg_label), run_time=1.5)
        self.play(FadeIn(axes_note_bg), FadeIn(axes_note))
        self.wait(3.0)
        self.play(FadeOut(beat2, run_time=0.8))

        # A translated representative curve, labelled only with the general
        # h and v from the narration.
        translated_formula = MathTex(r"y=\frac{k}{x-h}+v", color=BLUE_TERM).scale(0.95)
        translated_formula.move_to(BAND_CHART_CENTER + UP * 1.5)
        translated_bg = BackgroundRectangle(translated_formula, color=BLACK, fill_opacity=1, buff=0.14)
        ax = Axes(
            x_range=[-3, 4, 1], y_range=[-3, 3, 1],
            x_length=7.0, y_length=2.4, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.2)
        h, v = 0.8, 0.25
        branches = VGroup(
            ax.plot(lambda x: 1 / (x - h) + v, x_range=[-2.8, h - 0.38], color=BLUE_TERM, stroke_width=4),
            ax.plot(lambda x: 1 / (x - h) + v, x_range=[h + 0.38, 3.8], color=BLUE_TERM, stroke_width=4),
        )
        vertical = DashedLine(ax.c2p(h, -2.9), ax.c2p(h, 2.9), color=ORANGE_TERM, stroke_width=3)
        horizontal = DashedLine(ax.c2p(-2.9, v), ax.c2p(3.9, v), color=TEAL_TERM, stroke_width=3)
        centre = Dot(ax.c2p(h, v), color=GREEN_OK, radius=0.08)
        centre_label = MathTex(r"(h,v)", color=GREEN_OK).scale(0.78)
        centre_label.move_to(ax.c2p(h + 0.62, v + 0.7))
        centre_bg = BackgroundRectangle(centre_label, color=BLACK, fill_opacity=0.96, buff=0.09)
        xh = MathTex(r"x=h", color=ORANGE_TERM).scale(0.7).move_to(ax.c2p(h + 0.5, 2.35))
        yv = MathTex(r"y=v", color=TEAL_TERM).scale(0.7).move_to(ax.c2p(-2.35, v + 0.55))
        xh_bg = BackgroundRectangle(xh, color=BLACK, fill_opacity=0.96, buff=0.09)
        yv_bg = BackgroundRectangle(yv, color=BLACK, fill_opacity=0.96, buff=0.09)
        shift_note = Text("h shifts right; v shifts up", font_size=19, color=GREEN_OK)
        shift_note.move_to(BAND_CHART_CENTER + DOWN * 1.36)
        shift_bg = BackgroundRectangle(shift_note, color=BLACK, fill_opacity=0.96, buff=0.1)
        beat3 = beat_group(
            translated_bg, translated_formula, ax, branches, vertical, horizontal,
            centre, centre_bg, centre_label, xh_bg, xh, yv_bg, yv, shift_bg, shift_note,
        )
        self.play(FadeIn(translated_bg), Write(translated_formula))
        self.play(Create(ax), Create(branches), run_time=1.7)
        self.play(Create(vertical), FadeIn(xh_bg), FadeIn(xh))
        self.play(Create(horizontal), FadeIn(yv_bg), FadeIn(yv))
        self.play(FadeIn(centre), FadeIn(centre_bg), FadeIn(centre_label))
        self.play(FadeIn(shift_bg), FadeIn(shift_note))
        self.wait(3.0)
        self.play(FadeOut(beat3, run_time=0.8))

        animate_final_definition(
            self,
            r"y=\frac{k}{x-h}+v,\qquad \text{centre }(h,v)",
            "New asymptotes: x = h and y = v.",
            final_wait=70.0,
        )
