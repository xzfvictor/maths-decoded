"""
Manim scene for the lesson `log-laws`
(topic `l10a-an-logarithms-scales`).

The three logarithm laws come from the index laws, because logs are
really exponents in disguise. Show product, quotient, power laws; then
add consequences: log(1) = 0, log_a(a) = 1, a^(log_a x) = x.

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


class LogLawsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Logarithm laws",
            "Products become sums, quotients become differences.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Three laws (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        law1 = MathTex(
            r"\log(mn) \;=\; \log m \;+\; \log n",
            color=BLUE_TERM,
        ).scale(1.0)
        law1.move_to(BAND_CHART_CENTER + UP * 0.95)
        law1_bg = BackgroundRectangle(law1, color=BLACK, fill_opacity=1, buff=0.25)
        law1_bg.move_to(law1.get_center())
        beat_2 = beat_group(beat_2, law1, law1_bg)
        self.play(FadeIn(law1_bg, run_time=0.4), Write(law1, run_time=1.6))
        self.wait(1.5)

        law2 = MathTex(
            r"\log\!\left(\dfrac{m}{n}\right) \;=\; \log m \;-\; \log n",
            color=ORANGE_TERM,
        ).scale(1.0)
        law2.next_to(law1, DOWN, buff=0.5)
        law2_bg = BackgroundRectangle(law2, color=BLACK, fill_opacity=1, buff=0.25)
        law2_bg.move_to(law2.get_center())
        beat_2 = beat_group(beat_2, law2, law2_bg)
        self.play(FadeIn(law2_bg, run_time=0.4), Write(law2, run_time=1.7))
        self.wait(1.5)

        law3 = MathTex(
            r"\log(m^{k}) \;=\; k\,\log m",
            color=GREEN_OK,
        ).scale(1.0)
        law3.next_to(law2, DOWN, buff=0.5)
        law3_bg = BackgroundRectangle(law3, color=BLACK, fill_opacity=1, buff=0.25)
        law3_bg.move_to(law3.get_center())
        beat_2 = beat_group(beat_2, law3, law3_bg)
        self.play(FadeIn(law3_bg, run_time=0.4), Write(law3, run_time=1.5))
        self.wait(2.5)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Why: logs are exponents in disguise (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        why = Text("Why do these laws work?", font_size=24, color=BLUE_TERM)
        why.move_to(BAND_CHART_CENTER + UP * 1.0)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.15)
        why_bg.move_to(why.get_center())
        beat_3 = beat_group(beat_3, why, why_bg)
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.0))
        self.wait(1.5)

        # Add exponents when multiplying the underlying numbers.
        line1 = MathTex(
            r"\text{Add exponents} \;=\; \text{multiply the numbers}",
            color=ORANGE_TERM,
        ).scale(0.95)
        line1.move_to(BAND_CHART_CENTER + UP * 0.3)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=1, buff=0.2)
        line1_bg.move_to(line1.get_center())
        beat_3 = beat_group(beat_3, line1, line1_bg)
        self.play(FadeIn(line1_bg, run_time=0.4), FadeIn(line1, run_time=1.6))
        self.wait(1.5)

        line2 = MathTex(
            r"\text{Subtract exponents} \;=\; \text{divide the numbers}",
            color=ORANGE_TERM,
        ).scale(0.95)
        line2.next_to(line1, DOWN, buff=0.45)
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=1, buff=0.2)
        line2_bg.move_to(line2.get_center())
        beat_3 = beat_group(beat_3, line2, line2_bg)
        self.play(FadeIn(line2_bg, run_time=0.4), FadeIn(line2, run_time=1.6))
        self.wait(6.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Three handy consequences (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        head = Text("Three handy consequences",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.1)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_4 = beat_group(beat_4, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        c1 = MathTex(
            r"\log(1) \;=\; 0",
            color=GREEN_OK,
        ).scale(1.0)
        c1.move_to(BAND_CHART_CENTER + UP * 0.4)
        c1_bg = BackgroundRectangle(c1, color=BLACK, fill_opacity=1, buff=0.22)
        c1_bg.move_to(c1.get_center())
        beat_4 = beat_group(beat_4, c1, c1_bg)
        self.play(FadeIn(c1_bg, run_time=0.4), Write(c1, run_time=1.3))
        self.wait(1.0)

        c2 = MathTex(
            r"\log_{a}(a) \;=\; 1",
            color=ORANGE_TERM,
        ).scale(1.0)
        c2.next_to(c1, DOWN, buff=0.4)
        c2_bg = BackgroundRectangle(c2, color=BLACK, fill_opacity=1, buff=0.22)
        c2_bg.move_to(c2.get_center())
        beat_4 = beat_group(beat_4, c2, c2_bg)
        self.play(FadeIn(c2_bg, run_time=0.4), Write(c2, run_time=1.3))
        self.wait(1.0)

        c3 = MathTex(
            r"a^{\,\log_{a}(x)} \;=\; x",
            color=TEAL_TERM,
        ).scale(1.0)
        c3.next_to(c2, DOWN, buff=0.4)
        c3_bg = BackgroundRectangle(c3, color=BLACK, fill_opacity=1, buff=0.22)
        c3_bg.move_to(c3.get_center())
        beat_4 = beat_group(beat_4, c3, c3_bg)
        self.play(FadeIn(c3_bg, run_time=0.4), Write(c3, run_time=1.4))
        self.wait(7.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~43 s, total ≈ 95 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\begin{gathered}\log(mn)=\log m+\log n\\ \log(m/n)=\log m-\log n\\ \log(m^{k})=k\log m\end{gathered}",
            "Logs are exponents in disguise — they obey the index laws.",
            final_wait=43.0,
        )
