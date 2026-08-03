import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class UnitCircleRadiansScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Radians and the unit circle",
            "Wrap a number line around a circle of radius one.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Definition: radians = arc length (~26 s)
        # ──────────────────────────────────────────────────────────────────
        ax = Axes(
            x_range=[-1.6, 1.6, 1],
            y_range=[-1.6, 1.6, 1],
            x_length=2.6,
            y_length=2.6,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        ).move_to(BAND_CHART_CENTER + UP * 0.05)

        circle = Circle(radius=1.3, color=BLUE_TERM, stroke_width=2).move_to(ax.get_center())
        for m in (ax, circle):
            m.set_z_index(0)
        self.play(Create(ax, run_time=1.2), Create(circle, run_time=1.2))
        self.wait(2.0)

        # Mark radius = 1
        radius = Line(
            ax.get_center(),
            ax.c2p(1, 0),
            color=BLUE_TERM,
            stroke_width=3,
        )
        radius_lbl = MathTex("r = 1", color=BLUE_TERM).scale(0.8)
        radius_lbl.next_to(radius, DOWN, buff=0.15)
        radius_lbl_bg = BackgroundRectangle(radius_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        radius_lbl_bg.move_to(radius_lbl.get_center())
        self.play(Create(radius, run_time=1.0))
        self.play(FadeIn(radius_lbl_bg, run_time=0.3), FadeIn(radius_lbl, run_time=0.8))
        self.wait(3.0)

        # Define radians
        defn = Text(
            "Angle in radians = arc length swept out",
            font_size=22,
            color=BLUE_TERM,
        ).move_to(BAND_CHART_CENTER + DOWN * 1.2)
        defn_bg = BackgroundRectangle(defn, color=BLACK, fill_opacity=0.95, buff=0.15)
        defn_bg.move_to(defn.get_center())
        self.play(FadeIn(defn_bg, run_time=0.4), FadeIn(defn, run_time=1.2))
        self.wait(8.0)

        beat1 = beat_group(ax, circle, radius, radius_lbl, radius_lbl_bg, defn, defn_bg)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Conversions: 2pi = 360, pi = 180, 1 rad ≈ 57.3 deg (~30 s)
        # ──────────────────────────────────────────────────────────────────
        full = make_equation_card(
            r"2\pi \;\text{rad} \;=\; 360^{\circ}",
            color=TEAL_TERM,
            scale=1.0,
        )
        full.move_to(BAND_CHART_CENTER + UP * 0.8)
        self.play(FadeIn(full, run_time=1.4))
        self.wait(3.0)

        half = make_equation_card(
            r"\pi \;\text{rad} \;=\; 180^{\circ}",
            color=TEAL_TERM,
            scale=1.0,
        )
        half.next_to(full, DOWN, buff=0.5)
        self.play(FadeIn(half, run_time=1.4))
        self.wait(3.0)

        one_rad = make_equation_card(
            r"1 \;\text{rad} \;\approx\; 57.3^{\circ}",
            color=TEAL_TERM,
            scale=0.95,
        )
        one_rad.next_to(half, DOWN, buff=0.5)
        self.play(FadeIn(one_rad, run_time=1.4))
        self.wait(10.0)

        beat2 = beat_group(full, half, one_rad)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Read-off: (cos, sin) on the circle (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Mini unit circle.
        ax2 = Axes(
            x_range=[-1.6, 1.6, 1],
            y_range=[-1.6, 1.6, 1],
            x_length=2.6,
            y_length=2.6,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 1.2},
        ).move_to(BAND_CHART_CENTER + LEFT * 2.2 + UP * 0.2)
        c2 = Circle(radius=1.3, color=BLUE_TERM, stroke_width=2).move_to(ax2.get_center())
        for m in (ax2, c2):
            m.set_z_index(0)

        # A point on the circle at angle ~0.7 rad (Q1).
        import math as _m
        theta = 0.9
        px = _m.cos(theta)
        py = _m.sin(theta)
        dot = Dot(ax2.c2p(px, py), color=ORANGE_TERM, radius=0.08)
        dot.set_z_index(3)

        # The angle arc.
        arc = Arc(radius=0.5, start_angle=0, angle=theta, color=ORANGE_TERM, stroke_width=2)
        arc.move_arc_center_to(ax2.get_center())

        theta_lbl = MathTex(r"\theta", color=ORANGE_TERM).scale(0.8)
        theta_lbl.move_to(ax2.get_center() + RIGHT * 0.6 + UP * 0.25)
        theta_lbl_bg = BackgroundRectangle(theta_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        theta_lbl_bg.move_to(theta_lbl.get_center())

        self.play(Create(ax2, run_time=0.8), Create(c2, run_time=0.8))
        self.play(Create(arc, run_time=1.0))
        self.play(FadeIn(theta_lbl_bg, run_time=0.3), FadeIn(theta_lbl, run_time=0.8))
        self.play(FadeIn(dot, run_time=0.8))
        self.wait(3.0)

        # Point coordinates.
        coord = MathTex(
            r"(\cos\theta,\; \sin\theta)",
            color=GREEN_OK,
        ).scale(1.0)
        coord.move_to(BAND_CHART_CENTER + RIGHT * 2.6 + UP * 0.2)
        coord_bg = BackgroundRectangle(coord, color=BLACK, fill_opacity=0.95, buff=0.18)
        coord_bg.move_to(coord.get_center())
        self.play(FadeIn(coord_bg, run_time=0.4), FadeIn(coord, run_time=1.4))
        self.wait(6.0)

        beat3 = beat_group(ax2, c2, arc, dot, theta_lbl, theta_lbl_bg, coord, coord_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~40 s, total ≈ 90 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\theta \;\text{rad} \;\mapsto\; (\cos\theta,\; \sin\theta)",
            "Read sine and cosine for free from the unit circle.",
            final_wait=40.0,
        )
