"""
Manim scene for the lesson `construction-algorithms`
(topic `l9-sp-geometric-algorithms`).

A construction algorithm is a finite list of compass-and-straightedge
steps that produces a target shape. The animation walks through the
perpendicular-bisector recipe (arcs from each endpoint, join the
crossings), then lists other common building blocks, and rejects "any
straightedge is fine — even a ruler with markings".

Target duration: ~101.8 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ConstructionAlgorithmsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Algorithms for constructions",
            "Compass + straightedge = any standard geometric construction.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: perpendicular bisector of AB (~26 s)
        # ──────────────────────────────────────────────────────────────────
        # Horizontal segment AB.
        a_pt = [-4.0, 0.0, 0.0]
        b_pt = [2.0, 0.0, 0.0]
        a_dot = Dot(a_pt, color=BLUE_TERM)
        b_dot = Dot(b_pt, color=TEAL_TERM)
        a_lbl = MathTex("A", color=BLUE_TERM).scale(0.9).next_to(a_dot, DOWN, buff=0.2)
        b_lbl = MathTex("B", color=TEAL_TERM).scale(0.9).next_to(b_dot, DOWN, buff=0.2)
        ab = Line(a_pt, b_pt, color=WHITE, stroke_width=4)
        for m in [a_lbl, b_lbl]:
            m.set_z_index(2)
        a_lbl_bg = BackgroundRectangle(a_lbl, color=BLACK, fill_opacity=0.9, buff=0.08)
        a_lbl_bg.move_to(a_lbl.get_center())
        b_lbl_bg = BackgroundRectangle(b_lbl, color=BLACK, fill_opacity=0.9, buff=0.08)
        b_lbl_bg.move_to(b_lbl.get_center())

        self.play(
            Create(ab, run_time=1.0),
            FadeIn(a_dot, run_time=0.4),
            FadeIn(b_dot, run_time=0.4),
            FadeIn(a_lbl_bg, run_time=0.3),
            FadeIn(a_lbl, run_time=0.5),
            FadeIn(b_lbl_bg, run_time=0.3),
            FadeIn(b_lbl, run_time=0.5),
        )
        self.wait(1.5)

        # Two arcs above the segment — radius > AB/2.
        arc1 = Arc(
            radius=3.4, start_angle=0, angle=PI,
            color=BLUE_TERM, stroke_width=2,
        ).move_arc_center_to(a_pt)
        arc2 = Arc(
            radius=3.4, start_angle=PI, angle=PI,
            color=TEAL_TERM, stroke_width=2,
        ).move_arc_center_to(b_pt)
        self.play(Create(arc1, run_time=1.2), Create(arc2, run_time=1.2))
        self.wait(1.5)

        # Mark where the two arcs cross.
        cross_left = Dot([-1.0, 1.7, 0.0], color=GREEN_OK, radius=0.08)
        cross_right = Dot([-1.0, -1.7, 0.0], color=GREEN_OK, radius=0.08)
        perp = Line(cross_left.get_center(), cross_right.get_center(),
                    color=GREEN_OK, stroke_width=4)

        self.play(FadeIn(cross_left, run_time=0.4), FadeIn(cross_right, run_time=0.4))
        self.wait(0.8)
        self.play(Create(perp, run_time=1.2))
        self.wait(1.5)

        # Caption.
        cap = Text(
            "The line through the two crossings is the perpendicular bisector.",
            font_size=22, color=GREEN_OK,
        ).move_to(BAND_CHART_CENTER + DOWN * 1.8)
        cap_bg = BackgroundRectangle(cap, color=BLACK, fill_opacity=0.95, buff=0.16)
        cap_bg.move_to(cap.get_center())
        self.play(FadeIn(cap_bg, run_time=0.4), FadeIn(cap, run_time=1.6))
        self.wait(3.5)

        beat2 = VGroup(ab, a_dot, b_dot, a_lbl, b_lbl, a_lbl_bg, b_lbl_bg,
                       arc1, arc2, cross_left, cross_right, perp, cap, cap_bg)
        self.play(FadeOut(beat2, run_time=1.5))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Recipe format + common building blocks (~26 s)
        # ──────────────────────────────────────────────────────────────────
        recipe = MathTex(
            r"\text{Recipe: Inputs} \;\to\; \text{Steps} \;\to\; \text{Outputs}",
            color=WHITE,
        ).scale(1.0)
        recipe.move_to(BAND_CHART_CENTER + UP * 1.2)
        recipe_bg = BackgroundRectangle(recipe, color=BLACK, fill_opacity=1, buff=0.24)
        recipe_bg.move_to(recipe.get_center())
        self.play(FadeIn(recipe_bg, run_time=0.4), FadeIn(recipe, run_time=1.6))
        self.wait(2.5)

        # List four building blocks.
        block1 = make_term_card(r"\perp\, \text{bisector}", r"\text{midpoint + 90°}", BLUE_TERM)
        block2 = make_term_card(r"\perp\, \text{from point}", r"\text{drop a 90°}", TEAL_TERM)
        block3 = make_term_card(r"\angle\, \text{bisector}", r"\text{split angle in 2}", ORANGE_TERM)
        block4 = make_term_card(r"\text{copy angle}", r"\text{move to new vertex}", GREEN_OK)
        blocks = VGroup(block1, block2, block3, block4).arrange_in_grid(
            rows=2, cols=2, buff=0.6,
        )
        blocks.move_to(BAND_CHART_CENTER + DOWN * 0.4)
        for grp in blocks:
            for m in grp:
                m.set_z_index(2)

        for b in blocks:
            self.play(FadeIn(b, shift=UP * 0.2, run_time=0.85))
            self.wait(0.8)

        self.wait(3.0)

        beat3 = VGroup(recipe, recipe_bg, blocks)
        self.play(FadeOut(beat3, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: a ruler with markings is NOT allowed (~10 s)
        # ──────────────────────────────────────────────────────────────────
        bad = Text(
            "A ruler with markings can replace the compass + straightedge.",
            font_size=22, color=WHITE,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.7)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(2.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=1.0))

        fix = Text(
            "Compass + straightedge only — no measurements, no protractor.",
            font_size=20, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.4))
        self.wait(2.0)

        beat4 = VGroup(bad, bad_bg, cross, fix, fix_bg)
        self.play(FadeOut(beat4, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 101.8 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Algorithm} \;:\; \text{Inputs} \;\to\; \text{Steps} \;\to\; \text{Outputs}",
            "Build from compass-and-straightedge blocks, each step a primitive.",
            final_wait=39.0,
        )
