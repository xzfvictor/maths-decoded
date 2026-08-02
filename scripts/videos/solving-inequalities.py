"""
Manim scene for the lesson `solving-inequalities`
(topic `l8-a-linear-equations-inequalities`).

Solving one-variable inequalities is like solving equations, with one
critical twist: if you divide or multiply both sides by a negative,
the inequality sign flips. The scene walks through a positive-divide
case (no flip), then the negative-divide case with a visually striking
sign-flip animation.

Target duration: ~87 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, YELLOW_HIGHLIGHT, make_term_card, make_equation_card,
    animate_intro, animate_final_definition, beat_group,
)
from manim import *


class SolvingInequalitiesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Solving inequalities",
            "Same as equations — except when you divide by a negative.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Positive divisor: 2x + 3 < 11 → x < 4 (no flip, ~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        start_card = make_equation_card("2x + 3 < 11", color=BLUE_TERM, scale=1.1)
        start_card.move_to(BAND_CHART_CENTER + UP * 1.0)
        for m in start_card:
            m.set_z_index(2)
        self.play(FadeIn(start_card, run_time=1.4))
        self.wait(2.0)

        note1 = Text("Subtract 3 from both sides", font_size=22, color=BLUE_TERM)
        note1.next_to(start_card, DOWN, buff=0.5)
        note1_bg = BackgroundRectangle(note1, color=BLACK, fill_opacity=0.95, buff=0.15)
        note1_bg.move_to(note1.get_center())
        self.play(FadeIn(note1_bg, run_time=0.4), FadeIn(note1, run_time=0.9))
        self.wait(1.5)

        step1 = make_equation_card("2x < 8", color=BLUE_TERM, scale=1.1)
        step1.move_to(BAND_CHART_CENTER + UP * 1.0)
        for m in step1:
            m.set_z_index(2)
        self.play(Transform(start_card, step1, run_time=1.5))
        self.wait(2.0)

        note2 = Text("Divide by 2 — positive, so NO flip", font_size=22, color=GREEN_OK)
        note2.next_to(start_card, DOWN, buff=0.5)
        note2_bg = BackgroundRectangle(note2, color=BLACK, fill_opacity=0.95, buff=0.15)
        note2_bg.move_to(note2.get_center())

        step2 = make_equation_card("x < 4", color=GREEN_OK, scale=1.1)
        step2.move_to(BAND_CHART_CENTER + UP * 1.0)
        for m in step2:
            m.set_z_index(2)

        self.play(
            FadeOut(VGroup(note1, note1_bg), run_time=0.6),
            FadeIn(note2_bg, run_time=0.4),
            FadeIn(note2, run_time=0.9),
        )
        self.wait(1.0)
        self.play(Transform(start_card, step2, run_time=1.5))
        self.wait(2.0)
        self.play(Indicate(start_card, color=GREEN_OK, scale_factor=1.06), run_time=1.5)
        self.wait(2.0)

        beat_2.add(start_card, note2, note2_bg)
        self.play(FadeOut(beat_2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Negative divisor: -2x + 3 ≤ 9 → x ≥ -3 (FLIP, ~36 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        neg_start = make_equation_card(r"-2x + 3 \leq 9", color=BLUE_TERM, scale=1.1)
        neg_start.move_to(BAND_CHART_CENTER + UP * 1.4)
        for m in neg_start:
            m.set_z_index(2)
        self.play(FadeIn(neg_start, run_time=1.4))
        self.wait(2.0)

        neg_step1 = make_equation_card(r"-2x \leq 6", color=BLUE_TERM, scale=1.1)
        neg_step1.move_to(BAND_CHART_CENTER + UP * 1.4)
        for m in neg_step1:
            m.set_z_index(2)
        self.play(Transform(neg_start, neg_step1, run_time=1.5))
        self.wait(1.5)

        # Show "÷ (-2)" big label below the equation and the sign-flip
        # visual further down to avoid overlap with the equation.
        divider = Text("÷ (-2)", font_size=28, color=YELLOW_HIGHLIGHT)
        divider.move_to(BAND_CHART_CENTER + UP * 0.0)
        divider_bg = BackgroundRectangle(divider, color=BLACK, fill_opacity=1, buff=0.2)
        divider_bg.move_to(divider.get_center())

        sign_pair = VGroup(
            MathTex(r"\leq", color=RED_REJECT).scale(1.6),
            MathTex(r"\Rightarrow", color=WHITE).scale(1.1),
            MathTex(r"\geq", color=GREEN_OK).scale(1.6),
        ).arrange(RIGHT, buff=0.5)
        sign_pair.move_to(BAND_CHART_CENTER + DOWN * 1.1)
        sign_bg = BackgroundRectangle(sign_pair, color=BLACK, fill_opacity=1, buff=0.3)
        sign_bg.move_to(sign_pair.get_center())

        self.play(
            FadeIn(divider_bg, run_time=0.5),
            FadeIn(divider, run_time=1.0),
            FadeIn(sign_bg, run_time=0.5),
            FadeIn(sign_pair, run_time=1.2),
        )
        self.wait(2.0)

        cross_sign = Cross(sign_pair[0], color=RED_REJECT, stroke_width=6)
        self.play(Create(cross_sign, run_time=1.0))
        self.play(
            Indicate(sign_pair[2], color=GREEN_OK, scale_factor=1.25),
            run_time=2.0,
        )
        self.wait(1.5)

        flip_note = Text(
            "Sign FLIPS — because we divided by a NEGATIVE",
            font_size=20,
            color=YELLOW_HIGHLIGHT,
        )
        flip_note.next_to(neg_start, DOWN, buff=0.45)
        flip_note_bg = BackgroundRectangle(flip_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        flip_note_bg.move_to(flip_note.get_center())
        self.play(FadeIn(flip_note_bg, run_time=0.4), FadeIn(flip_note, run_time=1.0))
        self.wait(2.5)

        result = make_equation_card(r"x \geq -3", color=GREEN_OK, scale=1.3)
        result.move_to(BAND_CHART_CENTER + UP * 1.4)
        for m in result:
            m.set_z_index(2)

        self.play(
            FadeOut(divider, run_time=0.8),
            FadeOut(divider_bg, run_time=0.8),
            FadeOut(sign_pair, run_time=0.8),
            FadeOut(sign_bg, run_time=0.8),
            FadeOut(cross_sign, run_time=0.8),
            FadeOut(flip_note, run_time=0.8),
            FadeOut(flip_note_bg, run_time=0.8),
            FadeOut(neg_start, run_time=0.8),
        )
        self.play(FadeIn(result, run_time=1.5))
        self.wait(2.0)
        self.play(Indicate(result, color=GREEN_OK, scale_factor=1.08), run_time=1.5)
        self.wait(2.0)

        beat_3.add(result)
        self.play(FadeOut(beat_3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Final takeaway (~18 s, total ≈ 87 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"(-2) \cdot x \;\Rightarrow\; \text{flip}",
            "Dividing by a negative flips the inequality sign.",
            final_wait=29.0,
        )