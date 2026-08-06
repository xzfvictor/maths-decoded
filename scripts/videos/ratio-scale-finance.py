"""
Manim scene for the lesson `ratio-scale-finance`
(topic `l9-m-modelling-proportion`).

A ratio compares two quantities; a scale turns a drawing into reality;
financial problems reduce to unit rates. The scene scales a concrete
recipe (4 serves → 7 serves) by a unit rate, then generalises, then
rejects the mistake of scaling area by the length factor.

The audio narrative runs ~38 s; the scene is paced to match.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class RatioScaleFinanceScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Ratio, scale & financial contexts",
            "Scale quantities in proportion — same rate, larger or smaller.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete recipe: 4 serves 200 g flour → 7 serves ?
        # (~9 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        original = MathTex(
            r"4 \text{ serves } \Rightarrow 200\text{ g flour}",
            color=BLUE_TERM,
        ).scale(0.85)
        original.move_to(BAND_CHART_CENTER + UP * 1.4)
        original_bg = BackgroundRectangle(original, color=BLACK, fill_opacity=1, buff=0.22)
        original_bg.move_to(original.get_center())
        beat_2.add(original, original_bg)
        self.play(FadeIn(original_bg, run_time=0.4), Write(original, run_time=1.2))
        self.wait(0.4)

        # Compute the unit rate: 200 / 4 = 50 g per serve.
        rate = MathTex(
            r"200 \div 4 = 50 \text{ g/serve}",
            color=GREEN_OK,
        ).scale(0.9)
        rate.next_to(original, DOWN, buff=0.4)
        rate_bg = BackgroundRectangle(rate, color=BLACK, fill_opacity=1, buff=0.22)
        rate_bg.move_to(rate.get_center())
        beat_2.add(rate, rate_bg)
        self.play(FadeIn(rate_bg, run_time=0.4), Write(rate, run_time=1.2))
        self.wait(0.4)

        # New serving count.
        new_q = MathTex(
            r"7 \text{ serves } \Rightarrow \;? \text{ g flour}",
            color=ORANGE_TERM,
        ).scale(0.9)
        new_q.move_to(BAND_CHART_CENTER + UP * 0.0)
        new_q_bg = BackgroundRectangle(new_q, color=BLACK, fill_opacity=1, buff=0.22)
        new_q_bg.move_to(new_q.get_center())
        beat_2.add(new_q, new_q_bg)
        self.play(FadeIn(new_q_bg, run_time=0.4), Write(new_q, run_time=1.0))
        self.wait(0.3)

        answer = MathTex(
            r"7 \times 50 = 350 \text{ g flour}",
            color=GREEN_OK,
        ).scale(1.05)
        answer.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        answer_bg = BackgroundRectangle(answer, color=BLACK, fill_opacity=1, buff=0.25)
        answer_bg.move_to(answer.get_center())
        beat_2.add(answer, answer_bg)
        self.play(FadeIn(answer_bg, run_time=0.4), Write(answer, run_time=1.4))
        self.wait(0.8)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: unit rate × quantity = total (~7 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        general = make_equation_card(
            r"\text{total} = \text{unit rate} \times \text{quantity}",
            color=BLUE_TERM, scale=0.95,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in general:
            m.set_z_index(2)
        beat_3.add(general)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.2))
        self.wait(0.4)

        examples = VGroup(
            MathTex(r"\text{price: } \$/kg",  color=ORANGE_TERM).scale(0.75),
            MathTex(r"\text{wages: } \$/\text{hr}",  color=ORANGE_TERM).scale(0.75),
            MathTex(r"\text{fuel: } \text{c}/\text{km}", color=ORANGE_TERM).scale(0.75),
        ).arrange(RIGHT, buff=0.5)
        examples.next_to(general, DOWN, buff=0.45)
        ex_bg = BackgroundRectangle(examples, color=BLACK, fill_opacity=0.95, buff=0.18)
        ex_bg.move_to(examples.get_center())
        beat_3.add(examples, ex_bg)
        self.play(FadeIn(ex_bg, run_time=0.4), FadeIn(examples, run_time=1.2))
        self.wait(1.4)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Scale trick: lengths × n, areas × n², volumes × n³ (~7 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        wrong = MathTex(
            r"\text{scale } 1:2 \;\Rightarrow\; \text{area} \times 2 \text{?}",
            color=RED_REJECT,
        ).scale(0.85)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.9)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        beat_4.add(wrong, wrong_bg)
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.2))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4.add(cross)
        self.play(Create(cross, run_time=0.8))
        self.wait(0.4)

        right = MathTex(
            r"\text{lengths} \times n,\ \ \text{areas} \times n^{2},\ \ "
            r"\text{volumes} \times n^{3}",
            color=GREEN_OK,
        ).scale(0.7)
        right.next_to(wrong, DOWN, buff=0.45)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=1, buff=0.25)
        right_bg.move_to(right.get_center())
        beat_4.add(right, right_bg)
        self.play(FadeIn(right_bg, run_time=0.4), Write(right, run_time=1.4))
        self.wait(0.8)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"\text{total} = \text{rate} \times \text{quantity}",
            "Same rate, any quantity — scale up or down in proportion.",
            final_wait=122.2,
        )
