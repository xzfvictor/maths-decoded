"""
Manim scene for the lesson `linear-nonlinear`
(topic `l10a-aa-simultaneous-equations`).

Solve {y = x + 1, y = x² - 2} by substitution. Discriminant check
determines 0, 1, or 2 intersection points. Reject forgetting to
substitute back to find y.

Target duration: ~80 s (matches the audio narration length).
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


class LinearNonlinearScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Linear and non-linear: parabola meets line",
            "Substitution gives a quadratic — solve for the x-intersections",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Plot y = x + 1 and y = x² - 2 (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 3.5, 1],
            x_length=6.0,
            y_length=2.6,
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

        # y = x² - 2 and y = x + 1. Solve: x²-2 = x+1 → x²-x-3 = 0 → x = (1±√13)/2.
        # Use discriminant 13 for nice non-integer roots. We'll show two clear
        # intersections: use y = x + 1 and y = x² - 2 directly. Then x²-x-3=0.
        # Roots: x ≈ 2.30 and x ≈ -1.30. Use x_range so both visible.
        parabola = ax.plot(
            lambda x: x**2 - 2,
            x_range=[-2.1, 2.1],
            color=BLUE_TERM,
            stroke_width=4,
        )
        line = ax.plot(
            lambda x: x + 1,
            x_range=[-2.7, 0.4],
            color=ORANGE_TERM,
            stroke_width=4,
        )
        beat_2 = beat_group(beat_2, parabola, line)

        self.play(Create(ax), run_time=1.2)
        self.play(
            *[Write(lbl) for lbl in x_lbls],
            *[Write(lbl) for lbl in y_lbls],
            Write(zero_origin),
            run_time=1.4,
        )
        self.play(Create(parabola), run_time=1.6)
        self.play(Create(line), run_time=1.4)

        # Intersection dots.
        x1, x2 = (1 - np.sqrt(13)) / 2, (1 + np.sqrt(13)) / 2
        y1, y2 = x1 + 1, x2 + 1
        i1 = Dot(ax.c2p(x1, y1), color=GREEN_OK, radius=0.08)
        i2 = Dot(ax.c2p(x2, y2), color=GREEN_OK, radius=0.08)
        lbl1 = MathTex(r"x_{1}", color=GREEN_OK).scale(0.9)
        lbl1.next_to(i1, DL, buff=0.15)
        lbl1_bg = BackgroundRectangle(lbl1, color=BLACK, fill_opacity=0.95, buff=0.1)
        lbl1_bg.move_to(lbl1.get_center())
        lbl2 = MathTex(r"x_{2}", color=GREEN_OK).scale(0.9)
        lbl2.next_to(i2, DR, buff=0.15)
        lbl2_bg = BackgroundRectangle(lbl2, color=BLACK, fill_opacity=0.95, buff=0.1)
        lbl2_bg.move_to(lbl2.get_center())
        beat_2 = beat_group(beat_2, i1, i2, lbl1, lbl1_bg, lbl2, lbl2_bg)
        self.play(
            FadeIn(i1, run_time=0.3),
            FadeIn(i2, run_time=0.3),
        )
        self.play(
            FadeIn(lbl1_bg, run_time=0.2), FadeIn(lbl1, run_time=0.5),
            FadeIn(lbl2_bg, run_time=0.2), FadeIn(lbl2, run_time=0.5),
        )
        self.wait(1.5)

        # Curve labels.
        par_lbl = MathTex(r"y = x^{2} - 2", color=BLUE_TERM).scale(0.8)
        par_lbl.next_to(parabola, UR, buff=0.2).shift(DOWN * 0.5)
        par_lbl_bg = BackgroundRectangle(par_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        par_lbl_bg.move_to(par_lbl.get_center())
        beat_2 = beat_group(beat_2, par_lbl, par_lbl_bg)
        self.play(FadeIn(par_lbl_bg, run_time=0.3), FadeIn(par_lbl, run_time=0.6))
        self.wait(1.5)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Algebra: substitute and solve the quadratic (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        sub = MathTex(
            r"x + 1 = x^{2} - 2 \quad\Rightarrow\quad x^{2} - x - 3 = 0",
            color=GREEN_OK,
        ).scale(0.95)
        sub.move_to(BAND_CHART_CENTER + UP * 0.8)
        sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=1, buff=0.25)
        sub_bg.move_to(sub.get_center())
        beat_3 = beat_group(beat_3, sub, sub_bg)
        self.play(FadeIn(sub_bg, run_time=0.4), Write(sub, run_time=1.8))
        self.wait(1.0)

        # Quadratic formula.
        qf = MathTex(
            r"x = \dfrac{1 \pm \sqrt{1 + 12}}{2} = \dfrac{1 \pm \sqrt{13}}{2}",
            color=GREEN_OK,
        ).scale(0.95)
        qf.next_to(sub, DOWN, buff=0.5)
        qf_bg = BackgroundRectangle(qf, color=BLACK, fill_opacity=1, buff=0.25)
        qf_bg.move_to(qf.get_center())
        beat_3 = beat_group(beat_3, qf, qf_bg)
        self.play(FadeIn(qf_bg, run_time=0.4), Write(qf, run_time=1.8))
        self.wait(1.5)

        # Two solutions.
        sol = MathTex(
            r"x \approx 2.30 \text{ or } x \approx -1.30",
            color=GREEN_OK,
        ).scale(0.95)
        sol.next_to(qf, DOWN, buff=0.5)
        sol_bg = BackgroundRectangle(sol, color=BLACK, fill_opacity=1, buff=0.2)
        sol_bg.move_to(sol.get_center())
        beat_3 = beat_group(beat_3, sol, sol_bg)
        self.play(FadeIn(sol_bg, run_time=0.3), Write(sol, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: forget to substitute back to find y (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\text{found } x, \text{ done?}",
            color=RED_REJECT,
        ).scale(1.1)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.3),
            Write(wrong, run_time=1.3),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        expl = Text(
            "Plug x back into y = x + 1 to get the y-value too.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        expl_bg = BackgroundRectangle(expl, color=BLACK, fill_opacity=0.95, buff=0.18)
        expl_bg.move_to(expl.get_center())
        beat_4 = beat_group(beat_4, expl, expl_bg)
        self.play(FadeIn(expl_bg, run_time=0.3), FadeIn(expl, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~35 s, total ≈ 80 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Substitute} \to \text{quadratic} \to \text{back-substitute for } y",
            "The quadratic's discriminant tells you how many intersections.",
            final_wait=35.0,
        )
