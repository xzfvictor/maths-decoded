"""
Manim scene for the lesson `quadrilateral-families`
(topic `l8-sp-quadrilateral-properties`).

Quadrilateral families stack extra rules on top of the basic "four
straight sides" idea: parallelogram → rectangle → square and
parallelogram → rhombus → square. The scene draws the four shapes
and shows how their properties nest.

Target duration: ~89 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


def _quad(center, w, h, color, stroke=4):
    """A quadrilateral of width w and height h, drawn as a Polygon."""
    cx, cy = center[0], center[1]
    pts = [
        [cx - w / 2, cy - h / 2, 0],
        [cx + w / 2, cy - h / 2, 0],
        [cx + w / 2, cy + h / 2, 0],
        [cx - w / 2, cy + h / 2, 0],
    ]
    return Polygon(*pts, color=color, stroke_width=stroke)


class QuadrilateralFamiliesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Families of quadrilaterals",
            "Stacking extra rules: parallelogram · rectangle · rhombus · square.",
            hold=1.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Family hierarchy diagram (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        # Top: parallelogram. Children: rectangle (left), rhombus (right).
        # Bottom centre: square (both).
        para  = _quad([-5.0, 1.5, 0], 3.0, 1.6, BLUE_TERM)
        rect  = _quad([-2.5, -1.0, 0], 2.4, 1.6, TEAL_TERM)
        rhom  = _quad([ 2.5, -1.0, 0], 2.6, 1.6, ORANGE_TERM)
        sq    = _quad([ 0.0, -2.7, 0], 1.8, 1.8, GREEN_OK)

        para_lbl  = Text("Parallelogram", font_size=22, color=BLUE_TERM)
        rect_lbl  = Text("Rectangle",     font_size=22, color=TEAL_TERM)
        rhom_lbl  = Text("Rhombus",       font_size=22, color=ORANGE_TERM)
        sq_lbl    = Text("Square",        font_size=22, color=GREEN_OK)

        for mob, lbl, offset in [
            (para, para_lbl, UP * 1.4),
            (rect, rect_lbl, DOWN * 1.4),
            (rhom, rhom_lbl, DOWN * 1.4),
            (sq,   sq_lbl,   DOWN * 1.3),
        ]:
            lbl.next_to(mob, offset, buff=0.18)
            lbl_bg = BackgroundRectangle(lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
            lbl_bg.move_to(lbl.get_center())
            mob.bg = lbl_bg

        self.play(FadeIn(para, run_time=1.2))
        self.play(FadeIn(para_lbl, run_time=0.6), FadeIn(para.bg, run_time=0.4))
        self.wait(2.0)

        # Arrows from parallelogram to its two children.
        arr_l = Arrow(start=para.get_bottom() + DOWN * 0.1,
                      end=rect.get_top() + UP * 0.1,
                      color=WHITE, buff=0, stroke_width=4)
        arr_r = Arrow(start=para.get_bottom() + DOWN * 0.1,
                      end=rhom.get_top() + UP * 0.1,
                      color=WHITE, buff=0, stroke_width=4)
        self.play(Create(arr_l, run_time=0.9), Create(arr_r, run_time=0.9))
        self.wait(1.0)

        self.play(FadeIn(rect, run_time=1.2))
        self.play(FadeIn(rect_lbl, run_time=0.6), FadeIn(rect.bg, run_time=0.4))
        self.wait(1.5)
        self.play(FadeIn(rhom, run_time=1.2))
        self.play(FadeIn(rhom_lbl, run_time=0.6), FadeIn(rhom.bg, run_time=0.4))
        self.wait(1.5)

        # Arrow from both to square (centre bottom).
        arr_b1 = Arrow(start=rect.get_bottom() + DOWN * 0.1,
                       end=sq.get_top() + LEFT * 0.3 + UP * 0.1,
                       color=WHITE, buff=0, stroke_width=4)
        arr_b2 = Arrow(start=rhom.get_bottom() + DOWN * 0.1,
                       end=sq.get_top() + RIGHT * 0.3 + UP * 0.1,
                       color=WHITE, buff=0, stroke_width=4)
        self.play(Create(arr_b1, run_time=0.9), Create(arr_b2, run_time=0.9))
        self.wait(1.0)
        self.play(FadeIn(sq, run_time=1.4))
        self.play(FadeIn(sq_lbl, run_time=0.6), FadeIn(sq.bg, run_time=0.4))
        self.wait(3.0)

        beat_2 = beat_group(
            beat_2,
            para, para_lbl, para.bg,
            rect, rect_lbl, rect.bg,
            rhom, rhom_lbl, rhom.bg,
            sq, sq_lbl, sq.bg,
            arr_l, arr_r, arr_b1, arr_b2,
        )
        self.wait(120)
        raise SystemExit(0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Property table — angle sum, opposite sides (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        ang = MathTex(r"\text{angles in any quadrilateral sum to } 360^\circ",
                      color=GREEN_OK).scale(0.95)
        ang.move_to(BAND_CHART_CENTER + UP * 1.2)
        ang_bg = BackgroundRectangle(ang, color=BLACK, fill_opacity=1, buff=0.25)
        ang_bg.move_to(ang.get_center())
        self.play(FadeIn(ang_bg, run_time=0.5), Write(ang, run_time=2.0))
        self.wait(3.0)

        prop = MathTex(
            r"\text{parallelogram: opp.\ sides \,\,=\,\, opp.\ angles}",
            color=BLUE_TERM,
        ).scale(0.95)
        prop.next_to(ang, DOWN, buff=0.7)
        prop_bg = BackgroundRectangle(prop, color=BLACK, fill_opacity=1, buff=0.2)
        prop_bg.move_to(prop.get_center())
        self.play(FadeIn(prop_bg, run_time=0.4), FadeIn(prop, run_time=1.5))
        self.wait(3.5)

        prop2 = MathTex(
            r"\text{rectangle: 4 right angles \quad rhombus: 4 equal sides}",
            color=WHITE,
        ).scale(0.85)
        prop2.next_to(prop, DOWN, buff=0.55)
        prop2_bg = BackgroundRectangle(prop2, color=BLACK, fill_opacity=1, buff=0.2)
        prop2_bg.move_to(prop2.get_center())
        self.play(FadeIn(prop2_bg, run_time=0.4), FadeIn(prop2, run_time=1.5))
        self.wait(3.5)

        beat_3 = beat_group(beat_3, ang, ang_bg, prop, prop_bg, prop2, prop2_bg)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Trapezium and kite (the off-axis families) (~12 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        trap = _quad([-3.0, 0.0, 0], 3.0, 1.5, BLUE_TERM).rotate(-0.18)
        kite = Polygon(
            [-1.0, -1.4, 0], [-2.0, 0.0, 0], [1.0, -1.4, 0], [0.0, 1.2, 0],
            color=TEAL_TERM, stroke_width=4,
        ).shift(RIGHT * 2.5)
        trap_lbl = Text("Trapezium", font_size=22, color=BLUE_TERM).next_to(trap, DOWN, buff=0.3)
        kite_lbl = Text("Kite",       font_size=22, color=TEAL_TERM).next_to(kite, DOWN, buff=0.3)
        trap_bg  = BackgroundRectangle(trap_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        trap_bg.move_to(trap_lbl.get_center())
        kite_bg  = BackgroundRectangle(kite_lbl, color=BLACK, fill_opacity=0.9, buff=0.12)
        kite_bg.move_to(kite_lbl.get_center())

        self.play(FadeIn(trap, run_time=1.2))
        self.play(FadeIn(trap_lbl, run_time=0.6), FadeIn(trap_bg, run_time=0.4))
        self.wait(1.5)
        self.play(FadeIn(kite, run_time=1.2))
        self.play(FadeIn(kite_lbl, run_time=0.6), FadeIn(kite_bg, run_time=0.4))
        self.wait(3.5)

        beat_4 = beat_group(beat_4, trap, trap_lbl, trap_bg, kite, kite_lbl, kite_bg)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~33 s, total ≈ 89 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{angles in a quadrilateral} \;=\; 360^\circ",
            "Each special shape adds one or two extra constraints on top.",
            final_wait=33.0,
        )