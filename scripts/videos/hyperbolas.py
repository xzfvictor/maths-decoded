"""
Manim scene for the lesson `hyperbolas`
(topic `l10a-aa-parabolas-curves`).

The reciprocal function y = 1/x is a hyperbola with two branches, an
x-asymptote at y = 0 and a y-asymptote at x = 0. The animation shows
the curve, the asymptotes, and the rejection of the "x = 0" point.

Target duration: ~98 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *
import numpy as np


class HyperbolasScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "The hyperbola y = 1/x",
            "Two branches with axes as asymptotes",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Plot y = 1/x on axes (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        ax = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-2, 1.4, 1],
            x_length=5.6,
            y_length=2.6,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.1)
        beat_2 = beat_group(beat_2, ax)

        # Tick labels (manually placed for control).
        x_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(i, 0), DOWN, buff=0.15)
            for i in [-1, 1]
        ])
        y_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(0, i), LEFT, buff=0.15)
            for i in [-1, 1]
        ])
        # Hide the implicit "0" on the axes by skipping 0.
        zero_origin = MathTex("0", font_size=22).next_to(ax.c2p(0, 0), DL, buff=0.1)
        beat_2 = beat_group(beat_2, x_lbls, y_lbls, zero_origin)

        self.play(Create(ax), run_time=1.4)
        self.play(
            *[Write(lbl) for lbl in x_lbls],
            *[Write(lbl) for lbl in y_lbls],
            Write(zero_origin),
            run_time=1.6,
        )
        self.wait(1.5)

        # Right branch (positive x).
        right_branch = ax.plot(
            lambda x: 1.0 / x,
            x_range=[0.7, 3.3],
            color=BLUE_TERM,
            stroke_width=4,
        )
        # Left branch (negative x).
        left_branch = ax.plot(
            lambda x: 1.0 / x,
            x_range=[-3.3, -0.7],
            color=BLUE_TERM,
            stroke_width=4,
        )
        beat_2 = beat_group(beat_2, right_branch, left_branch)

        self.play(Create(right_branch), run_time=2.0)
        self.play(Create(left_branch), run_time=2.0)
        self.wait(2.0)

        # Label the curve.
        curve_lbl = MathTex(r"y = \dfrac{1}{x}", color=BLUE_TERM).scale(0.85)
        curve_lbl.move_to(ax.c2p(2.4, 0.4))
        curve_lbl_bg = BackgroundRectangle(curve_lbl, color=BLACK, fill_opacity=1, buff=0.18)
        curve_lbl_bg.move_to(curve_lbl.get_center())
        beat_2 = beat_group(beat_2, curve_lbl, curve_lbl_bg)
        self.play(FadeIn(curve_lbl_bg, run_time=0.4), Write(curve_lbl, run_time=1.4))
        self.wait(3.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Asymptotes x = 0 and y = 0 (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        ax2 = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-2, 1.4, 1],
            x_length=5.6,
            y_length=2.6,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.1)
        beat_3 = beat_group(beat_3, ax2)
        x_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(i, 0), DOWN, buff=0.15)
            for i in [-1, 1]
        ])
        y_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(0, i), LEFT, buff=0.15)
            for i in [-1, 1]
        ])
        zero2 = MathTex("0", font_size=22).next_to(ax2.c2p(0, 0), DL, buff=0.1)
        beat_3 = beat_group(beat_3, x_lbls2, y_lbls2, zero2)

        rb2 = ax2.plot(lambda x: 1.0 / x, x_range=[0.7, 3.3], color=BLUE_TERM, stroke_width=4)
        lb2 = ax2.plot(lambda x: 1.0 / x, x_range=[-3.3, -0.7], color=BLUE_TERM, stroke_width=4)
        beat_3 = beat_group(beat_3, rb2, lb2)

        self.play(Create(ax2), run_time=1.2)
        self.play(
            *[Write(lbl) for lbl in x_lbls2],
            *[Write(lbl) for lbl in y_lbls2],
            Write(zero2),
            run_time=1.4,
        )
        self.play(Create(rb2), Create(lb2), run_time=2.0)

        # Dashed asymptotes.
        x_asy = DashedLine(
            start=ax2.c2p(-3.4, 0),
            end=ax2.c2p(3.4, 0),
            color=ORANGE_TERM,
            stroke_width=3,
        )
        y_asy = DashedLine(
            start=ax2.c2p(0, -1.95),
            end=ax2.c2p(0, 1.35),
            color=ORANGE_TERM,
            stroke_width=3,
        )
        beat_3 = beat_group(beat_3, x_asy, y_asy)

        x_asy_lbl = MathTex(r"y = 0", color=ORANGE_TERM).scale(0.9)
        x_asy_lbl.next_to(x_asy, RIGHT, buff=0.2).shift(UP * 0.2)
        x_asy_lbl_bg = BackgroundRectangle(x_asy_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        x_asy_lbl_bg.move_to(x_asy_lbl.get_center())
        y_asy_lbl = MathTex(r"x = 0", color=ORANGE_TERM).scale(0.9)
        y_asy_lbl.move_to(ax2.c2p(0.55, 1.05))
        y_asy_lbl_bg = BackgroundRectangle(y_asy_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        y_asy_lbl_bg.move_to(y_asy_lbl.get_center())
        beat_3 = beat_group(beat_3, x_asy_lbl, x_asy_lbl_bg, y_asy_lbl, y_asy_lbl_bg)

        self.play(Create(x_asy), run_time=1.0)
        self.play(FadeIn(x_asy_lbl_bg, run_time=0.3), FadeIn(x_asy_lbl, run_time=0.8))
        self.wait(1.0)
        self.play(Create(y_asy), run_time=1.0)
        self.play(FadeIn(y_asy_lbl_bg, run_time=0.3), FadeIn(y_asy_lbl, run_time=0.8))
        self.wait(2.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: x = 0 is not on the graph (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        bad_pt_note = MathTex(r"\dfrac{1}{0}", color=RED_REJECT).scale(1.05)
        bad_pt_note.move_to(BAND_CHART_CENTER + UP * 0.55)
        bad_pt_bg = BackgroundRectangle(bad_pt_note, color=BLACK, fill_opacity=1, buff=0.25)
        bad_pt_bg.move_to(bad_pt_note.get_center())
        beat_4 = beat_group(beat_4, bad_pt_note, bad_pt_bg)
        self.play(FadeIn(bad_pt_bg, run_time=0.4), Write(bad_pt_note, run_time=1.6))
        self.wait(1.0)

        cross = Cross(bad_pt_note, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, cross)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.5)

        undefined_lbl = Text("At x = 0, this is undefined", font_size=22, color=RED_REJECT)
        undefined_lbl.next_to(bad_pt_note, DOWN, buff=0.45)
        undefined_bg = BackgroundRectangle(undefined_lbl, color=BLACK, fill_opacity=0.95, buff=0.18)
        undefined_bg.move_to(undefined_lbl.get_center())
        beat_4 = beat_group(beat_4, undefined_lbl, undefined_bg)
        self.play(FadeIn(undefined_bg, run_time=0.3), FadeIn(undefined_lbl, run_time=0.8))

        note2 = Text(
            "Both branches get closer to x = 0 without ever reaching it.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(undefined_lbl, DOWN, buff=0.45)
        note2_bg = BackgroundRectangle(note2, color=BLACK, fill_opacity=0.95, buff=0.18)
        note2_bg.move_to(note2.get_center())
        beat_4 = beat_group(beat_4, note2, note2_bg)
        self.play(FadeIn(note2_bg, run_time=0.4), FadeIn(note2, run_time=1.2))
        self.wait(3.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~45 s, total ≈ 98 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Hyperbola: } y = \dfrac{k}{x} \text{ with asymptotes } x = 0,\ y = 0",
            "Two branches, never touch the axes.",
            final_wait=45.0,
        )
