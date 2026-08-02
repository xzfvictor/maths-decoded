"""
Manim scene for the lesson `zero-and-negative`
(topic `l9-a-exponent-laws-variables`).

Zero exponent: a^0 = 1 for any non-zero a (with variables too).
Negative exponent: a^(-n) = 1/a^n flips the term upside down.

Target duration: ~95 s (matches the audio narration length of 95.36 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ZeroAndNegativeScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Zero and negative exponents",
            "a^0 = 1,  and  a^(-n) = 1 / a^n",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Why a^0 = 1: a^n / a^n = 1 but also a^(n-n) = a^0 (~18 s)
        # ──────────────────────────────────────────────────────────────────
        line1 = MathTex(r"\dfrac{a^{n}}{a^{n}} \;=\; 1", color=BLUE_TERM).scale(1.1)
        line1.move_to(BAND_CHART_CENTER + UP * 1.4)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=1, buff=0.25)
        line1_bg.move_to(line1.get_center())

        self.play(
            FadeIn(line1_bg, run_time=0.4),
            Write(line1, run_time=1.6),
        )
        self.wait(2.5)

        line2 = MathTex(
            r"\dfrac{a^{n}}{a^{n}} \;=\; a^{\,n - n} \;=\; a^{0}",
            color=TEAL_TERM,
        ).scale(1.05)
        line2.next_to(line1, DOWN, buff=0.5)
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=1, buff=0.25)
        line2_bg.move_to(line2.get_center())

        self.play(
            FadeIn(line2_bg, run_time=0.4),
            Write(line2, run_time=1.6),
        )
        self.wait(3.0)

        line3 = MathTex(
            r"\therefore \; a^{0} \;=\; 1 \quad (\text{for } a \neq 0)",
            color=GREEN_OK,
        ).scale(1.1)
        line3.next_to(line2, DOWN, buff=0.5)
        line3_bg = BackgroundRectangle(line3, color=BLACK, fill_opacity=1, buff=0.25)
        line3_bg.move_to(line3.get_center())

        self.play(
            FadeIn(line3_bg, run_time=0.4),
            Write(line3, run_time=1.6),
        )
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(line1, line1_bg, line2, line2_bg, line3, line3_bg),
                    run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Variables example: (x^2 + 1)^0 = 1 (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Even with variables — anything non-zero to the 0 is 1:",
                    font_size=22, color=WHITE)
        head.move_to(BAND_CHART_CENTER + UP * 1.4)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        eq1 = make_equation_card(r"x^{0} = 1", color=GREEN_OK, scale=1.0)
        eq1.move_to(BAND_CHART_CENTER + UP * 0.4)
        eq2 = make_equation_card(r"(x^{2} + 1)^{0} = 1", color=GREEN_OK, scale=1.0)
        eq2.move_to(BAND_CHART_CENTER + DOWN * 0.5)

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
        )
        self.wait(1.5)
        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.0))
        self.wait(1.5)
        self.play(FadeIn(eq2, shift=UP * 0.2, run_time=1.0))
        self.wait(3.5)

        self.play(
            FadeOut(VGroup(head, head_bg, eq1, eq2), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Negative exponent: a^(-n) = 1 / a^n (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("Negative exponent flips the term upside down:",
                     font_size=22, color=WHITE)
        head2.move_to(BAND_CHART_CENTER + UP * 1.4)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        rule = make_equation_card(
            r"a^{-n} \;=\; \dfrac{1}{a^{n}}",
            color=ORANGE_TERM, scale=1.1,
        )
        rule.move_to(BAND_CHART_CENTER + UP * 0.2)

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=1.0),
        )
        self.wait(1.5)
        self.play(FadeIn(rule, shift=UP * 0.2, run_time=1.4))
        self.wait(3.0)

        self.play(
            FadeOut(VGroup(head2, head2_bg, rule), run_time=1.2),
        )

        # Apply: x^(-3) = 1 / x^3.
        ex = make_equation_card(r"x^{-3} \;=\; \dfrac{1}{x^{3}}", color=GREEN_OK, scale=1.1)
        ex.move_to(BAND_CHART_CENTER + UP * 0.4)

        note = Text(
            "Same rule with variables: the reciprocal appears.",
            font_size=22, color=GREEN_OK,
        ).next_to(ex, DOWN, buff=0.45)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())

        self.play(FadeIn(ex, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(ex, note, note_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~37 s, total ≈ 95 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{0} \;=\; 1, \quad a^{-n} \;=\; \dfrac{1}{a^{n}} \quad (\text{for } a \neq 0)",
            "Zero exponent → 1; negative exponent → reciprocal.",
            final_wait=36.0,
        )