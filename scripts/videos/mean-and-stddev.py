import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class MeanAndStddevScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Mean and standard deviation",
            "Two summaries: where the centre is, and how spread out.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Mean: sum / count (~30 s)
        # ──────────────────────────────────────────────────────────────────
        data = [4, 6, 6, 7, 8, 9]
        # Sum = 40, mean = 40/6 ≈ 6.667
        mean_val = sum(data) / len(data)

        # Show the data row.
        data_row = VGroup(*[MathTex(str(d), color=BLUE_TERM).scale(1.0) for d in data])
        data_row.arrange(RIGHT, buff=0.5)
        data_row.move_to(BAND_CHART_CENTER + UP * 0.9)
        self.play(*[FadeIn(m, run_time=0.5) for m in data_row], run_time=2.0)
        self.wait(2.0)

        # The mean formula.
        formula = make_equation_card(
            r"\bar{x} \;=\; \dfrac{\sum x_i}{n}",
            color=BLUE_TERM,
            scale=1.0,
        )
        formula.next_to(data_row, DOWN, buff=0.7)
        self.play(FadeIn(formula, run_time=1.4))
        self.wait(3.0)

        # Concrete sum.
        concrete = MathTex(
            r"\bar{x} \;=\; \dfrac{4+6+6+7+8+9}{6} \;=\; 6.67",
            color=GREEN_OK,
        ).scale(0.95)
        concrete.next_to(formula, DOWN, buff=0.5)
        concrete_bg = BackgroundRectangle(concrete, color=BLACK, fill_opacity=0.95, buff=0.18)
        concrete_bg.move_to(concrete.get_center())
        self.play(FadeIn(concrete_bg, run_time=0.4), FadeIn(concrete, run_time=1.4))
        self.wait(11.0)

        beat1 = beat_group(data_row, formula, concrete, concrete_bg)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Standard deviation (~32 s)
        # ──────────────────────────────────────────────────────────────────
        step1 = Text(
            "1. Find each value's distance from the mean.",
            font_size=22,
            color=BLUE_TERM,
        ).move_to(BAND_CHART_CENTER + UP * 1.1)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=0.95, buff=0.15)
        step1_bg.move_to(step1.get_center())
        self.play(FadeIn(step1_bg, run_time=0.4), FadeIn(step1, run_time=1.2))
        self.wait(2.5)

        step2 = Text(
            "2. Square those distances (drops the negative signs).",
            font_size=22,
            color=TEAL_TERM,
        ).next_to(step1, DOWN, buff=0.4)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=0.95, buff=0.15)
        step2_bg.move_to(step2.get_center())
        self.play(FadeIn(step2_bg, run_time=0.4), FadeIn(step2, run_time=1.2))
        self.wait(2.5)

        step3 = Text(
            "3. Average the squares, then take the square root.",
            font_size=22,
            color=ORANGE_TERM,
        ).move_to(BAND_CHART_CENTER + UP * 0.25)
        step3_bg = BackgroundRectangle(step3, color=BLACK, fill_opacity=0.95, buff=0.15)
        step3_bg.move_to(step3.get_center())
        self.play(FadeIn(step3_bg, run_time=0.4), FadeIn(step3, run_time=1.2))
        self.wait(2.5)

        sd = make_equation_card(
            r"s \;=\; \sqrt{\dfrac{\sum (x_i - \bar{x})^2}{n}}",
            color=GREEN_OK,
            scale=1.0,
        )
        sd.move_to(BAND_CHART_CENTER + DOWN * 1.05)
        self.play(FadeIn(sd, run_time=1.6))
        self.wait(8.0)

        beat2 = beat_group(step1, step1_bg, step2, step2_bg, step3, step3_bg, sd)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Contrast: tight vs spread (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Tight cluster: small stddev.
        tight = MathTex(
            r"\{5,\; 5.5,\; 6,\; 6.5,\; 7\} \;\rightarrow\; s \approx 0.71",
            color=GREEN_OK,
        ).scale(0.85)
        tight.move_to(BAND_CHART_CENTER + UP * 0.6)
        tight_bg = BackgroundRectangle(tight, color=BLACK, fill_opacity=0.95, buff=0.18)
        tight_bg.move_to(tight.get_center())
        self.play(FadeIn(tight_bg, run_time=0.4), FadeIn(tight, run_time=1.4))
        self.wait(3.0)

        spread = MathTex(
            r"\{1,\; 3,\; 6,\; 9,\; 11\} \;\rightarrow\; s \approx 3.74",
            color=RED_REJECT,
        ).scale(0.85)
        spread.next_to(tight, DOWN, buff=0.5)
        spread_bg = BackgroundRectangle(spread, color=BLACK, fill_opacity=0.95, buff=0.18)
        spread_bg.move_to(spread.get_center())
        self.play(FadeIn(spread_bg, run_time=0.4), FadeIn(spread, run_time=1.4))
        self.wait(7.0)

        beat3 = beat_group(tight, tight_bg, spread, spread_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~44 s, total ≈ 98 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\bar{x} = \tfrac{1}{n}\sum x_i,\;\; s = \sqrt{\tfrac{1}{n}\sum (x_i - \bar{x})^2}",
            "Mean locates the centre; standard deviation measures spread.",
            final_wait=44.0,
        )
