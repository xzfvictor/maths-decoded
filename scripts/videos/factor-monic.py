"""
Manim scene for the lesson `factor-monic`
(topic `l10a-aa-factorising-quadratics`).

Factorise a monic quadratic x^2 + bx + c by finding two numbers m, n
with m + n = b and m * n = c. The animation walks through x^2 + 7x + 12,
shows the rule, and rejects the mistake of swapping the column
("two numbers that add to c and multiply to b").

Target duration: ~86.6 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class FactorMonicScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Factorising monic quadratics",
            "Find two numbers whose sum is b and product is c.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: x^2 + 7x + 12 = (x + 3)(x + 4) (~26 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Find two numbers: sum = 7, product = 12",
                    font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        # Show the original quadratic.
        pq = MathTex(r"x^{2} + 7x + 12", color=BLUE_TERM).scale(1.3)
        pq.move_to(BAND_CHART_CENTER + UP * 0.5)
        pq_bg = BackgroundRectangle(pq, color=BLACK, fill_opacity=1, buff=0.3)
        pq_bg.move_to(pq.get_center())
        beat_2 = beat_group(beat_2, pq, pq_bg)
        self.play(FadeIn(pq_bg, run_time=0.4), Write(pq, run_time=1.6))
        self.wait(1.0)

        # Highlight b = 7 and c = 12.
        b_note = Text("b = 7  (the x-coefficient)", font_size=22, color=ORANGE_TERM)
        b_note.next_to(pq, DOWN, buff=0.5)
        b_note_bg = BackgroundRectangle(b_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        b_note_bg.move_to(b_note.get_center())
        beat_2 = beat_group(beat_2, b_note, b_note_bg)
        self.play(FadeIn(b_note_bg, run_time=0.3), FadeIn(b_note, run_time=1.0))
        self.wait(0.5)

        c_note = Text("c = 12  (the constant)", font_size=22, color=TEAL_TERM)
        c_note.next_to(b_note, DOWN, buff=0.3)
        c_note_bg = BackgroundRectangle(c_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        c_note_bg.move_to(c_note.get_center())
        beat_2 = beat_group(beat_2, c_note, c_note_bg)
        self.play(FadeIn(c_note_bg, run_time=0.3), FadeIn(c_note, run_time=1.0))
        self.wait(1.0)

        # The two numbers: 3 and 4.
        found = MathTex(
            r"3 + 4 = 7,\quad 3 \cdot 4 = 12",
            color=GREEN_OK,
        ).scale(1.0)
        found.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        found_bg = BackgroundRectangle(found, color=BLACK, fill_opacity=1, buff=0.25)
        found_bg.move_to(found.get_center())
        beat_2 = beat_group(beat_2, found, found_bg)
        self.play(FadeIn(found_bg, run_time=0.4), Write(found, run_time=1.6))
        self.wait(1.5)

        # Clear the working stack before the final factorisation so the
        # answer card remains inside the chart band without touching notes.
        working = beat_group(pq, pq_bg, b_note, b_note_bg, c_note, c_note_bg, found, found_bg)
        self.play(FadeOut(working, run_time=0.5))
        self.wait(0.2)

        # The factorisation.
        ans = MathTex(
            r"x^{2} + 7x + 12 = (x + 3)(x + 4)",
            color=GREEN_OK,
        ).scale(1.2)
        ans.move_to(BAND_CHART_CENTER + DOWN * 0.2)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.3)
        ans_bg.move_to(ans.get_center())
        beat_2 = beat_group(beat_2, ans, ans_bg)
        self.play(FadeIn(ans_bg, run_time=0.4), Write(ans, run_time=1.8))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The general rule (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head3 = Text("General rule", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        beat_3 = beat_group(beat_3, head3, head3_bg)
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        rule = MathTex(
            r"x^{2} + bx + c = (x + m)(x + n),\quad m + n = b,\; mn = c",
            color=BLUE_TERM,
        ).scale(0.9)
        rule.move_to(BAND_CHART_CENTER + UP * 0.5)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.25)
        rule_bg.move_to(rule.get_center())
        beat_3 = beat_group(beat_3, rule, rule_bg)
        self.play(FadeIn(rule_bg, run_time=0.4), Write(rule, run_time=2.0))
        self.wait(1.5)

        # Sign tip.
        tip = Text(
            "If c > 0, m and n share the sign of b. If c < 0, they have opposite signs.",
            font_size=22, color=ORANGE_TERM,
        ).next_to(rule, DOWN, buff=0.5)
        tip_bg = BackgroundRectangle(tip, color=BLACK, fill_opacity=0.95, buff=0.15)
        tip_bg.move_to(tip.get_center())
        beat_3 = beat_group(beat_3, tip, tip_bg)
        self.play(FadeIn(tip_bg, run_time=0.3), FadeIn(tip, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: swap m + n with mn (~16 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\text{find two numbers: sum = 12, product = 7?}",
            color=RED_REJECT,
        ).scale(0.95)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.6),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        fix = Text(
            "Sum goes with b, product goes with c — never swap.",
            font_size=22, color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        beat_4 = beat_group(beat_4, fix, fix_bg)
        self.play(FadeIn(fix_bg, run_time=0.3), FadeIn(fix, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=39 s, total ≈ 86.6 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"x^{2} + bx + c = (x + m)(x + n)\ \text{ when } m + n = b,\ mn = c",
            "Hunt for two numbers — sum gives b, product gives c.",
            final_wait=39.0,
        )
