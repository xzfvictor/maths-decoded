"""
Manim scene for the lesson `percentage-error`
(topic `l9-m-errors-in-measurements`).

Percentage error is the relative error expressed as a percentage —
the right tool for comparing across very different scales.

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


class PercentageErrorScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Percentage error",
            "Relative error × 100 — compare across very different scales.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The formula (~5 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        formula = MathTex(
            r"\text{percentage error} = "
            r"\dfrac{\text{absolute error}}{\text{true value}} \times 100\%",
            color=GREEN_OK,
        ).scale(0.85)
        formula.move_to(BAND_CHART_CENTER + UP * 0.8)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.25)
        formula_bg.move_to(formula.get_center())
        beat_2.add(formula, formula_bg)
        self.play(FadeIn(formula_bg, run_time=0.4), Write(formula, run_time=2.0))
        self.wait(0.6)

        rel_link = Text("Just relative error written as a percent.",
                        font_size=18, color=WHITE)
        rel_link.next_to(formula, DOWN, buff=0.4)
        rel_link_bg = BackgroundRectangle(rel_link, color=BLACK, fill_opacity=0.95, buff=0.15)
        rel_link_bg.move_to(rel_link.get_center())
        beat_2.add(rel_link, rel_link_bg)
        self.play(FadeIn(rel_link_bg, run_time=0.4), FadeIn(rel_link, run_time=0.9))
        self.wait(1.2)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: 50 m race (~6 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()
        ex_label = Text("50 m race:  measured 50.4 s,  true 50.0 s",
                        font_size=20, color=BLUE_TERM)
        ex_label.move_to(BAND_CHART_CENTER + UP * 1.3)
        ex_label_bg = BackgroundRectangle(ex_label, color=BLACK, fill_opacity=1, buff=0.2)
        ex_label_bg.move_to(ex_label.get_center())
        beat_3.add(ex_label, ex_label_bg)
        self.play(FadeIn(ex_label_bg, run_time=0.4), FadeIn(ex_label, run_time=1.2))
        self.wait(0.4)

        step1 = MathTex(
            r"|\,50.4 - 50.0\,| = 0.4 \text{ s}",
            color=WHITE,
        ).scale(0.85)
        step1.move_to(BAND_CHART_CENTER + UP * 0.2)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=1, buff=0.25)
        step1_bg.move_to(step1.get_center())
        beat_3.add(step1, step1_bg)
        self.play(FadeIn(step1_bg, run_time=0.4), Write(step1, run_time=1.2))
        self.wait(0.4)

        step2 = MathTex(
            r"\dfrac{0.4}{50.0} \times 100\% = 0.8\%",
            color=GREEN_OK,
        ).scale(0.85)
        step2.move_to(BAND_CHART_CENTER + DOWN * 0.8)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=1, buff=0.25)
        step2_bg.move_to(step2.get_center())
        beat_3.add(step2, step2_bg)
        self.play(FadeIn(step2_bg, run_time=0.4), Write(step2, run_time=1.4))
        self.wait(0.6)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Cross-scale comparison (~5 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()
        comp_title = Text("Two measurements, very different scales",
                          font_size=20, color=WHITE)
        comp_title.move_to(BAND_CHART_CENTER + UP * 1.3)
        comp_title_bg = BackgroundRectangle(comp_title, color=BLACK, fill_opacity=1, buff=0.2)
        comp_title_bg.move_to(comp_title.get_center())
        beat_4.add(comp_title, comp_title_bg)
        self.play(FadeIn(comp_title_bg, run_time=0.4), FadeIn(comp_title, run_time=1.0))
        self.wait(0.3)

        # Measurement A: 100 ± 1 g → 1%.
        a_line = MathTex(
            r"A:\; 100 \pm 1 \text{ g} \;\Rightarrow\; 1\%",
            color=BLUE_TERM,
        ).scale(0.85)
        a_line.move_to(BAND_CHART_CENTER + UP * 0.3)
        a_line_bg = BackgroundRectangle(a_line, color=BLACK, fill_opacity=1, buff=0.25)
        a_line_bg.move_to(a_line.get_center())
        beat_4.add(a_line, a_line_bg)
        self.play(FadeIn(a_line_bg, run_time=0.4), Write(a_line, run_time=1.2))
        self.wait(0.3)

        # Measurement B: 1.0 ± 0.1 g → 10%.
        b_line = MathTex(
            r"B:\; 1.0 \pm 0.1 \text{ g} \;\Rightarrow\; 10\%",
            color=ORANGE_TERM,
        ).scale(0.85)
        b_line.move_to(BAND_CHART_CENTER + DOWN * 0.4)
        b_line_bg = BackgroundRectangle(b_line, color=BLACK, fill_opacity=1, buff=0.25)
        b_line_bg.move_to(b_line.get_center())
        beat_4.add(b_line, b_line_bg)
        self.play(FadeIn(b_line_bg, run_time=0.4), Write(b_line, run_time=1.2))
        self.wait(0.4)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Reject: forgetting × 100 (~4 s)
        # ──────────────────────────────────────────────────────────────────
        beat_5 = beat_group()
        bad = MathTex(
            r"\dfrac{\text{absolute error}}{\text{true value}} \;\Rightarrow\; 0.008",
            color=RED_REJECT,
        ).scale(0.8)
        bad.move_to(BAND_CHART_CENTER + UP * 0.4)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        beat_5.add(bad, bad_bg)
        self.play(FadeIn(bad_bg, run_time=0.4), Write(bad, run_time=1.4))
        self.wait(0.3)

        bad_note = Text(
            "Forgot × 100 — that is relative, not percentage.",
            font_size=18, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.4)
        bad_note_bg = BackgroundRectangle(bad_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        bad_note_bg.move_to(bad_note.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        beat_5.add(cross, bad_note, bad_note_bg)
        self.play(Create(cross, run_time=0.9))
        self.play(FadeIn(bad_note_bg, run_time=0.4), FadeIn(bad_note, run_time=0.9))
        self.wait(0.6)

        self.play(FadeOut(beat_5, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\dfrac{|\,\text{measured} - \text{true}\,|}{\text{true}} \times 100\%",
            "Use percentage error to compare across very different scales.",
            final_wait=20.0,
        )
