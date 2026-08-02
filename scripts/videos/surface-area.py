"""
Manim scene for the lesson `surface-area`
(topic `l9-m-prisms-cylinders`).

Surface area sums the area of every face on the outside of a solid.
The scene unpacks a 5 × 4 × 3 rectangular box face-by-face, then
generalises the SA = 2(lw + lh + wh) formula, and finally unrolls
the cylinder into two circles plus a curved rectangle.

Target duration: ~100 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SurfaceAreaScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Surface area of prisms & cylinders",
            "Sum every face. For cylinders: two circles + curved side.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete box: 5 × 4 × 3, list three face pairs (~25 s)
        # ──────────────────────────────────────────────────────────────────
        intro = Text("A 5 × 4 × 3 cm box has three pairs of faces:",
                     font_size=22, color=BLUE_TERM)
        intro.move_to(BAND_CHART_CENTER + UP * 1.0)
        intro_bg = BackgroundRectangle(intro, color=BLACK, fill_opacity=0.95, buff=0.15)
        intro_bg.move_to(intro.get_center())
        self.play(FadeIn(intro_bg, run_time=0.4), FadeIn(intro, run_time=1.2))
        self.wait(1.5)

        # Three face-pair cards.
        f1 = make_term_card("5 \\times 4 = 20", "two faces (cm²)", BLUE_TERM)
        f2 = make_term_card("5 \\times 3 = 15", "two faces (cm²)", TEAL_TERM)
        f3 = make_term_card("4 \\times 3 = 12", "two faces (cm²)", ORANGE_TERM)
        row = VGroup(f1, f2, f3).arrange(RIGHT, buff=0.5)
        row.move_to(BAND_CHART_CENTER + UP * 0.0)
        for m in row:
            m.set_z_index(2)
        self.play(
            FadeIn(f1, shift=UP * 0.2, run_time=0.9),
            FadeIn(f2, shift=UP * 0.2, run_time=0.9),
            FadeIn(f3, shift=UP * 0.2, run_time=0.9),
        )
        self.wait(2.0)

        # Add the doubled total.
        total = MathTex(
            r"SA \;=\; 2(20 + 15 + 12) \;=\; 2 \times 47 \;=\; 94 \text{ cm}^2",
            color=GREEN_OK,
        ).scale(1.0)
        total.next_to(row, DOWN, buff=0.55)
        total_bg = BackgroundRectangle(total, color=BLACK, fill_opacity=1, buff=0.22)
        total_bg.move_to(total.get_center())
        self.play(FadeIn(total_bg, run_time=0.4), Write(total, run_time=1.8))
        self.wait(2.5)
        self.play(
            FadeOut(intro, run_time=0.6),
            FadeOut(intro_bg, run_time=0.6),
            FadeOut(row, run_time=0.6),
            FadeOut(total, run_time=0.6),
            FadeOut(total_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: SA = 2(lw + lh + wh) (~20 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(
            r"SA \;=\; 2(lw + lh + wh)",
            color=BLUE_TERM, scale=1.3,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        note = Text("Three pairs of identical rectangles — add and double.",
                    font_size=22, color=BLUE_TERM)
        note.next_to(general, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.2))
        self.wait(3.0)
        self.play(
            FadeOut(general, run_time=0.8),
            FadeOut(note, run_time=0.8),
            FadeOut(note_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Cylinder SA: 2πr² + 2πrh (~18 s)
        # ──────────────────────────────────────────────────────────────────
        cyl = make_equation_card(
            r"SA \;=\; 2\pi r^{2} \;+\; 2\pi r h",
            color=ORANGE_TERM, scale=1.15,
        )
        cyl.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in cyl:
            m.set_z_index(2)
        self.play(FadeIn(cyl, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        labels = VGroup(
            Text("two end-circles", font_size=20, color=ORANGE_TERM),
            Text("curved side (unrolls to 2πr × h)", font_size=20, color=ORANGE_TERM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        labels.next_to(cyl, DOWN, buff=0.5)
        lab_bg = BackgroundRectangle(labels, color=BLACK, fill_opacity=0.95, buff=0.18)
        lab_bg.move_to(labels.get_center())
        self.play(FadeIn(lab_bg, run_time=0.4), FadeIn(labels, run_time=1.4))
        self.wait(2.5)
        self.play(
            FadeOut(cyl, run_time=0.8),
            FadeOut(labels, run_time=0.8),
            FadeOut(lab_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~32 s, total ≈ 100 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"SA \;=\; 2\pi r^{2} + 2\pi r h",
            "Two circles + curved side. (For prisms: 2 × (sum of face areas).)",
            final_wait=32.0,
        )
