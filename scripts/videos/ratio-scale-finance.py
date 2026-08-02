"""
Manim scene for the lesson `ratio-scale-finance`
(topic `l9-m-modelling-proportion`).

A ratio compares two quantities; a scale turns a drawing into reality.
The scene scales a concrete recipe (4 serves → 7 serves) by a unit rate,
then generalises the proportional reasoning, and rejects the mistake
of scaling an area by the length factor (it should scale by n^2).

Target duration: ~97 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class RatioScaleFinanceScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Ratio, scale & financial contexts",
            "Scale quantities in proportion — same rate, larger or smaller.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete recipe: 4 serves 200 g flour → 7 serves ?
        # (~25 s)
        # ──────────────────────────────────────────────────────────────────
        # Original recipe card.
        original = MathTex(r"4 \text{ serves } \Rightarrow 200\text{ g flour}", color=BLUE_TERM).scale(0.95)
        original.move_to(BAND_CHART_CENTER + UP * 0.8)
        original_bg = BackgroundRectangle(original, color=BLACK, fill_opacity=1, buff=0.22)
        original_bg.move_to(original.get_center())

        self.play(FadeIn(original_bg, run_time=0.4), Write(original, run_time=1.6))
        self.wait(2.0)

        # Compute the unit rate: 200 / 4 = 50 g per serve.
        rate = MathTex(r"200 \div 4 = 50 \text{ g/serve}", color=GREEN_OK).scale(1.0)
        rate.next_to(original, DOWN, buff=0.55)
        rate_bg = BackgroundRectangle(rate, color=BLACK, fill_opacity=1, buff=0.22)
        rate_bg.move_to(rate.get_center())
        self.play(FadeIn(rate_bg, run_time=0.4), Write(rate, run_time=1.6))
        self.wait(2.5)

        # New serving count and the final answer.
        new_q = MathTex(r"7 \text{ serves } \Rightarrow \;? \text{ g flour}", color=ORANGE_TERM).scale(1.0)
        new_q.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        new_q_bg = BackgroundRectangle(new_q, color=BLACK, fill_opacity=1, buff=0.22)
        new_q_bg.move_to(new_q.get_center())
        self.play(FadeIn(new_q_bg, run_time=0.4), Write(new_q, run_time=1.4))
        self.wait(1.5)

        answer = MathTex(r"7 \times 50 = 350 \text{ g flour}", color=GREEN_OK).scale(1.2)
        answer.move_to(BAND_CHART_CENTER + DOWN * 1.7)
        answer_bg = BackgroundRectangle(answer, color=BLACK, fill_opacity=1, buff=0.25)
        answer_bg.move_to(answer.get_center())
        self.play(FadeIn(answer_bg, run_time=0.4), Write(answer, run_time=1.6))
        self.wait(3.0)
        self.play(
            FadeOut(original, run_time=0.8),
            FadeOut(original_bg, run_time=0.8),
            FadeOut(rate, run_time=0.8),
            FadeOut(rate_bg, run_time=0.8),
            FadeOut(new_q, run_time=0.8),
            FadeOut(new_q_bg, run_time=0.8),
            FadeOut(answer, run_time=0.8),
            FadeOut(answer_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: unit rate × quantity = total (~22 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(
            r"\text{total} = \text{unit rate} \times \text{quantity}",
            color=BLUE_TERM, scale=1.05,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.4))
        self.wait(2.5)

        # Examples in three flavours.
        examples = VGroup(
            MathTex(r"\text{price: } \$/kg", color=ORANGE_TERM).scale(0.85),
            MathTex(r"\text{wages: } \$/\text{hr}", color=ORANGE_TERM).scale(0.85),
            MathTex(r"\text{fuel: } \text{c}/\text{km}", color=ORANGE_TERM).scale(0.85),
        ).arrange(RIGHT, buff=0.6)
        examples.next_to(general, DOWN, buff=0.55)
        ex_bg = BackgroundRectangle(examples, color=BLACK, fill_opacity=0.95, buff=0.18)
        ex_bg.move_to(examples.get_center())
        self.play(FadeIn(ex_bg, run_time=0.4), FadeIn(examples, run_time=1.4))
        self.wait(4.0)
        self.play(
            FadeOut(general, run_time=0.8),
            FadeOut(examples, run_time=0.8),
            FadeOut(ex_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: scaling area by the length factor (~12 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(
            r"\text{scale } 1:2 \;\Rightarrow\; \text{area} \times 2 \text{?}",
            color=RED_REJECT,
        ).scale(0.95)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.4)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.5))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.5)

        right = MathTex(
            r"\text{lengths} \times 2,\ \ \text{areas} \times 2^{2},\ \ \text{volumes} \times 2^{3}",
            color=GREEN_OK,
        ).scale(0.85)
        right.next_to(wrong, DOWN, buff=0.6)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=1, buff=0.25)
        right_bg.move_to(right.get_center())
        self.play(FadeIn(right_bg, run_time=0.4), Write(right, run_time=1.6))
        self.wait(2.5)
        self.play(
            FadeOut(wrong, run_time=0.6),
            FadeOut(wrong_bg, run_time=0.6),
            FadeOut(cross, run_time=0.6),
            FadeOut(right, run_time=0.6),
            FadeOut(right_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~33 s, total ≈ 97 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{total} \;=\; \text{rate} \times \text{quantity}",
            "Same rate, any quantity — scale up or down in proportion.",
            final_wait=37.0,
        )
