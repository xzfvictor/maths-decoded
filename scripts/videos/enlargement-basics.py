"""
Manim scene for the lesson `enlargement-basics`
(topic `l9-sp-enlargement-transformation`).

An enlargement scales every point from a centre C by a factor k, so
P' lies on the ray from C through P with CP' = k * CP. The shape stays
similar; lengths scale by k, areas by k^2. The animation scales a
triangle from the origin by k = 2, generalises the rule, and rejects
"k can be zero".

Target duration: ~93.6 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class EnlargementBasicsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Enlargement with a scale factor",
            "Every point moves along its ray from C by factor k.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: triangle scaled by k=2 from origin (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Original triangle on the left; image on the right.
        original = Polygon(
            [-5.5, -0.5, 0], [-4.0, -0.5, 0], [-4.75, 1.0, 0],
            color=BLUE_TERM, stroke_width=4,
        )
        original_lbl = MathTex(r"\triangle ABC", color=BLUE_TERM).scale(0.9)
        original_lbl.next_to(original, DOWN, buff=0.3)
        original_lbl_bg = BackgroundRectangle(original_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        original_lbl_bg.move_to(original_lbl.get_center())

        image = Polygon(
            [-1.5, -1.5, 0], [2.5, -1.5, 0], [0.5, 2.0, 0],
            color=ORANGE_TERM, stroke_width=4,
        )
        image_lbl = MathTex(r"\triangle A'B'C'", color=ORANGE_TERM).scale(0.9)
        image_lbl.next_to(image, DOWN, buff=0.3)
        image_lbl_bg = BackgroundRectangle(image_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        image_lbl_bg.move_to(image_lbl.get_center())

        self.play(
            Create(original, run_time=1.4),
            FadeIn(original_lbl_bg, run_time=0.4),
            FadeIn(original_lbl, run_time=0.8),
        )
        self.wait(1.5)
        self.play(
            Create(image, run_time=1.4),
            FadeIn(image_lbl_bg, run_time=0.4),
            FadeIn(image_lbl, run_time=0.8),
        )
        self.wait(1.5)

        # Centre dot at origin between them.
        centre = Dot([0.0, 0.0, 0.0], color=WHITE, radius=0.08)
        centre_lbl = MathTex("C", color=WHITE).scale(0.9).next_to(centre, UR, buff=0.15)
        centre_lbl_bg = BackgroundRectangle(centre_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        centre_lbl_bg.move_to(centre_lbl.get_center())
        self.play(FadeIn(centre, run_time=0.5), FadeIn(centre_lbl, run_time=0.5),
                  FadeIn(centre_lbl_bg, run_time=0.3))
        self.wait(1.0)

        # k = 2 callout above.
        k_lbl = MathTex(r"k \;=\; 2", color=GREEN_OK).scale(1.3)
        k_lbl.move_to(BAND_CHART_CENTER + UP * 2.2)
        k_lbl_bg = BackgroundRectangle(k_lbl, color=BLACK, fill_opacity=1, buff=0.22)
        k_lbl_bg.move_to(k_lbl.get_center())
        self.play(FadeIn(k_lbl_bg, run_time=0.4), FadeIn(k_lbl, run_time=1.0))
        self.wait(1.5)

        # CP' = k * CP note.
        cp = MathTex(
            r"CP' \;=\; k \cdot CP",
            color=GREEN_OK,
        ).scale(1.05)
        cp.next_to(original_lbl, DOWN, buff=0.5)
        cp_bg = BackgroundRectangle(cp, color=BLACK, fill_opacity=1, buff=0.22)
        cp_bg.move_to(cp.get_center())
        self.play(FadeIn(cp_bg, run_time=0.4), FadeIn(cp, run_time=1.5))
        self.wait(3.0)

        beat2 = VGroup(original, original_lbl, original_lbl_bg, image, image_lbl, image_lbl_bg,
                       centre, centre_lbl, centre_lbl_bg, k_lbl, k_lbl_bg, cp, cp_bg)
        self.play(FadeOut(beat2, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — What scales with k (~22 s)
        # ──────────────────────────────────────────────────────────────────
        len_card = make_term_card(r"\text{Length}", r"\times k", BLUE_TERM)
        area_card = make_term_card(r"\text{Area}", r"\times k^{2}", TEAL_TERM)
        vol_card = make_term_card(r"\text{Volume}", r"\times k^{3}", ORANGE_TERM)
        row = VGroup(len_card, area_card, vol_card).arrange(RIGHT, buff=0.55)
        row.move_to(BAND_CHART_CENTER + UP * 0.6)
        for grp in row:
            for m in grp:
                m.set_z_index(2)

        for c in row:
            self.play(FadeIn(c, shift=UP * 0.2, run_time=0.9))
            self.wait(1.0)

        # Concrete counter-check: a square of side 10, k = 0.5 → area 25.
        worked = MathTex(
            r"\text{Side 10, } k = 0.5: \text{ area} = (10 \cdot 0.5)^{2} = 25",
            color=GREEN_OK,
        ).scale(1.0)
        worked.next_to(row, DOWN, buff=0.6)
        worked_bg = BackgroundRectangle(worked, color=BLACK, fill_opacity=1, buff=0.22)
        worked_bg.move_to(worked.get_center())
        self.play(FadeIn(worked_bg, run_time=0.4), FadeIn(worked, run_time=2.0))
        self.wait(3.5)

        shape_note = Text(
            "Shape stays similar — only size changes.",
            font_size=22, color=GREEN_OK,
        ).next_to(worked, DOWN, buff=0.5)
        sn_bg = BackgroundRectangle(shape_note, color=BLACK, fill_opacity=0.95, buff=0.16)
        sn_bg.move_to(shape_note.get_center())
        self.play(FadeIn(sn_bg, run_time=0.4), FadeIn(shape_note, run_time=1.4))
        self.wait(3.0)

        beat3 = VGroup(row, worked, worked_bg, shape_note, sn_bg)
        self.play(FadeOut(beat3, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: k = 0 collapses the shape to a point (~10 s)
        # ──────────────────────────────────────────────────────────────────
        bad = MathTex(
            r"k \;=\; 0 \text{ keeps the shape — it just shrinks}",
            color=WHITE,
        ).scale(0.9)
        bad.move_to(BAND_CHART_CENTER + UP * 0.7)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.22)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(2.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=1.0))

        fix = Text(
            "Every point lands on the centre — there is no shape left.",
            font_size=20, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.4))
        self.wait(2.0)

        beat4 = VGroup(bad, bad_bg, cross, fix, fix_bg)
        self.play(FadeOut(beat4, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 93.6 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"CP' \;=\; k \cdot CP",
            "k > 1 enlarges; 0 < k < 1 shrinks; k < 0 flips through C.",
            final_wait=35.0,
        )
