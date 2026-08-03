"""
Manim scene for the lesson `log-laws`
(topic `l10a-an-logarithms-scales`).

Three log laws: log(xy) = log(x) + log(y), log(x/y) = log(x) - log(y),
log(x^n) = n·log(x). Worked example. Reject the "log of a sum is the
sum of logs" mistake.

Target duration: ~95 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *
import numpy as np


class LogLawsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Logarithm laws",
            "Products become sums, quotients become differences",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Two of the three laws on display (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        law1 = MathTex(
            r"\log(xy) = \log(x) + \log(y)",
            color=BLUE_TERM,
        ).scale(1.0)
        law1.move_to(BAND_CHART_CENTER + UP * 0.9)
        law1_bg = BackgroundRectangle(law1, color=BLACK, fill_opacity=1, buff=0.25)
        law1_bg.move_to(law1.get_center())
        beat_2 = beat_group(beat_2, law1, law1_bg)
        self.play(FadeIn(law1_bg, run_time=0.4), Write(law1, run_time=1.6))
        self.wait(1.0)

        law2 = MathTex(
            r"\log\!\left(\dfrac{x}{y}\right) = \log(x) - \log(y)",
            color=ORANGE_TERM,
        ).scale(1.0)
        law2.next_to(law1, DOWN, buff=0.5)
        law2_bg = BackgroundRectangle(law2, color=BLACK, fill_opacity=1, buff=0.25)
        law2_bg.move_to(law2.get_center())
        beat_2 = beat_group(beat_2, law2, law2_bg)
        self.play(FadeIn(law2_bg, run_time=0.4), Write(law2, run_time=1.6))
        self.wait(1.5)

        law3 = MathTex(
            r"\log(x^{n}) = n\,\log(x)",
            color=GREEN_OK,
        ).scale(1.0)
        law3.next_to(law2, DOWN, buff=0.5)
        law3_bg = BackgroundRectangle(law3, color=BLACK, fill_opacity=1, buff=0.25)
        law3_bg.move_to(law3.get_center())
        beat_2 = beat_group(beat_2, law3, law3_bg)
        self.play(FadeIn(law3_bg, run_time=0.4), Write(law3, run_time=1.5))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: log_10(200) = log_10(2) + 2 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        ex = MathTex(
            r"\log_{10}(200) = \log_{10}(2 \times 100) = \log_{10}(2) + \log_{10}(100)",
            color=BLUE_TERM,
        ).scale(0.9)
        ex.move_to(BAND_CHART_CENTER + UP * 0.8)
        ex_bg = BackgroundRectangle(ex, color=BLACK, fill_opacity=1, buff=0.25)
        ex_bg.move_to(ex.get_center())
        beat_3 = beat_group(beat_3, ex, ex_bg)
        self.play(FadeIn(ex_bg, run_time=0.4), Write(ex, run_time=1.8))
        self.wait(1.0)

        result = MathTex(
            r"= \log_{10}(2) + 2",
            color=GREEN_OK,
        ).scale(1.0)
        result.next_to(ex, DOWN, buff=0.5)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=1, buff=0.2)
        result_bg.move_to(result.get_center())
        beat_3 = beat_group(beat_3, result, result_bg)
        self.play(FadeIn(result_bg, run_time=0.4), Write(result, run_time=1.4))
        self.wait(1.5)

        # Use law 3 on a different example.
        ex2 = MathTex(
            r"\log(x^{3}) = 3\,\log(x)",
            color=ORANGE_TERM,
        ).scale(0.95)
        ex2.next_to(result, DOWN, buff=0.5)
        ex2_bg = BackgroundRectangle(ex2, color=BLACK, fill_opacity=1, buff=0.2)
        ex2_bg.move_to(ex2.get_center())
        beat_3 = beat_group(beat_3, ex2, ex2_bg)
        self.play(FadeIn(ex2_bg, run_time=0.4), Write(ex2, run_time=1.5))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: log of a sum is the sum of logs (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\log(x + y) = \log(x) + \log(y)\ \text{?}",
            color=RED_REJECT,
        ).scale(1.0)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.4),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        right = Text(
            "log only splits products, quotients, and powers — not sums.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=0.95, buff=0.18)
        right_bg.move_to(right.get_center())
        beat_4 = beat_group(beat_4, right, right_bg)
        self.play(FadeIn(right_bg, run_time=0.3), FadeIn(right, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~43 s, total ≈ 95 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\begin{gathered}\log(xy)=\log x+\log y\\\log(x/y)=\log x-\log y\\\log(x^{n})=n\log x\end{gathered}",
            "Logs split products and powers — not sums.",
            final_wait=43.0,
        )
