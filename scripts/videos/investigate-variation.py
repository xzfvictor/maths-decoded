"""
Manim scene for the lesson `investigate-variation`
(topic `l10a-aa-functions-relations`).

Three patterns of variation: direct (y = kx), inverse (y = k/x), and
joint (z = kxy). The animation compares side-by-side formula cards and
points out the qualitative shape of each.

Target duration: ~82.4 s (matches the audio narration length).
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


class InvestigateVariationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Direct, inverse, joint variation",
            "Three patterns that show how quantities change together.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Direct variation: y = kx (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Direct variation", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.45)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        direct = make_equation_card(
            r"y \;=\; k\,x",
            color=BLUE_TERM, scale=1.0,
        )
        direct.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(direct, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        dnote = Text(
            "Doubling x doubles y. Straight line through origin.",
            font_size=20, color=WHITE,
        )
        dnote.next_to(direct, DOWN, buff=0.55)
        dnote_bg = BackgroundRectangle(dnote, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        dnote_bg.move_to(dnote.get_center())
        self.play(FadeIn(dnote_bg, run_time=0.4),
                  FadeIn(dnote, run_time=1.0))
        self.wait(2.0)

        eg = make_equation_card(
            r"\text{e.g. } y = 3x:\ (1,3),(2,6),(3,9)",
            color=BLUE_TERM, scale=0.65,
        )
        eg.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        self.play(FadeIn(eg, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        beat2 = beat_group(head, head_bg, direct, dnote, dnote_bg, eg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Inverse variation: y = k/x (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Inverse variation", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        inv = make_equation_card(
            r"y \;=\; \dfrac{k}{x}",
            color=TEAL_TERM, scale=1.3,
        )
        inv.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(inv, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        inote = Text(
            "Doubling x halves y. Hyperbola.",
            font_size=20, color=WHITE,
        ).next_to(inv, DOWN, buff=0.4)
        inote_bg = BackgroundRectangle(inote, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        inote_bg.move_to(inote.get_center())
        self.play(FadeIn(inote_bg, run_time=0.4),
                  FadeIn(inote, run_time=1.0))
        self.wait(2.0)

        beat3 = beat_group(head3, head3_bg, inv, inote, inote_bg)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Joint variation: z = kxy (~10 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Joint variation", font_size=26, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        joint = make_equation_card(
            r"z \;=\; k\,x\,y",
            color=ORANGE_TERM, scale=1.3,
        )
        joint.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(joint, shift=UP * 0.2, run_time=1.6))
        self.wait(1.5)

        jnote = Text(
            "z scales with the product of x and y.",
            font_size=20, color=WHITE,
        ).next_to(joint, DOWN, buff=0.4)
        jnote_bg = BackgroundRectangle(jnote, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        jnote_bg.move_to(jnote.get_center())
        self.play(FadeIn(jnote_bg, run_time=0.4),
                  FadeIn(jnote, run_time=1.0))
        self.wait(1.5)

        beat4 = beat_group(head4, head4_bg, joint, jnote, jnote_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 82.4 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y=kx,\ y=\tfrac{k}{x},\ z=kxy",
            "Pick the form that matches how the quantities change.",
            final_wait=37.0,
        )