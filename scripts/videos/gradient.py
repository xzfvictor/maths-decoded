"""
Manim scene for the lesson `gradient`
(topic `l9-a-gradient-midpoint-distance`).

Gradient (slope) of a line through (x1, y1) and (x2, y2):
  m = (y2 - y1) / (x2 - x1)

Rises (vertical change) over runs (horizontal change).

Target duration: ~20 s (audio is short — 17 s; padded to final_wait).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class GradientScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Gradient of a line segment",
            "Rise over run: vertical change ÷ horizontal change",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The formula (~4 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Gradient = rise ÷ run",
                    font_size=22, color=WHITE)
        head.move_to(BAND_CHART_CENTER + UP * 1.3)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        eq = make_equation_card(
            r"m \;=\; \dfrac{y_{2} - y_{1}}{x_{2} - x_{1}}",
            color=BLUE_TERM, scale=1.1,
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
        # Beat 3 — Worked example: (1, 3) and (5, 11) → 8/4 = 2 (~5 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text("e.g.  (1, 3)  and  (5, 11):",
                     font_size=22, color=WHITE)
        head2.move_to(BAND_CHART_CENTER + UP * 1.3)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())

        eq2 = make_equation_card(
            r"m \;=\; \dfrac{11 - 3}{5 - 1} \;=\; \dfrac{8}{4} \;=\; 2",
            color=GREEN_OK, scale=0.95,
        )
        eq2.move_to(BAND_CHART_CENTER + UP * 0.0)

        self.play(
            FadeIn(head2_bg, run_time=0.3),
            FadeIn(head2, run_time=0.7),
            FadeIn(eq2, shift=UP * 0.2, run_time=1.4),
        )
        self.wait(2.0)

        beat2 = VGroup(head2, head2_bg, eq2)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Sign convention note (~2 s)
        # ──────────────────────────────────────────────────────────────────
        sign = Text(
            "m > 0 line rises to the right;  m < 0 line falls.",
            font_size=22, color=GREEN_OK,
        )
        sign.move_to(BAND_CHART_CENTER + UP * 0.0)
        sign_bg = BackgroundRectangle(sign, color=BLACK, fill_opacity=0.95, buff=0.18)
        sign_bg.move_to(sign.get_center())

        self.play(FadeIn(sign_bg, run_time=0.4), FadeIn(sign, run_time=1.0))
        self.wait(1.0)
        self.play(FadeOut(VGroup(sign, sign_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"m \;=\; \dfrac{y_{2} - y_{1}}{x_{2} - x_{1}}",
            "Rise over run: how much y changes per unit of x.",
            final_wait=93.4,
        )
