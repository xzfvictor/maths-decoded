"""
Manim scene for the lesson `parabolas`
(topic `l10a-aa-parabolas-curves`).

The parabola y = ax² + bx + c has a vertex, a y-intercept, and an axis
of symmetry. Animation shows vertex form, y-intercept, and rejection of
the "vertex is at the y-intercept" mistake.

Target duration: ~75 s (matches the audio narration length).
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


class ParabolasScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Parabolas: y = ax² + bx + c",
            "Vertex, y-intercept, axis of symmetry",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Plot y = x² - 2x - 3, show vertex & y-intercept (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        ax = Axes(
            x_range=[-2.5, 4.5, 1],
            y_range=[-5, 4, 1],
            x_length=6.0,
            y_length=2.4,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        beat_2 = beat_group(beat_2, ax)

        x_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(i, 0), DOWN, buff=0.15)
            for i in [-2, -1, 1, 2, 3, 4]
        ])
        y_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(0, i), LEFT, buff=0.15)
            for i in [-4, -2, 2]
        ])
        zero_origin = MathTex("0", font_size=22).next_to(ax.c2p(0, 0), DL, buff=0.1)
        beat_2 = beat_group(beat_2, x_lbls, y_lbls, zero_origin)

        # y = x² - 2x - 3, vertex at (1, -4), y-int at -3.
        parabola = ax.plot(
            lambda x: x**2 - 2 * x - 3,
            x_range=[-1.7, 4.0],
            color=BLUE_TERM,
            stroke_width=4,
        )
        beat_2 = beat_group(beat_2, parabola)

        self.play(Create(ax), run_time=1.4)
        self.play(
            *[Write(lbl) for lbl in x_lbls],
            *[Write(lbl) for lbl in y_lbls],
            Write(zero_origin),
            run_time=1.5,
        )
        self.play(Create(parabola), run_time=2.0)
        self.wait(1.5)

        # Mark the vertex (1, -4) — labeled to the RIGHT of the dot
        # so it does not overlap the x-axis labels.
        vertex_dot = Dot(ax.c2p(1, -4), color=GREEN_OK, radius=0.08)
        vertex_lbl = MathTex(r"\text{vertex } (1, -4)", color=GREEN_OK).scale(0.85)
        vertex_lbl.move_to(ax.c2p(2.1, -3.6))
        vertex_lbl_bg = BackgroundRectangle(vertex_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        vertex_lbl_bg.move_to(vertex_lbl.get_center())
        beat_2 = beat_group(beat_2, vertex_dot, vertex_lbl, vertex_lbl_bg)
        self.play(FadeIn(vertex_dot, run_time=0.3))
        self.play(FadeIn(vertex_lbl_bg, run_time=0.3), FadeIn(vertex_lbl, run_time=0.9))
        self.wait(1.5)

        # Mark y-intercept (0, -3).
        yint_dot = Dot(ax.c2p(0, -3), color=ORANGE_TERM, radius=0.08)
        yint_lbl = MathTex(r"y\text{-int } (0, -3)", color=ORANGE_TERM).scale(0.9)
        yint_lbl.next_to(yint_dot, LEFT, buff=0.25)
        yint_lbl_bg = BackgroundRectangle(yint_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        yint_lbl_bg.move_to(yint_lbl.get_center())
        beat_2 = beat_group(beat_2, yint_dot, yint_lbl, yint_lbl_bg)
        self.play(FadeIn(yint_dot, run_time=0.3))
        self.play(FadeIn(yint_lbl_bg, run_time=0.3), FadeIn(yint_lbl, run_time=0.9))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Axis of symmetry x = 1 (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        ax2 = Axes(
            x_range=[-2.5, 4.5, 1],
            y_range=[-5, 4, 1],
            x_length=6.0,
            y_length=2.4,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        beat_3 = beat_group(beat_3, ax2)
        x_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(i, 0), DOWN, buff=0.15)
            for i in [-2, -1, 1, 2, 3, 4]
        ])
        y_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(0, i), LEFT, buff=0.15)
            for i in [-4, -2, 2]
        ])
        zero2 = MathTex("0", font_size=22).next_to(ax2.c2p(0, 0), DL, buff=0.1)
        beat_3 = beat_group(beat_3, x_lbls2, y_lbls2, zero2)

        par2 = ax2.plot(lambda x: x**2 - 2 * x - 3, x_range=[-1.7, 4.0], color=BLUE_TERM, stroke_width=4)
        beat_3 = beat_group(beat_3, par2)

        self.play(Create(ax2), run_time=1.0)
        self.play(
            *[Write(lbl) for lbl in x_lbls2],
            *[Write(lbl) for lbl in y_lbls2],
            Write(zero2),
            run_time=1.2,
        )
        self.play(Create(par2), run_time=1.5)

        # Dashed vertical line at x = 1 (kept inside the chart).
        sym_line = DashedLine(
            start=ax2.c2p(1, -4.5),
            end=ax2.c2p(1, 3.5),
            color=GREEN_OK,
            stroke_width=3,
        )
        sym_lbl = MathTex(r"x = 1", color=GREEN_OK).scale(1.0)
        sym_lbl.move_to(ax2.c2p(1.45, 3.4))
        sym_lbl_bg = BackgroundRectangle(sym_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        sym_lbl_bg.move_to(sym_lbl.get_center())
        beat_3 = beat_group(beat_3, sym_line, sym_lbl, sym_lbl_bg)

        self.play(Create(sym_line), run_time=1.0)
        self.play(FadeIn(sym_lbl_bg, run_time=0.3), FadeIn(sym_lbl, run_time=0.8))

        # Annotate: the parabola is symmetric about this line.
        sym_note = Text("parabola is symmetric about x = 1", font_size=22, color=GREEN_OK)
        sym_note.next_to(sym_line, RIGHT, buff=0.4).shift(DOWN * 0.6)
        sym_note_bg = BackgroundRectangle(sym_note, color=BLACK, fill_opacity=0.95, buff=0.12)
        sym_note_bg.move_to(sym_note.get_center())
        beat_3 = beat_group(beat_3, sym_note, sym_note_bg)
        self.play(FadeIn(sym_note_bg, run_time=0.3), FadeIn(sym_note, run_time=1.0))
        self.wait(3.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: "vertex is at the y-intercept" (~17 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        wrong = MathTex(r"\text{vertex} = y\text{-intercept}? \quad (1,-4) \neq (0,-3)", color=RED_REJECT).scale(0.9)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        beat_4 = beat_group(beat_4, wrong, wrong_bg)
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.6))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, cross)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.5)

        right = Text("Use x = -b/(2a) for the vertex's x-value.", font_size=22, color=GREEN_OK)
        right.next_to(wrong, DOWN, buff=0.6)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=0.95, buff=0.18)
        right_bg.move_to(right.get_center())
        beat_4 = beat_group(beat_4, right, right_bg)
        self.play(FadeIn(right_bg, run_time=0.3), FadeIn(right, run_time=1.0))
        self.wait(2.5)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~32 s, total ≈ 75 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Parabola: } y = ax^{2}+bx+c,\quad \text{vertex at } x = -\dfrac{b}{2a}",
            "Symmetric about the vertical line through the vertex.",
            final_wait=32.0,
        )
