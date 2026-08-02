"""
Manim scene for the lesson `generalising-patterns`
(topic `l8-a-linear-functions-relations`).

Replace specific numbers with variables; the pattern that worked for
the examples works for every case.

Target duration: ~85 s (matches audio).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro, animate_final_definition,
)
from manim import *


class GeneralisingPatternsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Generalising patterns to formulas",
            "Specific cases first — then write the rule for all n.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Specific cases (~20 s)
        # ──────────────────────────────────────────────────────────────────
        intro = Text("Sequence: 3, 7, 11, 15, 19, ...", font_size=24, color=BLUE_TERM)
        intro.move_to(BAND_CHART_CENTER + UP * 1.5)
        intro_bg = BackgroundRectangle(intro, color=BLACK, fill_opacity=0.95, buff=0.18)
        intro_bg.move_to(intro.get_center())
        self.play(FadeIn(intro_bg, run_time=0.4), FadeIn(intro, run_time=1.4))
        self.wait(2.5)

        # Show the differences.
        diff = Text("Differences: 4, 4, 4, 4 — constant.", font_size=22, color=TEAL_TERM)
        diff.move_to(BAND_CHART_CENTER + UP * 0.5)
        diff_bg = BackgroundRectangle(diff, color=BLACK, fill_opacity=0.95, buff=0.18)
        diff_bg.move_to(diff.get_center())
        self.play(
            FadeOut(VGroup(intro, intro_bg), run_time=0.6),
            FadeIn(diff_bg, run_time=0.4),
            FadeIn(diff, run_time=1.4),
        )
        self.wait(3.0)

        linear = Text("Constant difference → linear pattern.", font_size=22, color=ORANGE_TERM)
        linear.next_to(diff, DOWN, buff=0.6)
        linear_bg = BackgroundRectangle(linear, color=BLACK, fill_opacity=0.95, buff=0.18)
        linear_bg.move_to(linear.get_center())
        self.play(FadeIn(linear_bg, run_time=0.4), FadeIn(linear, run_time=1.4))
        self.wait(3.0)
        self.play(
            FadeOut(VGroup(diff, diff_bg, linear, linear_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Replace numbers with variables (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Show the substitution.
        step1 = Text("Each term: add 4 to the previous.", font_size=22, color=BLUE_TERM)
        step1.move_to(BAND_CHART_CENTER + UP * 1.5)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=0.95, buff=0.18)
        step1_bg.move_to(step1.get_center())
        self.play(FadeIn(step1_bg, run_time=0.4), FadeIn(step1, run_time=1.4))
        self.wait(2.5)

        step2 = MathTex(r"a_n = a_{n-1} + 4", color=WHITE).scale(1.1)
        step2.move_to(BAND_CHART_CENTER + UP * 0.3)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=1, buff=0.3)
        step2_bg.move_to(step2.get_center())
        self.play(
            FadeOut(VGroup(step1, step1_bg), run_time=0.6),
            FadeIn(step2_bg, run_time=0.4),
            Write(step2, run_time=1.6),
        )
        self.wait(3.0)

        # Use a_1 = 3 to find the constant.
        use1 = Text("Use a_1 = 3: a_n = 4n - 1", font_size=22, color=TEAL_TERM)
        use1.next_to(step2, DOWN, buff=0.6)
        use1_bg = BackgroundRectangle(use1, color=BLACK, fill_opacity=0.95, buff=0.18)
        use1_bg.move_to(use1.get_center())
        self.play(FadeIn(use1_bg, run_time=0.4), FadeIn(use1, run_time=1.4))
        self.wait(3.0)
        self.play(
            FadeOut(VGroup(step2, step2_bg, use1, use1_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Test the general formula (~17 s)
        # ──────────────────────────────────────────────────────────────────
        intro4 = Text("Test on n = 5", font_size=22, color=BLUE_TERM)
        intro4.move_to(BAND_CHART_CENTER + UP * 1.5)
        intro4_bg = BackgroundRectangle(intro4, color=BLACK, fill_opacity=0.95, buff=0.18)
        intro4_bg.move_to(intro4.get_center())
        self.play(FadeIn(intro4_bg, run_time=0.4), FadeIn(intro4, run_time=1.0))
        self.wait(1.5)

        test = MathTex(r"a_5 = 4(5) - 1 = 19\;\;\checkmark", color=GREEN_OK).scale(1.1)
        test.move_to(BAND_CHART_CENTER + UP * 0.3)
        test_bg = BackgroundRectangle(test, color=BLACK, fill_opacity=1, buff=0.3)
        test_bg.move_to(test.get_center())
        self.play(
            FadeOut(VGroup(intro4, intro4_bg), run_time=0.5),
            FadeIn(test_bg, run_time=0.4),
            Write(test, run_time=1.6),
        )
        self.wait(2.0)

        # The general formula.
        gen = MathTex(r"a_n \;=\; 4n - 1", color=GREEN_OK).scale(1.3)
        gen.move_to(BAND_CHART_CENTER + DOWN * 0.8)
        gen_bg = BackgroundRectangle(gen, color=BLACK, fill_opacity=1, buff=0.3)
        gen_bg.move_to(gen.get_center())
        gen_box = SurroundingRectangle(gen, color=GREEN_OK, buff=0.3, stroke_width=3)
        self.play(
            FadeOut(VGroup(test, test_bg), run_time=0.6),
            FadeIn(gen_bg, run_time=0.4),
            Write(gen, run_time=1.6),
        )
        self.play(Create(gen_box, run_time=1.0))
        self.wait(3.0)
        self.play(
            FadeOut(VGroup(gen, gen_bg, gen_box), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~18 s, total ≈ 85 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{General formula} \;\Rightarrow\; \text{predict any term}",
            "Replace specific numbers with variables; the rule still holds.",
            final_wait=37.0,
        )