"""
Manim scene for the lesson `making-conjectures`
(topic `l8-a-linear-functions-relations`).

A conjecture is a guess. Test it on new data; a single counter-example
disproves it.

Target duration: ~79 s (matches audio).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro, animate_final_definition,
)
from manim import *


class MakingConjecturesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Making and testing conjectures",
            "Guess the rule. Test it. One counter-example kills it.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Spot the pattern (~20 s)
        # ──────────────────────────────────────────────────────────────────
        intro = Text("From a table, find the rule.", font_size=22, color=BLUE_TERM)
        intro.move_to(BAND_CHART_CENTER + UP * 1.5)
        intro_bg = BackgroundRectangle(intro, color=BLACK, fill_opacity=0.95, buff=0.18)
        intro_bg.move_to(intro.get_center())
        self.play(FadeIn(intro_bg, run_time=0.4), FadeIn(intro, run_time=1.2))
        self.wait(2.0)

        # Build a small table: x, y, diff
        table = VGroup(
            Text("x", font_size=22, color=WHITE),
            Text("1", font_size=22, color=BLUE_TERM),
            Text("2", font_size=22, color=BLUE_TERM),
            Text("3", font_size=22, color=BLUE_TERM),
            Text("4", font_size=22, color=BLUE_TERM),
        ).arrange(RIGHT, buff=0.7)
        table.move_to(BAND_CHART_CENTER + UP * 0.4)
        row2 = VGroup(
            Text("y", font_size=22, color=WHITE),
            Text("5", font_size=22, color=GREEN_OK),
            Text("8", font_size=22, color=GREEN_OK),
            Text("11", font_size=22, color=GREEN_OK),
            Text("14", font_size=22, color=GREEN_OK),
        ).arrange(RIGHT, buff=0.7)
        row2.next_to(table, DOWN, buff=0.4)
        for r in [table, row2]:
            for c in r:
                c.bg = BackgroundRectangle(c, color=BLACK, fill_opacity=0.9, buff=0.1)
                c.bg.move_to(c.get_center())
        for c in table:
            self.play(FadeIn(c.bg, run_time=0.2), FadeIn(c, run_time=0.4))
        self.wait(0.5)
        for c in row2:
            self.play(FadeIn(c.bg, run_time=0.2), FadeIn(c, run_time=0.4))
        self.wait(2.0)

        # Conjecture.
        conj = MathTex(r"y \;=\; 3x + 2", color=GREEN_OK).scale(1.2)
        conj.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        conj_bg = BackgroundRectangle(conj, color=BLACK, fill_opacity=1, buff=0.3)
        conj_bg.move_to(conj.get_center())
        conj_box = SurroundingRectangle(conj, color=GREEN_OK, buff=0.3, stroke_width=3)
        self.play(
            FadeOut(VGroup(intro, intro_bg), run_time=0.6),
        )
        self.play(FadeIn(conj_bg, run_time=0.5), Write(conj, run_time=1.6))
        self.play(Create(conj_box, run_time=1.0))
        self.wait(3.0)
        self.play(
            FadeOut(VGroup(table, *[c.bg for c in table]), run_time=0.8),
            FadeOut(VGroup(row2, *[c.bg for c in row2]), run_time=0.8),
            FadeOut(VGroup(conj, conj_bg, conj_box), run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Test the conjecture (~22 s)
        # ──────────────────────────────────────────────────────────────────
        test_intro = Text("Test on x = 5", font_size=22, color=BLUE_TERM)
        test_intro.move_to(BAND_CHART_CENTER + UP * 1.5)
        test_intro_bg = BackgroundRectangle(test_intro, color=BLACK, fill_opacity=0.95, buff=0.18)
        test_intro_bg.move_to(test_intro.get_center())
        self.play(FadeIn(test_intro_bg, run_time=0.4), FadeIn(test_intro, run_time=1.0))
        self.wait(1.5)

        test_eq = MathTex(r"y = 3(5) + 2 = 17", color=WHITE).scale(1.1)
        test_eq.move_to(BAND_CHART_CENTER + UP * 0.3)
        test_eq_bg = BackgroundRectangle(test_eq, color=BLACK, fill_opacity=1, buff=0.3)
        test_eq_bg.move_to(test_eq.get_center())
        self.play(
            FadeOut(VGroup(test_intro, test_intro_bg), run_time=0.5),
            FadeIn(test_eq_bg, run_time=0.4),
            Write(test_eq, run_time=1.8),
        )
        self.wait(2.5)

        passes = Text("Passes. Conjecture survives this test.", font_size=22, color=GREEN_OK)
        passes.next_to(test_eq, DOWN, buff=0.7)
        passes_bg = BackgroundRectangle(passes, color=BLACK, fill_opacity=0.95, buff=0.18)
        passes_bg.move_to(passes.get_center())
        self.play(FadeIn(passes_bg, run_time=0.4), FadeIn(passes, run_time=1.4))
        self.wait(3.0)
        self.play(
            FadeOut(VGroup(test_eq, test_eq_bg, passes, passes_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Counter-example disproves (~17 s)
        # ──────────────────────────────────────────────────────────────────
        ce_intro = Text("\"All primes are odd.\"", font_size=22, color=BLUE_TERM)
        ce_intro.move_to(BAND_CHART_CENTER + UP * 1.5)
        ce_intro_bg = BackgroundRectangle(ce_intro, color=BLACK, fill_opacity=0.95, buff=0.18)
        ce_intro_bg.move_to(ce_intro.get_center())
        self.play(FadeIn(ce_intro_bg, run_time=0.4), FadeIn(ce_intro, run_time=1.2))
        self.wait(2.0)

        ce = Text("Counter-example: 2 is prime, and even.", font_size=22, color=RED_REJECT)
        ce.move_to(BAND_CHART_CENTER + UP * 0.3)
        ce_bg = BackgroundRectangle(ce, color=BLACK, fill_opacity=0.95, buff=0.18)
        ce_bg.move_to(ce.get_center())
        self.play(
            FadeOut(VGroup(ce_intro, ce_intro_bg), run_time=0.5),
            FadeIn(ce_bg, run_time=0.4),
            FadeIn(ce, run_time=1.4),
        )
        self.wait(2.5)

        verdict = Text("Conjecture: false.", font_size=24, color=RED_REJECT)
        verdict.next_to(ce, DOWN, buff=0.7)
        verdict_bg = BackgroundRectangle(verdict, color=BLACK, fill_opacity=0.95, buff=0.18)
        verdict_bg.move_to(verdict.get_center())
        self.play(FadeIn(verdict_bg, run_time=0.4), FadeIn(verdict, run_time=1.0))
        self.wait(3.0)
        self.play(
            FadeOut(VGroup(ce, ce_bg, verdict, verdict_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~13 s, total ≈ 79 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{1 counter-example} \;\Rightarrow\; \text{conjecture false}",
            "Many tests support; one counter-example disproves.",
            final_wait=30.0,
        )