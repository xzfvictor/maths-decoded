"""
Manim scene for the lesson `distance`
(topic `l9-a-gradient-midpoint-distance`).

Distance between two points comes from Pythagoras' theorem.
distance = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )

Target duration: ~20 s (audio is short — 14 s; padded to final_wait).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class DistanceScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Distance between two points",
            "Pythagoras on the coordinate plane",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The formula (~4 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Distance = hypotenuse of a right triangle",
                    font_size=22, color=WHITE)
        head.move_to(BAND_CHART_CENTER + UP * 1.3)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        eq = make_equation_card(
            r"d \;=\; \sqrt{(x_{2}-x_{1})^{2} + (y_{2}-y_{1})^{2}}",
            color=BLUE_TERM, scale=1.05,
        )
        eq.move_to(BAND_CHART_CENTER + UP * 0.0)

        self.play(
            FadeIn(head_bg, run_time=0.3),
            FadeIn(head, run_time=0.7),
            FadeIn(eq, shift=UP * 0.2, run_time=1.4),
        )
        self.wait(2.0)

        beat1 = VGroup(head, head_bg, eq)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: (1,2) and (4,6) → 5 (~4 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("e.g.  (1, 2)  and  (4, 6):",
                     font_size=22, color=WHITE)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        eq2 = make_equation_card(
            r"d \;=\; \sqrt{(4-1)^{2} + (6-2)^{2}} \;=\; \sqrt{9 + 16} \;=\; \sqrt{25} \;=\; 5",
            color=GREEN_OK, scale=0.8,
        )
        eq2.move_to(BAND_CHART_CENTER + UP * 0.0)

        self.play(
            FadeIn(head2_bg, run_time=0.3),
            FadeIn(head2, run_time=0.7),
            FadeIn(eq2, shift=UP * 0.2, run_time=1.6),
        )
        self.wait(2.0)

        beat2 = VGroup(head2, head2_bg, eq2)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Final takeaway (final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"d \;=\; \sqrt{(x_{2}-x_{1})^{2} + (y_{2}-y_{1})^{2}}",
            "Horizontal gap and vertical gap form the two legs of a right triangle.",
            final_wait=57.0,
        )
