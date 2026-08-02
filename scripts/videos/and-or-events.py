"""
Manim scene for the lesson `and-or-events`
(topic `l9-p-relative-frequencies`).

For two events:
  "and"     → P(A) × P(B) (independent)
  inclusive "or"  → P(A) + P(B) - P(A and B)
  exclusive "or"  → P(A) + P(B) when A and B can't both happen.

Target duration: ~79.3 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class AndOrEventsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            '"And", inclusive "or", exclusive "or"',
            "Multiply for 'and'. Add, then subtract the overlap, for 'or'.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — "And" rule with concrete example (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text('"And" — both events occur', font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        rule = MathTex(
            r"\Pr(A \text{ and } B) \;\approx\; \Pr(A) \times \Pr(B)",
        ).scale(1.0)
        rule[0][0:6].set_color(BLUE_TERM)        # Pr(A and B)
        rule[0][10:13].set_color(BLUE_TERM)      # Pr(A
        rule[0][17:20].set_color(BLUE_TERM)      # Pr(B
        rule.move_to(BAND_CHART_CENTER + UP * 0.4)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.28)
        rule_bg.move_to(rule.get_center())

        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(rule_bg, run_time=0.4), Write(rule, run_time=1.6))
        self.wait(2.0)

        # Independence tag.
        indep = Text("for independent events", font_size=22, color=GREEN_OK)
        indep.next_to(rule, DOWN, buff=0.45)
        indep_bg = BackgroundRectangle(indep, color=BLACK, fill_opacity=0.95, buff=0.15)
        indep_bg.move_to(indep.get_center())
        self.play(FadeIn(indep_bg, run_time=0.4), FadeIn(indep, run_time=1.0))
        self.wait(3.0)

        # Concrete: 0.3 * 0.4 = 0.12.
        ex = MathTex(
            r"\Pr(\text{rain}) = 0.3,\; \Pr(\text{windy}) = 0.4 \;\Rightarrow\;"
            r"0.3 \times 0.4 = 0.12",
            color=ORANGE_TERM,
        ).scale(0.85)
        ex.move_to(BAND_CHART_CENTER + DOWN * 1.4)
        ex_bg = BackgroundRectangle(ex, color=BLACK, fill_opacity=1, buff=0.25)
        ex_bg.move_to(ex.get_center())
        self.play(FadeIn(ex_bg, run_time=0.4), FadeIn(ex, run_time=1.4))
        self.wait(4.0)

        self.play(
            FadeOut(VGroup(head, head_bg, rule, rule_bg, indep, indep_bg,
                           ex, ex_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Inclusive "or" rule with worked example (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text('Inclusive "or" — at least one', font_size=24, color=TEAL_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.7)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        rule2 = MathTex(
            r"\Pr(A \text{ or } B) \;\approx\; \Pr(A) + \Pr(B) - \Pr(A \text{ and } B)",
        ).scale(0.95)
        rule2.move_to(BAND_CHART_CENTER + UP * 0.4)
        rule2_bg = BackgroundRectangle(rule2, color=BLACK, fill_opacity=1, buff=0.28)
        rule2_bg.move_to(rule2.get_center())

        self.play(FadeIn(head2_bg, run_time=0.4), FadeIn(head2, run_time=1.0))
        self.wait(0.6)
        self.play(FadeIn(rule2_bg, run_time=0.4), Write(rule2, run_time=2.0))
        self.wait(2.0)

        # Why subtract the overlap.
        why = Text(
            "Subtract the overlap once — otherwise you'd count it twice.",
            font_size=22, color=ORANGE_TERM,
        ).next_to(rule2, DOWN, buff=0.5)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.2))
        self.wait(2.0)

        # Concrete: 0.5 + 0.3 - 0.1 = 0.7.
        ex2 = MathTex(
            r"0.5 + 0.3 - 0.1 = 0.7",
            color=GREEN_OK,
        ).scale(1.1)
        ex2.next_to(why, DOWN, buff=0.5)
        ex2_bg = BackgroundRectangle(ex2, color=BLACK, fill_opacity=1, buff=0.28)
        ex2_bg.move_to(ex2.get_center())
        self.play(FadeIn(ex2_bg, run_time=0.4), Write(ex2, run_time=1.4))
        self.wait(4.0)

        self.play(
            FadeOut(VGroup(head2, head2_bg, rule2, rule2_bg, why, why_bg,
                           ex2, ex2_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Exclusive "or": no overlap, just add (~12 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text('Exclusive "or" — one or the other, not both',
                     font_size=22, color=ORANGE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())

        rule3 = MathTex(
            r"\Pr(A \text{ xor } B) \;=\; \Pr(A) + \Pr(B) \quad (\Pr(A \text{ and } B) = 0)",
        ).scale(0.85)
        rule3.move_to(BAND_CHART_CENTER + UP * 0.4)
        rule3_bg = BackgroundRectangle(rule3, color=BLACK, fill_opacity=1, buff=0.25)
        rule3_bg.move_to(rule3.get_center())

        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(rule3_bg, run_time=0.4), Write(rule3, run_time=1.6))
        self.wait(2.5)

        # Concrete: 0.6 + 0.3 = 0.9.
        ex3 = MathTex(
            r"0.6 + 0.3 = 0.9",
            color=GREEN_OK,
        ).scale(1.1)
        ex3.next_to(rule3, DOWN, buff=0.5)
        ex3_bg = BackgroundRectangle(ex3, color=BLACK, fill_opacity=1, buff=0.28)
        ex3_bg.move_to(ex3.get_center())
        self.play(FadeIn(ex3_bg, run_time=0.4), Write(ex3, run_time=1.2))
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(head3, head3_bg, rule3, rule3_bg, ex3, ex3_bg),
                    run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 79.3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{And: multiply. Or: add then subtract the overlap.}",
            "Independent 'and' = P(A)·P(B). Mutually exclusive 'or' = P(A)+P(B).",
            final_wait=30.0,
        )
