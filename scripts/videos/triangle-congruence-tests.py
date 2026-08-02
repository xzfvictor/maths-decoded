"""
Manim scene for the lesson `triangle-congruence-tests`
(topic `l8-sp-congruence-similarity`).

Two triangles are congruent if you can place one perfectly on top of the
other. Four shortcut tests prove congruence without checking every side
and angle: SSS, SAS, AAS, RHS. The scene introduces the four tests,
walks through a worked SAS example, and warns about including angles.

Target duration: ~99 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
)
from manim import *


def triangle_mobject(scale: float = 1.0, color=WHITE) -> VGroup:
    """A simple 3-4-5 right-ish triangle (for SAS demonstration)."""
    a = [-2 * scale, -1.5 * scale, 0]
    b = [2 * scale, -1.5 * scale, 0]
    c = [-2 * scale, 1.5 * scale, 0]
    sides = Polygon(a, b, c, color=color, stroke_width=4)
    return sides


class TriangleCongruenceTestsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Triangle congruence tests",
            "Four shortcuts — SSS, SAS, AAS, RHS — to prove congruence.",
            hold=1.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Name the four tests (~20 s)
        # ──────────────────────────────────────────────────────────────────
        # A 2x2 grid of the four test cards.
        sss = make_term_card(r"\text{SSS}", r"\text{3 sides}", BLUE_TERM)
        sas = make_term_card(r"\text{SAS}", r"\text{2 sides, included angle}", TEAL_TERM)
        aas = make_term_card(r"\text{AAS}", r"\text{2 angles, non-included side}", ORANGE_TERM)
        rhs = make_term_card(r"\text{RHS}", r"\text{right angle, hyp., side}", RED_REJECT)
        grid = VGroup(sss, sas, aas, rhs).arrange_in_grid(
            rows=2, cols=2, buff=0.5
        )
        grid.scale(0.75)
        grid.move_to(BAND_CHART_CENTER + UP * 0.5)
        for grp in grid:
            for m in grp:
                m.set_z_index(2)

        self.play(FadeIn(sss, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(sas, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(aas, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(rhs, shift=UP * 0.2, run_time=1.0))
        self.wait(4.0)

        # Highlight the "included" word in SAS.
        # Anchor the "included" text inside the safe area (y ∈ [-1.5, 1.8]).
        # The grid's bottom row labels sit around y = -1.0 (after scale 0.75),
        # so pin the text at y = -1.35 with no reliance on next_to chain.
        incl = Text("‘included’ = the angle BETWEEN the two sides", font_size=18, color=GREEN_OK)
        incl.move_to([0, -1.35, 0])
        incl_bg = BackgroundRectangle(incl, color=BLACK, fill_opacity=0.95, buff=0.15)
        incl_bg.move_to(incl.get_center())
        self.play(FadeIn(incl_bg, run_time=0.4), FadeIn(incl, run_time=1.2))
        self.wait(4.5)

        beat2 = VGroup(grid, incl, incl_bg)
        self.play(FadeOut(beat2, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: SAS (concrete) (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Two triangles with the same SAS fingerprint: same two sides
        # meeting at the same included angle — so they are congruent.
        tri1 = triangle_mobject(0.7, color=BLUE_TERM).shift(LEFT * 3.0 + UP * 0.7)
        tri2 = triangle_mobject(0.7, color=TEAL_TERM).shift(RIGHT * 3.0 + UP * 0.7)
        self.play(Create(tri1, run_time=1.5), Create(tri2, run_time=1.5))
        self.wait(2.0)

        # Side labels.
        lbl1 = MathTex("5", color=BLUE_TERM).scale(0.9).next_to(tri1, DOWN, buff=0.2)
        lbl2 = MathTex("5", color=TEAL_TERM).scale(0.9).next_to(tri2, DOWN, buff=0.2)
        lbl1_bg = BackgroundRectangle(lbl1, color=BLACK, fill_opacity=0.9, buff=0.1)
        lbl1_bg.move_to(lbl1.get_center())
        lbl2_bg = BackgroundRectangle(lbl2, color=BLACK, fill_opacity=0.9, buff=0.1)
        lbl2_bg.move_to(lbl2.get_center())
        self.play(FadeIn(lbl1, run_time=0.6), FadeIn(lbl2, run_time=0.6))
        self.wait(1.5)

        # Same side labels.
        lbl3 = MathTex("8", color=BLUE_TERM).scale(0.9).next_to(tri1, LEFT, buff=0.2)
        lbl4 = MathTex("8", color=TEAL_TERM).scale(0.9).next_to(tri2, RIGHT, buff=0.2)
        lbl3_bg = BackgroundRectangle(lbl3, color=BLACK, fill_opacity=0.9, buff=0.1)
        lbl3_bg.move_to(lbl3.get_center())
        lbl4_bg = BackgroundRectangle(lbl4, color=BLACK, fill_opacity=0.9, buff=0.1)
        lbl4_bg.move_to(lbl4.get_center())
        self.play(FadeIn(lbl3, run_time=0.6), FadeIn(lbl4, run_time=0.6))
        self.wait(1.5)

        # Included angle.
        ang1 = MathTex(r"60^\circ", color=BLUE_TERM).scale(0.9).move_to(tri1.get_center() + UP * 0.2 + RIGHT * 0.2)
        ang2 = MathTex(r"60^\circ", color=TEAL_TERM).scale(0.9).move_to(tri2.get_center() + UP * 0.2 + RIGHT * 0.2)
        ang1_bg = BackgroundRectangle(ang1, color=BLACK, fill_opacity=0.9, buff=0.1)
        ang1_bg.move_to(ang1.get_center())
        ang2_bg = BackgroundRectangle(ang2, color=BLACK, fill_opacity=0.9, buff=0.1)
        ang2_bg.move_to(ang2.get_center())
        self.play(FadeIn(ang1, run_time=0.6), FadeIn(ang2, run_time=0.6))
        self.wait(2.0)

        # Verdict.
        verdict = MathTex(r"\triangle ABC \cong \triangle DEF", color=GREEN_OK).scale(1.0)
        verdict.move_to(BAND_CHART_CENTER + DOWN * 2.0)
        verdict_bg = BackgroundRectangle(verdict, color=BLACK, fill_opacity=1, buff=0.2)
        verdict_bg.move_to(verdict.get_center())
        self.play(FadeIn(verdict_bg, run_time=0.5), Write(verdict, run_time=1.8))
        self.wait(3.5)

        beat3 = VGroup(tri1, tri2, lbl1, lbl2, lbl1_bg, lbl2_bg, lbl3, lbl4, lbl3_bg, lbl4_bg,
                       ang1, ang2, ang1_bg, ang2_bg, verdict, verdict_bg)
        self.play(FadeOut(beat3, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: two sides + a non-included angle is NOT enough (~12 s)
        # ──────────────────────────────────────────────────────────────────
        bad = make_equation_card(
            r"\text{2 sides + a non-included angle} \;\;\not\!\!\!\Longrightarrow\;\; \text{congruent}",
            color=RED_REJECT, scale=0.85
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in bad:
            m.set_z_index(2)
        self.play(FadeIn(bad, run_time=1.5))
        self.wait(4.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=1.0))
        self.wait(3.0)
        beat4 = VGroup(bad, cross)
        self.play(FadeOut(beat4, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~38 s, total ≈ 99 s)
        # Custom layout: the shared animate_final_definition helper places
        # the box at y = -1.7 and the sub below it (y ≈ -2.5), which is
        # below the safe-area floor (y = -1.5). Build the takeaway inline
        # with explicit positions so both rows sit above y = -1.5.
        # ──────────────────────────────────────────────────────────────────
        eq5 = MathTex(
            r"\text{CPCT} \;\;=\;\; \text{matching sides and angles are equal}",
        ).scale(0.85)
        eq5.move_to([0, -0.5, 0])
        eq5_bg = BackgroundRectangle(eq5, color=BLACK, fill_opacity=1, buff=0.25)
        eq5_bg.move_to(eq5.get_center())
        box5 = SurroundingRectangle(eq5, color=GREEN_OK, buff=0.3, stroke_width=3)
        sub5 = Text(
            "Once congruent by one of SSS, SAS, AAS, RHS — every pair matches.",
            font_size=18, color=GREEN_OK,
        )
        sub5.move_to([0, -1.2, 0])
        sub5_bg = BackgroundRectangle(sub5, color=BLACK, fill_opacity=0.95, buff=0.15)
        sub5_bg.move_to(sub5.get_center())
        self.play(FadeIn(eq5_bg, run_time=0.5), Write(eq5, run_time=2.0))
        self.play(Create(box5, run_time=1.0))
        self.play(Indicate(eq5, color=GREEN_OK, scale_factor=1.05), run_time=1.5)
        self.play(FadeIn(sub5_bg, run_time=0.4), FadeIn(sub5, run_time=1.0))
        self.wait(38.0)