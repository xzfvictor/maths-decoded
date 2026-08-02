"""
Manim scene for the lesson `solving-quadratics`
(topic `l9-a-quadratic-functions-equations`).

Solve ax² + bx + c = 0 by rewriting as a product of factors and
applying the null factor law (if A·B = 0 then A = 0 or B = 0). The
animation walks through x² - 5x + 6 = 0 → (x - 2)(x - 3) = 0 → x = 2
or 3, generalises to two numbers whose product is c and sum is b, and
rejects the common mistake of dividing by x (which loses the x = 0
root).

Target duration: ~100 s (matches the audio narration length of 99.86 s).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SolvingQuadraticsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Solving quadratic equations",
            "Factor and apply the null factor law.",
            hold=2.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: x² - 5x + 6 = 0 → x = 2 or 3 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        eq1 = make_equation_card(r"x^{2} - 5x + 6 = 0",
                                  color=BLUE_TERM, scale=1.3)
        eq1.move_to(BAND_CHART_CENTER + UP * 0.9)
        for m in eq1:
            m.set_z_index(2)
        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.5))
        self.wait(1.5)

        # Hunt for two numbers with product 6 and sum -5.
        head = Text("Two numbers:  product = 6,  sum = -5",
                    font_size=22, color=ORANGE_TERM)
        head.move_to(BAND_CHART_CENTER + DOWN * 0.1)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        self.play(FadeIn(head_bg, run_time=0.5), FadeIn(head, run_time=1.2))
        self.wait(1.5)

        ans = MathTex(r"-2 \;\text{ and }\; -3",
                     color=GREEN_OK).scale(1.1)
        ans.next_to(head, DOWN, buff=0.45)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.25)
        ans_bg.move_to(ans.get_center())
        self.play(FadeIn(ans_bg, run_time=0.5), FadeIn(ans, run_time=1.5))
        self.wait(1.5)

        # Factorise.
        eq2 = make_equation_card(r"(x - 2)(x - 3) = 0",
                                  color=GREEN_OK, scale=1.3)
        eq2.move_to(eq1.get_center())
        for m in eq2:
            m.set_z_index(2)
        self.play(Transform(eq1, eq2, run_time=1.4))
        self.wait(1.2)

        # Null factor law: each bracket = 0.
        nfl = MathTex(r"x - 2 = 0 \;\text{ or }\; x - 3 = 0",
                      color=GREEN_OK).scale(0.9)
        nfl.move_to(BAND_CHART_CENTER + DOWN * 1.3)
        nfl_bg = BackgroundRectangle(nfl, color=BLACK, fill_opacity=1, buff=0.25)
        nfl_bg.move_to(nfl.get_center())
        self.play(FadeIn(nfl_bg, run_time=0.5), FadeIn(nfl, run_time=1.5))
        self.wait(1.5)

        # Final solutions.
        sol = make_equation_card(r"x = 2 \;\text{ or }\; x = 3",
                                  color=GREEN_OK, scale=1.4)
        sol.move_to(BAND_CHART_CENTER + DOWN * 2.2)
        for m in sol:
            m.set_z_index(2)
        self.play(FadeIn(sol, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        beat2_group = VGroup(eq1, head, head_bg, ans, ans_bg,
                             nfl, nfl_bg, sol)
        self.play(FadeOut(beat2_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — General rule for monic quadratics (~18 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(
            r"x^{2} + b\,x + c \;=\; (x + m)(x + n)",
            color=BLUE_TERM,
            scale=1.0,
        )
        general.move_to(BAND_CHART_CENTER + UP * 1.0)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        line1 = MathTex(r"m \cdot n = c", color=GREEN_OK).scale(0.95)
        line2 = MathTex(r"m + n = b", color=ORANGE_TERM).scale(0.95)
        line1.next_to(general, DOWN, buff=0.5)
        line2.next_to(line1, DOWN, buff=0.35)
        line1_bg = BackgroundRectangle(line1, color=BLACK, fill_opacity=0.95, buff=0.18)
        line1_bg.move_to(line1.get_center())
        line2_bg = BackgroundRectangle(line2, color=BLACK, fill_opacity=0.95, buff=0.18)
        line2_bg.move_to(line2.get_center())
        self.play(FadeIn(line1_bg, run_time=0.4), FadeIn(line1, run_time=1.0))
        self.wait(0.8)
        self.play(FadeIn(line2_bg, run_time=0.4), FadeIn(line2, run_time=1.0))
        self.wait(1.0)

        # Then apply the null factor law.
        nfl_card = make_equation_card(
            r"AB = 0 \;\Rightarrow\; A = 0 \;\text{ or }\; B = 0",
            color=GREEN_OK,
            scale=0.95,
        )
        nfl_card.move_to(BAND_CHART_CENTER + DOWN * 1.6)
        for m in nfl_card:
            m.set_z_index(2)
        self.play(FadeIn(nfl_card, shift=UP * 0.2, run_time=1.3))
        self.wait(2.0)

        beat3_group = VGroup(general, line1, line1_bg, line2, line2_bg, nfl_card)
        self.play(FadeOut(beat3_group, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: dividing by x (loses x = 0 root) (~10 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(
            r"\dfrac{x^{2}}{x} - 5 \cdot \dfrac{x}{x} + 6 \cdot \dfrac{1}{x}",
            color=RED_REJECT,
        ).scale(0.85)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.8)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())

        self.play(FadeIn(wrong_bg, run_time=0.5), Write(wrong, run_time=1.4))
        self.wait(1.0)

        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.7))
        self.wait(0.8)

        note = MathTex(
            r"\text{Dividing by } x \text{ LOSES the } x = 0 \text{ root.}",
            color=RED_REJECT,
        ).scale(0.85)
        note.next_to(wrong, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.5))
        self.wait(1.0)
        self.play(
            FadeOut(VGroup(wrong, wrong_bg, cross, note, note_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=38 s, total ≈ 100 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"(x + m)(x + n) = 0 \;\Rightarrow\; x = -m \;\text{ or }\; x = -n",
            "Find m, n with mn = c and m + n = b, then set each factor to 0.",
            final_wait=38.0,
        )