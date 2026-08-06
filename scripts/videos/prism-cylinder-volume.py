"""
Manim scene for the lesson `prism-cylinder-volume`
(topic `l9-m-prisms-cylinders`).

The volume of any right prism or cylinder is the area of its
cross-section times its length. The scene works a concrete rectangular
tank (40 × 25 × 30 cm), generalises, and special-cases the cylinder.

The audio narrative runs ~27 s; the scene is paced to match.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class PrismCylinderVolumeScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Volume of prisms & cylinders",
            "Cross-section area × height — for any right prism or cylinder.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete rectangular tank: 40 × 25 × 30 cm (~8 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        d1 = make_term_card("l = 40", "length (cm)", BLUE_TERM)
        d2 = make_term_card("w = 25", "width (cm)", TEAL_TERM)
        d3 = make_term_card("h = 30", "height (cm)", ORANGE_TERM)
        row = VGroup(d1, d2, d3).arrange(RIGHT, buff=0.5)
        row.move_to(BAND_CHART_CENTER + UP * 1.0)
        for m in row:
            m.set_z_index(2)
        beat_2.add(row)
        self.play(
            FadeIn(d1, shift=UP * 0.2, run_time=0.8),
            FadeIn(d2, shift=UP * 0.2, run_time=0.8),
            FadeIn(d3, shift=UP * 0.2, run_time=0.8),
        )
        self.wait(0.5)

        # The volume of a rectangular prism: l × w × h.
        calc = MathTex(
            r"V = 40 \times 25 \times 30 = 30{,}000 \text{ cm}^3",
            color=GREEN_OK,
        ).scale(0.85)
        calc.move_to(BAND_CHART_CENTER + UP * 0.0)
        calc_bg = BackgroundRectangle(calc, color=BLACK, fill_opacity=1, buff=0.25)
        calc_bg.move_to(calc.get_center())
        beat_2.add(calc, calc_bg)
        self.play(FadeIn(calc_bg, run_time=0.4), Write(calc, run_time=1.4))
        self.wait(0.4)

        # Convert cm³ to litres.
        litres = MathTex(
            r"1{,}000 \text{ cm}^3 = 1 \text{ L} \;\Rightarrow\; 30 \text{ L}",
            color=ORANGE_TERM,
        ).scale(0.85)
        litres.next_to(calc, DOWN, buff=0.4)
        litres_bg = BackgroundRectangle(litres, color=BLACK, fill_opacity=0.95, buff=0.22)
        litres_bg.move_to(litres.get_center())
        beat_2.add(litres, litres_bg)
        self.play(FadeIn(litres_bg, run_time=0.4), FadeIn(litres, run_time=1.0))
        self.wait(0.8)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: V = A × h for any right prism (~6 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        general = make_equation_card(r"V = A \times h", color=BLUE_TERM, scale=1.1)
        general.move_to(BAND_CHART_CENTER + UP * 0.8)
        for m in general:
            m.set_z_index(2)
        beat_3.add(general)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.2))
        self.wait(0.4)

        # Label each variable.
        lbl_a = Text("A = area of cross-section", font_size=18, color=BLUE_TERM)
        lbl_a.next_to(general, DOWN, buff=0.4)
        lbl_a_bg = BackgroundRectangle(lbl_a, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl_a_bg.move_to(lbl_a.get_center())

        lbl_h = Text("h = length / height", font_size=18, color=BLUE_TERM)
        lbl_h.next_to(lbl_a, DOWN, buff=0.25)
        lbl_h_bg = BackgroundRectangle(lbl_h, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl_h_bg.move_to(lbl_h.get_center())

        beat_3.add(lbl_a, lbl_a_bg, lbl_h, lbl_h_bg)
        self.play(FadeIn(lbl_a_bg, run_time=0.4), FadeIn(lbl_a, run_time=0.8))
        self.wait(0.4)
        self.play(FadeIn(lbl_h_bg, run_time=0.4), FadeIn(lbl_h, run_time=0.8))
        self.wait(1.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Cylinder case: V = πr²h (~5 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        cylinder = make_equation_card(
            r"V = \pi r^{2} h",
            color=ORANGE_TERM, scale=1.1,
        )
        cylinder.move_to(BAND_CHART_CENTER + UP * 0.8)
        for m in cylinder:
            m.set_z_index(2)
        beat_4.add(cylinder)
        self.play(FadeIn(cylinder, shift=UP * 0.2, run_time=1.2))
        self.wait(0.3)

        note = Text(
            "Cross-section is a circle — area πr².",
            font_size=18, color=ORANGE_TERM,
        )
        note.next_to(cylinder, DOWN, buff=0.45)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        beat_4.add(note, note_bg)
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=0.9))
        self.wait(0.6)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"V = A \times h",
            "Cross-section area × height — for any right prism or cylinder.",
            final_wait=105.8,
        )
