"""
Manim scene for the lesson `one-solution`
(topic `l10a-asp-trig-equations`).

Solve simple trig equations in [0, 2π) using a three-step recipe:
(1) find the principal (acute) angle, (2) identify which quadrants
give the right sign, (3) use the symmetry that the second-quadrant
angle equals π - α. Worked example: sin θ = ½ gives π/6 and 5π/6.
Tip: double-check the calculator is in the right units.

Target duration: ~80 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class OneSolutionScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Trig equations with two solutions",
            "Find the principal angle, then the symmetry angle.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The question: sin θ = ½ (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        eq = make_equation_card(r"\sin(\theta) \;=\; 0.5",
                                color=BLUE_TERM, scale=1.1)
        eq.move_to(BAND_CHART_CENTER + UP * 0.95)
        beat_2 = beat_group(beat_2, eq)
        self.play(FadeIn(eq, run_time=1.4))
        self.wait(1.5)

        # Principal angle.
        principal = MathTex(
            r"\alpha \;=\; \dfrac{\pi}{6} \quad (30^{\circ})",
            color=ORANGE_TERM,
        ).scale(1.0)
        principal.next_to(eq, DOWN, buff=0.55)
        principal_bg = BackgroundRectangle(principal, color=BLACK,
                                            fill_opacity=1, buff=0.18)
        principal_bg.move_to(principal.get_center())
        beat_2 = beat_group(beat_2, principal, principal_bg)
        self.play(FadeIn(principal_bg, run_time=0.4), FadeIn(principal, run_time=1.4))
        self.wait(2.5)

        # Where sine is positive.
        where = Text("Sine is positive in quadrants I and II.",
                     font_size=22, color=BLUE_TERM)
        where.next_to(principal, DOWN, buff=0.45)
        where_bg = BackgroundRectangle(where, color=BLACK, fill_opacity=0.95, buff=0.15)
        where_bg.move_to(where.get_center())
        beat_2 = beat_group(beat_2, where, where_bg)
        self.play(FadeIn(where_bg, run_time=0.4), FadeIn(where, run_time=1.2))
        self.wait(5.5)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Two solutions: π/6 and 5π/6 (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        ans1 = make_term_card(r"\dfrac{\pi}{6}", "Q I", BLUE_TERM)
        ans2 = make_term_card(r"\dfrac{5\pi}{6}", "Q II", TEAL_TERM)
        pair = VGroup(ans1, ans2).arrange(RIGHT, buff=1.4)
        pair.move_to(BAND_CHART_CENTER + UP * 0.7)
        for m in pair:
            m.set_z_index(2)
        beat_3 = beat_group(beat_3, ans1, ans2)
        self.play(FadeIn(ans1, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)
        self.play(FadeIn(ans2, shift=UP * 0.2, run_time=1.2))
        self.wait(2.0)

        rel = MathTex(
            r"\text{2nd angle} \;=\; \pi \;-\; \alpha",
            color=GREEN_OK,
        ).scale(0.95)
        rel.next_to(pair, DOWN, buff=0.7)
        rel_bg = BackgroundRectangle(rel, color=BLACK, fill_opacity=0.95, buff=0.18)
        rel_bg.move_to(rel.get_center())
        beat_3 = beat_group(beat_3, rel, rel_bg)
        self.play(FadeIn(rel_bg, run_time=0.4), Write(rel, run_time=1.5))
        self.wait(7.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Cosine and tangent quadrant map (~15 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        head = Text("Which quadrants are positive?",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.05)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_4 = beat_group(beat_4, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        qmap = MathTex(
            r"\sin:\,\text{I,\,II} \quad \cos:\,\text{I,\,IV} \quad \tan:\,\text{I,\,III}",
            color=GREEN_OK,
        ).scale(0.95)
        qmap.next_to(head, DOWN, buff=0.5)
        qmap_bg = BackgroundRectangle(qmap, color=BLACK, fill_opacity=1, buff=0.2)
        qmap_bg.move_to(qmap.get_center())
        beat_4 = beat_group(beat_4, qmap, qmap_bg)
        self.play(FadeIn(qmap_bg, run_time=0.4), Write(qmap, run_time=1.8))
        self.wait(8.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Tip: degrees vs radians (~13 s)
        # ──────────────────────────────────────────────────────────────────
        tip = Text(
            "Tip: check your calculator is in degrees or radians.",
            font_size=24,
            color=ORANGE_TERM,
        )
        tip.move_to(BAND_CHART_CENTER + UP * 0.9)
        tip_bg = BackgroundRectangle(tip, color=BLACK, fill_opacity=1, buff=0.2)
        tip_bg.move_to(tip.get_center())
        self.play(FadeIn(tip_bg, run_time=0.4), FadeIn(tip, run_time=1.4))
        self.wait(11.0)
        self.play(FadeOut(VGroup(tip, tip_bg), run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (~35 s, total ≈ 80 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\sin\theta = 0.5 \;\Rightarrow\; \theta = \dfrac{\pi}{6},\;\dfrac{5\pi}{6}",
            "Principal angle, then the symmetry angle from the right quadrant.",
            final_wait=35.0,
        )
