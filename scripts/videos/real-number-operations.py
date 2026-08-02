"""
Manim scene for the lesson `real-number-operations`
(topic `l9-n-real-numbers`).

Real numbers are closed under +, -, *, /. The animation shows the four
operations with concrete examples, highlights the rule "rational + irrational
= irrational", and rejects the misconception that 1.41421356... is just an
approximation we can round away.

Target duration: ~102.4 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class RealNumberOperationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Operating with real numbers",
            "Add, subtract, multiply, divide — and stay inside the reals.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: the four operations (~24 s)
        # ──────────────────────────────────────────────────────────────────
        ops = VGroup(
            make_term_card(r"3 + \sqrt{2}", "sum", BLUE_TERM),
            make_term_card(r"5 - \sqrt{2}", "difference", TEAL_TERM),
            make_term_card(r"2 \cdot \sqrt{3}", "product", ORANGE_TERM),
            make_term_card(r"\dfrac{\sqrt{8}}{2}", "quotient", GREEN_OK),
        ).arrange(RIGHT, buff=0.5)
        ops.move_to(BAND_CHART_CENTER + UP * 0.3)
        for o in ops:
            o.set_z_index(2)

        # Reveal in pairs.
        self.play(FadeIn(ops[0], shift=UP * 0.2, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(ops[1], shift=UP * 0.2, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(ops[2], shift=UP * 0.2, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(ops[3], shift=UP * 0.2, run_time=1.0))
        self.wait(3.0)

        # Common-result statement.
        note = Text(
            "All four results are still real numbers.",
            font_size=22, color=GREEN_OK,
        ).next_to(ops, DOWN, buff=0.6)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.2))
        self.wait(4.0)

        self.play(
            FadeOut(VGroup(ops, note, note_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: closed under + - * / (~18 s)
        # ──────────────────────────────────────────────────────────────────
        closed = MathTex(
            r"\text{Reals are closed under } +,\ -,\ \times,\ \div",
        ).scale(1.0)
        closed.move_to(BAND_CHART_CENTER + UP * 1.2)
        closed_bg = BackgroundRectangle(closed, color=BLACK, fill_opacity=1, buff=0.28)
        closed_bg.move_to(closed.get_center())
        self.play(FadeIn(closed_bg, run_time=0.4), Write(closed, run_time=2.0))
        self.wait(3.0)

        # The caveat.
        caveat = Text(
            "...as long as the divisor isn't zero.",
            font_size=22, color=ORANGE_TERM,
        ).next_to(closed, DOWN, buff=0.5)
        caveat_bg = BackgroundRectangle(caveat, color=BLACK, fill_opacity=0.95, buff=0.18)
        caveat_bg.move_to(caveat.get_center())
        self.play(FadeIn(caveat_bg, run_time=0.4), FadeIn(caveat, run_time=1.2))
        self.wait(3.0)

        self.play(
            FadeOut(VGroup(closed, closed_bg, caveat, caveat_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Key rule: rational + irrational = irrational (~20 s)
        # ──────────────────────────────────────────────────────────────────
        rule = make_equation_card(
            r"\text{rational} + \text{irrational} = \text{irrational}",
            color=GREEN_OK, scale=1.0,
        )
        rule.move_to(BAND_CHART_CENTER + UP * 0.7)
        self.play(FadeIn(rule, shift=UP * 0.2, run_time=1.4))
        self.wait(3.0)

        # Worked example: 3 + pi is irrational.
        ex = MathTex(
            r"3 + \pi \;=\; \text{irrational}",
            color=ORANGE_TERM,
        ).scale(1.0)
        ex.next_to(rule, DOWN, buff=0.6)
        ex_bg = BackgroundRectangle(ex, color=BLACK, fill_opacity=1, buff=0.25)
        ex_bg.move_to(ex.get_center())
        self.play(FadeIn(ex_bg, run_time=0.4), Write(ex, run_time=1.6))
        self.wait(3.0)

        # Pitfall call-out: irrational + irrational can still be rational!
        pit = Text(
            "Pitfall: irrational + irrational CAN be rational.",
            font_size=22, color=RED_REJECT,
        ).next_to(ex, DOWN, buff=0.5)
        pit_bg = BackgroundRectangle(pit, color=BLACK, fill_opacity=0.95, buff=0.18)
        pit_bg.move_to(pit.get_center())
        self.play(FadeIn(pit_bg, run_time=0.4), FadeIn(pit, run_time=1.4))
        self.wait(5.0)

        self.play(
            FadeOut(VGroup(rule, ex, ex_bg, pit, pit_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 102.4 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Reals closed under } +,\ -,\ \times,\ \div",
            "Adding a non-zero rational to an irrational keeps it irrational.",
            final_wait=39.0,
        )
