"""
Manim scene for the lesson `real-number-operations`
(topic `l9-n-real-numbers`).

Real numbers are closed under +, -, *, / (except division by 0).
The animation shows the four operations, highlights the rule
"rational + irrational = irrational", and notes that irrational +
irrational can still be rational (e.g. sqrt(2) + (-sqrt(2)) = 0).

Render target: ~43 s audio + 20 s final wait.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class RealNumberOperationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Operating with real numbers",
            "Add, subtract, multiply, divide — and stay inside the reals.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: 1/2 + 1/3 = 5/6 (rational + rational = rational)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Rational + Rational = Rational",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.1)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.13)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.3), FadeIn(head, run_time=0.7))
        self.wait(0.4)

        ex = MathTex(
            r"\dfrac{1}{2} + \dfrac{1}{3} = \dfrac{5}{6}",
            color=GREEN_OK,
        ).scale(1.1)
        ex.move_to(BAND_CHART_CENTER + UP * 0.0)
        ex_bg = BackgroundRectangle(ex, color=BLACK, fill_opacity=1, buff=0.22)
        ex_bg.move_to(ex.get_center())
        self.play(FadeIn(ex_bg, run_time=0.4), Write(ex, run_time=1.3))
        self.wait(0.6)

        note = Text("still rational",
                    font_size=20, color=GREEN_OK)
        note.next_to(ex, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.13)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.3), FadeIn(note, run_time=0.7))
        self.wait(0.6)

        beat2 = beat_group(head, head_bg, ex, ex_bg, note, note_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: rational + irrational = irrational
        # ──────────────────────────────────────────────────────────────────
        rule = MathTex(
            r"\text{rational} + \text{irrational} \;=\; \text{irrational}",
            color=BLUE_TERM,
        ).scale(1.0)
        rule.move_to(BAND_CHART_CENTER + UP * 0.7)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.25)
        rule_bg.move_to(rule.get_center())
        self.play(FadeIn(rule_bg, run_time=0.4), Write(rule, run_time=1.3))
        self.wait(0.6)

        # Worked example: sqrt(2) + 3 is irrational.
        ex2 = MathTex(
            r"\sqrt{2} + 3 \;=\; \text{irrational}",
            color=ORANGE_TERM,
        ).scale(1.0)
        ex2.next_to(rule, DOWN, buff=0.5)
        ex2_bg = BackgroundRectangle(ex2, color=BLACK, fill_opacity=1, buff=0.22)
        ex2_bg.move_to(ex2.get_center())
        self.play(FadeIn(ex2_bg, run_time=0.4), Write(ex2, run_time=1.3))
        self.wait(0.6)

        # Why: a rational can't cancel an infinite decimal tail.
        why = Text("a clean fraction can't cancel the infinite tail",
                   font_size=20, color=BLUE_TERM)
        why.next_to(ex2, DOWN, buff=0.4)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.13)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.3), FadeIn(why, run_time=0.7))
        self.wait(0.6)

        beat3 = beat_group(rule, rule_bg, ex2, ex2_bg, why, why_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Contrast: irrational + irrational can be rational!
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Pitfall", font_size=24, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.1)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.13)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.3), FadeIn(head4, run_time=0.7))
        self.wait(0.4)

        ex_irr = MathTex(
            r"\sqrt{2} + (-\sqrt{2}) = 0",
            color=GREEN_OK,
        ).scale(1.1)
        ex_irr.move_to(BAND_CHART_CENTER + UP * 0.15)
        ex_irr_bg = BackgroundRectangle(ex_irr, color=BLACK, fill_opacity=1, buff=0.22)
        ex_irr_bg.move_to(ex_irr.get_center())
        self.play(FadeIn(ex_irr_bg, run_time=0.4), Write(ex_irr, run_time=1.2))
        self.wait(0.5)

        ex_irr2 = MathTex(
            r"\sqrt{2} + \sqrt{3} \;=\; \text{irrational}",
            color=RED_REJECT,
        ).scale(1.0)
        ex_irr2.next_to(ex_irr, DOWN, buff=0.45)
        ex_irr2_bg = BackgroundRectangle(ex_irr2, color=BLACK, fill_opacity=1, buff=0.22)
        ex_irr2_bg.move_to(ex_irr2.get_center())
        self.play(FadeIn(ex_irr2_bg, run_time=0.4), Write(ex_irr2, run_time=1.2))
        self.wait(0.6)

        beat4 = beat_group(
            head4, head4_bg, ex_irr, ex_irr_bg, ex_irr2, ex_irr2_bg,
        )
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"\text{Reals closed under } +,\ -,\ \times,\ \div",
            "Adding a non-zero rational to an irrational keeps it irrational.",
            final_wait=136.2,
        )
