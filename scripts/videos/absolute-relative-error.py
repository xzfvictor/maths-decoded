"""
Manim scene for the lesson `absolute-relative-error`
(topic `l9-m-errors-in-measurements`).

Absolute error is $|measured - true|$ in the original units; relative
error divides by the true value to remove units. Same idea, two
flavours.

The audio narrative runs ~25 s; the scene is paced to match.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class AbsoluteRelativeErrorScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Absolute and relative error",
            "Same units vs no units — pick the right one for the comparison.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Absolute error: formula + units + worked example (~7 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        abs_eq = MathTex(
            r"\text{absolute error} = \bigl|\text{measured} - \text{true}\bigr|",
            color=BLUE_TERM,
        ).scale(0.85)
        abs_eq.move_to(BAND_CHART_CENTER + UP * 1.4)
        abs_eq_bg = BackgroundRectangle(abs_eq, color=BLACK, fill_opacity=1, buff=0.25)
        abs_eq_bg.move_to(abs_eq.get_center())
        beat_2.add(abs_eq, abs_eq_bg)
        self.play(FadeIn(abs_eq_bg, run_time=0.4), Write(abs_eq, run_time=1.6))
        self.wait(0.6)

        units_note = Text("Same units as the measurement.",
                          font_size=18, color=BLUE_TERM)
        units_note.next_to(abs_eq, DOWN, buff=0.3)
        units_note_bg = BackgroundRectangle(units_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        units_note_bg.move_to(units_note.get_center())
        beat_2.add(units_note, units_note_bg)
        self.play(FadeIn(units_note_bg, run_time=0.4), FadeIn(units_note, run_time=0.9))
        self.wait(0.5)

        # Worked example: timber measured 3.45 m, true 3.50 m.
        example = MathTex(
            r"\bigl|\,3.45 \,\text{m} - 3.50 \,\text{m}\,\bigr| = 0.05 \,\text{m}",
            color=WHITE,
        ).scale(0.85)
        example.move_to(BAND_CHART_CENTER + DOWN * 0.3)
        example_bg = BackgroundRectangle(example, color=BLACK, fill_opacity=1, buff=0.25)
        example_bg.move_to(example.get_center())
        beat_2.add(example, example_bg)
        self.play(FadeIn(example_bg, run_time=0.4), Write(example, run_time=1.6))
        self.wait(0.8)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Relative error: formula + worked example (~7 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        rel_eq = MathTex(
            r"\text{relative error} = "
            r"\dfrac{\text{absolute error}}{\text{true value}}",
            color=TEAL_TERM,
        ).scale(0.85)
        rel_eq.move_to(BAND_CHART_CENTER + UP * 1.4)
        rel_eq_bg = BackgroundRectangle(rel_eq, color=BLACK, fill_opacity=1, buff=0.25)
        rel_eq_bg.move_to(rel_eq.get_center())
        beat_3.add(rel_eq, rel_eq_bg)
        self.play(FadeIn(rel_eq_bg, run_time=0.4), Write(rel_eq, run_time=1.6))
        self.wait(0.5)

        no_units = Text("No units — a pure number.",
                        font_size=18, color=TEAL_TERM)
        no_units.next_to(rel_eq, DOWN, buff=0.3)
        no_units_bg = BackgroundRectangle(no_units, color=BLACK, fill_opacity=0.95, buff=0.15)
        no_units_bg.move_to(no_units.get_center())
        beat_3.add(no_units, no_units_bg)
        self.play(FadeIn(no_units_bg, run_time=0.4), FadeIn(no_units, run_time=0.9))
        self.wait(0.4)

        # Worked example: bag measured 1.02 kg, true 1.00 kg.
        rel_example = MathTex(
            r"\dfrac{0.02}{1.00} = 0.02",
            color=WHITE,
        ).scale(0.95)
        rel_example.move_to(BAND_CHART_CENTER + DOWN * 0.3)
        rel_example_bg = BackgroundRectangle(rel_example, color=BLACK, fill_opacity=1, buff=0.25)
        rel_example_bg.move_to(rel_example.get_center())
        beat_3.add(rel_example, rel_example_bg)
        self.play(FadeIn(rel_example_bg, run_time=0.4), Write(rel_example, run_time=1.4))
        self.wait(0.7)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: dividing by measured value (~4 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        bad = MathTex(
            r"\dfrac{\text{absolute error}}{\text{measured value}}",
            color=RED_REJECT,
        ).scale(0.85)
        bad.move_to(BAND_CHART_CENTER + UP * 0.6)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        beat_4.add(bad, bad_bg)
        self.play(FadeIn(bad_bg, run_time=0.4), Write(bad, run_time=1.6))
        self.wait(0.4)

        bad_note = Text(
            "Always divide by the TRUE value, not the measured one.",
            font_size=18, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.4)
        bad_note_bg = BackgroundRectangle(bad_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        bad_note_bg.move_to(bad_note.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        beat_4.add(cross, bad_note, bad_note_bg)
        self.play(Create(cross, run_time=0.9))
        self.play(FadeIn(bad_note_bg, run_time=0.4), FadeIn(bad_note, run_time=0.9))
        self.wait(0.6)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\dfrac{|\,\text{measured} - \text{true}\,|}{\text{true}}",
            "Absolute: original units.  Relative: unit-free fraction.",
            final_wait=20.0,
        )
