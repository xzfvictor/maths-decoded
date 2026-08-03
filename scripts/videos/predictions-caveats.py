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
            "Use the line for prediction — but know where it fails.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Interpolation: in-range x, trustworthy (~28 s)
        # ──────────────────────────────────────────────────────────────────
        ax = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 11, 1],
            x_length=6.0,
            y_length=2.5,
            tips=False,
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
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=BLUE_TERM, radius=0.06) for x, y in pts
        ])
        dots.set_z_index(2)
        line = ax.plot(
            lambda x: 1 + 0.8 * x,
            x_range=[0.0, 10.0],
            color=GREEN_OK,
            stroke_width=3,
        )
        line.set_z_index(3)

        self.play(Create(ax, run_time=1.0))
        self.play(*[FadeIn(m, run_time=0.5) for m in x_lbls])
        self.play(FadeIn(dots, run_time=1.2), Create(line, run_time=1.5))
        self.wait(3.0)

        # Mark a query x in the data range.
        qx = 4.5
        qy = 1 + 0.8 * qx
        qdot = Dot(ax.c2p(qx, qy), color=ORANGE_TERM, radius=0.08)
        qdot.set_z_index(4)
        qlbl = MathTex("x = 4.5", color=ORANGE_TERM).scale(0.8)
        qlbl.next_to(qdot, UR, buff=0.15)
        qlbl_bg = BackgroundRectangle(qlbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        qlbl_bg.move_to(qlbl.get_center())
        self.play(FadeIn(qdot, run_time=0.6))
        self.play(FadeIn(qlbl_bg, run_time=0.3), FadeIn(qlbl, run_time=0.8))
        self.wait(3.0)

        # In-range note.
        ok = Text(
            "Inside the data range — trustworthy interpolation.",
            font_size=22,
            color=GREEN_OK,
        ).move_to(BAND_CHART_CENTER + DOWN * 1.25)
        ok_bg = BackgroundRectangle(ok, color=BLACK, fill_opacity=0.95, buff=0.15)
        ok_bg.move_to(ok.get_center())
        self.play(FadeIn(ok_bg, run_time=0.4), FadeIn(ok, run_time=1.2))
        self.wait(8.0)

        beat1 = beat_group(ax, x_lbls, dots, line, qdot, qlbl, qlbl_bg, ok, ok_bg)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Extrapolation: out-of-range, risky (~28 s)
        # ──────────────────────────────────────────────────────────────────
        # Same scatter + line, but a query far to the right.
        ax2 = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 16, 2],
            x_length=6.0,
            y_length=2.5,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        ).move_to(BAND_CHART_CENTER + UP * 0.05)
        x_lbls2 = VGroup(*[
            MathTex(str(i), font_size=18).next_to(ax2.c2p(i, 0), DOWN, buff=0.12)
            for i in [0, 5, 10, 12, 14]
        ])
        for m in (ax2, x_lbls2):
            m.set_z_index(0)

        # Same line, but extended past the data range.
        line2 = ax2.plot(
            lambda x: 1 + 0.8 * x,
            x_range=[0.0, 14.0],
            color=RED_REJECT,
            stroke_width=3,
        )
        line2.set_z_index(2)

        # A query way out at x = 13.
        qx2 = 13.0
        qy2 = 1 + 0.8 * qx2
        qdot2 = Dot(ax2.c2p(qx2, qy2), color=ORANGE_TERM, radius=0.08)
        qdot2.set_z_index(3)
        qlbl2 = MathTex("x = 13", color=ORANGE_TERM).scale(0.8)
        qlbl2.next_to(qdot2, UR, buff=0.15)
        qlbl2_bg = BackgroundRectangle(qlbl2, color=BLACK, fill_opacity=0.95, buff=0.1)
        qlbl2_bg.move_to(qlbl2.get_center())

        # Dashed boundary to mark "end of data".
        boundary = DashedLine(
            ax2.c2p(10, 0),
            ax2.c2p(10, 16),
            color=RED_REJECT,
            stroke_width=2,
        )
        boundary.set_z_index(1)
        end_lbl = Text("end of data", font_size=18, color=RED_REJECT)
        end_lbl.move_to(ax2.c2p(10, 14))
        end_lbl_bg = BackgroundRectangle(end_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        end_lbl_bg.move_to(end_lbl.get_center())

        self.play(Create(ax2, run_time=1.0))
        self.play(*[FadeIn(m, run_time=0.5) for m in x_lbls2])
        self.play(Create(boundary, run_time=0.8))
        self.play(FadeIn(end_lbl_bg, run_time=0.3), FadeIn(end_lbl, run_time=0.8))
        self.play(Create(line2, run_time=1.5))
        self.play(FadeIn(qdot2, run_time=0.6))
        self.play(FadeIn(qlbl2_bg, run_time=0.3), FadeIn(qlbl2, run_time=0.8))
        self.wait(3.0)

        risk = Text(
            "Outside the data range — extrapolation is risky.",
            font_size=22,
            color=RED_REJECT,
        ).move_to(BAND_CHART_CENTER + DOWN * 1.25)
        risk_bg = BackgroundRectangle(risk, color=BLACK, fill_opacity=0.95, buff=0.15)
        risk_bg.move_to(risk.get_center())
        self.play(FadeIn(risk_bg, run_time=0.4), FadeIn(risk, run_time=1.2))
        self.wait(10.0)

        beat2 = beat_group(ax2, x_lbls2, boundary, end_lbl, end_lbl_bg, line2, qdot2, qlbl2, qlbl2_bg, risk, risk_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Curved data: the line is the wrong tool (~30 s)
        # ──────────────────────────────────────────────────────────────────
        ax3 = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 26, 4],
            x_length=6.0,
            y_length=2.5,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        ).move_to(BAND_CHART_CENTER + UP * 0.05)
        for m in (ax3,):
            m.set_z_index(0)

        # Parabolic-ish points.
        curve_pts = [
            (1.0, 0.5), (2.0, 1.5), (3.0, 3.0), (4.0, 5.0),
            (5.0, 7.5), (6.0, 10.5), (7.0, 14.0), (8.0, 18.0),
            (9.0, 22.5), (10.0, 27.5),
        ]
        curve_dots = VGroup(*[
            Dot(ax3.c2p(x, y), color=BLUE_TERM, radius=0.06) for x, y in curve_pts
        ])
        curve_dots.set_z_index(2)

        # The (bad) straight fit through it.
        bad_line = ax3.plot(
            lambda x: -1.5 + 2.0 * x,
            x_range=[0.0, 10.0],
            color=RED_REJECT,
            stroke_width=3,
        )
        bad_line.set_z_index(3)

        self.play(Create(ax3, run_time=1.0))
        self.play(FadeIn(curve_dots, run_time=1.2), Create(bad_line, run_time=1.5))
        self.wait(3.0)

        warn = Text(
            "Data is curved — a straight line is the wrong tool.",
            font_size=22,
            color=RED_REJECT,
        ).move_to(BAND_CHART_CENTER + DOWN * 1.25)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.15)
        warn_bg.move_to(warn.get_center())
        self.play(FadeIn(warn_bg, run_time=0.4), FadeIn(warn, run_time=1.2))
        self.wait(10.0)

        beat3 = beat_group(ax3, curve_dots, bad_line, warn, warn_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~50 s, total ≈ 110 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Interpolate in-range. Extrapolate with caution.}",
            "A straight line only fits when the data is roughly straight.",
            final_wait=50.0,
        )
