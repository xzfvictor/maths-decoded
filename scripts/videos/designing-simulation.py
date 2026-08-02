"""
Manim scene for the lesson `designing-simulation`
(topic `l9-p-simulations`).

A simulation imitates a chance experiment with random numbers. Map
each outcome onto a number, then run the random number generator
many times. Reject the "any digit will do" trap: the mapping must
respect the real probabilities.

Target duration: ~74.6 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class DesigningSimulationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Designing a simulation",
            "Map each outcome to a random number — then run it many times.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The five-step recipe (~22 s)
        # ──────────────────────────────────────────────────────────────────
        steps = VGroup(
            make_term_card("1.\,\text{Identify}", "random components", BLUE_TERM),
            make_term_card("2.\,\text{Map}", "outcome → number", TEAL_TERM),
            make_term_card("3.\,\text{Run}", "many trials", ORANGE_TERM),
            make_term_card("4.\,\text{Record}", "outcomes of interest", GREEN_OK),
            make_term_card("5.\,\text{Estimate}", "relative frequency", BLUE_TERM),
        ).arrange(DOWN, buff=0.32)
        steps.move_to(BAND_CHART_CENTER + UP * 0.4)
        for s in steps:
            s.set_z_index(2)

        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.15, run_time=0.7))
            self.wait(0.6)

        # 5th step already revealed in the loop; pause then move on.
        self.wait(4.0)

        self.play(FadeOut(steps, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Concrete example: a die as a fair coin (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Example: simulate a fair coin with a die",
                    font_size=22, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        # The mapping: even ⇒ Head, odd ⇒ Tail.
        even = MathTex(r"2,\ 4,\ 6 \;\Rightarrow\; \text{Head}", color=GREEN_OK).scale(1.0)
        odd = MathTex(r"1,\ 3,\ 5 \;\Rightarrow\; \text{Tail}", color=TEAL_TERM).scale(1.0)
        even.move_to(BAND_CHART_CENTER + UP * 0.4)
        odd.next_to(even, DOWN, buff=0.5)
        even_bg = BackgroundRectangle(even, color=BLACK, fill_opacity=1, buff=0.25)
        even_bg.move_to(even.get_center())
        odd_bg = BackgroundRectangle(odd, color=BLACK, fill_opacity=1, buff=0.25)
        odd_bg.move_to(odd.get_center())

        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(even_bg, run_time=0.4), Write(even, run_time=1.4))
        self.wait(0.5)
        self.play(FadeIn(odd_bg, run_time=0.4), Write(odd, run_time=1.4))
        self.wait(2.0)

        why = MathTex(
            r"\text{Each side has probability } \tfrac{3}{6} = \tfrac{1}{2} \text{ — exactly fair.}",
            color=GREEN_OK,
        ).scale(0.9)
        why.next_to(odd, DOWN, buff=0.55)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=1, buff=0.25)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.4))
        self.wait(5.0)

        self.play(
            FadeOut(VGroup(head, head_bg, even, even_bg, odd, odd_bg,
                           why, why_bg), run_time=1.2),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: "any digit will do" (~8 s)
        # ──────────────────────────────────────────────────────────────────
        bad = Text(
            '"Just use 0 for head and 1 for tail — done."',
            font_size=22, color=WHITE,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.6)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(1.5)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=1.0))
        self.wait(1.0)

        fix = Text(
            "The mapping must match the real probabilities.",
            font_size=22, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.4))
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(bad, bad_bg, cross, fix, fix_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 74.6 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Map outcomes to numbers; match real probabilities.}",
            "Run the random number generator many times, then estimate.",
            final_wait=28.0,
        )
