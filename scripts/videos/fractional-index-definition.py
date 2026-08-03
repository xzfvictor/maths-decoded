"""
Manim scene for the lesson `fractional-index-definition`
(topic `l10a-an-fractional-exponents`).

Fractional exponents split into a root and a power: a^(m/n) means
take the n-th root of a, then raise it to the m-th power. Examples:
a^(1/2) = sqrt(a), a^(1/3) = cube root, a^(-1/2) = 1/sqrt(a).
All five index laws still work.

Target duration: ~83 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class FractionalIndexDefinitionScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Fractional indices",
            "Fractional exponents are surds in disguise.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Split into root and power (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        split = MathTex(
            r"a^{m/n} \;=\; \text{(n-th root of a)}^{m}",
            color=BLUE_TERM,
        ).scale(1.05)
        split.move_to(BAND_CHART_CENTER + UP * 0.7)
        split_bg = BackgroundRectangle(split, color=BLACK, fill_opacity=1, buff=0.25)
        split_bg.move_to(split.get_center())
        beat_2 = beat_group(beat_2, split, split_bg)
        self.play(FadeIn(split_bg, run_time=0.4), Write(split, run_time=1.8))
        self.wait(1.5)

        bot = Text("bottom = root    top = power", font_size=22, color=ORANGE_TERM)
        bot.next_to(split, DOWN, buff=0.5)
        bot_bg = BackgroundRectangle(bot, color=BLACK, fill_opacity=0.95, buff=0.15)
        bot_bg.move_to(bot.get_center())
        beat_2 = beat_group(beat_2, bot, bot_bg)
        self.play(FadeIn(bot_bg, run_time=0.4), FadeIn(bot, run_time=1.2))
        self.wait(2.0)

        # a^(1/n) special case.
        simple = MathTex(
            r"a^{1/n} \;=\; \sqrt[n]{a} \quad \text{(the n-th root)}",
            color=BLUE_TERM,
        ).scale(0.95)
        simple.next_to(bot, DOWN, buff=0.45)
        simple_bg = BackgroundRectangle(simple, color=BLACK, fill_opacity=1, buff=0.2)
        simple_bg.move_to(simple.get_center())
        beat_2 = beat_group(beat_2, simple, simple_bg)
        self.play(FadeIn(simple_bg, run_time=0.4), Write(simple, run_time=1.6))
        self.wait(2.5)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Familiar: a^(1/2) and a^(1/3) (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        sq = MathTex(
            r"a^{1/2} \;=\; \sqrt{a}",
            color=GREEN_OK,
        ).scale(1.0)
        sq.move_to(BAND_CHART_CENTER + UP * 0.6)
        sq_bg = BackgroundRectangle(sq, color=BLACK, fill_opacity=1, buff=0.22)
        sq_bg.move_to(sq.get_center())
        beat_3 = beat_group(beat_3, sq, sq_bg)
        self.play(FadeIn(sq_bg, run_time=0.4), Write(sq, run_time=1.4))
        self.wait(1.5)

        cube = MathTex(
            r"a^{1/3} \;=\; \sqrt[3]{a}",
            color=ORANGE_TERM,
        ).scale(1.0)
        cube.next_to(sq, DOWN, buff=0.4)
        cube_bg = BackgroundRectangle(cube, color=BLACK, fill_opacity=1, buff=0.22)
        cube_bg.move_to(cube.get_center())
        beat_3 = beat_group(beat_3, cube, cube_bg)
        self.play(FadeIn(cube_bg, run_time=0.4), Write(cube, run_time=1.4))
        self.wait(1.5)

        # Negative fractional exponent: a^(-1/2) = 1/sqrt(a).
        neg = MathTex(
            r"a^{-1/2} \;=\; \dfrac{1}{\sqrt{a}}",
            color=TEAL_TERM,
        ).scale(1.0)
        neg.next_to(cube, DOWN, buff=0.4)
        neg_bg = BackgroundRectangle(neg, color=BLACK, fill_opacity=1, buff=0.22)
        neg_bg.move_to(neg.get_center())
        beat_3 = beat_group(beat_3, neg, neg_bg)
        self.play(FadeIn(neg_bg, run_time=0.4), Write(neg, run_time=1.5))
        self.wait(3.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Index laws still apply (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        laws = Text("All five index laws still apply.",
                    font_size=24, color=BLUE_TERM)
        laws.move_to(BAND_CHART_CENTER + UP * 0.95)
        laws_bg = BackgroundRectangle(laws, color=BLACK, fill_opacity=0.95, buff=0.15)
        laws_bg.move_to(laws.get_center())
        beat_4 = beat_group(beat_4, laws, laws_bg)
        self.play(FadeIn(laws_bg, run_time=0.4), FadeIn(laws, run_time=1.2))
        self.wait(1.5)

        line1 = MathTex(
            r"a^{m} \cdot a^{n} \;=\; a^{m+n}",
            color=GREEN_OK,
        ).scale(1.0)
        line1.move_to(BAND_CHART_CENTER + UP * 0.15)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=1, buff=0.2)
        line1_bg.move_to(line1.get_center())
        beat_4 = beat_group(beat_4, line1, line1_bg)
        self.play(FadeIn(line1_bg, run_time=0.4), Write(line1, run_time=1.4))
        self.wait(1.2)

        line2 = MathTex(
            r"\dfrac{a^{m}}{a^{n}} \;=\; a^{m-n} \qquad (a^{m})^{n} \;=\; a^{mn}",
            color=ORANGE_TERM,
        ).scale(0.95)
        line2.next_to(line1, DOWN, buff=0.45)
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=1, buff=0.2)
        line2_bg.move_to(line2.get_center())
        beat_4 = beat_group(beat_4, line2, line2_bg)
        self.play(FadeIn(line2_bg, run_time=0.4), Write(line2, run_time=1.6))
        self.wait(6.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~36 s, total ≈ 83 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{m/n} = \sqrt[n]{a^{m}} = \left(\sqrt[n]{a}\right)^{m}",
            "Fractional indices aren't new — just index laws with a root inside.",
            final_wait=36.0,
        )
