"""
Manim scene for the lesson `prism-cylinder-volume`
(topic `l9-m-prisms-cylinders`).

The volume of any right prism or cylinder is the area of its
cross-section times its length. The scene builds a concrete rectangular
tank (40 × 25 × 30 cm), generalises the formula, then highlights
the cylinder case V = πr²h.

Target duration: ~86 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class PrismCylinderVolumeScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Volume of prisms & cylinders",
            "Cross-section area × height — for any right prism or cylinder.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete rectangular tank: 40 × 25 × 30 cm (~25 s)
        # ──────────────────────────────────────────────────────────────────
        # Three dimension cards in a row.
        d1 = make_term_card("l = 40", "length (cm)", BLUE_TERM)
        d2 = make_term_card("w = 25", "width (cm)", TEAL_TERM)
        d3 = make_term_card("h = 30", "height (cm)", ORANGE_TERM)
        row = VGroup(d1, d2, d3).arrange(RIGHT, buff=0.55)
        row.move_to(BAND_CHART_CENTER + UP * 0.7)
        for m in row:
            m.set_z_index(2)
        self.play(
            FadeIn(d1, shift=UP * 0.2, run_time=1.0),
            FadeIn(d2, shift=UP * 0.2, run_time=1.0),
            FadeIn(d3, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(2.0)

        # The volume of a rectangular prism: l × w × h.
        calc = MathTex(
            r"V \;=\; 40 \times 25 \times 30 \;=\; 30{,}000 \text{ cm}^3",
            color=GREEN_OK,
        ).scale(1.05)
        calc.move_to(BAND_CHART_CENTER + DOWN * 0.4)
        calc_bg = BackgroundRectangle(calc, color=BLACK, fill_opacity=1, buff=0.25)
        calc_bg.move_to(calc.get_center())
        self.play(FadeIn(calc_bg, run_time=0.4), Write(calc, run_time=2.0))
        self.wait(2.5)

        # Convert cm³ to litres.
        litres = MathTex(
            r"1{,}000 \text{ cm}^3 = 1 \text{ L} \;\Rightarrow\; 30 \text{ L}",
            color=ORANGE_TERM,
        ).scale(1.0)
        litres.next_to(calc, DOWN, buff=0.55)
        litres_bg = BackgroundRectangle(litres, color=BLACK, fill_opacity=0.95, buff=0.22)
        litres_bg.move_to(litres.get_center())
        self.play(FadeIn(litres_bg, run_time=0.4), FadeIn(litres, run_time=1.4))
        self.wait(2.5)
        self.play(
            FadeOut(row, run_time=0.8),
            FadeOut(calc, run_time=0.8),
            FadeOut(calc_bg, run_time=0.8),
            FadeOut(litres, run_time=0.8),
            FadeOut(litres_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: V = A × h for any right prism (~20 s)
        # ──────────────────────────────────────────────────────────────────
        general = make_equation_card(r"V \;=\; A \times h", color=BLUE_TERM, scale=1.4)
        general.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in general:
            m.set_z_index(2)
        self.play(FadeIn(general, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        # Label each variable.
        lbl_a = Text("A = area of cross-section", font_size=22, color=BLUE_TERM)
        lbl_a.next_to(general, DOWN, buff=0.5)
        lbl_a_bg = BackgroundRectangle(lbl_a, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl_a_bg.move_to(lbl_a.get_center())

        lbl_h = Text("h = length / height", font_size=22, color=BLUE_TERM)
        lbl_h.next_to(lbl_a, DOWN, buff=0.3)
        lbl_h_bg = BackgroundRectangle(lbl_h, color=BLACK, fill_opacity=0.95, buff=0.15)
        lbl_h_bg.move_to(lbl_h.get_center())

        self.play(FadeIn(lbl_a_bg, run_time=0.4), FadeIn(lbl_a, run_time=1.0))
        self.wait(1.0)
        self.play(FadeIn(lbl_h_bg, run_time=0.4), FadeIn(lbl_h, run_time=1.0))
        self.wait(3.0)
        self.play(
            FadeOut(general, run_time=0.8),
            FadeOut(lbl_a, run_time=0.8),
            FadeOut(lbl_a_bg, run_time=0.8),
            FadeOut(lbl_h, run_time=0.8),
            FadeOut(lbl_h_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Cylinder case: V = πr²h (~14 s)
        # ──────────────────────────────────────────────────────────────────
        cylinder = make_equation_card(
            r"V \;=\; \pi r^{2} h",
            color=ORANGE_TERM, scale=1.4,
        )
        cylinder.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in cylinder:
            m.set_z_index(2)
        self.play(FadeIn(cylinder, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        note = Text(
            "Cross-section is a circle — area πr².",
            font_size=22, color=ORANGE_TERM,
        )
        note.next_to(cylinder, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.2))
        self.wait(2.5)
        self.play(
            FadeOut(cylinder, run_time=0.8),
            FadeOut(note, run_time=0.8),
            FadeOut(note_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~32 s, total ≈ 86 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"V \;=\; A \times h",
            "Cross-section area × height — for any right prism or cylinder.",
            final_wait=32.0,
        )
