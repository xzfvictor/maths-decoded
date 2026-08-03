"""
Manim scene for the lesson `linear-fit-equation`
(topic `l10a-ast-bivariate-lines`).

Finding the line of best fit for paired data via least squares. The
formulas are a headache by hand, so use software (spreadsheet,
graphics calculator, Desmos/GeoGebra). The slope is "extra x adds
slope×y units"; the intercept is the predicted y at x = 0 — only
meaningful when 0 is near the data range.

Target duration: ~76 s (matches the audio narration length).
"""

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
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "The least-squares line",
            "Software finds the slope and intercept for you.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete scatterplot (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        def scatter(color=BLUE_TERM):
            axes = Axes(
                x_range=[0, 10, 2], y_range=[0, 10, 2],
                x_length=4.8, y_length=2.4, tips=False,
                axis_config={"include_numbers": False, "stroke_width": 1.5},
            )
            points = [(1, 1.7), (2, 2.4), (3, 3.6), (4, 4.0), (5, 5.3),
                      (6, 5.7), (7, 6.8), (8, 7.4), (9, 8.2)]
            dots = VGroup(*[Dot(axes.c2p(x, y), color=color, radius=0.06)
                            for x, y in points])
            return axes, dots

        head = Text("A roughly linear pattern",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.0 + LEFT * 2.6)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)

        ax, dots = scatter()
        grp = VGroup(ax, dots).move_to(BAND_CHART_CENTER + LEFT * 2.6 + UP * -0.05)
        beat_2 = beat_group(beat_2, grp)

        prompt = Text("Can one line summarise the trend?",
                      font_size=20, color=ORANGE_TERM)
        prompt.move_to(BAND_CHART_CENTER + UP * -1.1 + LEFT * 2.6)
        prompt_bg = BackgroundRectangle(prompt, color=BLACK, fill_opacity=0.95, buff=0.14)
        prompt_bg.move_to(prompt.get_center())
        beat_2 = beat_group(beat_2, prompt, prompt_bg)

        self.play(FadeIn(head_bg, run_time=0.3), FadeIn(head, run_time=0.9),
                  Create(ax, run_time=1.0))
        self.play(LaggedStart(*[FadeIn(d, run_time=0.4) for d in dots],
                             lag_ratio=0.08), run_time=1.3)
        self.play(FadeIn(prompt_bg, run_time=0.4), FadeIn(prompt, run_time=1.0))
        self.wait(4.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Software tools do the work (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head3 = Text("Let the computer find it",
                     font_size=24, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.1)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        beat_3 = beat_group(beat_3, head3, head3_bg)
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        # Three side-by-side tool cards.
        c1 = make_equation_card(
            r"\text{Spreadsheet: } \texttt{=SLOPE(...)}",
            color=BLUE_TERM, scale=0.7,
        )
        c1.move_to(BAND_CHART_CENTER + UP * 0.15 + LEFT * 3.3)
        c2 = make_equation_card(
            r"\text{Graphics calculator}",
            color=BLUE_TERM, scale=0.7,
        )
        c2.move_to(BAND_CHART_CENTER + UP * 0.15)
        c3 = make_equation_card(
            r"\text{Desmos / GeoGebra}",
            color=BLUE_TERM, scale=0.7,
        )
        c3.move_to(BAND_CHART_CENTER + UP * 0.15 + RIGHT * 3.3)
        tools = VGroup(c1, c2, c3)
        beat_3 = beat_group(beat_3, c1, c2, c3)
        self.play(FadeIn(c1, shift=UP * 0.2, run_time=1.0))
        self.wait(0.3)
        self.play(FadeIn(c2, shift=UP * 0.2, run_time=1.0))
        self.wait(0.3)
        self.play(FadeIn(c3, shift=UP * 0.2, run_time=1.0))
        self.wait(6.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Interpret slope and intercept (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        head4 = Text("Now interpret the numbers",
                     font_size=24, color=BLUE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.05)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        beat_4 = beat_group(beat_4, head4, head4_bg)
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.6)

        slope = MathTex(
            r"\text{slope: } \Delta y \;=\; \text{slope} \times \Delta x",
            color=ORANGE_TERM,
        ).scale(0.95)
        slope.move_to(BAND_CHART_CENTER + UP * 0.25)
        slope_bg = BackgroundRectangle(slope, color=BLACK, fill_opacity=1, buff=0.2)
        slope_bg.move_to(slope.get_center())
        beat_4 = beat_group(beat_4, slope, slope_bg)
        self.play(FadeIn(slope_bg, run_time=0.4), FadeIn(slope, run_time=1.6))
        self.wait(2.0)

        intr = MathTex(
            r"\text{intercept} \;=\; y(0) \quad \text{only if } 0 \text{ is in range}",
            color=GREEN_OK,
        ).scale(0.95)
        intr.next_to(slope, DOWN, buff=0.45)
        intr_bg = BackgroundRectangle(intr, color=BLACK, fill_opacity=1, buff=0.2)
        intr_bg.move_to(intr.get_center())
        beat_4 = beat_group(beat_4, intr, intr_bg)
        self.play(FadeIn(intr_bg, run_time=0.4), FadeIn(intr, run_time=2.0))
        self.wait(8.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~32 s, total ≈ 76 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\hat y = a + b\,x \quad\Longleftrightarrow\quad b = \text{slope},\; a = \text{intercept}",
            "Let the software compute it; your skill is interpreting the numbers.",
            final_wait=32.0,
        )
