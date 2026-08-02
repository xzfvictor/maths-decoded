"""
Manim scene for the lesson `time-zones`
(topic `l8-m-time-time-zones`).

Time in zone B = time in zone A + (offset of B − offset of A). The
scene walks through a Sydney ↔ London conversion, then rejects the
common mistake of forgetting to roll the clock over to the previous
day when the answer goes negative.

Target duration: ~80 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class TimeZonesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Time zones",
            "Time in B = Time in A + (offset B − offset A)",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: 10:00 in Sydney → London (~18 s)
        # ──────────────────────────────────────────────────────────────────
        sydney = make_equation_card(
            r"\text{Sydney: } 10{:}00,\ \text{UTC} +10",
            color=BLUE_TERM, scale=1.0,
        )
        sydney.move_to(BAND_CHART_CENTER + UP * 1.0)
        for m in sydney:
            m.set_z_index(2)

        london = make_equation_card(
            r"\text{London: ?},\ \text{UTC} +0",
            color=ORANGE_TERM, scale=1.0,
        )
        london.next_to(sydney, DOWN, buff=0.5)
        for m in london:
            m.set_z_index(2)

        self.play(FadeIn(sydney, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)
        self.play(FadeIn(london, shift=UP * 0.2, run_time=1.2))
        self.wait(2.0)

        # Arrow from Sydney to London with the offset difference.
        diff = MathTex(r"0 - 10 = -10\ \text{hours}", color=GREEN_OK).scale(0.95)
        diff.next_to(london, DOWN, buff=0.5)
        diff_bg = BackgroundRectangle(diff, color=BLACK, fill_opacity=1, buff=0.2)
        diff_bg.move_to(diff.get_center())
        self.play(FadeIn(diff_bg, run_time=0.4), Write(diff, run_time=1.6))
        self.wait(2.5)
        self.play(
            FadeOut(sydney, run_time=0.8),
            FadeOut(london, run_time=0.8),
            FadeOut(diff, run_time=0.8),
            FadeOut(diff_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: offset-difference formula (~18 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(
            r"\text{time in B} = \text{time in A} + (\text{offset}_B - \text{offset}_A)",
            color=BLUE_TERM, scale=0.95,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        rules = VGroup(
            Text("if answer ≥ 24  →  subtract 24, add a day", font_size=22, color=GREEN_OK),
            Text("if answer <  0  →  add 24, go back a day", font_size=22, color=GREEN_OK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rules.next_to(general, DOWN, buff=0.55)
        for r in rules:
            bg = BackgroundRectangle(r, color=BLACK, fill_opacity=0.95, buff=0.15)
            bg.move_to(r.get_center())
            r.bg = bg
        rules_bgs = VGroup(*[r.bg for r in rules])

        self.play(FadeIn(rules_bgs, run_time=0.5), FadeIn(rules, run_time=1.4))
        self.wait(4.0)
        self.play(
            FadeOut(general, run_time=1.0),
            FadeOut(rules, run_time=1.0),
            FadeOut(rules_bgs, run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: forgetting the day rollover gives a "negative
        # clock" (~10 s)
        # ──────────────────────────────────────────────────────────────────
        wrong = MathTex(r"\text{London: } -{:}00\ \text{?}", color=RED_REJECT).scale(1.1)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.5)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.4))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.0)

        right = MathTex(
            r"\text{London: } 00{:}00,\ \text{previous day}",
            color=GREEN_OK,
        ).scale(1.1)
        right.next_to(wrong, DOWN, buff=0.5)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=1, buff=0.25)
        right_bg.move_to(right.get_center())
        self.play(
            FadeOut(wrong, run_time=0.6),
            FadeOut(wrong_bg, run_time=0.6),
            FadeOut(cross, run_time=0.6),
            FadeIn(right_bg, run_time=0.4),
            Write(right, run_time=1.4),
        )
        self.wait(3.0)
        self.play(
            FadeOut(right, run_time=0.8),
            FadeOut(right_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~30 s, total ≈ 80 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{time in B} = \text{time in A} + (\text{offset}_B - \text{offset}_A)",
            "Roll the clock over when the answer leaves [0, 24).",
            final_wait=30.0,
        )
