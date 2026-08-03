"""
Manim scene for the lesson `testing-conjectures`
(topic `l10a-aa-functions-relations`).

Test a conjectured relationship against data. The workflow: conjecture
a form, compute predicted y-values, compare to actual y-values, accept
or reject. A small worked example shows y = 3x vs. y = x^2 fits.

Target duration: ~94.7 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class TestingConjecturesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Testing conjectures against data",
            "Conjecture → predict → compare → accept or reject.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The four-step process (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("The test cycle", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        steps = [
            ("1. Conjecture", BLUE_TERM),
            ("2. Predict", TEAL_TERM),
            ("3. Compare", ORANGE_TERM),
            ("4. Decide", GREEN_OK),
        ]
        chain = VGroup()
        for i, (txt, col) in enumerate(steps):
            card = Text(txt, font_size=22, color=col)
            card.move_to(BAND_CHART_CENTER + UP * 0.7 + DOWN * i * 0.7)
            card_bg = BackgroundRectangle(card, color=BLACK,
                                          fill_opacity=0.95, buff=0.18)
            card_bg.move_to(card.get_center())
            chain.add(VGroup(card_bg, card))

        self.play(
            LaggedStart(*[FadeIn(c, shift=UP * 0.2, run_time=0.7)
                          for c in chain], lag_ratio=0.4),
        )
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, chain)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Concrete: data table, conjecture y = 3x (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Worked example", font_size=26, color=BLUE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        # Data table: (x, y_actual).
        rows = [
            ("x", "y"),
            ("1", "3"),
            ("2", "6"),
            ("3", "9"),
            ("4", "12"),
        ]
        tbl = VGroup()
        for i, (a, b) in enumerate(rows):
            ca = Text(a, font_size=22,
                      color=BLUE_TERM if i > 0 else WHITE).move_to(LEFT * 1.5 + UP * 0.7 + DOWN * i * 0.55)
            cb = Text(b, font_size=22,
                      color=BLUE_TERM if i > 0 else WHITE).move_to(RIGHT * 0.3 + UP * 0.7 + DOWN * i * 0.55)
            tbl.add(ca, cb)
        tbl.move_to(BAND_CHART_CENTER + UP * 0.4)

        # Row backgrounds
        tbl_bg = BackgroundRectangle(tbl, color=BLACK, fill_opacity=0.95, buff=0.25)
        tbl_bg.move_to(tbl.get_center())

        self.play(FadeIn(tbl_bg, run_time=0.4),
                  LaggedStart(*[FadeIn(r, run_time=0.5) for r in tbl],
                              lag_ratio=0.15))
        self.wait(1.5)

        conj = make_equation_card(
            r"\text{Conjecture: } y = 3x",
            color=GREEN_OK, scale=0.95,
        )
        conj.move_to(BAND_CHART_CENTER + DOWN * 1.4)
        self.play(FadeIn(conj, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        beat3 = beat_group(head3, head3_bg, tbl, tbl_bg, conj)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Test a wrong conjecture: y = x^2 (~12 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Reject a poor fit", font_size=26, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        wrong = make_equation_card(
            r"y = x^{2}\ :\ (1,1),(2,4),(3,9),(4,16)",
            color=RED_REJECT, scale=0.95,
        )
        wrong.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(wrong, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        verdict = Text(
            "Predicted y = 16 but actual y = 12 — conjecture rejected.",
            font_size=20, color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.4)
        verdict_bg = BackgroundRectangle(verdict, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        verdict_bg.move_to(verdict.get_center())
        self.play(FadeIn(verdict_bg, run_time=0.4),
                  FadeIn(verdict, run_time=1.0))
        self.wait(2.0)

        beat4 = beat_group(head4, head4_bg, wrong, verdict, verdict_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 94.7 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Predict} \rightarrow \text{Compare} \rightarrow "
            r"\text{Decide}",
            "A conjecture fits when predicted values match the data.",
            final_wait=43.0,
        )