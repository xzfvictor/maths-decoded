"""
Manim scene for the lesson `plan-investigation`
(topic `l9-st-statistical-investigations`).

A statistical investigation is a cycle: question → population → sampling
→ collection → analysis → conclusion. Doing the steps in order avoids the
"collect first, decide what to ask later" trap.

Target duration: ~80 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class PlanInvestigationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Planning a statistical investigation",
            "Question → sample → collect → analyse → communicate.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Pose the question first (~18 s)
        # ──────────────────────────────────────────────────────────────────
        # Card 1: Question.
        q_card = make_term_card(
            "\\text{Pose a question}",
            "something answerable with data",
            BLUE_TERM,
        )
        q_card.move_to(BAND_CHART_CENTER + UP * 0.5)
        q_card.set_z_index(2)

        self.play(FadeIn(q_card, shift=UP * 0.2, run_time=1.2))
        self.wait(2.5)

        wrong = Text(
            "Don't collect first — ask first.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(q_card, DOWN, buff=0.5)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=0.95, buff=0.18)
        wrong_bg.move_to(wrong.get_center())
        self.play(FadeIn(wrong_bg, run_time=0.5), FadeIn(wrong, run_time=1.2))
        self.wait(5.0)
        self.play(
            FadeOut(q_card, run_time=1.0),
            FadeOut(VGroup(wrong, wrong_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Population, sampling method, variables (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Three step-cards on a horizontal row.
        step1 = make_term_card(
            "\\text{Population}",
            "the group you care about",
            BLUE_TERM,
        )
        step2 = make_term_card(
            "\\text{Sampling method}",
            "random? stratified?",
            TEAL_TERM,
        )
        step3 = make_term_card(
            "\\text{Variables}",
            "what you measure",
            ORANGE_TERM,
        )
        row = VGroup(step1, step2, step3).arrange(RIGHT, buff=0.4)
        row.move_to(BAND_CHART_CENTER + UP * 0.4)
        for c in row:
            c.set_z_index(2)

        self.play(FadeIn(step1, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(step2, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(step3, shift=UP * 0.2, run_time=1.0))
        self.wait(3.0)

        warn = Text(
            "Pick the population and method BEFORE collecting.",
            font_size=22,
            color=TEAL_TERM,
        ).next_to(row, DOWN, buff=0.5)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.18)
        warn_bg.move_to(warn.get_center())
        self.play(FadeIn(warn_bg, run_time=0.5), FadeIn(warn, run_time=1.2))
        self.wait(7.0)
        self.play(
            FadeOut(row, run_time=1.0),
            FadeOut(VGroup(warn, warn_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Collect, analyse, interpret, communicate (~18 s)
        # ──────────────────────────────────────────────────────────────────
        # Two paired cards.
        c1 = make_term_card(
            "\\text{Collect}",
            "carefully and honestly",
            BLUE_TERM,
        )
        c2 = make_term_card(
            "\\text{Analyse}",
            "displays + summary stats",
            TEAL_TERM,
        )
        c3 = make_term_card(
            "\\text{Communicate}",
            "result + limitations",
            GREEN_OK,
        )
        row2 = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.4)
        row2.move_to(BAND_CHART_CENTER + UP * 0.5)
        for c in row2:
            c.set_z_index(2)

        self.play(FadeIn(c1, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(c2, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(c3, shift=UP * 0.2, run_time=1.0))
        self.wait(2.5)

        note = Text(
            "Don't claim more than the data supports.",
            font_size=22,
            color=YELLOW,
        ).next_to(row2, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.5), FadeIn(note, run_time=1.2))
        self.wait(5.0)
        self.play(
            FadeOut(row2, run_time=1.0),
            FadeOut(VGroup(note, note_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (total ≈ 80 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Question} \to \text{Sample} \to \text{Analyse}",
            "Plan first, then collect — never the other way around.",
            final_wait=30.0,
        )
