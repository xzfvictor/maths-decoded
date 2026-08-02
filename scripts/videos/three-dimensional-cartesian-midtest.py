"""
Manim scene for the lesson `three-dimensional-cartesian`
(topic `l8-sp-3d-coordinates`).

To go from a flat plane to 3D space, just add a third axis (z) that runs
up and down. All three axes meet at the origin (0, 0, 0) and slice space
into eight octants. A point becomes an ordered triple (x, y, z).

Target duration: ~90 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class ThreeDimensionalCartesianScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Three-dimensional coordinates",
            "Add a z-axis to the x-y plane — points become (x, y, z).",
            hold=1.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — 2D plane review, then add the z-axis (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        # Draw a simple 2D axes pair first (top half).
        x_axis = Arrow(start=[-5.0, 0.5, 0], end=[5.0, 0.5, 0],
                       color=BLUE_TERM, buff=0, stroke_width=4)
        y_axis = Arrow(start=[-2.5, -2.0, 0], end=[-2.5, 3.5, 0],
                       color=BLUE_TERM, buff=0, stroke_width=4)
        x_lbl = MathTex("x", color=BLUE_TERM).scale(1.2).next_to(x_axis, RIGHT, buff=0.2)
        y_lbl = MathTex("y", color=BLUE_TERM).scale(1.2).next_to(y_axis, UP, buff=0.2)
        # Keep the y-label out of the subtitle band; subtitle lives at y ≈ 2.4.
        y_lbl.move_to([y_axis.get_start()[0], 1.4, 0])
        o_lbl = MathTex("O", color=WHITE).scale(0.9).move_to([-2.7, 0.2, 0])
        o_lbl_bg = BackgroundRectangle(o_lbl, color=BLACK, fill_opacity=0.9, buff=0.1)
        o_lbl_bg.move_to(o_lbl.get_center())

        self.play(Create(x_axis, run_time=1.0), Create(y_axis, run_time=1.0))
        self.play(FadeIn(x_lbl, run_time=0.5), FadeIn(y_lbl, run_time=0.5))
        self.play(FadeIn(o_lbl, run_time=0.4), FadeIn(o_lbl_bg, run_time=0.3))
        self.wait(2.5)

        # Point (3, 2) on the 2D plane.
        p_2d = Dot([-2.5 + 3.0, 0.5 + 2.0, 0], color=GREEN_OK, radius=0.1)
        p_2d_lbl = MathTex("(3,\,2)", color=GREEN_OK).scale(0.9).next_to(p_2d, UR, buff=0.15)
        p_2d_lbl_bg = BackgroundRectangle(p_2d_lbl, color=BLACK, fill_opacity=0.9, buff=0.1)
        p_2d_lbl_bg.move_to(p_2d_lbl.get_center())
        self.play(FadeIn(p_2d, run_time=0.8), FadeIn(p_2d_lbl, run_time=0.6),
                  FadeIn(p_2d_lbl_bg, run_time=0.4))
        self.wait(2.0)

        # Now add the z-axis going up.
        z_axis = Arrow(start=[-2.5, 0.5, 0], end=[-2.5, 0.5 + 4.0, 0],
                       color=ORANGE_TERM, buff=0, stroke_width=4)
        z_lbl = MathTex("z", color=ORANGE_TERM).scale(1.2).next_to(z_axis, UP, buff=0.2)
        self.play(Create(z_axis, run_time=1.5))
        self.play(FadeIn(z_lbl, run_time=0.5))
        self.wait(2.5)

        beat_2 = beat_group(beat_2, x_axis, y_axis, x_lbl, y_lbl, o_lbl, o_lbl_bg,
                            p_2d, p_2d_lbl, p_2d_lbl_bg,
                            z_axis, z_lbl)
        self.wait(120)
        raise SystemExit(0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Concrete 3D point: (1, 2, 3) (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        # Build a 3D coordinate frame: x across, y into-page (faked as
        # diagonal up-right), z vertical. Mark a point at (1, 2, 3).
        ax_x = Arrow(start=[-5.0, -1.5, 0], end=[3.0, -1.5, 0],
                     color=BLUE_TERM, buff=0, stroke_width=4)
        ax_y = Arrow(start=[-5.0, -1.5, 0], end=[-3.0, 0.5, 0],
                     color=TEAL_TERM, buff=0, stroke_width=4)
        ax_z = Arrow(start=[-5.0, -1.5, 0], end=[-5.0, 2.5, 0],
                     color=ORANGE_TERM, buff=0, stroke_width=4)
        lbl_x = MathTex("x", color=BLUE_TERM).scale(1.1).next_to(ax_x, RIGHT, buff=0.2)
        lbl_y = MathTex("y", color=TEAL_TERM).scale(1.1).next_to(ax_y, UR, buff=0.2)
        lbl_z = MathTex("z", color=ORANGE_TERM).scale(1.1).next_to(ax_z, UP, buff=0.2)
        origin = Dot([-5.0, -1.5, 0], color=WHITE, radius=0.08)
        o_lbl2 = MathTex("(0,0,0)", color=WHITE).scale(0.8).next_to(origin, DL, buff=0.2)
        o_lbl2_bg = BackgroundRectangle(o_lbl2, color=BLACK, fill_opacity=0.9, buff=0.1)
        o_lbl2_bg.move_to(o_lbl2.get_center())

        self.play(Create(ax_x, run_time=1.0), Create(ax_y, run_time=1.0),
                  Create(ax_z, run_time=1.0))
        self.play(FadeIn(lbl_x, run_time=0.4), FadeIn(lbl_y, run_time=0.4),
                  FadeIn(lbl_z, run_time=0.4))
        self.play(FadeIn(origin, run_time=0.5), FadeIn(o_lbl2, run_time=0.4),
                  FadeIn(o_lbl2_bg, run_time=0.3))
        self.wait(2.5)

        # Mark the point (1, 2, 3): x = 1 (RIGHT), y = 2 (diagonal UR), z = 3 (UP).
        # Position = origin + 1·x_dir + 2·y_dir + 3·z_dir (unit = 1).
        x_dir = np.array([8.0, 0.0, 0.0]) / 1.0       # x-axis runs from -5 → +3
        y_dir = np.array([2.0, 2.0, 0.0]) / 1.0       # y-axis runs from -5,-1.5 → -3,0.5
        z_dir = np.array([0.0, 4.0, 0.0]) / 1.0       # z-axis runs from -5,-1.5 → -5,2.5
        # Choose a "natural" scale per unit so 1 unit of each axis ≈ 0.8 screen units.
        sx = 0.8; sy = 0.8; sz = 0.8
        pos = np.array([-5.0, -1.5, 0.0]) + 1.0 * x_dir / np.linalg.norm(x_dir) * sx \
              + 2.0 * y_dir / np.linalg.norm(y_dir) * sy \
              + 3.0 * z_dir / np.linalg.norm(z_dir) * sz

        p3 = Dot(pos, color=GREEN_OK, radius=0.1)
        p3_lbl = MathTex("(1,\,2,\,3)", color=GREEN_OK).scale(0.9).next_to(p3, UR, buff=0.2)
        p3_lbl_bg = BackgroundRectangle(p3_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        p3_lbl_bg.move_to(p3_lbl.get_center())
        self.play(FadeIn(p3, run_time=0.8), FadeIn(p3_lbl, run_time=0.6),
                  FadeIn(p3_lbl_bg, run_time=0.4))
        self.wait(3.0)

        # Annotation: x=1, y=2, z=3.
        explain = Text("x = 1 across · y = 2 forward · z = 3 up", font_size=22, color=GREEN_OK)
        explain.move_to(BAND_CHART_CENTER + DOWN * 2.7)
        explain_bg = BackgroundRectangle(explain, color=BLACK, fill_opacity=0.95, buff=0.15)
        explain_bg.move_to(explain.get_center())
        self.play(FadeIn(explain_bg, run_time=0.4), FadeIn(explain, run_time=1.2))
        self.wait(4.0)

        beat_3 = beat_group(beat_3, ax_x, ax_y, ax_z, lbl_x, lbl_y, lbl_z,
                            origin, o_lbl2, o_lbl2_bg,
                            p3, p3_lbl, p3_lbl_bg,
                            explain, explain_bg)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Order matters: swapping gives a different point (~10 s)
        # ──────────────────────────────────────────────────────────────────
        swapped = MathTex(r"(3,\,1,\,2) \;\neq\; (1,\,2,\,3)", color=RED_REJECT).scale(1.1)
        swapped.move_to(BAND_CHART_CENTER + UP * 0.5)
        swapped_bg = BackgroundRectangle(swapped, color=BLACK, fill_opacity=1, buff=0.25)
        swapped_bg.move_to(swapped.get_center())
        self.play(FadeIn(swapped_bg, run_time=0.5), Write(swapped, run_time=2.0))
        self.wait(3.5)

        warn = Text(
            "Swapping two numbers gives a completely different point.",
            font_size=22, color=RED_REJECT,
        ).next_to(swapped, DOWN, buff=0.6)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=0.95, buff=0.15)
        warn_bg.move_to(warn.get_center())
        self.play(FadeIn(warn_bg, run_time=0.4), FadeIn(warn, run_time=1.2))
        self.wait(3.0)

        beat_4 = beat_group(swapped, swapped_bg, warn, warn_bg)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~34 s, total ≈ 90 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Point in space} \;=\; (x,\; y,\; z)",
            "Three perpendicular axes meet at the origin (0, 0, 0).",
            final_wait=34.0,
        )