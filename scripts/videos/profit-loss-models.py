"""
Manim scene for the lesson `profit-loss-models`
(topic `l8-a-linear-modelling`).

Two linear models usually describe a business: revenue R = pn, cost
C = vn + f. Break-even is where R = C.

Target duration: ~97 s (matches audio).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro, animate_final_definition,
)
from manim import *


class ProfitLossModelsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Profit and loss with linear models",
            "Revenue up, cost up — find where they meet.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Revenue model R = p*n (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Use the running example: mugs at $10 each, costs $6 + $80 fixed.
        intro = Text(
            "Selling mugs: price $10 each.",
            font_size=22,
            color=BLUE_TERM,
        ).move_to(BAND_CHART_CENTER + UP * 1.5)
        intro_bg = BackgroundRectangle(intro, color=BLACK, fill_opacity=0.95, buff=0.18)
        intro_bg.move_to(intro.get_center())
        self.play(FadeIn(intro_bg, run_time=0.4), FadeIn(intro, run_time=1.2))
        self.wait(2.5)

        revenue = MathTex(r"R \;=\; p \cdot n \;=\; 10n", color=BLUE_TERM).scale(1.2)
        revenue.move_to(BAND_CHART_CENTER + UP * 0.2)
        rev_bg = BackgroundRectangle(revenue, color=BLACK, fill_opacity=1, buff=0.3)
        rev_bg.move_to(revenue.get_center())
        self.play(
            FadeOut(VGroup(intro, intro_bg), run_time=0.8),
            FadeIn(rev_bg, run_time=0.5),
            Write(revenue, run_time=1.8),
        )
        self.wait(4.0)
        rev_lbl = Text("Revenue (money in)", font_size=20, color=BLUE_TERM)
        rev_lbl.next_to(revenue, DOWN, buff=0.5)
        rev_lbl_bg = BackgroundRectangle(rev_lbl, color=BLACK, fill_opacity=0.9, buff=0.15)
        rev_lbl_bg.move_to(rev_lbl.get_center())
        self.play(FadeIn(rev_lbl_bg, run_time=0.4), FadeIn(rev_lbl, run_time=1.0))
        self.wait(3.0)
        self.play(
            FadeOut(VGroup(revenue, rev_bg, rev_lbl, rev_lbl_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Cost model C = v*n + f (~22 s)
        # ──────────────────────────────────────────────────────────────────
        intro2 = Text(
            "Each mug costs $6 to make, plus $80 fixed per day.",
            font_size=22,
            color=ORANGE_TERM,
        ).move_to(BAND_CHART_CENTER + UP * 1.5)
        intro2_bg = BackgroundRectangle(intro2, color=BLACK, fill_opacity=0.95, buff=0.18)
        intro2_bg.move_to(intro2.get_center())
        self.play(FadeIn(intro2_bg, run_time=0.4), FadeIn(intro2, run_time=1.4))
        self.wait(2.5)

        cost = MathTex(r"C \;=\; 6n + 80", color=ORANGE_TERM).scale(1.2)
        cost.move_to(BAND_CHART_CENTER + UP * 0.2)
        cost_bg = BackgroundRectangle(cost, color=BLACK, fill_opacity=1, buff=0.3)
        cost_bg.move_to(cost.get_center())
        self.play(
            FadeOut(VGroup(intro2, intro2_bg), run_time=0.8),
            FadeIn(cost_bg, run_time=0.5),
            Write(cost, run_time=1.8),
        )
        self.wait(4.0)
        cost_lbl = Text("Cost (money out)", font_size=20, color=ORANGE_TERM)
        cost_lbl.next_to(cost, DOWN, buff=0.5)
        cost_lbl_bg = BackgroundRectangle(cost_lbl, color=BLACK, fill_opacity=0.9, buff=0.15)
        cost_lbl_bg.move_to(cost_lbl.get_center())
        self.play(FadeIn(cost_lbl_bg, run_time=0.4), FadeIn(cost_lbl, run_time=1.0))
        self.wait(3.0)
        self.play(
            FadeOut(VGroup(cost, cost_bg, cost_lbl, cost_lbl_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Break-even: R = C, solve for n (~25 s)
        # ──────────────────────────────────────────────────────────────────
        setup = MathTex(r"10n \;=\; 6n + 80", color=WHITE).scale(1.2)
        setup.move_to(BAND_CHART_CENTER + UP * 1.2)
        setup_bg = BackgroundRectangle(setup, color=BLACK, fill_opacity=1, buff=0.3)
        setup_bg.move_to(setup.get_center())
        self.play(FadeIn(setup_bg, run_time=0.5), Write(setup, run_time=1.8))
        self.wait(3.0)

        solve = MathTex(r"4n \;=\; 80", color=WHITE).scale(1.2)
        solve.move_to(BAND_CHART_CENTER + UP * 0.1)
        solve_bg = BackgroundRectangle(solve, color=BLACK, fill_opacity=1, buff=0.3)
        solve_bg.move_to(solve.get_center())
        self.play(
            FadeOut(setup_bg, run_time=0.5),
            FadeOut(setup, run_time=0.5),
            FadeIn(solve_bg, run_time=0.5),
            Write(solve, run_time=1.4),
        )
        self.wait(2.5)

        ans = MathTex(r"n \;=\; 20 \text{ mugs}", color=GREEN_OK).scale(1.2)
        ans.move_to(BAND_CHART_CENTER + DOWN * 0.8)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.3)
        ans_bg.move_to(ans.get_center())
        ans_box = SurroundingRectangle(ans, color=GREEN_OK, buff=0.3, stroke_width=3)
        self.play(
            FadeOut(solve_bg, run_time=0.4),
            FadeOut(solve, run_time=0.4),
            FadeIn(ans_bg, run_time=0.5),
            Write(ans, run_time=1.5),
        )
        self.play(Create(ans_box, run_time=1.0))
        self.wait(5.0)
        self.play(
            FadeOut(VGroup(ans, ans_bg, ans_box), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~22 s, total ≈ 97 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Break-even:}\;\; pn \;=\; vn + f",
            "Set revenue = cost and solve for n.",
            final_wait=43.0,
        )