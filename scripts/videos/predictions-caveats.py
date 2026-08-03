"""
Manim scene for the lesson `predictions-caveats`
(topic `l10a-ast-bivariate-lines`).

Using a line of best fit to predict new values: interpolation between
data points is trustworthy, but extrapolation outside the range is
risky. A line is only the right tool when the data is roughly linear.
Communicate uncertainty: residuals tell you how far each point sits
above or below the line.

Target duration: ~110 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class PredictionsCaveatsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Predictions and their caveats",
            "Interpolation is fine, extrapolation is risky.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Interpolation vs extrapolation (~28 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        ax = Axes(
            x_range=[0, 11, 1], y_range=[0, 11, 1],
            x_length=5.2, y_length=2.3, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        ).move_to(BAND_CHART_CENTER + UP * 0.05)
        x_lbls = VGroup(*[
            MathTex(str(i), font_size=18).next_to(ax.c2p(i, 0), DOWN, buff=0.12)
            for i in [0, 5, 10]
        ])
        for m in (ax, x_lbls):
            m.set_z_index(0)

        pts = [
            (1.0, 1.7), (2.0, 2.4), (3.0, 3.6), (4.0, 4.0),
            (5.0, 5.3), (6.0, 5.7), (7.0, 6.8), (8.0, 7.4),
            (9.0, 8.2), (10.0, 9.1),
        ]
        dots = VGroup(*[Dot(ax.c2p(x, y), color=BLUE_TERM, radius=0.05)
                        for x, y in pts])
        dots.set_z_index(2)
        line = ax.plot(lambda x: 1 + 0.8 * x,
                       x_range=[0.0, 10.0], color=GREEN_OK, stroke_width=3)
        line.set_z_index(3)
        beat_2 = beat_group(beat_2, ax, x_lbls, dots, line)
        self.play(Create(ax, run_time=1.0))
        self.play(*[FadeIn(m, run_time=0.5) for m in x_lbls])
        self.play(FadeIn(dots, run_time=1.0), Create(line, run_time=1.4))
        self.wait(2.0)

        # Mark the interpolation point (x = 4.5).
        qx, qy = 4.5, 1 + 0.8 * 4.5
        qdot = Dot(ax.c2p(qx, qy), color=ORANGE_TERM, radius=0.07)
        qdot.set_z_index(4)
        qlbl = MathTex("x = 4.5", color=ORANGE_TERM).scale(0.7)
        qlbl.next_to(qdot, UR, buff=0.12)
        qlbl_bg = BackgroundRectangle(qlbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        qlbl_bg.move_to(qlbl.get_center())
        beat_2 = beat_group(beat_2, qdot, qlbl, qlbl_bg)
        self.play(FadeIn(qdot, run_time=0.5))
        self.play(FadeIn(qlbl_bg, run_time=0.3), FadeIn(qlbl, run_time=0.7))

        ok = Text("Inside the range — interpolation is trustworthy.",
                  font_size=20, color=GREEN_OK)
        ok.move_to(BAND_CHART_CENTER + DOWN * 1.1)
        ok_bg = BackgroundRectangle(ok, color=BLACK, fill_opacity=0.95, buff=0.13)
        ok_bg.move_to(ok.get_center())
        beat_2 = beat_group(beat_2, ok, ok_bg)
        self.play(FadeIn(ok_bg, run_time=0.4), FadeIn(ok, run_time=1.0))
        self.wait(7.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Curved data: the line is the wrong tool (~28 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        ax3 = Axes(
            x_range=[0, 11, 1], y_range=[0, 26, 4],
            x_length=5.2, y_length=2.3, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        ).move_to(BAND_CHART_CENTER + UP * 0.05)
        ax3.set_z_index(0)

        # Quadratic-shaped data.
        curve_pts = [
            (1.0, 0.5), (2.0, 1.5), (3.0, 3.0), (4.0, 5.0),
            (5.0, 7.5), (6.0, 10.5), (7.0, 14.0), (8.0, 18.0),
            (9.0, 22.5), (10.0, 27.5),
        ]
        curve_dots = VGroup(*[Dot(ax3.c2p(x, y), color=BLUE_TERM, radius=0.05)
                              for x, y in curve_pts])
        curve_dots.set_z_index(2)

        bad_line = ax3.plot(lambda x: -1.5 + 2.0 * x,
                            x_range=[0.0, 10.0], color=RED_REJECT, stroke_width=3)
        bad_line.set_z_index(3)
        beat_3 = beat_group(beat_3, ax3, curve_dots, bad_line)
        self.play(Create(ax3, run_time=1.0))
        self.play(FadeIn(curve_dots, run_time=1.0), Create(bad_line, run_time=1.4))
        self.wait(2.5)

        warn = Text("Data curves — fit a curve, not a line.",
                    font_size=22, color=RED_REJECT)
        warn.move_to(BAND_CHART_CENTER + DOWN * 1.1)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.14)
        warn_bg.move_to(warn.get_center())
        beat_3 = beat_group(beat_3, warn, warn_bg)
        self.play(FadeIn(warn_bg, run_time=0.4), FadeIn(warn, run_time=1.2))
        self.wait(13.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Uncertainty and residuals (~30 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        # Simple scatter+line: vertical residual sticks.
        ax4 = Axes(
            x_range=[0, 10, 1], y_range=[0, 10, 2],
            x_length=4.8, y_length=2.3, tips=False,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        ).move_to(BAND_CHART_CENTER + UP * 0.4 + LEFT * 2.8)
        x_lbls4 = VGroup(*[
            MathTex(str(i), font_size=18).next_to(ax4.c2p(i, 0), DOWN, buff=0.12)
            for i in [0, 5]
        ])
        fit = ax4.plot(lambda x: 1 + 0.7 * x,
                       x_range=[0, 10], color=GREEN_OK, stroke_width=3)

        # Three scattered points with residual sticks.
        samples = [(2, 3.0, 1.4), (5, 4.7, 0.2), (8, 6.2, -1.0)]
        res_sticks = VGroup()
        sample_dots = VGroup()
        for x, y, resid in samples:
            sample_dots.add(Dot(ax4.c2p(x, y), color=BLUE_TERM, radius=0.06))
            on_line = 1 + 0.7 * x
            stick = Line(ax4.c2p(x, on_line), ax4.c2p(x, y),
                         color=ORANGE_TERM, stroke_width=2)
            res_sticks.add(stick)

        beat_4 = beat_group(beat_4, ax4, x_lbls4, fit, sample_dots, res_sticks)
        self.play(Create(ax4, run_time=0.8))
        self.play(*[FadeIn(m, run_time=0.4) for m in x_lbls4])
        self.play(Create(fit, run_time=1.0))
        self.play(FadeIn(sample_dots, run_time=0.8))
        self.play(*[Create(s, run_time=0.5) for s in res_sticks])

        # Uncertainty and residual message.
        msg = MathTex(
            r"\text{residual} = y_{\text{obs}} - \hat y",
            color=ORANGE_TERM,
        ).scale(0.95)
        msg.move_to(BAND_CHART_CENTER + UP * 0.4 + RIGHT * 2.8)
        msg_bg = BackgroundRectangle(msg, color=BLACK, fill_opacity=1, buff=0.2)
        msg_bg.move_to(msg.get_center())
        beat_4 = beat_group(beat_4, msg, msg_bg)
        self.play(FadeIn(msg_bg, run_time=0.4), FadeIn(msg, run_time=1.4))
        self.wait(1.5)

        check = Text(
            "Plot residuals — random is good, patterned means rethink.",
            font_size=20, color=GREEN_OK,
        )
        check.move_to(BAND_CHART_CENTER + UP * 0.4 + RIGHT * 2.8 + DOWN * 0.8)
        check_bg = BackgroundRectangle(check, color=BLACK, fill_opacity=0.95, buff=0.14)
        check_bg.move_to(check.get_center())
        beat_4 = beat_group(beat_4, check, check_bg)
        self.play(FadeIn(check_bg, run_time=0.4), FadeIn(check, run_time=1.4))
        self.wait(7.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~50 s, total ≈ 110 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Interpolate in-range. Extrapolate with caution.}",
            "Predict, then check residuals before trusting the line.",
            final_wait=50.0,
        )
