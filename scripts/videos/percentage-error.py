"""
Manim scene for the lesson `percentage-error`
(topic `l9-m-errors-in-measurements`).

Percentage error is the relative error expressed as a percentage. It is
the right tool for comparing measurements across very different scales
(e.g. 1 kg vs 100 kg).

Render target: ~84.31 s, matched to the audio narration length.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class PercentageErrorScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (visible for entire animation) + intro (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Percentage error",
            "Relative error × 100 — compare across very different scales.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The formula (~12 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = VGroup()
        formula = MathTex(
            r"\text{percentage error} \;=\; "
            r"\dfrac{\text{absolute error}}{\text{true value}} \times 100\%",
            color=GREEN_OK,
        ).scale(0.95)
        # Anchor the formula at the chart center (y = 0) so its
        # BackgroundRectangle never reaches up into the subtitle's band.
        formula.move_to(BAND_CHART_CENTER)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.25)
        formula_bg.move_to(formula.get_center())
        beat_2.add(formula, formula_bg)
        self.play(FadeIn(formula_bg, run_time=0.5), Write(formula, run_time=2.2))
        self.wait(3.0)

        rel_link = Text("Just relative error, written as a %.",
                        font_size=20, color=WHITE)
        rel_link.next_to(formula, DOWN, buff=0.4)
        rel_link_bg = BackgroundRectangle(rel_link, color=BLACK, fill_opacity=0.95, buff=0.15)
        rel_link_bg.move_to(rel_link.get_center())
        beat_2.add(rel_link, rel_link_bg)
        self.play(FadeIn(rel_link_bg, run_time=0.4), FadeIn(rel_link, run_time=1.0))
        self.wait(2.5)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: 50 m race (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = VGroup()
        ex_label = Text("50 m race:  measured 50.4 s,  true 50.0 s",
                        font_size=22, color=BLUE_TERM)
        ex_label.move_to(BAND_CHART_CENTER + UP * 1.5)
        ex_label_bg = BackgroundRectangle(ex_label, color=BLACK, fill_opacity=1, buff=0.2)
        ex_label_bg.move_to(ex_label.get_center())
        beat_3.add(ex_label, ex_label_bg)
        self.play(FadeIn(ex_label_bg, run_time=0.4), FadeIn(ex_label, run_time=1.4))
        self.wait(1.5)

        step1 = MathTex(r"|\,50.4 - 50.0\,| \;=\; 0.4 \text{ s}",
                        color=WHITE).scale(0.95)
        step1.move_to(BAND_CHART_CENTER + UP * 0.4)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=1, buff=0.25)
        step1_bg.move_to(step1.get_center())
        beat_3.add(step1, step1_bg)
        self.play(FadeIn(step1_bg, run_time=0.5), Write(step1, run_time=1.6))
        self.wait(1.5)

        step2 = MathTex(
            r"\dfrac{0.4}{50.0} \times 100\% \;=\; 0.8\%",
            color=GREEN_OK,
        ).scale(0.95)
        step2.move_to(BAND_CHART_CENTER + DOWN * 0.4)
        step2_bg = BackgroundRectangle(step2, color=BLACK, fill_opacity=1, buff=0.25)
        step2_bg.move_to(step2.get_center())
        beat_3.add(step2, step2_bg)
        self.play(FadeIn(step2_bg, run_time=0.5), Write(step2, run_time=1.8))
        self.wait(2.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Cross-scale comparison (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = VGroup()
        comp_title = Text("Two measurements, very different scales",
                          font_size=22, color=WHITE)
        comp_title.move_to(BAND_CHART_CENTER + UP * 1.6)
        comp_title_bg = BackgroundRectangle(comp_title, color=BLACK, fill_opacity=1, buff=0.2)
        comp_title_bg.move_to(comp_title.get_center())
        beat_4.add(comp_title, comp_title_bg)
        self.play(FadeIn(comp_title_bg, run_time=0.4), FadeIn(comp_title, run_time=1.2))
        self.wait(1.0)

        # Measurement A: 100 ± 1 g → 1%.
        a_line = MathTex(r"A:\; 100 \pm 1 \text{ g} \;\Rightarrow\; 1\%",
                         color=BLUE_TERM).scale(0.95)
        a_line.move_to(BAND_CHART_CENTER + UP * 0.4)
        a_line_bg = BackgroundRectangle(a_line, color=BLACK, fill_opacity=1, buff=0.25)
        a_line_bg.move_to(a_line.get_center())
        beat_4.add(a_line, a_line_bg)
        self.play(FadeIn(a_line_bg, run_time=0.5), Write(a_line, run_time=1.6))
        self.wait(1.0)

        # Measurement B: 1.0 ± 0.1 g → 10%.
        b_line = MathTex(r"B:\; 1.0 \pm 0.1 \text{ g} \;\Rightarrow\; 10\%",
                         color=ORANGE_TERM).scale(0.95)
        b_line.move_to(BAND_CHART_CENTER + DOWN * 0.2)
        b_line_bg = BackgroundRectangle(b_line, color=BLACK, fill_opacity=1, buff=0.25)
        b_line_bg.move_to(b_line.get_center())
        beat_4.add(b_line, b_line_bg)
        self.play(FadeIn(b_line_bg, run_time=0.5), Write(b_line, run_time=1.6))
        self.wait(1.5)

        takeaway = Text("B has the larger error despite the smaller absolute gap.",
                        font_size=20, color=GREEN_OK)
        takeaway.next_to(VGroup(a_line, b_line), DOWN, buff=0.5)
        takeaway_bg = BackgroundRectangle(takeaway, color=BLACK, fill_opacity=0.95, buff=0.15)
        takeaway_bg.move_to(takeaway.get_center())
        beat_4.add(takeaway, takeaway_bg)
        self.play(FadeIn(takeaway_bg, run_time=0.4), FadeIn(takeaway, run_time=1.2))
        self.wait(2.0)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Reject: forgetting × 100 (~10 s)
        # ──────────────────────────────────────────────────────────────────
        beat_5 = VGroup()
        bad = MathTex(
            r"\dfrac{\text{absolute error}}{\text{true value}} \;\Rightarrow\; 0.008",
            color=RED_REJECT,
        ).scale(0.9)
        bad.move_to(BAND_CHART_CENTER + UP * 0.2)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        beat_5.add(bad, bad_bg)
        self.play(FadeIn(bad_bg, run_time=0.5), Write(bad, run_time=1.8))
        self.wait(1.0)

        bad_note = Text("Forgot × 100  —  that is relative, not percentage.",
                        font_size=20, color=RED_REJECT)
        bad_note.next_to(bad, DOWN, buff=0.5)
        bad_note_bg = BackgroundRectangle(bad_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        bad_note_bg.move_to(bad_note.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        beat_5.add(cross)
        self.play(Create(cross, run_time=1.0))
        beat_5.add(bad_note, bad_note_bg)
        self.play(FadeIn(bad_note_bg, run_time=0.4), FadeIn(bad_note, run_time=1.0))
        self.wait(2.0)

        self.play(FadeOut(beat_5, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (~final_wait = 32 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\dfrac{|\,\text{measured} - \text{true}\,|}{\text{true}} \times 100\%",
            "Use percentage error to compare across very different scales.",
            final_wait=32.0,
        )