"""
Manim scene for the lesson `similarity-aspects`
(topic `l9-sp-enlargement-transformation`).

An enlargement preserves shape: angles are unchanged, parallel lines
stay parallel, but every length scales by |k|, every area by k^2, every
volume by k^3. The animation starts with two similar triangles,
spells out the three scaling laws, and rejects "similar = congruent".

Target duration: ~87.4 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SimilarityAspectsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Similarity: what stays, what changes",
            "Angles unchanged — lengths, areas, volumes scale by powers of k.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete similar triangles (~22 s)
        # ──────────────────────────────────────────────────────────────────
        small = Polygon(
            [-5.5, -0.5, 0], [-4.0, -0.5, 0], [-4.75, 1.0, 0],
            color=BLUE_TERM, stroke_width=4,
        )
        big = Polygon(
            [-1.0, -1.5, 0], [3.0, -1.5, 0], [1.0, 2.0, 0],
            color=TEAL_TERM, stroke_width=4,
        )

        self.play(Create(small, run_time=1.4))
        self.wait(1.0)
        self.play(Create(big, run_time=1.4))
        self.wait(1.5)

        # Angles preserved note.
        ang = MathTex(
            r"\text{Matching angles are equal}",
            color=GREEN_OK,
        ).scale(0.95)
        ang.move_to(BAND_CHART_CENTER + UP * 2.1)
        ang_bg = BackgroundRectangle(ang, color=BLACK, fill_opacity=1, buff=0.22)
        ang_bg.move_to(ang.get_center())
        self.play(FadeIn(ang_bg, run_time=0.4), FadeIn(ang, run_time=1.4))
        self.wait(2.5)

        # Ratio rule.
        ratio = MathTex(
            r"\dfrac{AB}{DE} \;=\; \dfrac{BC}{EF} \;=\; \dfrac{CA}{FD} \;=\; k",
            color=WHITE,
        ).scale(0.95)
        ratio.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        ratio_bg = BackgroundRectangle(ratio, color=BLACK, fill_opacity=1, buff=0.24)
        ratio_bg.move_to(ratio.get_center())
        self.play(FadeIn(ratio_bg, run_time=0.5), Write(ratio, run_time=2.0))
        self.wait(3.0)

        k_val = MathTex(r"k \;=\; 2", color=GREEN_OK).scale(1.3)
        k_val.next_to(ratio, DOWN, buff=0.4)
        k_val_bg = BackgroundRectangle(k_val, color=BLACK, fill_opacity=1, buff=0.2)
        k_val_bg.move_to(k_val.get_center())
        self.play(FadeIn(k_val_bg, run_time=0.4), FadeIn(k_val, run_time=1.2))
        self.wait(3.0)

        beat2 = VGroup(small, big, ang, ang_bg, ratio, ratio_bg, k_val, k_val_bg)
        self.play(FadeOut(beat2, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Length / Area / Volume scaling (~22 s)
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
            self.play(FadeIn(c, shift=UP * 0.2, run_time=0.85))
            self.wait(1.0)

        # Worked example: 12 cm perimeter, k = 5 → 60 cm.
        eg = MathTex(
            r"\text{Perimeter } 12 \to 12 \times 5 \;=\; 60 \text{ cm}",
            color=GREEN_OK,
        ).scale(1.0)
        eg.next_to(row, DOWN, buff=0.55)
        eg_bg = BackgroundRectangle(eg, color=BLACK, fill_opacity=1, buff=0.22)
        eg_bg.move_to(eg.get_center())
        self.play(FadeIn(eg_bg, run_time=0.4), FadeIn(eg, run_time=1.6))
        self.wait(2.5)

        eg2 = MathTex(
            r"\text{Volume } 40, \, k=2: \;40 \times 2^{3} \;=\; 320",
            color=GREEN_OK,
        ).scale(1.0)
        eg2.next_to(eg, DOWN, buff=0.4)
        eg2_bg = BackgroundRectangle(eg2, color=BLACK, fill_opacity=1, buff=0.22)
        eg2_bg.move_to(eg2.get_center())
        self.play(FadeIn(eg2_bg, run_time=0.4), FadeIn(eg2, run_time=1.6))
        self.wait(4.0)

        beat3 = VGroup(row, eg, eg_bg, eg2, eg2_bg)
        self.play(FadeOut(beat3, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: similar = congruent (~10 s)
        # ──────────────────────────────────────────────────────────────────
        bad = Text(
            "Two similar shapes must be congruent (the same size).",
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
            "Similar allows different sizes; congruent means k = 1 exactly.",
            font_size=20, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.4))
        self.wait(2.0)

        beat4 = VGroup(bad, bad_bg, cross, fix, fix_bg)
        self.play(FadeOut(beat4, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 87.4 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Similar} \;\Longrightarrow\; \text{angles equal, sides in ratio } k",
            "Lengths scale by k, areas by k^2, volumes by k^3.",
            final_wait=33.0,
        )
