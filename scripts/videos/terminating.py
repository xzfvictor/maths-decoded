"""
Manim scene for the lesson `terminating`
(topic `l8-n-fractions-decimals`).

A fraction p/q (in lowest terms) gives a terminating decimal iff the
prime factors of q are only 2s and 5s. Conversion is long division: work
through the remainders until one hits 0.

Target duration: ~90 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class TerminatingScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Fractions to terminating decimals",
            "Divide numerator by denominator — does the remainder reach 0?",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Worked long division: 3 / 8 = 0.375 (~16 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("3 / 8, step by step", font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
        )

        steps = [
            r"3.000 \div 8 = 0 \;\; \text{r} \; 3",
            r"30 \div 8 = 3 \;\; \text{r} \; 6",
            r"60 \div 8 = 7 \;\; \text{r} \; 4",
            r"40 \div 8 = 5 \;\; \text{r} \; 0",
        ]

        step_mobs = []
        anchor = head.get_center() + DOWN * 0.7
        # Stack them, each below the previous.
        for i, s in enumerate(steps):
            mob = MathTex(s, color=WHITE).scale(0.85)
            if i == 0:
                mob.move_to(anchor)
            else:
                mob.next_to(step_mobs[-1], DOWN, buff=0.18)
            mob_bg = BackgroundRectangle(mob, color=BLACK,
                                         fill_opacity=1, buff=0.15)
            mob_bg.move_to(mob.get_center())
            step_mobs.append(VGroup(mob_bg, mob))

            self.play(FadeIn(mob_bg, run_time=0.3), Write(mob, run_time=0.9))
            self.wait(0.5)

        # Final answer card.
        self.play(
            FadeOut(VGroup(head, head_bg), run_time=0.6),
        )
        for grp in step_mobs[:-1]:
            self.play(grp.animate.set_opacity(0.35), run_time=0.4)

        ans = MathTex(r"\dfrac{3}{8} \;=\; 0.375", color=GREEN_OK).scale(1.3)
        ans.move_to(BAND_CHART_CENTER + DOWN * 0.4)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.3)
        ans_bg.move_to(ans.get_center())
        self.play(
            FadeIn(ans_bg, run_time=0.4),
            Write(ans, run_time=1.6),
        )
        self.wait(3.0)

        self.play(
            FadeOut(VGroup(*step_mobs, ans, ans_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The rule + 9/40 = 0.225 (~16 s)
        # ──────────────────────────────────────────────────────────────────
        rule = MathTex(
            r"\dfrac{p}{q} \text{ terminates } \;\Leftrightarrow\;"
            r"q \text{ has only } 2\text{s and }5\text{s}",
            color=BLUE_TERM,
        ).scale(0.95)
        rule.move_to(BAND_CHART_CENTER + UP * 1.4)
        rule_bg = BackgroundRectangle(rule, color=BLACK,
                                      fill_opacity=1, buff=0.25)
        rule_bg.move_to(rule.get_center())

        self.play(
            FadeIn(rule_bg, run_time=0.5),
            Write(rule, run_time=2.0),
        )
        self.wait(3.5)

        # Decompose 40.
        decomp = MathTex(
            r"40 \;=\; 2^{3} \times 5 \;\;\Rightarrow\;\; \text{ terminates}",
            color=GREEN_OK,
        ).scale(1.0)
        decomp.next_to(rule, DOWN, buff=0.5)
        decomp_bg = BackgroundRectangle(decomp, color=BLACK,
                                        fill_opacity=1, buff=0.25)
        decomp_bg.move_to(decomp.get_center())

        self.play(
            FadeIn(decomp_bg, run_time=0.5),
            Write(decomp, run_time=1.5),
        )
        self.wait(2.5)

        # The result of 9/40.
        ans2 = MathTex(
            r"\dfrac{9}{40} \;=\; 0.225",
            color=GREEN_OK,
        ).scale(1.1)
        ans2.next_to(decomp, DOWN, buff=0.5)
        ans2_bg = BackgroundRectangle(ans2, color=BLACK,
                                       fill_opacity=1, buff=0.25)
        ans2_bg.move_to(ans2.get_center())

        self.play(
            FadeIn(ans2_bg, run_time=0.5),
            Write(ans2, run_time=1.4),
        )
        self.wait(3.0)

        self.play(
            FadeOut(VGroup(rule, rule_bg, decomp, decomp_bg, ans2, ans2_bg),
                    run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Contrast: 1/3 has factor 3 → NOT terminating (~14 s)
        # ──────────────────────────────────────────────────────────────────
        bad = make_equation_card(
            r"\dfrac{1}{3}",
            color=RED_REJECT, scale=1.2,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 1.0)

        no = Text(
            "q has factor 3 → does NOT terminate",
            font_size=22, color=RED_REJECT,
        )
        no.next_to(bad, DOWN, buff=0.4)
        no_bg = BackgroundRectangle(no, color=BLACK,
                                   fill_opacity=0.95, buff=0.15)
        no_bg.move_to(no.get_center())

        self.play(FadeIn(bad, shift=UP * 0.2, run_time=1.2))
        self.wait(2.0)
        self.play(
            FadeIn(no_bg, run_time=0.4),
            FadeIn(no, run_time=0.9),
        )
        self.wait(3.0)

        rec = MathTex(
            r"\dfrac{1}{3} \;=\; 0.\overline{3}",
            color=ORANGE_TERM,
        ).scale(1.1)
        rec.next_to(VGroup(bad, no, no_bg), DOWN, buff=0.5)
        rec_bg = BackgroundRectangle(rec, color=BLACK,
                                    fill_opacity=1, buff=0.25)
        rec_bg.move_to(rec.get_center())

        self.play(
            FadeIn(rec_bg, run_time=0.4),
            Write(rec, run_time=1.4),
        )
        self.wait(3.5)

        self.play(
            FadeOut(VGroup(bad, no, no_bg, rec, rec_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (total ≈ 90 s; final_wait = 35 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\dfrac{p}{q} \text{ terminates} \;\Leftrightarrow\;"
            r"q = 2^{k} \cdot 5^{m}",
            "Only prime factors 2 and 5 in the denominator.",
            final_wait=35.0,
        )
