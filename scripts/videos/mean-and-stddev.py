"""
Manim scene for the lesson `mean-and-stddev`
(topic `l10a-ast-mean-standard-deviation`).

Generic summary of two measures: the mean (balance point, sum divided
by count) and the standard deviation (square the distances from the
mean, average, take the square root). Caveat: textbooks differ on
whether to divide by n or n - 1 — both appear in Year 10A.

Target duration: ~98 s (matches the audio narration length).
"""

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
            "Centre and spread — the two key summaries of a list of numbers.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Mean: balance point of the data (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Mean = balance point",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.1)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.5)

        # Step 1: add everything.
        step1 = MathTex(
            r"1.\;\text{Sum all the values:}\; \sum x_i",
            color=GREEN_OK,
        ).scale(0.95)
        step1.move_to(BAND_CHART_CENTER + UP * 0.4)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=1, buff=0.2)
        step1_bg.move_to(step1.get_center())
        beat_2 = beat_group(beat_2, step1, step1_bg)
        self.play(FadeIn(step1_bg, run_time=0.4), FadeIn(step1, run_time=1.4))
        self.wait(2.0)

        # Step 2: divide by count.
        step2 = MathTex(
            r"2.\;\text{Divide by how many:}\; n",
            color=GREEN_OK,
        ).scale(0.95)
        step2.next_to(step1, DOWN, buff=0.45)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=1, buff=0.2)
        step2_bg.move_to(step2.get_center())
        beat_2 = beat_group(beat_2, step2, step2_bg)
        self.play(FadeIn(step2_bg, run_time=0.4), FadeIn(step2, run_time=1.2))
        self.wait(2.0)

        # The mean formula.
        formula = make_equation_card(
            r"\bar{x} \;=\; \dfrac{1}{n}\sum x_i",
            color=BLUE_TERM, scale=1.0,
        )
        formula.move_to(BAND_CHART_CENTER + DOWN * 0.85)
        beat_2 = beat_group(beat_2, formula)
        self.play(FadeIn(formula, run_time=1.4))
        self.wait(5.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Standard deviation: how spread out (~28 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head3 = Text("Standard deviation = spread",
                     font_size=24, color=BLUE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.15)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        beat_3 = beat_group(beat_3, head3, head3_bg)
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        s1 = Text("1. Find each value's distance from the mean.",
                  font_size=22, color=BLUE_TERM)
        s1.move_to(BAND_CHART_CENTER + UP * 0.45)
        s1_bg = BackgroundRectangle(s1, color=BLACK, fill_opacity=0.95, buff=0.15)
        s1_bg.move_to(s1.get_center())
        beat_3 = beat_group(beat_3, s1, s1_bg)
        self.play(FadeIn(s1_bg, run_time=0.4), FadeIn(s1, run_time=1.4))
        self.wait(1.5)

        s2 = Text("2. Square those distances (kills the negatives).",
                  font_size=22, color=TEAL_TERM)
        s2.next_to(s1, DOWN, buff=0.35)
        s2_bg = BackgroundRectangle(s2, color=BLACK, fill_opacity=0.95, buff=0.15)
        s2_bg.move_to(s2.get_center())
        beat_3 = beat_group(beat_3, s2, s2_bg)
        self.play(FadeIn(s2_bg, run_time=0.4), FadeIn(s2, run_time=1.4))
        self.wait(1.5)

        s3 = Text("3. Average, then take the square root.",
                  font_size=22, color=ORANGE_TERM)
        s3.next_to(s2, DOWN, buff=0.35)
        s3_bg = BackgroundRectangle(s3, color=BLACK, fill_opacity=0.95, buff=0.15)
        s3_bg.move_to(s3.get_center())
        beat_3 = beat_group(beat_3, s3, s3_bg)
        self.play(FadeIn(s3_bg, run_time=0.4), FadeIn(s3, run_time=1.4))
        self.wait(2.0)

        # Generic formula (population, ÷ n).
        sd = make_equation_card(
            r"s \;=\; \sqrt{\dfrac{1}{n}\sum (x_i - \bar{x})^{2}}",
            color=GREEN_OK, scale=0.92,
        )
        sd.move_to(BAND_CHART_CENTER + DOWN * 0.85)
        beat_3 = beat_group(beat_3, sd)
        self.play(FadeIn(sd, run_time=1.6))
        self.wait(8.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Caveat: n vs n − 1 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        head4 = Text("Sample vs population caveat",
                     font_size=24, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.05)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        beat_4 = beat_group(beat_4, head4, head4_bg)
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(1.0)

        pop = MathTex(
            r"\text{Population: divide by } n",
            color=BLUE_TERM,
        ).scale(0.95)
        pop.move_to(BAND_CHART_CENTER + UP * 0.3)
        pop_bg = BackgroundRectangle(pop, color=BLACK, fill_opacity=1, buff=0.2)
        pop_bg.move_to(pop.get_center())
        beat_4 = beat_group(beat_4, pop, pop_bg)
        self.play(FadeIn(pop_bg, run_time=0.4), FadeIn(pop, run_time=1.4))
        self.wait(2.0)

        samp = MathTex(
            r"\text{Sample: divide by } n-1",
            color=ORANGE_TERM,
        ).scale(0.95)
        samp.next_to(pop, DOWN, buff=0.45)
        samp_bg = BackgroundRectangle(samp, color=BLACK, fill_opacity=1, buff=0.2)
        samp_bg.move_to(samp.get_center())
        beat_4 = beat_group(beat_4, samp, samp_bg)
        self.play(FadeIn(samp_bg, run_time=0.4), FadeIn(samp, run_time=1.4))
        self.wait(1.5)

        note = Text("Both appear in Year 10A — keep an eye out.",
                    font_size=22, color=GREEN_OK)
        note.next_to(samp, DOWN, buff=0.45)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        beat_4 = beat_group(beat_4, note, note_bg)
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.2))
        self.wait(7.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~44 s, total ≈ 98 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\bar{x} = \tfrac{1}{n}\sum x_i,\;\; s = \sqrt{\tfrac{1}{n-1}\sum (x_i - \bar{x})^{2}}",
            "Mean locates the centre; standard deviation measures the spread.",
            final_wait=44.0,
        )
