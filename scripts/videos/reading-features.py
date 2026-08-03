"""
Manim scene for the lesson `reading-features`
(topic `l10a-aa-polynomial-features`).

From the graph of a polynomial, identify roots, max/min, and axis of
symmetry. Reject the mistake of confusing roots with the y-intercept.

Target duration: ~85 s (matches the audio narration length).
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


class ReadingFeaturesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Reading features from a polynomial graph",
            "Roots, turning points, axis of symmetry",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Show cubic with two clear roots (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6.0,
            y_length=2.4,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        beat_2 = beat_group(beat_2, ax)

        x_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(i, 0), DOWN, buff=0.15)
            for i in [-2, -1, 1, 2]
        ])
        y_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(0, i), LEFT, buff=0.15)
            for i in [-2, 2]
        ])
        zero_origin = MathTex("0", font_size=22).next_to(ax.c2p(0, 0), DL, buff=0.1)
        beat_2 = beat_group(beat_2, x_lbls, y_lbls, zero_origin)

        # Cubic y = x^3 - 3x  (roots at -sqrt(3), 0, sqrt(3); local max at -1, min at 1).
        cubic = ax.plot(
            lambda x: x**3 - 3 * x,
            x_range=[-2.1, 2.1],
            color=BLUE_TERM,
            stroke_width=4,
        )
        beat_2 = beat_group(beat_2, cubic)

        self.play(Create(ax), run_time=1.4)
        self.play(
            *[Write(lbl) for lbl in x_lbls],
            *[Write(lbl) for lbl in y_lbls],
            Write(zero_origin),
            run_time=1.5,
        )
        self.play(Create(cubic), run_time=2.0)
        self.wait(1.5)

        # Mark the roots.
        roots = [
            (np.sqrt(3), r"x \approx 1.73"),
            (-np.sqrt(3), r"x \approx -1.73"),
        ]
        for rx, lbl_tex in roots:
            dot = Dot(ax.c2p(rx, 0), color=GREEN_OK, radius=0.08)
            lbl = MathTex(lbl_tex, color=GREEN_OK).scale(0.85)
            lbl.next_to(dot, DOWN if rx > 0 else UP, buff=0.2)
            lbl_bg = BackgroundRectangle(lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
            lbl_bg.move_to(lbl.get_center())
            beat_2 = beat_group(beat_2, dot, lbl, lbl_bg)
            self.play(FadeIn(dot, run_time=0.3))
            self.play(FadeIn(lbl_bg, run_time=0.3), FadeIn(lbl, run_time=0.7))
            self.wait(1.0)

        # Annotation. Explicitly positioned inside the safe band so it
        # cannot extend past the title/subtitle at the top.
        root_lbl = Text("roots: x-values where y = 0", font_size=22, color=GREEN_OK)
        root_lbl.move_to(BAND_CHART_CENTER + LEFT * 3.0 + UP * 0.4)
        root_lbl_bg = BackgroundRectangle(root_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        root_lbl_bg.move_to(root_lbl.get_center())
        beat_2 = beat_group(beat_2, root_lbl, root_lbl_bg)
        self.play(FadeIn(root_lbl_bg, run_time=0.3), FadeIn(root_lbl, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Turning points and axis of symmetry (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        ax2 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6.0,
            y_length=2.4,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + DOWN * 0.05)
        beat_3 = beat_group(beat_3, ax2)
        x_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(i, 0), DOWN, buff=0.15)
            for i in [-2, -1, 1, 2]
        ])
        y_lbls2 = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax2.c2p(0, i), LEFT, buff=0.15)
            for i in [-2, 2]
        ])
        zero2 = MathTex("0", font_size=22).next_to(ax2.c2p(0, 0), DL, buff=0.1)
        beat_3 = beat_group(beat_3, x_lbls2, y_lbls2, zero2)

        cubic2 = ax2.plot(lambda x: x**3 - 3 * x, x_range=[-2.1, 2.1], color=BLUE_TERM, stroke_width=4)
        beat_3 = beat_group(beat_3, cubic2)

        self.play(Create(ax2), run_time=1.0)
        self.play(
            *[Write(lbl) for lbl in x_lbls2],
            *[Write(lbl) for lbl in y_lbls2],
            Write(zero2),
            run_time=1.2,
        )
        self.play(Create(cubic2), run_time=1.5)

        # Local max at x = -1, y = 2.
        max_dot = Dot(ax2.c2p(-1, 2), color=ORANGE_TERM, radius=0.08)
        max_lbl = MathTex(r"\text{local max}", color=ORANGE_TERM).scale(0.85)
        max_lbl.next_to(max_dot, UL, buff=0.2)
        max_lbl_bg = BackgroundRectangle(max_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        max_lbl_bg.move_to(max_lbl.get_center())
        beat_3 = beat_group(beat_3, max_dot, max_lbl, max_lbl_bg)
        self.play(FadeIn(max_dot, run_time=0.3))
        self.play(FadeIn(max_lbl_bg, run_time=0.3), FadeIn(max_lbl, run_time=0.7))
        self.wait(1.0)

        # Local min at x = 1, y = -2.
        min_dot = Dot(ax2.c2p(1, -2), color=ORANGE_TERM, radius=0.08)
        min_lbl = MathTex(r"\text{local min}", color=ORANGE_TERM).scale(0.85)
        min_lbl.next_to(min_dot, DR, buff=0.2)
        min_lbl_bg = BackgroundRectangle(min_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        min_lbl_bg.move_to(min_lbl.get_center())
        beat_3 = beat_group(beat_3, min_dot, min_lbl, min_lbl_bg)
        self.play(FadeIn(min_dot, run_time=0.3))
        self.play(FadeIn(min_lbl_bg, run_time=0.3), FadeIn(min_lbl, run_time=0.7))
        self.wait(1.5)

        # Annotation about turning points, kept inside the safe area.
        tp_note = Text("turning points (peaks/troughs)", font_size=22, color=ORANGE_TERM)
        tp_note.move_to(BAND_CHART_CENTER + RIGHT * 2.6 + UP * 0.4)
        tp_note_bg = BackgroundRectangle(tp_note, color=BLACK, fill_opacity=0.95, buff=0.12)
        tp_note_bg.move_to(tp_note.get_center())
        beat_3 = beat_group(beat_3, tp_note, tp_note_bg)
        self.play(FadeIn(tp_note_bg, run_time=0.3), FadeIn(tp_note, run_time=1.0))
        self.wait(2.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: roots are NOT the y-intercept (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        wrong = MathTex(
            r"\text{root} = y\text{-intercept?}",
            color=RED_REJECT,
        ).scale(1.1)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        beat_4 = beat_group(beat_4, wrong, wrong_bg)
        self.play(FadeIn(wrong_bg, run_time=0.4), Write(wrong, run_time=1.5))
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, cross)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.0)

        # Explanation.
        expl = Text(
            "Roots are x-values where y = 0; the y-intercept is where x = 0.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        expl_bg = BackgroundRectangle(expl, color=BLACK, fill_opacity=0.95, buff=0.18)
        expl_bg.move_to(expl.get_center())
        beat_4 = beat_group(beat_4, expl, expl_bg)
        self.play(FadeIn(expl_bg, run_time=0.3), FadeIn(expl, run_time=1.0))
        self.wait(2.0)

        rem = Text("Read them on different axes.", font_size=22, color=GREEN_OK)
        rem.next_to(expl, DOWN, buff=0.4)
        rem_bg = BackgroundRectangle(rem, color=BLACK, fill_opacity=0.95, buff=0.18)
        rem_bg.move_to(rem.get_center())
        beat_4 = beat_group(beat_4, rem, rem_bg)
        self.play(FadeIn(rem_bg, run_time=0.3), FadeIn(rem, run_time=0.9))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~38 s, total ≈ 85 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Roots: } y = 0,\quad \text{Turning points: } \dfrac{dy}{dx} = 0",
            "Read each feature from its own axis.",
            final_wait=38.0,
        )
