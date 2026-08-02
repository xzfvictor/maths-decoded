"""
Manim scene for the lesson `testing-and-debugging`
(topic `l8-a-algorithms-testing`).

Run the algorithm on chosen inputs; use boundary and edge cases to
find errors, then fix and re-test.

Target duration: ~108 s (matches audio).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_equation_card, animate_intro, animate_final_definition,
)
from manim import *


class TestingAndDebuggingScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Testing and debugging algorithms",
            "Try good cases, then bad cases, then fix what broke.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Test case types (~25 s)
        # ──────────────────────────────────────────────────────────────────
        intro = Text("What makes a good test case?", font_size=24, color=WHITE)
        intro.move_to(BAND_CHART_CENTER + UP * 1.5)
        intro_bg = BackgroundRectangle(intro, color=BLACK, fill_opacity=0.95, buff=0.18)
        intro_bg.move_to(intro.get_center())
        self.play(FadeIn(intro_bg, run_time=0.4), FadeIn(intro, run_time=1.2))
        self.wait(2.0)

        cases = VGroup(
            Text("Typical: a regular input", font_size=22, color=BLUE_TERM),
            Text("Boundary: an edge value (empty, 1 element)", font_size=22, color=TEAL_TERM),
            Text("Edge: unusual but valid (duplicates)", font_size=22, color=ORANGE_TERM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        cases.move_to(BAND_CHART_CENTER + UP * 0.0)
        for c in cases:
            c.set_z_index(2)
            c.bg = BackgroundRectangle(c, color=BLACK, fill_opacity=0.9, buff=0.15)
            c.bg.move_to(c.get_center())
        for c in cases:
            self.play(FadeIn(c.bg, run_time=0.3), FadeIn(c, run_time=0.8))
            self.wait(1.5)
        self.wait(2.0)
        self.play(FadeOut(VGroup(intro, intro_bg), run_time=0.8))
        self.play(FadeOut(VGroup(*[c for c in cases], *[c.bg for c in cases]), run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Common bug types (~30 s)
        # ──────────────────────────────────────────────────────────────────
        intro3 = Text("Common bug types", font_size=24, color=WHITE)
        intro3.move_to(BAND_CHART_CENTER + UP * 1.5)
        intro3_bg = BackgroundRectangle(intro3, color=BLACK, fill_opacity=0.95, buff=0.18)
        intro3_bg.move_to(intro3.get_center())
        self.play(FadeIn(intro3_bg, run_time=0.4), FadeIn(intro3, run_time=1.2))
        self.wait(2.0)

        bugs = VGroup(
            Text("Off-by-one: loop runs one too few/many times", font_size=20, color=RED_REJECT),
            Text("Wrong operator: < instead of <=", font_size=20, color=RED_REJECT),
            Text("Misinitialised variable: starts at the wrong value", font_size=20, color=RED_REJECT),
            Text("Wrong step order: B done before A when order matters", font_size=20, color=RED_REJECT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        bugs.move_to(BAND_CHART_CENTER + UP * 0.0)
        for b in bugs:
            b.set_z_index(2)
            b.bg = BackgroundRectangle(b, color=BLACK, fill_opacity=0.9, buff=0.15)
            b.bg.move_to(b.get_center())
        for b in bugs:
            self.play(FadeIn(b.bg, run_time=0.3), FadeIn(b, run_time=0.8))
            self.wait(1.5)
        self.wait(2.0)
        self.play(FadeOut(VGroup(intro3, intro3_bg), run_time=0.8))
        self.play(FadeOut(VGroup(*[b for b in bugs], *[b.bg for b in bugs]), run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Fix-and-retest loop (~25 s)
        # ──────────────────────────────────────────────────────────────────
        intro4 = Text("The fix-and-retest loop", font_size=24, color=GREEN_OK)
        intro4.move_to(BAND_CHART_CENTER + UP * 1.5)
        intro4_bg = BackgroundRectangle(intro4, color=BLACK, fill_opacity=0.95, buff=0.18)
        intro4_bg.move_to(intro4.get_center())
        self.play(FadeIn(intro4_bg, run_time=0.4), FadeIn(intro4, run_time=1.2))
        self.wait(2.0)

        loop_steps = VGroup(
            Text("1. Run on a test case", font_size=22, color=BLUE_TERM),
            Text("2. If wrong, find the first bad line", font_size=22, color=ORANGE_TERM),
            Text("3. Fix it", font_size=22, color=GREEN_OK),
            Text("4. Re-test (failing + passing)", font_size=22, color=TEAL_TERM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        loop_steps.move_to(BAND_CHART_CENTER + UP * 0.0)
        for s in loop_steps:
            s.set_z_index(2)
            s.bg = BackgroundRectangle(s, color=BLACK, fill_opacity=0.9, buff=0.15)
            s.bg.move_to(s.get_center())
        for s in loop_steps:
            self.play(FadeIn(s.bg, run_time=0.3), FadeIn(s, run_time=0.8))
            self.wait(1.4)
        self.wait(2.0)
        self.play(
            FadeOut(VGroup(intro4, intro4_bg), run_time=0.8),
            FadeOut(VGroup(*[s for s in loop_steps], *[s.bg for s in loop_steps]), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~21 s, total ≈ 108 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Test} \;\to\; \text{Fix} \;\to\; \text{Re-test}",
            "Use typical, boundary, and edge cases — not just nice inputs.",
            final_wait=55.0,
        )