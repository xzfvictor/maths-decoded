"""
Manim scene for the lesson `trig-ratios-constant`
(topic `l9-sp-trig-ratios-similar`).

When you scale a right triangle by a factor k, the k cancels in any
ratio of two sides. That is why sin, cos and tan of an angle are the
same for every right triangle with that angle.

Target duration: ≈ 44 s (matches audio + 20 s hold).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, animate_intro, animate_final_definition,
)
from manim import *


class TrigRatiosConstantScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Why trig ratios are constant",
            "Scale cancels — the ratio depends only on the angle.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Two similar right triangles share sin theta (~10 s)
        # ──────────────────────────────────────────────────────────────────
        # Small 3-4-5 (opposite = 3, hypotenuse = 5) and a 6-8-10 (k = 2).
        # Sized so both fit inside the safe area (y ∈ [-1.5, 1.8]).
        small = Polygon(
            [-4.5, -1.0, 0], [-4.5, 1.5, 0], [-2.5, -1.0, 0],
            color=BLUE_TERM, stroke_width=4,
        )
        big = Polygon(
            [1.0, -1.5, 0], [1.0, 1.5, 0], [4.5, -1.5, 0],
            color=TEAL_TERM, stroke_width=4,
        )
        self.play(Create(small, run_time=1.2))
        self.wait(0.6)
        self.play(Create(big, run_time=1.2))
        self.wait(1.0)

        # Annotate the opposite and hypotenuse on each.
        small_anno = MathTex(
            r"\text{opp} = 3,\; \text{hyp} = 5",
            color=BLUE_TERM,
        ).scale(0.7).next_to(small, DOWN, buff=0.25)
        small_anno_bg = BackgroundRectangle(small_anno, color=BLACK, fill_opacity=0.95, buff=0.1)
        small_anno_bg.move_to(small_anno.get_center())

        big_anno = MathTex(
            r"\text{opp} = 6,\; \text{hyp} = 10",
            color=TEAL_TERM,
        ).scale(0.7).next_to(big, DOWN, buff=0.25)
        big_anno_bg = BackgroundRectangle(big_anno, color=BLACK, fill_opacity=0.95, buff=0.1)
        big_anno_bg.move_to(big_anno.get_center())

        self.play(FadeIn(small_anno_bg, run_time=0.2), FadeIn(small_anno, run_time=0.7))
        self.play(FadeIn(big_anno_bg, run_time=0.2), FadeIn(big_anno, run_time=0.7))
        self.wait(1.0)

        # Show the two ratios side by side.
        r1 = MathTex(r"\sin\theta = \dfrac{3}{5} = 0.6", color=BLUE_TERM).scale(0.85)
        r1.move_to(BAND_CHART_CENTER + DOWN * 2.2 + LEFT * 3.0)
        r1_bg = BackgroundRectangle(r1, color=BLACK, fill_opacity=1, buff=0.18)
        r1_bg.move_to(r1.get_center())

        r2 = MathTex(r"\sin\theta = \dfrac{6}{10} = 0.6", color=TEAL_TERM).scale(0.85)
        r2.move_to(BAND_CHART_CENTER + DOWN * 2.2 + RIGHT * 3.0)
        r2_bg = BackgroundRectangle(r2, color=BLACK, fill_opacity=1, buff=0.18)
        r2_bg.move_to(r2.get_center())

        self.play(FadeIn(r1_bg, run_time=0.3), Write(r1, run_time=1.2))
        self.wait(0.3)
        self.play(FadeIn(r2_bg, run_time=0.3), Write(r2, run_time=1.2))
        self.wait(1.0)

        beat2_group = VGroup(
            small, big,
            small_anno, small_anno_bg, big_anno, big_anno_bg,
            r1, r1_bg, r2, r2_bg,
        )
        self.play(FadeOut(beat2_group, run_time=1.1))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The k cancels — algebra (~9 s)
        # ──────────────────────────────────────────────────────────────────
        title_k = MathTex(
            r"\sin\theta \;=\; \dfrac{\text{opposite}}{\text{hypotenuse}}",
            color=WHITE,
        ).scale(0.85)
        title_k.move_to(BAND_CHART_CENTER + UP * 1.2)
        title_k_bg = BackgroundRectangle(title_k, color=BLACK, fill_opacity=1, buff=0.25)
        title_k_bg.move_to(title_k.get_center())
        self.play(FadeIn(title_k_bg, run_time=0.4), Write(title_k, run_time=1.6))
        self.wait(1.2)
        self.wait(0.5)

        # Scale by k: both sides multiply by k.
        scaled = MathTex(
            r"\sin\theta \;=\; \dfrac{k \cdot \text{opp}}{k \cdot \text{hyp}}",
            color=YELLOW,
        ).scale(0.85)
        scaled.next_to(title_k, DOWN, buff=0.5)
        scaled_bg = BackgroundRectangle(scaled, color=BLACK, fill_opacity=1, buff=0.25)
        scaled_bg.move_to(scaled.get_center())
        self.play(FadeIn(scaled_bg, run_time=0.4), Write(scaled, run_time=1.6))
        self.wait(1.5)
        self.wait(0.5)

        # k cancels — show the result with all three colours.
        cancel = MathTex(
            r"\sin\theta \;=\; \dfrac{\text{opp}}{\text{hyp}}",
            color=GREEN_OK,
        ).scale(0.85)
        cancel.next_to(scaled, DOWN, buff=0.5)
        cancel_bg = BackgroundRectangle(cancel, color=BLACK, fill_opacity=1, buff=0.25)
        cancel_bg.move_to(cancel.get_center())
        self.play(FadeIn(cancel_bg, run_time=0.4), Write(cancel, run_time=1.6))
        self.wait(1.5)

        # Box the final equal.
        box = SurroundingRectangle(cancel, color=GREEN_OK, buff=0.25, stroke_width=3)
        self.play(Create(box, run_time=0.8))
        self.wait(1.0)

        beat3_group = VGroup(
            title_k, title_k_bg, scaled, scaled_bg, cancel, cancel_bg, box,
        )
        self.play(FadeOut(beat3_group, run_time=1.1))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Same for cos and tan — quick win (~2 s)
        # ──────────────────────────────────────────────────────────────────
        same = MathTex(
            r"\cos\theta,\; \tan\theta \;=\; \dfrac{\text{adj}}{\text{hyp}},\; \dfrac{\text{opp}}{\text{adj}}",
            color=GREEN_OK,
        ).scale(0.8)
        same.move_to(BAND_CHART_CENTER + UP * 0.5)
        same_bg = BackgroundRectangle(same, color=BLACK, fill_opacity=1, buff=0.22)
        same_bg.move_to(same.get_center())
        self.play(FadeIn(same_bg, run_time=0.3), Write(same, run_time=1.4))
        self.wait(0.6)

        beat4_group = VGroup(same, same_bg)
        self.play(FadeOut(beat4_group, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final boxed takeaway (held; final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\sin\theta,\; \cos\theta,\; \tan\theta \;=\; \text{constant for a given } \theta",
            "Similar right triangles give the same three ratios.",
            final_wait=70.6,
        )
