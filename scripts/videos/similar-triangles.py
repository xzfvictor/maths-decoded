"""
Manim scene for the lesson `similar-triangles`
(topic `l9-sp-trig-ratios-similar`).

Two triangles are similar when their angles match and their sides
are in proportion. We draw two right triangles that share an
angle, show the matching-angle equality, then reveal the scale
factor relationship between matching sides.

Target duration: ~96.08 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SimilarTrianglesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Similar triangles",
            "Same angles, sides in proportion.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Two similar right triangles side by side (~25 s)
        # ──────────────────────────────────────────────────────────────────
        # Small triangle on the left, larger similar on the right.
        # Both are 3-4-5 right triangles so they share all three angles.
        small = Polygon(
            [-5.5, -1.0, 0], [-5.5, 2.0, 0], [-1.5, -1.0, 0],
            color=BLUE_TERM, stroke_width=4,
        )
        big = Polygon(
            [1.0, -2.0, 0], [1.0, 4.0, 0], [9.0, -2.0, 0],
            color=TEAL_TERM, stroke_width=4,
        )

        self.play(Create(small, run_time=1.6))
        self.wait(1.0)
        self.play(Create(big, run_time=1.6))
        self.wait(2.0)

        # Angle labels on each — both triangles carry the same 3 angles.
        # Place the angle text at each vertex.
        sa = MathTex("90^\\circ", color=WHITE).scale(0.7).move_to([-5.7, -0.7, 0])
        sb = MathTex(r"\theta", color=BLUE_TERM).scale(0.9).move_to([-5.1, 0.7, 0])
        sc = MathTex(r"\phi", color=BLUE_TERM).scale(0.9).move_to([-3.3, -0.7, 0])
        ba = MathTex("90^\\circ", color=WHITE).scale(0.7).move_to([0.8, -1.7, 0])
        bb = MathTex(r"\theta", color=TEAL_TERM).scale(0.9).move_to([1.4, 1.3, 0])
        bc = MathTex(r"\phi", color=TEAL_TERM).scale(0.9).move_to([5.2, -1.7, 0])

        for m in [sa, sb, sc, ba, bb, bc]:
            bg = BackgroundRectangle(m, color=BLACK, fill_opacity=0.9, buff=0.1)
            bg.move_to(m.get_center())
            m.bg = bg

        self.play(
            FadeIn(sa.bg, run_time=0.3), FadeIn(sa, run_time=0.6),
            FadeIn(sb.bg, run_time=0.3), FadeIn(sb, run_time=0.6),
            FadeIn(sc.bg, run_time=0.3), FadeIn(sc, run_time=0.6),
        )
        self.wait(1.5)
        self.play(
            FadeIn(ba.bg, run_time=0.3), FadeIn(ba, run_time=0.6),
            FadeIn(bb.bg, run_time=0.3), FadeIn(bb, run_time=0.6),
            FadeIn(bc.bg, run_time=0.3), FadeIn(bc, run_time=0.6),
        )
        self.wait(2.5)

        # Caption: matching angles.
        cap = Text(
            "Both triangles share the same three angles.",
            font_size=22, color=GREEN_OK,
        )
        cap.move_to(BAND_CHART_CENTER + DOWN * 2.7)
        cap_bg = BackgroundRectangle(cap, color=BLACK, fill_opacity=0.95, buff=0.18)
        cap_bg.move_to(cap.get_center())
        self.play(FadeIn(cap_bg, run_time=0.4), FadeIn(cap, run_time=1.4))
        self.wait(3.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Sides in proportion; scale factor (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat2_group = VGroup(
            small, big, sa, sa.bg, sb, sb.bg, sc, sc.bg,
            ba, ba.bg, bb, bb.bg, bc, bc.bg, cap, cap_bg,
        )
        self.play(FadeOut(beat2_group, run_time=1.5))

        # The side-ratio equation.
        ratio = MathTex(
            r"\dfrac{a}{A} \;=\; \dfrac{b}{B} \;=\; \dfrac{c}{C} \;=\; k",
            color=WHITE,
        ).scale(1.05)
        ratio.move_to(BAND_CHART_CENTER + UP * 0.7)
        ratio_bg = BackgroundRectangle(ratio, color=BLACK, fill_opacity=1, buff=0.28)
        ratio_bg.move_to(ratio.get_center())
        self.play(FadeIn(ratio_bg, run_time=0.5), Write(ratio, run_time=2.2))
        self.wait(3.0)

        # k = 3 example.
        kv = MathTex(r"k = 3", color=GREEN_OK).scale(1.4)
        kv.next_to(ratio, DOWN, buff=0.6)
        kv_bg = BackgroundRectangle(kv, color=BLACK, fill_opacity=1, buff=0.22)
        kv_bg.move_to(kv.get_center())
        self.play(FadeIn(kv_bg, run_time=0.4), FadeIn(kv, run_time=1.2))
        self.wait(1.5)

        # Numerical illustration.
        num = MathTex(
            r"a = 3, \; A = 9 \;\Rightarrow\; \dfrac{a}{A} = \dfrac{1}{3} = k",
            color=WHITE,
        ).scale(0.85)
        num.next_to(kv, DOWN, buff=0.6)
        num_bg = BackgroundRectangle(num, color=BLACK, fill_opacity=0.95, buff=0.2)
        num_bg.move_to(num.get_center())
        self.play(FadeIn(num_bg, run_time=0.4), FadeIn(num, run_time=1.4))
        self.wait(4.0)

        beat3_group = VGroup(ratio, ratio_bg, kv, kv_bg, num, num_bg)
        self.play(FadeOut(beat3_group, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject "same perimeter" as a similarity test (~9 s)
        # ──────────────────────────────────────────────────────────────────
        bad = MathTex(
            r"\text{same perimeter} \;\not\!\!\!\Rightarrow\; \text{similar}",
            color=RED_REJECT,
        ).scale(1.0)
        bad.move_to(BAND_CHART_CENTER + UP * 0.5)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), Write(bad, run_time=1.6))
        self.wait(1.5)

        why = Text(
            "Equal perimeter says nothing about matching angles.",
            font_size=22, color=RED_REJECT,
        )
        why.next_to(bad, DOWN, buff=0.6)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.2))
        self.wait(2.5)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=0.9))
        self.wait(2.0)

        beat4_group = VGroup(bad, bad_bg, why, why_bg, cross)
        self.play(FadeOut(beat4_group, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final boxed takeaway (held; total ≈ 96 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Similar} \;\Longleftrightarrow\; \text{angles equal, sides in ratio } k",
            "Equal angles + proportional sides. Both must hold.",
            final_wait=36.0,
        )
