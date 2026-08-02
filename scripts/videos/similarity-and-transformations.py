"""
Manim scene for the lesson `similarity-and-transformations`
(topic `l8-sp-congruence-similarity`).

Two shapes are similar when they have the same shape but possibly
different sizes — every matching side sits at the same scale factor.
We build a similar shape via enlargement and contrast with
congruence (translation, reflection, rotation).

Target duration: ~120 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class SimilarityAndTransformationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Similarity and transformations",
            "Same shape, different size (similar) — or identical (congruent).",
            hold=1.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete similar triangles with scale factor 2 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        # Small triangle on the left, big on the right. Both shrunk and
        # lowered so they sit inside the chart band y=[-1.5, 1.4] and
        # never touch the subtitle at y=2.3.
        small = Polygon(
            [-4.5, -0.5, 0], [-3.0, -0.5, 0], [-3.75, 1.0, 0],
            color=BLUE_TERM, stroke_width=4,
        )
        big = Polygon(
            [0.0, -1.0, 0], [3.0, -1.0, 0], [1.5, 1.4, 0],
            color=TEAL_TERM, stroke_width=4,
        )

        self.play(Create(small, run_time=1.5))
        self.wait(1.0)
        self.play(Create(big, run_time=1.5))
        self.wait(2.0)

        # Ratio statement — keep it just below the chart band.
        ratio = MathTex(
            r"\dfrac{AB}{DE} = \dfrac{BC}{EF} = \dfrac{CA}{FD} = k",
            color=WHITE,
        ).scale(0.95)
        ratio.move_to(DOWN * 2.4)
        ratio_bg = BackgroundRectangle(ratio, color=BLACK, fill_opacity=1, buff=0.25)
        ratio_bg.move_to(ratio.get_center())
        self.play(FadeIn(ratio_bg, run_time=0.5), Write(ratio, run_time=2.0))
        self.wait(3.0)

        k_val = MathTex(r"k = 2", color=GREEN_OK).scale(1.3)
        k_val.next_to(ratio, DOWN, buff=0.4)
        k_val_bg = BackgroundRectangle(k_val, color=BLACK, fill_opacity=1, buff=0.2)
        k_val_bg.move_to(k_val.get_center())
        self.play(FadeIn(k_val_bg, run_time=0.4), FadeIn(k_val, run_time=1.2))
        self.wait(3.5)

        beat_2.add(small, big, ratio, ratio_bg, k_val, k_val_bg)
        self.play(FadeOut(beat_2, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Enlargement: scale factor behaviour (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        tiny = Polygon(
            [-4.5, -0.5, 0], [-3.5, -0.5, 0], [-4.0, 0.5, 0],
            color=BLUE_TERM, stroke_width=4,
        )
        centre_dot = Dot([-2.0, 0.0, 0], color=WHITE, radius=0.1)
        centre_lbl = MathTex("C", color=WHITE).scale(0.9).next_to(centre_dot, DL, buff=0.15)

        enlarged = Polygon(
            [0.5, -1.0, 0], [3.5, -1.0, 0], [2.0, 1.0, 0],
            color=ORANGE_TERM, stroke_width=4,
        )

        self.play(Create(tiny, run_time=1.5))
        self.wait(1.0)
        self.play(FadeIn(centre_dot, run_time=0.6), FadeIn(centre_lbl, run_time=0.6))
        self.wait(1.5)

        arrow = Arrow(
            start=[-2.0, 0.0, 0], end=[0.5, 0.0, 0],
            color=GREEN_OK, buff=0, stroke_width=5,
        )
        scale_lbl = MathTex(r"k = 2", color=GREEN_OK).scale(1.0).next_to(arrow, UP, buff=0.2)
        scale_lbl_bg = BackgroundRectangle(scale_lbl, color=BLACK, fill_opacity=0.9, buff=0.1)
        scale_lbl_bg.move_to(scale_lbl.get_center())
        self.play(Create(arrow, run_time=1.2))
        self.play(FadeIn(scale_lbl, run_time=0.6), FadeIn(scale_lbl_bg, run_time=0.4))
        self.wait(1.5)
        self.play(Create(enlarged, run_time=1.5))
        self.wait(2.5)

        # Three k-regimes stacked to the right of the enlarged shape.
        regimes = VGroup(
            Text("k > 1 enlarges", font_size=20, color=GREEN_OK),
            Text("0 < k < 1 shrinks", font_size=20, color=TEAL_TERM),
            Text("k < 0 flips & mirrors", font_size=20, color=ORANGE_TERM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        regimes.next_to(enlarged, RIGHT, buff=0.6)
        regime_bgs = VGroup()
        for r in regimes:
            bg = BackgroundRectangle(r, color=BLACK, fill_opacity=0.95, buff=0.12)
            bg.move_to(r.get_center())
            regime_bgs.add(bg)
        self.play(FadeIn(regime_bgs, run_time=0.4), FadeIn(regimes, run_time=1.0))
        self.wait(3.0)

        beat_3.add(tiny, centre_dot, centre_lbl, arrow, scale_lbl, scale_lbl_bg,
                   enlarged, regimes, regime_bgs)
        self.play(FadeOut(beat_3, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Congruence: 3 transformations preserve size (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        trans = make_term_card(r"\text{Translation}", r"\text{slide}", BLUE_TERM)
        refl = make_term_card(r"\text{Reflection}", r"\text{flip}", TEAL_TERM)
        rot = make_term_card(r"\text{Rotation}", r"\text{turn}", ORANGE_TERM)
        row = VGroup(trans, refl, rot).arrange(RIGHT, buff=0.6)
        row.move_to(BAND_CHART_CENTER + UP * 0.6)
        for grp in row:
            for m in grp:
                m.set_z_index(2)
        self.play(FadeIn(trans, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(refl, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(rot, run_time=1.0))
        self.wait(2.5)

        keep = Text(
            "All three preserve lengths and angles → congruent.",
            font_size=22, color=GREEN_OK,
        ).next_to(row, DOWN, buff=0.5)
        keep_bg = BackgroundRectangle(keep, color=BLACK, fill_opacity=0.95, buff=0.15)
        keep_bg.move_to(keep.get_center())
        self.play(FadeIn(keep_bg, run_time=0.4), FadeIn(keep, run_time=1.2))
        self.wait(3.0)

        bad = Text(
            "One matching side or angle is NOT enough.",
            font_size=20, color=RED_REJECT,
        ).next_to(keep, DOWN, buff=0.4)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=0.95, buff=0.15)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.2))
        self.wait(3.0)

        beat_4.add(row, keep, keep_bg, bad, bad_bg)
        self.play(FadeOut(beat_4, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~47 s, total ≈ 120 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Similar} \;\Longleftrightarrow\; \text{angles equal, sides in ratio } k",
            "Congruent shapes are similar with k = 1 — same size.",
            final_wait=47.0,
        )