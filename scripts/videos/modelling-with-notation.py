"""
Manim scene for the lesson `modelling-with-notation`
(topic `l10a-aa-function-notation`).

Turn a word problem into a function f(x). Example: taxi fare where the
base fee is $3 and each km costs $2 — f(x) = 3 + 2x. Use f(8) to find
the fare for an 8 km trip.

Target duration: ~96.6 s (matches the audio narration length).
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


class ModellingWithNotationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Modelling with f(x)",
            "Turn a word problem into a function.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Word problem (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Word problem", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        word = Text(
            "A taxi charges $3 flag-fall plus $2 per km.",
            font_size=22, color=WHITE,
        ).move_to(BAND_CHART_CENTER + UP * 0.4)
        word_bg = BackgroundRectangle(word, color=BLACK, fill_opacity=0.95, buff=0.18)
        word_bg.move_to(word.get_center())
        self.play(FadeIn(word_bg, run_time=0.5), FadeIn(word, run_time=1.4))
        self.wait(2.0)

        q = Text(
            "Let f(x) be the fare for x kilometres.",
            font_size=22, color=BLUE_TERM,
        ).next_to(word, DOWN, buff=0.45)
        q_bg = BackgroundRectangle(q, color=BLACK, fill_opacity=0.95, buff=0.18)
        q_bg.move_to(q.get_center())
        self.play(FadeIn(q_bg, run_time=0.5), FadeIn(q, run_time=1.2))
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, word, word_bg, q, q_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Build the function f(x) = 3 + 2x (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Translate to f(x)", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        fn = make_equation_card(
            r"f(x) \;=\; 3 + 2x",
            color=GREEN_OK, scale=1.3,
        )
        fn.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(fn, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        leg1 = Text("3  =  base flag-fall",
                    font_size=20, color=BLUE_TERM)
        leg1.move_to(BAND_CHART_CENTER + DOWN * 0.4)
        leg1_bg = BackgroundRectangle(leg1, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        leg1_bg.move_to(leg1.get_center())
        self.play(FadeIn(leg1_bg, run_time=0.4), FadeIn(leg1, run_time=1.0))
        self.wait(1.0)

        leg2 = Text("2x =  $2 per kilometre, times x km",
                    font_size=20, color=BLUE_TERM)
        leg2.next_to(leg1, DOWN, buff=0.3)
        leg2_bg = BackgroundRectangle(leg2, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        leg2_bg.move_to(leg2.get_center())
        self.play(FadeIn(leg2_bg, run_time=0.4), FadeIn(leg2, run_time=1.0))
        self.wait(2.0)

        beat3 = beat_group(head3, head3_bg, fn, leg1, leg1_bg, leg2, leg2_bg)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Use f(8) to find fare (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Evaluate", font_size=26, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        plug = make_equation_card(
            r"f(8) \;=\; 3 + 2(8)",
            color=ORANGE_TERM, scale=1.1,
        )
        plug.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(plug, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        ans = make_equation_card(
            r"\;=\; 3 + 16 \;=\; \$19",
            color=GREEN_OK, scale=1.1,
        )
        ans.next_to(plug, DOWN, buff=0.7)
        self.play(FadeIn(ans, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        summary = Text("8 km trip costs $19.",
                       font_size=22, color=GREEN_OK)
        summary.next_to(ans, DOWN, buff=0.4)
        summary_bg = BackgroundRectangle(summary, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        summary_bg.move_to(summary.get_center())
        self.play(FadeIn(summary_bg, run_time=0.4),
                  FadeIn(summary, run_time=1.0))
        self.wait(3.0)

        beat4 = beat_group(head4, head4_bg, plug, ans, summary, summary_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 96.6 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"f(x) = \text{output formula},\ \text{from a real situation}",
            "Identify the input, the rate, and any fixed cost.",
            final_wait=43.0,
        )