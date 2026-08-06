"""
Manim scene for the lesson `plan-investigation`
(topic `l9-st-statistical-investigations`).

A statistical investigation is a cycle: question → population → sampling
→ collection → analysis → conclusion. Doing the steps in order avoids
the "collect first, decide what to ask later" trap.

Render target: ~70-80 s, final_wait=52.9 s.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class PlanInvestigationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Planning a statistical investigation",
            "Question → sample → collect → analyse → communicate.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Pose the question first
        # ──────────────────────────────────────────────────────────────────
        q_card = make_term_card(
            r"\text{Pose a question}",
            "something answerable with data",
            BLUE_TERM,
        )
        q_card.move_to(BAND_CHART_CENTER + UP * 0.5)
        q_card.set_z_index(2)

        self.play(FadeIn(q_card, shift=UP * 0.2, run_time=1.0))
        self.wait(1.0)

        ask_first = Text(
            "Ask first — don't collect first.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(q_card, DOWN, buff=0.5)
        ask_bg = BackgroundRectangle(ask_first, color=BLACK, fill_opacity=0.95, buff=0.18)
        ask_bg.move_to(ask_first.get_center())
        self.play(FadeIn(ask_bg, run_time=0.5), FadeIn(ask_first, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(beat_group(q_card, ask_first, ask_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Population, sampling method, variables
        # ──────────────────────────────────────────────────────────────────
        step1 = make_term_card(
            r"\text{Population}",
            "the group you care about",
            BLUE_TERM,
        )
        step2 = make_term_card(
            r"\text{Sampling method}",
            "random? stratified?",
            TEAL_TERM,
        )
        step3 = make_term_card(
            r"\text{Variables}",
            "what you measure",
            ORANGE_TERM,
        )
        row = VGroup(step1, step2, step3).arrange(RIGHT, buff=0.4)
        row.move_to(BAND_CHART_CENTER + UP * 0.4)
        for c in row:
            c.set_z_index(2)

        self.play(FadeIn(step1, shift=UP * 0.2, run_time=0.8))
        self.play(FadeIn(step2, shift=UP * 0.2, run_time=0.8))
        self.play(FadeIn(step3, shift=UP * 0.2, run_time=0.8))
        self.wait(1.0)

        warn = Text(
            "Pick the population and method BEFORE collecting.",
            font_size=22,
            color=TEAL_TERM,
        ).next_to(row, DOWN, buff=0.5)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.18)
        warn_bg.move_to(warn.get_center())
        self.play(FadeIn(warn_bg, run_time=0.5), FadeIn(warn, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(beat_group(row, warn, warn_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Collect, analyse, communicate
        # ──────────────────────────────────────────────────────────────────
        c1 = make_term_card(
            r"\text{Collect}",
            "carefully and honestly",
            BLUE_TERM,
        )
        c2 = make_term_card(
            r"\text{Analyse}",
            "displays + summary stats",
            TEAL_TERM,
        )
        c3 = make_term_card(
            r"\text{Communicate}",
            "result + limitations",
            GREEN_OK,
        )
        row2 = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.4)
        row2.move_to(BAND_CHART_CENTER + UP * 0.5)
        for c in row2:
            c.set_z_index(2)

        self.play(FadeIn(c1, shift=UP * 0.2, run_time=0.8))
        self.play(FadeIn(c2, shift=UP * 0.2, run_time=0.8))
        self.play(FadeIn(c3, shift=UP * 0.2, run_time=0.8))
        self.wait(1.0)

        note = Text(
            "Don't claim more than the data supports.",
            font_size=22,
            color=YELLOW,
        ).next_to(row2, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.5), FadeIn(note, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(beat_group(row2, note, note_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"\text{Question} \to \text{Sample} \to \text{Analyse}",
            "Plan first, then collect — never the other way around.",
            final_wait=52.9,
        )
