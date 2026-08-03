"""
Manim scene for the lesson `spheres-and-composites`
(topic `l10a-am-pyramids-cones-spheres`).

Sphere volume V = (4/3)πr³ and surface area A = 4πr². Then a composite
solid: a cylinder with a hemisphere on top. Reject confusing the
hemisphere with a full sphere.

Target duration: ~79 s (matches the audio narration length).
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


class SpheresAndCompositesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Spheres and composite solids",
            "V = (4/3)πr³,  A = 4πr²",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Sphere with V and A formulas (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        sphere = Sphere(
            radius=1.2,
            fill_color=BLUE_TERM,
            fill_opacity=0.35,
            stroke_width=3,
        )
        sphere.move_to(BAND_CHART_CENTER + LEFT * 3.0 + DOWN * 0.2)
        beat_2 = beat_group(beat_2, sphere)

        V_eq = MathTex(r"V = \dfrac{4}{3}\, \pi\, r^{3}", color=GREEN_OK).scale(1.0)
        V_eq.move_to(BAND_CHART_CENTER + RIGHT * 2.5 + UP * 0.5)
        V_eq_bg = BackgroundRectangle(V_eq, color=BLACK, fill_opacity=1, buff=0.25)
        V_eq_bg.move_to(V_eq.get_center())
        beat_3_inner = beat_group(V_eq, V_eq_bg)

        A_eq = MathTex(r"A = 4\, \pi\, r^{2}", color=BLUE_TERM).scale(1.0)
        A_eq.next_to(V_eq, DOWN, buff=0.5)
        A_eq_bg = BackgroundRectangle(A_eq, color=BLACK, fill_opacity=1, buff=0.25)
        A_eq_bg.move_to(A_eq.get_center())
        beat_3_inner = beat_group(beat_3_inner, A_eq, A_eq_bg)

        beat_2 = beat_group(beat_2, beat_3_inner)

        self.play(FadeIn(sphere, run_time=1.6))
        self.wait(1.0)
        self.play(FadeIn(V_eq_bg, run_time=0.4), Write(V_eq, run_time=1.6))
        self.wait(1.0)
        self.play(FadeIn(A_eq_bg, run_time=0.4), Write(A_eq, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Composite: cylinder + hemisphere on top (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        # Cylinder: radius 1, height 1.6, then hemisphere on top.
        cyl = Cylinder(
            radius=1.0,
            height=1.6,
            direction=UP,
            fill_color=BLUE_TERM,
            fill_opacity=0.3,
            stroke_width=3,
        )
        cyl.move_to(BAND_CHART_CENTER + LEFT * 3.0 + DOWN * 0.6)
        beat_3 = beat_group(beat_3, cyl)

        # Hemisphere on top of the cylinder.
        hemi = Sphere(
            radius=1.0,
            fill_color=ORANGE_TERM,
            fill_opacity=0.3,
            stroke_width=3,
        )
        # Position so the equator matches the top of the cylinder.
        hemi_center = cyl.get_top()
        hemi.move_to(hemi_center)
        beat_3 = beat_group(beat_3, hemi)

        # V formula on the right.
        Vc = MathTex(
            r"V = \pi r^{2} h + \dfrac{2}{3}\, \pi\, r^{3}",
            color=GREEN_OK,
        ).scale(1.0)
        Vc.move_to(BAND_CHART_CENTER + RIGHT * 2.5 + UP * 0.5)
        Vc_bg = BackgroundRectangle(Vc, color=BLACK, fill_opacity=1, buff=0.25)
        Vc_bg.move_to(Vc.get_center())
        beat_3 = beat_group(beat_3, Vc, Vc_bg)

        self.play(FadeIn(cyl, run_time=1.5))
        self.play(FadeIn(hemi, run_time=1.2))
        self.wait(1.0)
        self.play(FadeIn(Vc_bg, run_time=0.4), Write(Vc, run_time=1.8))
        self.wait(1.5)

        # Labels.
        lab1 = Text("cylinder: πr²h", font_size=22, color=BLUE_TERM)
        lab1.next_to(Vc, DOWN, buff=0.4)
        lab1_bg = BackgroundRectangle(lab1, color=BLACK, fill_opacity=0.95, buff=0.15)
        lab1_bg.move_to(lab1.get_center())
        lab2 = Text("hemisphere: (2/3)πr³", font_size=22, color=ORANGE_TERM)
        lab2.next_to(lab1, DOWN, buff=0.3)
        lab2_bg = BackgroundRectangle(lab2, color=BLACK, fill_opacity=0.95, buff=0.15)
        lab2_bg.move_to(lab2.get_center())
        beat_3 = beat_group(beat_3, lab1, lab1_bg, lab2, lab2_bg)
        self.play(
            FadeIn(lab1_bg, run_time=0.3), FadeIn(lab1, run_time=0.7),
            FadeIn(lab2_bg, run_time=0.3), FadeIn(lab2, run_time=0.7),
        )
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: hemisphere vs full sphere (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\text{hemisphere} = \dfrac{4}{3}\, \pi\, r^{3}\ \text{?}",
            color=RED_REJECT,
        ).scale(0.95)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.7)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.4),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        expl = Text(
            "A hemisphere is half a sphere — halve the volume formula.",
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
        # Beat 5 — Final takeaway (~34 s, total ≈ 79 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"V = \dfrac{4}{3}\pi r^{3},\quad A = 4\pi r^{2}",
            "Split a composite solid into familiar parts and add their volumes.",
            final_wait=34.0,
        )
