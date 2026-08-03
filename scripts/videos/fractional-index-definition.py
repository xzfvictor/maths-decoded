"""
Manim scene for the lesson `fractional-index-definition`
(topic `l10a-an-fractional-exponents`).

a^(1/n) is the n-th root of a. Worked example 16^(1/4) = 2 because
2^4 = 16. Reject the mistake of dividing the base by n.

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
import numpy as np


class FractionalIndexDefinitionScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "What does a^(1/n) mean?",
            "The n-th root of a",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Definition with squares, then nth roots (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        definition = MathTex(
            r"a^{1/n} = \sqrt[n]{a}",
            color=BLUE_TERM,
        ).scale(1.2)
        definition.move_to(BAND_CHART_CENTER + UP * 0.8)
        definition_bg = BackgroundRectangle(definition, color=BLACK, fill_opacity=1, buff=0.3)
        definition_bg.move_to(definition.get_center())
        beat_2 = beat_group(beat_2, definition, definition_bg)
        self.play(FadeIn(definition_bg, run_time=0.4), Write(definition, run_time=1.6))
        self.wait(1.5)

        # Familiar: square root.
        familiar = MathTex(
            r"a^{1/2} = \sqrt{a}\quad \text{(square root, the usual one)}",
            color=GREEN_OK,
        ).scale(0.95)
        familiar.next_to(definition, DOWN, buff=0.5)
        familiar_bg = BackgroundRectangle(familiar, color=BLACK, fill_opacity=1, buff=0.2)
        familiar_bg.move_to(familiar.get_center())
        beat_2 = beat_group(beat_2, familiar, familiar_bg)
        self.play(FadeIn(familiar_bg, run_time=0.4), Write(familiar, run_time=1.5))
        self.wait(1.5)

        # Cube root.
        cube = MathTex(
            r"a^{1/3} = \sqrt[3]{a}\quad \text{(cube root)}",
            color=ORANGE_TERM,
        ).scale(0.95)
        cube.next_to(familiar, DOWN, buff=0.4)
        cube_bg = BackgroundRectangle(cube, color=BLACK, fill_opacity=1, buff=0.2)
        cube_bg.move_to(cube.get_center())
        beat_2 = beat_group(beat_2, cube, cube_bg)
        self.play(FadeIn(cube_bg, run_time=0.4), Write(cube, run_time=1.5))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: 16^(1/4) = 2 (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        ex = MathTex(r"16^{1/4}", color=BLUE_TERM).scale(1.2)
        ex.move_to(BAND_CHART_CENTER + UP * 0.8)
        ex_bg = BackgroundRectangle(ex, color=BLACK, fill_opacity=1, buff=0.25)
        ex_bg.move_to(ex.get_center())
        beat_3 = beat_group(beat_3, ex, ex_bg)
        self.play(FadeIn(ex_bg, run_time=0.4), Write(ex, run_time=1.4))
        self.wait(1.0)

        # "Find the number that, when raised to 4, gives 16."
        ask = Text("What number, raised to 4, gives 16?", font_size=22, color=ORANGE_TERM)
        ask.next_to(ex, DOWN, buff=0.5)
        ask_bg = BackgroundRectangle(ask, color=BLACK, fill_opacity=1, buff=0.18)
        ask_bg.move_to(ask.get_center())
        beat_3 = beat_group(beat_3, ask, ask_bg)
        self.play(FadeIn(ask_bg, run_time=0.3), FadeIn(ask, run_time=1.0))
        self.wait(1.0)

        # Answer: 2^4 = 16, so 16^(1/4) = 2.
        ans = MathTex(
            r"2^{4} = 16 \quad\Rightarrow\quad 16^{1/4} = 2",
            color=GREEN_OK,
        ).scale(1.0)
        ans.next_to(ask, DOWN, buff=0.5)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.2)
        ans_bg.move_to(ans.get_center())
        beat_3 = beat_group(beat_3, ans, ans_bg)
        self.play(FadeIn(ans_bg, run_time=0.4), Write(ans, run_time=1.8))
        self.wait(2.0)

        # More examples.
        more = MathTex(
            r"27^{1/3} = 3,\quad 81^{1/4} = 3,\quad 32^{1/5} = 2",
            color=BLUE_TERM,
        ).scale(0.9)
        more.next_to(ans, DOWN, buff=0.5)
        more_bg = BackgroundRectangle(more, color=BLACK, fill_opacity=1, buff=0.2)
        more_bg.move_to(more.get_center())
        beat_3 = beat_group(beat_3, more, more_bg)
        self.play(FadeIn(more_bg, run_time=0.4), Write(more, run_time=1.6))
        self.wait(1.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: dividing the base by n (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"16^{1/4} = 16 \div 4 = 4\ \text{?}",
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
            "16^(1/4) is a root, not a quotient. The base 16 stays as a base.",
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
        # Beat 5 — Final takeaway (~36 s, total ≈ 83 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{1/n} = \sqrt[n]{a}\quad \text{(the n-th root of a)}",
            "Find the number that, when raised to n, gives a.",
            final_wait=36.0,
        )
