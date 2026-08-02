"""
Manim scene for the lesson `pythagoras-theorem`
(topic `l8-m-pythagoras`).

For a right-angled triangle, a² + b² = c² where c is the hypotenuse.
The scene builds a concrete 3-4-5 triangle, generalises the theorem,
and rejects the mistake of using it on a non-right triangle.

Target duration: ~88 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class PythagorasTheoremScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Pythagoras' theorem",
            "a² + b² = c² for any right-angled triangle",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Draw a right triangle, label a, b, c, then verify 3-4-5
        # (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        # 3-4-5 right triangle: legs 3 (horizontal) and 4 (vertical).
        A = np.array([-1.5, -1.0, 0.0])  # right-angle corner
        B = np.array([1.5, -1.0, 0.0])   # other end of leg a (= 3 wide)
        C = np.array([-1.5, 2.0, 0.0])   # shortened to stay below the subtitle

        tri = Polygon(A, B, C, color=BLUE_TERM, stroke_width=4)
        tri.move_to(BAND_CHART_CENTER + DOWN * 0.1)
        beat_2 = beat_group(beat_2, tri)

        # Right-angle marker at the triangle's shifted A vertex.
        right_mark = Square(
            side_length=0.3, color=BLUE_TERM, stroke_width=2
        ).move_to(tri.get_vertices()[0] + RIGHT * 0.15 + UP * 0.15)
        beat_2 = beat_group(beat_2, right_mark)

        # Side labels.
        a_lbl = MathTex("a = 3", color=BLUE_TERM).scale(0.9)
        a_lbl.next_to(tri, DOWN, buff=0.3)
        a_bg = BackgroundRectangle(a_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        a_bg.move_to(a_lbl.get_center())

        b_lbl = MathTex("b = 4", color=TEAL_TERM).scale(0.9)
        b_lbl.next_to(tri, LEFT, buff=0.3)
        b_bg = BackgroundRectangle(b_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        b_bg.move_to(b_lbl.get_center())

        c_lbl = MathTex("c = 5", color=ORANGE_TERM).scale(0.9)
        c_lbl.next_to(tri.get_center(), UR, buff=0.2).shift(LEFT * 0.1)
        c_bg = BackgroundRectangle(c_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        c_bg.move_to(c_lbl.get_center())
        beat_2 = beat_group(
            beat_2, a_bg, a_lbl, b_bg, b_lbl, c_bg, c_lbl,
        )

        self.play(Create(tri, run_time=1.4))
        self.play(Create(right_mark, run_time=0.6))
        self.wait(0.5)
        self.play(FadeIn(a_bg, run_time=0.3), FadeIn(a_lbl, run_time=0.8))
        self.play(FadeIn(b_bg, run_time=0.3), FadeIn(b_lbl, run_time=0.8))
        self.play(FadeIn(c_bg, run_time=0.3), FadeIn(c_lbl, run_time=0.8))
        self.wait(2.0)

        # Verify: 3² + 4² = 9 + 16 = 25 = 5².
        verify = MathTex(r"3^{2} + 4^{2} = 9 + 16 = 25 = 5^{2}", color=GREEN_OK).scale(1.0)
        verify.next_to(tri, DOWN, buff=0.8)
        verify_bg = BackgroundRectangle(verify, color=BLACK, fill_opacity=1, buff=0.2)
        verify_bg.move_to(verify.get_center())
        beat_2 = beat_group(beat_2, verify_bg, verify)
        self.play(FadeIn(verify_bg, run_time=0.4), Write(verify, run_time=1.8))
        self.wait(3.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: a² + b² = c² for any right triangle (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        general = make_equation_card(r"a^{2} + b^{2} = c^{2}", color=BLUE_TERM, scale=1.6)
        general.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in general:
            m.set_z_index(2)
        beat_3 = beat_group(beat_3, general)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        rules = VGroup(
            MathTex(r"\text{legs: } a, b", color=BLUE_TERM).scale(0.95),
            MathTex(r"\text{hypotenuse (longest): } c", color=ORANGE_TERM).scale(0.95),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rules.next_to(general, DOWN, buff=0.5)
        rule_bgs = VGroup()
        for r in rules:
            bg = BackgroundRectangle(r, color=BLACK, fill_opacity=0.95, buff=0.15)
            bg.move_to(r.get_center())
            rule_bgs.add(bg)
        beat_3 = beat_group(beat_3, rule_bgs, rules)
        self.play(FadeIn(rule_bgs, run_time=0.4), FadeIn(rules, run_time=1.4))
        self.wait(3.0)
        # Two rearrangements.
        rearr = VGroup(
            MathTex(r"c = \sqrt{a^{2} + b^{2}}", color=GREEN_OK).scale(0.9),
            MathTex(r"a = \sqrt{c^{2} - b^{2}}", color=GREEN_OK).scale(0.9),
        ).arrange(RIGHT, buff=0.6)
        rearr.next_to(rules, DOWN, buff=0.5)
        rearr_bg = BackgroundRectangle(rearr, color=BLACK, fill_opacity=0.95, buff=0.18)
        rearr_bg.move_to(rearr.get_center())
        beat_3 = beat_group(beat_3, rearr_bg, rearr)
        self.play(FadeIn(rearr_bg, run_time=0.4), FadeIn(rearr, run_time=1.4))
        self.wait(3.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: applying Pythagoras to a non-right triangle
        # (~10 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        # Skewed triangle (no right angle), scaled into the chart band.
        D = np.array([-1.5, -1.0, 0.0])
        E = np.array([2.0, -1.0, 0.0])
        F = np.array([0.4, 2.4, 0.0])
        skewed = Polygon(D, E, F, color=RED_REJECT, stroke_width=3)
        skewed.scale(0.8).move_to(BAND_CHART_CENTER + DOWN * 0.1)
        beat_4 = beat_group(beat_4, skewed)

        self.play(Create(skewed, run_time=1.2))
        self.wait(1.5)

        warning = Text("No right angle → Pythagoras does NOT apply.",
                       font_size=22, color=RED_REJECT)
        warning.next_to(skewed, DOWN, buff=0.5)
        warning_bg = BackgroundRectangle(warning, color=BLACK, fill_opacity=0.95, buff=0.18)
        warning_bg.move_to(warning.get_center())
        beat_4 = beat_group(beat_4, warning_bg, warning)
        self.play(FadeIn(warning_bg, run_time=0.4), FadeIn(warning, run_time=1.2))
        self.wait(2.5)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~32 s, total ≈ 88 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{2} + b^{2} = c^{2}",
            "c is the hypotenuse — the side opposite the right angle.",
            final_wait=32.0,
        )
