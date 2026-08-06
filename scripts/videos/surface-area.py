"""
Manim scene for the lesson `surface-area`
(topic `l9-m-prisms-cylinders`).

Surface area is the sum of every face on the outside of a solid.
The scene builds a 5 × 4 × 3 rectangular box face-by-face, then
generalises the SA = 2(lw + lh + wh) formula, and finally unrolls a
cylinder into two circles plus a curved rectangle.

The audio narrative runs ~41 s; the scene is paced to match.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SurfaceAreaScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Surface area of prisms & cylinders",
            "Sum every face. For cylinders: two circles + curved side.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete box: 5 × 4 × 3, list three face pairs (~9 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        intro = Text("A 5 × 4 × 3 cm box has three pairs of faces:",
                     font_size=18, color=BLUE_TERM)
        intro.move_to(BAND_CHART_CENTER + UP * 1.4)
        intro_bg = BackgroundRectangle(intro, color=BLACK, fill_opacity=0.95, buff=0.15)
        intro_bg.move_to(intro.get_center())
        beat_2.add(intro, intro_bg)
        self.play(FadeIn(intro_bg, run_time=0.4), FadeIn(intro, run_time=1.0))
        self.wait(0.4)

        # Three face-pair cards.
        f1 = make_term_card("5 \\times 4 = 20", "two faces (cm²)", BLUE_TERM)
        f2 = make_term_card("5 \\times 3 = 15", "two faces (cm²)", TEAL_TERM)
        f3 = make_term_card("4 \\times 3 = 12", "two faces (cm²)", ORANGE_TERM)
        row = VGroup(f1, f2, f3).arrange(RIGHT, buff=0.45)
        row.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in row:
            m.set_z_index(2)
        beat_2.add(row)
        self.play(
            FadeIn(f1, shift=UP * 0.2, run_time=0.8),
            FadeIn(f2, shift=UP * 0.2, run_time=0.8),
            FadeIn(f3, shift=UP * 0.2, run_time=0.8),
        )
        self.wait(0.5)

        # Add the doubled total.
        total = MathTex(
            r"SA = 2(20 + 15 + 12) = 2 \times 47 = 94 \text{ cm}^2",
            color=GREEN_OK,
        ).scale(0.8)
        total.next_to(row, DOWN, buff=0.45)
        total_bg = BackgroundRectangle(total, color=BLACK, fill_opacity=1, buff=0.22)
        total_bg.move_to(total.get_center())
        beat_2.add(total, total_bg)
        self.play(FadeIn(total_bg, run_time=0.4), Write(total, run_time=1.4))
        self.wait(0.8)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: SA = 2(lw + lh + wh) (~6 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        general = make_equation_card(
            r"SA = 2(lw + lh + wh)",
            color=BLUE_TERM, scale=1.05,
        )
        general.move_to(BAND_CHART_CENTER + UP * 0.8)
        for m in general:
            m.set_z_index(2)
        beat_3.add(general)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.2))
        self.wait(0.4)

        note = Text("Three pairs of identical rectangles — add and double.",
                    font_size=18, color=BLUE_TERM)
        note.next_to(general, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        beat_3.add(note, note_bg)
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(1.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Cylinder SA: 2πr² + 2πrh (~7 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        cyl = make_equation_card(
            r"SA = 2\pi r^{2} + 2\pi r h",
            color=ORANGE_TERM, scale=1.0,
        )
        cyl.move_to(BAND_CHART_CENTER + UP * 0.7)
        for m in cyl:
            m.set_z_index(2)
        beat_4.add(cyl)
        self.play(FadeIn(cyl, shift=UP * 0.2, run_time=1.2))
        self.wait(0.3)

        labels = VGroup(
            Text("two end-circles", font_size=18, color=ORANGE_TERM),
            Text("curved side (unrolls to 2πr × h)", font_size=18, color=ORANGE_TERM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        labels.next_to(cyl, DOWN, buff=0.4)
        lab_bg = BackgroundRectangle(labels, color=BLACK, fill_opacity=0.95, buff=0.18)
        lab_bg.move_to(labels.get_center())
        beat_4.add(labels, lab_bg)
        self.play(FadeIn(lab_bg, run_time=0.4), FadeIn(labels, run_time=1.0))
        self.wait(1.0)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"SA = 2\pi r^{2} + 2\pi r h",
            "Two circles + curved side.  (For prisms: 2 × (sum of face areas).)",
            final_wait=78.1,
        )
