import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class LinearFitEquationScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "The least-squares line",
            "Turn a roughly linear cloud into the prediction y = a + bx.",
        )

        def scatter(color=BLUE_TERM):
            axes = Axes(
                x_range=[0, 10, 2], y_range=[0, 10, 2],
                x_length=5.2, y_length=2.6, tips=False,
                axis_config={"include_numbers": False, "stroke_width": 1.5},
            ).move_to(BAND_CHART_CENTER + LEFT * 1.6 + UP * 0.05)
            points = [(1, 1.7), (2, 2.4), (3, 3.6), (4, 4.0), (5, 5.3),
                      (6, 5.7), (7, 6.8), (8, 7.4), (9, 8.2)]
            dots = VGroup(*[Dot(axes.c2p(x, y), color=color, radius=0.06) for x, y in points])
            return axes, dots

        # Beat 2 — concrete scatterplot.
        head2 = Text("A roughly linear pattern", font_size=24, color=BLUE_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.4 + RIGHT * 3.9)
        ax, dots = scatter()
        prompt = Text("Can one line summarise the trend?", font_size=21, color=ORANGE_TERM)
        prompt.move_to(BAND_CHART_CENTER + RIGHT * 3.7 + DOWN * 0.2)
        prompt_bg = BackgroundRectangle(prompt, color=BLACK, fill_opacity=0.95, buff=0.14)
        beat2 = beat_group(head2, ax, dots, prompt_bg, prompt)
        self.play(FadeIn(head2), Create(ax), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.08), run_time=1.3)
        self.play(FadeIn(prompt_bg), FadeIn(prompt), run_time=0.9)
        self.wait(4.0)
        self.play(FadeOut(beat2, run_time=0.8))

        # Beat 3 — generalise to the fitted equation.
        head3 = Text("Least squares chooses a and b", font_size=24, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.4 + RIGHT * 3.6)
        ax3, dots3 = scatter()
        fit_line = ax3.plot(lambda x: 1 + 0.8 * x, x_range=[0, 10], color=GREEN_OK, stroke_width=3)
        fit = make_equation_card(
            r"\hat y=a+bx", color=GREEN_OK, scale=1.0
        ).move_to(BAND_CHART_CENTER + RIGHT * 3.7 + UP * 0.35)
        labels = Text("a: intercept     b: slope", font_size=20, color=TEAL_TERM)
        labels.move_to(BAND_CHART_CENTER + RIGHT * 3.7 + DOWN * 0.65)
        labels_bg = BackgroundRectangle(labels, color=BLACK, fill_opacity=0.95, buff=0.14)
        beat3 = beat_group(head3, ax3, dots3, fit_line, fit, labels_bg, labels)
        self.play(FadeIn(head3), Create(ax3), FadeIn(dots3), run_time=1.2)
        self.play(Create(fit_line), FadeIn(fit), run_time=1.4)
        self.play(FadeIn(labels_bg), FadeIn(labels), run_time=0.9)
        self.wait(5.0)
        self.play(FadeOut(beat3, run_time=0.8))

        # Beat 4 — contrast and reject an unsuitable fit.
        head4 = Text("Reject a line when no trend is present", font_size=24, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.4 + RIGHT * 3.5)
        ax4, _ = scatter(RED_REJECT)
        random_points = [(1, 8), (2, 1), (3, 7), (4, 2.5), (5, 9),
                         (6, 3), (7, 8.5), (8, 4), (9, 6.5)]
        random_dots = VGroup(*[
            Dot(ax4.c2p(x, y), color=RED_REJECT, radius=0.06)
            for x, y in random_points
        ])
        reject = Text("No linear pattern: predictions would mislead.", font_size=20, color=RED_REJECT)
        reject.move_to(BAND_CHART_CENTER + RIGHT * 3.7 + DOWN * 0.3)
        reject_bg = BackgroundRectangle(reject, color=BLACK, fill_opacity=0.95, buff=0.14)
        beat4 = beat_group(head4, ax4, random_dots, reject_bg, reject)
        self.play(FadeIn(head4), Create(ax4), FadeIn(random_dots), run_time=1.3)
        self.play(FadeIn(reject_bg), FadeIn(reject), run_time=0.9)
        self.wait(5.0)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"\hat y=a+bx\quad\text{minimises}\quad\sum_i(y_i-\hat y_i)^2",
            "Use the line only when the scatterplot is roughly linear.",
            final_wait=32.0,
        )
