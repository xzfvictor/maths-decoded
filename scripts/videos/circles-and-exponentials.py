"""Manim scene aligned to the circles-and-exponentials narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    beat_group, make_equation_card, animate_intro,
    animate_final_definition,
)


class CirclesAndExponentialsScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Circles and exponentials",
            "Recognise two more non-linear curve families on sight.",
        )

        head = Text("Circle centred at the origin", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.48)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        circle = Circle(radius=1.18, color=BLUE_TERM, stroke_width=4).move_to(LEFT * 2.8 + DOWN * 0.05)
        centre = Dot(circle.get_center(), color=GREEN_OK, radius=0.07)
        radius = Line(circle.get_center(), circle.point_at_angle(PI / 5), color=ORANGE_TERM, stroke_width=4)
        r_label = MathTex(r"r", color=ORANGE_TERM).scale(0.85).next_to(radius, UP, buff=0.08)
        formula = make_equation_card(r"x^2+y^2=r^2", color=BLUE_TERM, scale=1.05)
        formula.move_to(RIGHT * 2.8 + UP * 0.32)
        origin = MathTex(r"\text{centre }(0,0)", color=GREEN_OK).scale(0.82)
        origin.move_to(RIGHT * 2.8 + DOWN * 0.42)
        origin_bg = BackgroundRectangle(origin, color=BLACK, fill_opacity=1, buff=0.13)
        range_note = Text("Domain and range depend on r; no asymptotes.", font_size=19, color=TEAL_TERM)
        range_note.move_to(RIGHT * 2.8 + DOWN * 1.0)
        range_bg = BackgroundRectangle(range_note, color=BLACK, fill_opacity=0.96, buff=0.1)
        beat2 = beat_group(
            head_bg, head, circle, centre, radius, r_label,
            formula, origin_bg, origin, range_bg, range_note,
        )
        self.play(FadeIn(head_bg), FadeIn(head))
        self.play(Create(circle), FadeIn(centre), run_time=1.4)
        self.play(Create(radius), FadeIn(r_label))
        self.play(FadeIn(formula), FadeIn(origin_bg), FadeIn(origin))
        self.play(FadeIn(range_bg), FadeIn(range_note))
        self.wait(2.5)
        self.play(FadeOut(beat2, run_time=0.8))

        head3 = MathTex(r"y=ab^x", color=GREEN_OK).scale(1.0)
        head3.move_to(BAND_CHART_CENTER + UP * 1.48)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=1, buff=0.16)
        growth_label = MathTex(r"b>1:\ \text{growth}", color=GREEN_OK).scale(0.78).move_to(LEFT * 3.2 + UP * 0.95)
        decay_label = MathTex(r"0<b<1:\ \text{decay}", color=ORANGE_TERM).scale(0.78).move_to(RIGHT * 3.2 + UP * 0.95)
        growth_bg = BackgroundRectangle(growth_label, color=BLACK, fill_opacity=0.95, buff=0.1)
        decay_bg = BackgroundRectangle(decay_label, color=BLACK, fill_opacity=0.95, buff=0.1)
        left_ax = Axes(
            x_range=[-2.2, 2.2, 1], y_range=[-0.2, 4, 1],
            x_length=4.5, y_length=2.05, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(LEFT * 3.2 + DOWN * 0.2)
        right_ax = Axes(
            x_range=[-2.2, 2.2, 1], y_range=[-0.2, 4, 1],
            x_length=4.5, y_length=2.05, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(RIGHT * 3.2 + DOWN * 0.2)
        growth = left_ax.plot(lambda x: 2 ** x, x_range=[-2.1, 1.95], color=GREEN_OK, stroke_width=4)
        decay = right_ax.plot(lambda x: 0.5 ** x, x_range=[-1.95, 2.1], color=ORANGE_TERM, stroke_width=4)
        g_asy = DashedLine(left_ax.c2p(-2.15, 0), left_ax.c2p(2.15, 0), color=TEAL_TERM, stroke_width=3)
        d_asy = DashedLine(right_ax.c2p(-2.15, 0), right_ax.c2p(2.15, 0), color=TEAL_TERM, stroke_width=3)
        asymptote = MathTex(r"y=0\ \text{ is the horizontal asymptote}", color=TEAL_TERM).scale(0.72)
        asymptote.move_to(BAND_CHART_CENTER + DOWN * 1.34)
        asymptote_bg = BackgroundRectangle(asymptote, color=BLACK, fill_opacity=1, buff=0.1)
        beat3 = beat_group(
            head3_bg, head3, growth_bg, growth_label, decay_bg, decay_label,
            left_ax, right_ax, growth, decay, g_asy, d_asy, asymptote_bg, asymptote,
        )
        self.play(FadeIn(head3_bg), Write(head3))
        self.play(Create(left_ax), Create(right_ax), run_time=1.2)
        self.play(Create(growth), FadeIn(growth_bg), FadeIn(growth_label), run_time=1.4)
        self.play(Create(decay), FadeIn(decay_bg), FadeIn(decay_label), run_time=1.4)
        self.play(Create(g_asy), Create(d_asy), FadeIn(asymptote_bg), FadeIn(asymptote))
        self.wait(2.5)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("What a and b tell you", font_size=26, color=TEAL_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.44)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        facts = VGroup(
            MathTex(r"y(0)=ab^0=a\quad\Rightarrow\quad a\text{ is the y-intercept}", color=BLUE_TERM).scale(0.78),
            MathTex(r"b>1\Rightarrow\text{growth}", color=GREEN_OK).scale(0.86),
            MathTex(r"0<b<1\Rightarrow\text{decay}", color=ORANGE_TERM).scale(0.86),
            Text("The curve stays above, but never touches, the x-axis.", font_size=19, color=TEAL_TERM),
        ).arrange(DOWN, buff=0.22).move_to(BAND_CHART_CENTER + DOWN * 0.12)
        fact_bgs = VGroup(*[
            BackgroundRectangle(item, color=BLACK, fill_opacity=0.97, buff=0.1)
            for item in facts
        ])
        beat4 = beat_group(head4_bg, head4, fact_bgs, facts)
        self.play(FadeIn(head4_bg), FadeIn(head4))
        for bg, item in zip(fact_bgs, facts):
            self.play(FadeIn(bg), FadeIn(item), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"x^2+y^2=r^2,\ y=ab^x\ (\text{asymptote }y=0)",
            "b > 1 gives growth; 0 < b < 1 gives decay.",
            final_wait=38.0,
        )
