"""
Manim scene for the lesson `absolute-relative-error`
(topic `l9-m-errors-in-measurements`).

Absolute error is $|measured - true|$ in the original units; relative
error divides by the true value to remove units, letting us compare
measurements across scales.

Render target: ~84.28 s, matched to the audio narration length.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class AbsoluteRelativeErrorScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (visible for entire animation) + intro (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Absolute and relative error",
            "Units vs no units — pick the right one for the comparison.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Absolute error formula and example (~24 s)
        # ──────────────────────────────────────────────────────────────────
        abs_eq = MathTex(
            r"\text{absolute error} \;=\; \bigl|\,\text{measured} - \text{true}\,\bigr|",
            color=BLUE_TERM,
        ).scale(0.95)
        abs_eq.move_to(BAND_CHART_CENTER + UP * 1.6)
        abs_eq_bg = BackgroundRectangle(abs_eq, color=BLACK, fill_opacity=1, buff=0.25)
        abs_eq_bg.move_to(abs_eq.get_center())
        self.play(FadeIn(abs_eq_bg, run_time=0.5), Write(abs_eq, run_time=2.0))
        self.wait(1.5)

        units_note = Text("Same units as the measurement.",
                          font_size=20, color=BLUE_TERM)
        units_note.next_to(abs_eq, DOWN, buff=0.4)
        units_note_bg = BackgroundRectangle(units_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        units_note_bg.move_to(units_note.get_center())
        self.play(FadeIn(units_note_bg, run_time=0.4), FadeIn(units_note, run_time=1.0))
        self.wait(2.5)

        # Concrete example: timber measured as 3.45 m, true 3.50 m.
        example = MathTex(
            r"\bigl|\,3.45 \,\text{m} - 3.50 \,\text{m}\,\bigr| \;=\; 0.05 \,\text{m}",
            color=WHITE,
        ).scale(0.95)
        example.move_to(BAND_CHART_CENTER + DOWN * 0.2)
        example_bg = BackgroundRectangle(example, color=BLACK, fill_opacity=1, buff=0.25)
        example_bg.move_to(example.get_center())
        self.play(FadeIn(example_bg, run_time=0.5), Write(example, run_time=2.0))
        self.wait(2.5)

        self.play(
            FadeOut(abs_eq, run_time=0.6),
            FadeOut(abs_eq_bg, run_time=0.6),
            FadeOut(units_note, run_time=0.6),
            FadeOut(units_note_bg, run_time=0.6),
            FadeOut(example, run_time=0.6),
            FadeOut(example_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Relative error formula and example (~24 s)
        # ──────────────────────────────────────────────────────────────────
        rel_eq = MathTex(
            r"\text{relative error} \;=\; "
            r"\dfrac{\text{absolute error}}{\text{true value}}",
            color=TEAL_TERM,
        ).scale(0.95)
        rel_eq.move_to(BAND_CHART_CENTER + UP * 1.6)
        rel_eq_bg = BackgroundRectangle(rel_eq, color=BLACK, fill_opacity=1, buff=0.25)
        rel_eq_bg.move_to(rel_eq.get_center())
        self.play(FadeIn(rel_eq_bg, run_time=0.5), Write(rel_eq, run_time=2.0))
        self.wait(1.5)

        no_units = Text("No units — a pure number.",
                        font_size=20, color=TEAL_TERM)
        no_units.next_to(rel_eq, DOWN, buff=0.4)
        no_units_bg = BackgroundRectangle(no_units, color=BLACK, fill_opacity=0.95, buff=0.15)
        no_units_bg.move_to(no_units.get_center())
        self.play(FadeIn(no_units_bg, run_time=0.4), FadeIn(no_units, run_time=1.0))
        self.wait(2.0)

        # Concrete example: bag measured 1.02 kg, true 1.00 kg.
        rel_example = MathTex(
            r"\dfrac{0.02}{1.00} \;=\; 0.02",
            color=WHITE,
        ).scale(1.0)
        rel_example.move_to(BAND_CHART_CENTER + DOWN * 0.2)
        rel_example_bg = BackgroundRectangle(rel_example, color=BLACK, fill_opacity=1, buff=0.25)
        rel_example_bg.move_to(rel_example.get_center())
        self.play(FadeIn(rel_example_bg, run_time=0.5), Write(rel_example, run_time=1.8))
        self.wait(2.5)

        self.play(
            FadeOut(rel_eq, run_time=0.6),
            FadeOut(rel_eq_bg, run_time=0.6),
            FadeOut(no_units, run_time=0.6),
            FadeOut(no_units_bg, run_time=0.6),
            FadeOut(rel_example, run_time=0.6),
            FadeOut(rel_example_bg, run_time=0.6),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: dividing by measured value (~12 s)
        # ──────────────────────────────────────────────────────────────────
        bad = MathTex(
            r"\dfrac{\text{absolute error}}{\text{measured value}}",
            color=RED_REJECT,
        ).scale(0.95)
        bad.move_to(BAND_CHART_CENTER + UP * 0.4)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.5), Write(bad, run_time=1.8))
        self.wait(1.0)

        bad_note = Text("Always divide by the TRUE value, not the measured one.",
                        font_size=20, color=RED_REJECT)
        bad_note.next_to(bad, DOWN, buff=0.5)
        bad_note_bg = BackgroundRectangle(bad_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        bad_note_bg.move_to(bad_note.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=1.0))
        self.play(FadeIn(bad_note_bg, run_time=0.4), FadeIn(bad_note, run_time=1.0))
        self.wait(2.5)

        self.play(
            FadeOut(bad, run_time=0.8),
            FadeOut(bad_bg, run_time=0.8),
            FadeOut(cross, run_time=0.8),
            FadeOut(bad_note, run_time=0.8),
            FadeOut(bad_note_bg, run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~final_wait = 32 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\dfrac{|\,\text{measured} - \text{true}\,|}{\text{true}}",
            "Absolute: in original units.  Relative: unit-free fraction.",
            final_wait=32.0,
        )