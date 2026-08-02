"""
Manim scene for the lesson `building-the-model`
(topic `l8-a-linear-modelling`).

A linear model is an equation of the form y = mx + c that approximates a
real situation. Translate the words into algebra.

Target duration: ~83 s (matches audio).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    make_equation_card, animate_intro, animate_final_definition,
)
from manim import *


class BuildingTheModelScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Building a linear model from words",
            "Define variables, translate the situation, use the model.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Define the variable (~20 s)
        # ──────────────────────────────────────────────────────────────────
        # "Let n be the number of items, B be the total bill."
        sentence = Text(
            "A plan costs $25 per month plus $0.10 per text.",
            font_size=24,
        ).move_to(BAND_CHART_CENTER + UP * 1.2)
        sentence_bg = BackgroundRectangle(sentence, color=BLACK, fill_opacity=1, buff=0.2)
        sentence_bg.move_to(sentence.get_center())
        self.play(FadeIn(sentence_bg, run_time=0.5), FadeIn(sentence, run_time=1.4))
        self.wait(2.5)

        # The variable definition.
        defn = Text(
            "Let n = number of texts,  B = monthly bill.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(sentence, DOWN, buff=0.7)
        defn_bg = BackgroundRectangle(defn, color=BLACK, fill_opacity=0.95, buff=0.18)
        defn_bg.move_to(defn.get_center())
        self.play(FadeIn(defn_bg, run_time=0.5), FadeIn(defn, run_time=1.4))
        self.wait(4.0)
        self.play(
            FadeOut(VGroup(sentence, sentence_bg), run_time=1.0),
            FadeOut(VGroup(defn, defn_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Translate words to equation (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Build the model step by step.
        fixed = MathTex(r"\text{fixed cost} = \$25", color=BLUE_TERM).scale(1.0)
        variable = MathTex(r"\text{variable cost} = \$0.10 \cdot n", color=ORANGE_TERM).scale(1.0)
        fixed.move_to(BAND_CHART_CENTER + UP * 1.2)
        variable.move_to(BAND_CHART_CENTER + UP * 0.1)
        for m in [fixed, variable]:
            m_bg = BackgroundRectangle(m, color=BLACK, fill_opacity=0.95, buff=0.18)
            m_bg.move_to(m.get_center())
            m.bg = m_bg
            m.set_z_index(2)

        self.play(
            FadeIn(fixed.bg, run_time=0.4),
            FadeIn(fixed, run_time=1.2),
        )
        self.wait(2.0)
        self.play(
            FadeIn(variable.bg, run_time=0.4),
            FadeIn(variable, run_time=1.4),
        )
        self.wait(3.0)

        # Combine into the final model.
        model = MathTex(r"B = 25 + 0.10\,n", color=GREEN_OK).scale(1.2)
        model.move_to(BAND_CHART_CENTER + DOWN * 0.7)
        model_bg = BackgroundRectangle(model, color=BLACK, fill_opacity=1, buff=0.3)
        model_bg.move_to(model.get_center())
        model_box = SurroundingRectangle(model, color=GREEN_OK, buff=0.3, stroke_width=3)

        self.play(
            FadeOut(fixed.bg, run_time=0.5),
            FadeOut(fixed, run_time=0.5),
            FadeOut(variable.bg, run_time=0.5),
            FadeOut(variable, run_time=0.5),
        )
        self.play(
            FadeIn(model_bg, run_time=0.5),
            Write(model, run_time=1.8),
        )
        self.play(Create(model_box, run_time=1.0))
        self.wait(4.0)
        self.play(
            FadeOut(VGroup(model, model_bg, model_box), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Use the model (~16 s)
        # ──────────────────────────────────────────────────────────────────
        # Substitute n = 80.
        use_math = MathTex(r"B = 25 + 0.10 \times 80 = 25 + 8 = 33", color=WHITE).scale(1.0)
        use_math.move_to(BAND_CHART_CENTER + UP * 0.5)
        use_bg = BackgroundRectangle(use_math, color=BLACK, fill_opacity=1, buff=0.3)
        use_bg.move_to(use_math.get_center())
        self.play(FadeIn(use_bg, run_time=0.5), Write(use_math, run_time=2.0))
        self.wait(3.0)

        # Result.
        result = Text(
            "For n = 80 texts, the bill is $33.",
            font_size=24,
            color=GREEN_OK,
        ).next_to(use_math, DOWN, buff=0.7)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=0.95, buff=0.18)
        result_bg.move_to(result.get_center())
        self.play(FadeIn(result_bg, run_time=0.4), FadeIn(result, run_time=1.2))
        self.wait(4.0)
        self.play(
            FadeOut(VGroup(use_math, use_bg), run_time=0.8),
            FadeOut(VGroup(result, result_bg), run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~18 s, total ≈ 83 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Total} \;=\; \text{fixed} + (\text{rate} \times \text{quantity})",
            "Define a variable, then translate the words into algebra.",
            final_wait=38.0,
        )