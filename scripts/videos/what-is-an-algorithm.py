"""
Manim scene for the lesson `what-is-an-algorithm`
(topic `l8-a-algorithms-testing`).

An algorithm is a finite, ordered set of clear steps that always
produces the same result for the same input.

Target duration: ~94 s (matches audio).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK,
    make_equation_card, animate_intro, animate_final_definition,
)
from manim import *


class WhatIsAnAlgorithmScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "What is an algorithm?",
            "A finite, ordered set of clear steps.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The three requirements (~25 s)
        # ──────────────────────────────────────────────────────────────────
        # 1. Unambiguous
        # 2. Finite
        # 3. Effective
        req1 = Text("1. Unambiguous", font_size=26, color=BLUE_TERM)
        req2 = Text("2. Finite", font_size=26, color=TEAL_TERM)
        req3 = Text("3. Effective", font_size=26, color=ORANGE_TERM)
        reqs = VGroup(req1, req2, req3).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        reqs.move_to(BAND_CHART_CENTER + UP * 0.6)
        for r in reqs:
            r.set_z_index(2)
            r_bg = BackgroundRectangle(r, color=BLACK, fill_opacity=0.95, buff=0.2)
            r_bg.move_to(r.get_center())
            r.bg = r_bg

        self.play(FadeIn(req1.bg, run_time=0.4), FadeIn(req1, shift=RIGHT * 0.2, run_time=1.0))
        self.wait(2.0)
        self.play(FadeIn(req2.bg, run_time=0.4), FadeIn(req2, shift=RIGHT * 0.2, run_time=1.0))
        self.wait(2.0)
        self.play(FadeIn(req3.bg, run_time=0.4), FadeIn(req3, shift=RIGHT * 0.2, run_time=1.0))
        self.wait(3.0)

        # Annotations.
        ann1 = Text("every step has one meaning", font_size=20, color=BLUE_TERM)
        ann1.next_to(req1, RIGHT, buff=0.6)
        ann1_bg = BackgroundRectangle(ann1, color=BLACK, fill_opacity=0.9, buff=0.15)
        ann1_bg.move_to(ann1.get_center())
        self.play(FadeIn(ann1_bg, run_time=0.4), FadeIn(ann1, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(ann1_bg, run_time=0.3), FadeOut(ann1, run_time=0.3))

        ann2 = Text("terminates", font_size=20, color=TEAL_TERM)
        ann2.next_to(req2, RIGHT, buff=0.6)
        ann2_bg = BackgroundRectangle(ann2, color=BLACK, fill_opacity=0.9, buff=0.15)
        ann2_bg.move_to(ann2.get_center())
        self.play(FadeIn(ann2_bg, run_time=0.4), FadeIn(ann2, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(ann2_bg, run_time=0.3), FadeOut(ann2, run_time=0.3))

        ann3 = Text("each step can be done", font_size=20, color=ORANGE_TERM)
        ann3.next_to(req3, RIGHT, buff=0.6)
        ann3_bg = BackgroundRectangle(ann3, color=BLACK, fill_opacity=0.9, buff=0.15)
        ann3_bg.move_to(ann3.get_center())
        self.play(FadeIn(ann3_bg, run_time=0.4), FadeIn(ann3, run_time=1.0))
        self.wait(3.0)
        self.play(
            FadeOut(VGroup(req1, req1.bg, req2, req2.bg, req3, req3.bg,
                           ann3, ann3_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: divisibility by 3 (~25 s)
        # ──────────────────────────────────────────────────────────────────
        intro = Text("Divisibility by 3: sum the digits.", font_size=22, color=BLUE_TERM)
        intro.move_to(BAND_CHART_CENTER + UP * 1.3)
        intro_bg = BackgroundRectangle(intro, color=BLACK, fill_opacity=0.95, buff=0.18)
        intro_bg.move_to(intro.get_center())
        self.play(FadeIn(intro_bg, run_time=0.4), FadeIn(intro, run_time=1.2))
        self.wait(2.5)

        steps = VGroup(
            Text("Step 1: add the digits.", font_size=20, color=WHITE),
            Text("Step 2: is the sum divisible by 3?", font_size=20, color=WHITE),
            Text("Step 3: yes → original is; no → original isn't.", font_size=20, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        steps.move_to(BAND_CHART_CENTER + DOWN * 0.2)
        for s in steps:
            s.set_z_index(2)
            s.bg = BackgroundRectangle(s, color=BLACK, fill_opacity=0.9, buff=0.15)
            s.bg.move_to(s.get_center())
        self.play(
            FadeOut(VGroup(intro, intro_bg), run_time=0.8),
        )
        for s in steps:
            self.play(FadeIn(s.bg, run_time=0.3), FadeIn(s, run_time=0.9))
            self.wait(1.2)
        self.wait(2.0)
        self.play(FadeOut(VGroup(*[s for s in steps], *[s.bg for s in steps]), run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Pseudocode block (~18 s)
        # ──────────────────────────────────────────────────────────────────
        pseudo_title = Text("Pseudocode:", font_size=22, color=GREEN_OK)
        pseudo_title.move_to(BAND_CHART_CENTER + UP * 1.5)
        pseudo_title_bg = BackgroundRectangle(pseudo_title, color=BLACK, fill_opacity=0.95, buff=0.15)
        pseudo_title_bg.move_to(pseudo_title.get_center())
        self.play(FadeIn(pseudo_title_bg, run_time=0.4), FadeIn(pseudo_title, run_time=1.0))
        self.wait(1.5)

        pseudo = Text(
            "if sum_of_digits(n) mod 3 == 0:\n"
            "    return 'yes'\n"
            "else:\n"
            "    return 'no'",
            font_size=22,
            color=BLUE_TERM,
            font="Courier New",
        ).move_to(BAND_CHART_CENTER + UP * 0.0)
        pseudo_bg = BackgroundRectangle(pseudo, color=BLACK, fill_opacity=0.95, buff=0.25)
        pseudo_bg.move_to(pseudo.get_center())
        self.play(FadeIn(pseudo_bg, run_time=0.5), FadeIn(pseudo, run_time=2.0))
        self.wait(5.0)
        self.play(
            FadeOut(VGroup(pseudo_title, pseudo_title_bg, pseudo, pseudo_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~18 s, total ≈ 94 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Algorithm} \;=\; \text{unambiguous} + \text{finite} + \text{effective}",
            "A precise recipe that always terminates and always works.",
            final_wait=40.0,
        )