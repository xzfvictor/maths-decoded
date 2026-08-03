"""
Manim scene for the lesson `function-notation-basics`
(topic `l10a-aa-function-notation`).

The function notation f(x) reads as "f of x". An input x is mapped to
an output f(x); the set of legal inputs is the domain, the set of
outputs is the range. A concrete example f(2) = 5 anchors the idea.

Target duration: ~120.9 s (matches the audio narration length).
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


class FunctionNotationBasicsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Function notation f(x)",
            "A function maps each input x to a single output f(x).",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — A concrete example f(x) = 2x + 1 (~25 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("A concrete example", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        rule = make_equation_card(
            r"f(x) \;=\; 2x + 1",
            color=BLUE_TERM, scale=1.2,
        )
        rule.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(rule, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        # Plug in x = 2: f(2) = 5.
        sub = make_equation_card(
            r"f(2) \;=\; 2(2) + 1 \;=\; 5",
            color=GREEN_OK, scale=1.1,
        )
        sub.next_to(rule, DOWN, buff=0.7)
        self.play(FadeIn(sub, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        note = Text('"f of 2 equals 5" — input 2, output 5.',
                    font_size=20, color=WHITE)
        note.next_to(sub, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(3.0)

        beat2 = beat_group(head, head_bg, rule, sub, note, note_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Domain and range (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Domain and range", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.45)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        domain = MathTex(
            r"\text{Domain} = \{\text{legal inputs}\}",
            color=TEAL_TERM,
        ).scale(0.9)
        domain.move_to(BAND_CHART_CENTER + UP * 0.45)
        domain_bg = BackgroundRectangle(domain, color=BLACK,
                                         fill_opacity=1, buff=0.18)
        domain_bg.move_to(domain.get_center())
        self.play(FadeIn(domain_bg, run_time=0.3),
                  FadeIn(domain, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)

        rng = MathTex(
            r"\text{Range} = \{\text{outputs}\}",
            color=ORANGE_TERM,
        ).scale(0.9)
        rng.next_to(domain, DOWN, buff=0.65)
        rng_bg = BackgroundRectangle(rng, color=BLACK,
                                     fill_opacity=1, buff=0.18)
        rng_bg.move_to(rng.get_center())
        self.play(FadeIn(rng_bg, run_time=0.3),
                  FadeIn(rng, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)

        eg = Text(
            "e.g. f(x) = 2x+1: domain = range = R",
            font_size=22,
            color=GREEN_OK,
        )
        eg.next_to(rng, DOWN, buff=0.55)
        eg_bg = BackgroundRectangle(eg, color=BLACK,
                                    fill_opacity=0.95, buff=0.15)
        eg_bg.move_to(eg.get_center())
        self.play(FadeIn(eg_bg, run_time=0.3), FadeIn(eg, run_time=1.2))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, domain, domain_bg, rng, rng_bg,
                           eg, eg_bg)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: one input, many outputs is NOT a function (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("What is NOT a function?", font_size=26, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        bad = make_equation_card(
            r"y \;=\; \pm\sqrt{1-x^{2}}",
            color=RED_REJECT, scale=1.1,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.2)
        self.play(FadeIn(bad, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        bad_note = Text(
            "One x gives two y's — fails the function test.",
            font_size=20, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.4)
        bad_note_bg = BackgroundRectangle(bad_note, color=BLACK,
                                          fill_opacity=0.95, buff=0.15)
        bad_note_bg.move_to(bad_note.get_center())
        self.play(FadeIn(bad_note_bg, run_time=0.4),
                  FadeIn(bad_note, run_time=1.0))
        self.wait(3.0)

        beat4 = beat_group(head4, head4_bg, bad, bad_note, bad_note_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 120.9 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"f(x) \text{ is the output when } x \text{ is the input}",
            "Each input x produces exactly one output f(x).",
            final_wait=55.0,
        )