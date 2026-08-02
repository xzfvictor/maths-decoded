"""
Manim scene for the lesson `right-prisms`
(topic `l8-m-volume-capacity-prisms`).

Volume of a right prism equals the area of its cross-section times
its length: V = A × l. The scene builds the formula by stacking the
same cross-section along a length, then rejects the common confusion
between volume and capacity units.

Target duration: ~99 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class RightPrismsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Volume of right prisms",
            "V = area of cross-section × length",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Build a stack visual: same rectangle cross-section
        # repeated along a length (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # A 4×3 rectangle cross-section, stacked 5 times to make a
        # 4 × 3 × 5 rectangular prism.
        layers = VGroup()
        for i in range(5):
            rect = Rectangle(
                width=1.4, height=1.0,
                color=BLUE_TERM, stroke_width=2,
                fill_color=BLUE_TERM, fill_opacity=0.25,
            )
            rect.shift(UP * 0.35 * i + LEFT * 0.0)
            layers.add(rect)

        layers.move_to(BAND_CHART_CENTER + UP * 0.5)

        # Caption underneath the stack.
        cap = Text("stack 5 layers of a 4 × 3 rectangle", font_size=22)
        cap.next_to(layers, DOWN, buff=0.45)
        cap_bg = BackgroundRectangle(cap, color=BLACK, fill_opacity=0.95, buff=0.15)
        cap_bg.move_to(cap.get_center())

        self.play(
            LaggedStart(*[FadeIn(r, run_time=0.4) for r in layers], lag_ratio=0.25),
        )
        self.wait(1.0)
        self.play(FadeIn(cap_bg, run_time=0.4), FadeIn(cap, run_time=1.0))
        self.wait(3.0)

        # Compute V from the numbers.
        calc = MathTex(r"V \;=\; 4 \times 3 \times 5 \;=\; 60\ \text{cm}^3", color=GREEN_OK).scale(1.1)
        calc.next_to(cap, DOWN, buff=0.5)
        calc_bg = BackgroundRectangle(calc, color=BLACK, fill_opacity=1, buff=0.2)
        calc_bg.move_to(calc.get_center())
        self.play(FadeIn(calc_bg, run_time=0.5), Write(calc, run_time=2.0))
        self.wait(3.0)
        self.play(
            FadeOut(layers, run_time=1.0),
            FadeOut(cap, run_time=1.0),
            FadeOut(cap_bg, run_time=1.0),
            FadeOut(calc, run_time=1.0),
            FadeOut(calc_bg, run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: V = A × l works for ANY cross-section (~22 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(r"V = A \times l", color=BLUE_TERM, scale=1.5)
        general.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        # The cross-section can be ANY shape — three examples.
        lbl_a = Text("A = area of cross-section", font_size=22, color=BLUE_TERM)
        lbl_a.next_to(general, DOWN, buff=0.5)
        lbl_a_bg = BackgroundRectangle(lbl_a, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl_a_bg.move_to(lbl_a.get_center())

        lbl_l = Text("l = length the shape travels", font_size=22, color=BLUE_TERM)
        lbl_l.next_to(lbl_a, DOWN, buff=0.3)
        lbl_l_bg = BackgroundRectangle(lbl_l, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl_l_bg.move_to(lbl_l.get_center())

        self.play(FadeIn(lbl_a_bg, run_time=0.4), FadeIn(lbl_a, run_time=1.0))
        self.wait(1.5)
        self.play(FadeIn(lbl_l_bg, run_time=0.4), FadeIn(lbl_l, run_time=1.0))
        self.wait(2.5)

        # Three cross-section shapes that all use V = A × l.
        examples = VGroup(
            MathTex(r"\text{rect: } A = w \times h", color=ORANGE_TERM).scale(0.7),
            MathTex(r"\text{tri: } A = \tfrac{1}{2} b h", color=ORANGE_TERM).scale(0.7),
            MathTex(r"\text{trap: } A = \tfrac{1}{2}(a + b) h", color=ORANGE_TERM).scale(0.7),
        ).arrange(RIGHT, buff=0.5)
        examples.next_to(lbl_l, DOWN, buff=0.5)
        ex_bg = BackgroundRectangle(examples, color=BLACK, fill_opacity=0.95, buff=0.18)
        ex_bg.move_to(examples.get_center())
        self.play(FadeIn(ex_bg, run_time=0.5), FadeIn(examples, run_time=1.4))
        self.wait(4.0)
        self.play(
            FadeOut(general, run_time=1.0),
            FadeOut(lbl_a, run_time=1.0),
            FadeOut(lbl_a_bg, run_time=1.0),
            FadeOut(lbl_l, run_time=1.0),
            FadeOut(lbl_l_bg, run_time=1.0),
            FadeOut(examples, run_time=1.0),
            FadeOut(ex_bg, run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: confusing volume and capacity units (~13 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(r"30{,}000\ \text{cm}^3 = 30{,}000\ \text{L}\ \text{?}", color=RED_REJECT).scale(0.95)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.5)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        self.play(FadeIn(wrong_bg, run_time=0.5), Write(wrong, run_time=1.6))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.8))
        self.wait(2.0)

        correction = MathTex(
            r"1\ \text{cm}^3 = 1\ \text{mL}, \quad 1\ \text{L} = 1000\ \text{cm}^3",
            color=GREEN_OK,
        ).scale(1.0)
        correction.next_to(wrong, DOWN, buff=0.6)
        correction_bg = BackgroundRectangle(correction, color=BLACK, fill_opacity=1, buff=0.25)
        correction_bg.move_to(correction.get_center())
        self.play(
            FadeOut(wrong, run_time=0.6),
            FadeOut(wrong_bg, run_time=0.6),
            FadeOut(cross, run_time=0.6),
            FadeIn(correction_bg, run_time=0.5),
            Write(correction, run_time=1.6),
        )
        self.wait(3.0)
        self.play(
            FadeOut(correction, run_time=0.8),
            FadeOut(correction_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~36 s, total ≈ 99 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"V \;=\; A \times l",
            "Cross-section area × length, for any right prism.",
            final_wait=38.0,
        )
