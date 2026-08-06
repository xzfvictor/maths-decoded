"""
Manim scene for the lesson `and-or-events`
(topic `l9-p-relative-frequencies`).

For two events:
  "and"     → P(A) × P(B) (independent)
  inclusive "or"  → P(A) + P(B) - P(A and B)
  exclusive "or"  → P(A) + P(B) when A and B can't both happen.

Render target: ~20 s audio + 20 s final wait.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class AndOrEventsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            '"And", inclusive "or", exclusive "or"',
            "Multiply for 'and'. Add, then subtract the overlap, for 'or'.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — "And" rule with concrete example
        # ──────────────────────────────────────────────────────────────────
        head = Text('"And" — both events occur',
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.2)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.13)
        head_bg.move_to(head.get_center())

        rule = MathTex(
            r"\Pr(A \text{ and } B) \;\approx\; \Pr(A) \times \Pr(B)",
        ).scale(0.95)
        rule.move_to(BAND_CHART_CENTER + UP * 0.3)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.25)
        rule_bg.move_to(rule.get_center())

        self.play(FadeIn(head_bg, run_time=0.3), FadeIn(head, run_time=0.7))
        self.wait(0.4)
        self.play(FadeIn(rule_bg, run_time=0.3), Write(rule, run_time=1.4))
        self.wait(0.5)

        # Independence tag.
        indep = Text("for independent events", font_size=20, color=GREEN_OK)
        indep.next_to(rule, DOWN, buff=0.4)
        indep_bg = BackgroundRectangle(indep, color=BLACK, fill_opacity=0.95, buff=0.13)
        indep_bg.move_to(indep.get_center())
        self.play(FadeIn(indep_bg, run_time=0.3), FadeIn(indep, run_time=0.7))
        self.wait(0.5)

        # Concrete: 0.3 * 0.4 = 0.12.
        ex = MathTex(
            r"0.3 \times 0.4 = 0.12",
            color=ORANGE_TERM,
        ).scale(1.0)
        ex.next_to(indep, DOWN, buff=0.4)
        ex_bg = BackgroundRectangle(ex, color=BLACK, fill_opacity=1, buff=0.22)
        ex_bg.move_to(ex.get_center())
        self.play(FadeIn(ex_bg, run_time=0.3), Write(ex, run_time=1.0))
        self.wait(0.6)

        beat2 = beat_group(
            head, head_bg, rule, rule_bg, indep, indep_bg, ex, ex_bg,
        )
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Inclusive "or" rule with worked example
        # ──────────────────────────────────────────────────────────────────
        head2 = Text('Inclusive "or" — at least one',
                     font_size=24, color=TEAL_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.2)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.13)
        head2_bg.move_to(head2.get_center())

        rule2 = MathTex(
            r"\Pr(A \text{ or } B) \;\approx\; "
            r"\Pr(A) + \Pr(B) - \Pr(A \text{ and } B)",
        ).scale(0.85)
        rule2.move_to(BAND_CHART_CENTER + UP * 0.3)
        rule2_bg = BackgroundRectangle(rule2, color=BLACK, fill_opacity=1, buff=0.22)
        rule2_bg.move_to(rule2.get_center())

        self.play(FadeIn(head2_bg, run_time=0.3), FadeIn(head2, run_time=0.7))
        self.wait(0.4)
        self.play(FadeIn(rule2_bg, run_time=0.3), Write(rule2, run_time=1.5))
        self.wait(0.4)

        # Why subtract the overlap.
        why = Text(
            "Subtract the overlap once — otherwise you'd count it twice.",
            font_size=20, color=ORANGE_TERM,
        ).next_to(rule2, DOWN, buff=0.45)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.13)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.3), FadeIn(why, run_time=0.8))
        self.wait(0.5)

        # Concrete: 0.5 + 0.3 - 0.1 = 0.7.
        ex2 = MathTex(
            r"0.5 + 0.3 - 0.1 = 0.7",
            color=GREEN_OK,
        ).scale(1.0)
        ex2.next_to(why, DOWN, buff=0.4)
        ex2_bg = BackgroundRectangle(ex2, color=BLACK, fill_opacity=1, buff=0.22)
        ex2_bg.move_to(ex2.get_center())
        self.play(FadeIn(ex2_bg, run_time=0.3), Write(ex2, run_time=1.0))
        self.wait(0.6)

        beat3 = beat_group(
            head2, head2_bg, rule2, rule2_bg, why, why_bg, ex2, ex2_bg,
        )
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Exclusive "or": no overlap, just add
        # ──────────────────────────────────────────────────────────────────
        head3 = Text('Exclusive "or" — one or the other, not both',
                     font_size=22, color=ORANGE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.2)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.13)
        head3_bg.move_to(head3.get_center())

        rule3 = MathTex(
            r"\Pr(A \text{ xor } B) = \Pr(A) + \Pr(B)",
        ).scale(1.0)
        rule3.move_to(BAND_CHART_CENTER + UP * 0.3)
        rule3_bg = BackgroundRectangle(rule3, color=BLACK, fill_opacity=1, buff=0.22)
        rule3_bg.move_to(rule3.get_center())

        self.play(FadeIn(head3_bg, run_time=0.3), FadeIn(head3, run_time=0.7))
        self.wait(0.3)
        self.play(FadeIn(rule3_bg, run_time=0.3), Write(rule3, run_time=1.2))
        self.wait(0.4)

        cond = Text("when events cannot both happen (overlap = 0)",
                    font_size=20, color=TEAL_TERM)
        cond.next_to(rule3, DOWN, buff=0.4)
        cond_bg = BackgroundRectangle(cond, color=BLACK, fill_opacity=0.95, buff=0.13)
        cond_bg.move_to(cond.get_center())
        self.play(FadeIn(cond_bg, run_time=0.3), FadeIn(cond, run_time=0.7))
        self.wait(0.5)

        # Concrete: 0.6 + 0.3 = 0.9.
        ex3 = MathTex(
            r"0.6 + 0.3 = 0.9",
            color=GREEN_OK,
        ).scale(1.0)
        ex3.next_to(cond, DOWN, buff=0.4)
        ex3_bg = BackgroundRectangle(ex3, color=BLACK, fill_opacity=1, buff=0.22)
        ex3_bg.move_to(ex3.get_center())
        self.play(FadeIn(ex3_bg, run_time=0.3), Write(ex3, run_time=0.9))
        self.wait(0.5)

        beat4 = beat_group(
            head3, head3_bg, rule3, rule3_bg, cond, cond_bg, ex3, ex3_bg,
        )
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{And: multiply. Or: add, then subtract the overlap.}",
            "Independent 'and' = P(A)·P(B). Exclusive 'or' = P(A)+P(B).",
            final_wait=20.0,
        )
