"""
Manim scene for the lesson `what-is-algorithm`
(topic `l10a-aa-algorithms-simulations`).

An algorithm is a finite, ordered, repeatable list of steps that always
finishes. The animation walks through a "find the largest of three numbers"
example, shows pseudocode, and rejects the mistake of writing an infinite loop.

Target duration: ~103.5 s (matches the audio narration length).
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


class WhatIsAlgorithmL10aAaScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "What is an algorithm?",
            "Finite, ordered, repeatable steps that always finish.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: largest of three numbers (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Find the largest of three numbers",
                    font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        # Three inputs.
        inputs = VGroup(
            MathTex(r"a = 4", color=BLUE_TERM).scale(1.0),
            MathTex(r"b = 9", color=BLUE_TERM).scale(1.0),
            MathTex(r"c = 6", color=BLUE_TERM).scale(1.0),
        ).arrange(RIGHT, buff=0.7)
        inputs.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in inputs:
            mb = BackgroundRectangle(m, color=BLACK, fill_opacity=0.95, buff=0.12)
            mb.move_to(m.get_center())
            m.bg = mb
            beat_2 = beat_group(beat_2, m, mb)
        for m in inputs:
            self.play(FadeIn(m.bg, run_time=0.2), FadeIn(m, run_time=0.5))
        self.wait(1.0)

        # Step list.
        steps_text = [
            (r"1.\;\text{set } M = a",                         BLUE_TERM),
            (r"2.\;\text{if } b > M,\; \text{set } M = b",     TEAL_TERM),
            (r"3.\;\text{if } c > M,\; \text{set } M = c",     ORANGE_TERM),
            (r"4.\;\text{output } M",                          GREEN_OK),
        ]
        steps = VGroup()
        for txt, color in steps_text:
            steps.add(MathTex(txt, color=color).scale(0.9))
        steps.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        steps.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        for s in steps:
            sb = BackgroundRectangle(s, color=BLACK, fill_opacity=0.95, buff=0.12)
            sb.move_to(s.get_center())
            s.bg = sb
            beat_2 = beat_group(beat_2, s, sb)
        for s in steps:
            self.play(FadeIn(s.bg, run_time=0.2), FadeIn(s, run_time=0.6))
            self.wait(0.5)
        self.wait(1.5)

        # Final answer.
        ans = MathTex(r"M = 9", color=GREEN_OK).scale(1.4)
        ans.move_to(BAND_CHART_CENTER + DOWN * 1.9)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.2)
        ans_bg.move_to(ans.get_center())
        beat_2 = beat_group(beat_2, ans, ans_bg)
        self.play(FadeIn(ans_bg, run_time=0.3), Write(ans, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Pseudocode is informal but exact (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head3 = Text("Written as pseudocode", font_size=26, color=BLUE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        beat_3 = beat_group(beat_3, head3, head3_bg)
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        pseudo = VGroup(
            Text("read a, b, c", font_size=22, color=WHITE),
            Text("M ← a", font_size=22, color=WHITE),
            Text("if b > M then M ← b", font_size=22, color=WHITE),
            Text("if c > M then M ← c", font_size=22, color=WHITE),
            Text("output M", font_size=22, color=GREEN_OK),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        pseudo.move_to(BAND_CHART_CENTER)
        for p in pseudo:
            pb = BackgroundRectangle(p, color=BLACK, fill_opacity=0.95, buff=0.12)
            pb.move_to(p.get_center())
            p.bg = pb
            beat_3 = beat_group(beat_3, p, pb)
        for p in pseudo:
            self.play(FadeIn(p.bg, run_time=0.2), FadeIn(p, run_time=0.5))
            self.wait(0.4)
        self.wait(1.5)

        # Caption explaining "pseudocode".
        cap = Text(
            "Plain English + a few symbols — anyone can read it.",
            font_size=22, color=GREEN_OK,
        ).next_to(pseudo, DOWN, buff=0.5)
        cap_bg = BackgroundRectangle(cap, color=BLACK, fill_opacity=0.95, buff=0.15)
        cap_bg.move_to(cap.get_center())
        beat_3 = beat_group(beat_3, cap, cap_bg)
        self.play(FadeIn(cap_bg, run_time=0.3), FadeIn(cap, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: an infinite loop is NOT an algorithm (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        head4 = Text("Not an algorithm", font_size=26, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        beat_4 = beat_group(beat_4, head4, head4_bg)
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        bad = MathTex(
            r"\text{while True: } M = M + 1",
            color=RED_REJECT,
        ).scale(1.0)
        bad.move_to(BAND_CHART_CENTER + UP * 0.4)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        beat_4 = beat_group(beat_4, bad, bad_bg)
        self.play(FadeIn(bad_bg, run_time=0.4), Write(bad, run_time=1.6))
        self.wait(1.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        beat_4 = beat_group(beat_4, cross)
        self.play(Create(cross, run_time=0.8))

        fix = Text(
            "It never stops — algorithms must terminate.",
            font_size=22, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        beat_4 = beat_group(beat_4, fix, fix_bg)
        self.play(FadeIn(fix_bg, run_time=0.3), FadeIn(fix, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=47 s, total ≈ 103.5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Algorithm} = \text{finite, ordered, repeatable steps with an output}",
            "Iterate, check, refine — bisection is a famous example.",
            final_wait=47.0,
        )
