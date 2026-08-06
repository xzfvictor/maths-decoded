"""
Manim scene for the lesson `data-type-display`
(topic `l9-st-choosing-displays`).

Match the display to the data type: categorical → bar/pie; one
numerical → histogram/dot plot; two numerical → scatterplot; over
time → line graph. We show the four "mismatch" pairings and end
on the rule.

Target duration: ≈ 47 s (matches audio + 20 s hold).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, animate_intro, animate_final_definition,
)
from manim import *


class DataTypeDisplayScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~3 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Matching data to display",
            "Pick the display that fits the data type and the question.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Four data-type cards (~10 s)
        # ──────────────────────────────────────────────────────────────────
        # Build a 2x2 grid of cards.
        cat  = make_term_card(r"\text{Categorical}", "fruit, colour", BLUE_TERM)
        one  = make_term_card(r"\text{One numerical}", "ages, scores", TEAL_TERM)
        two  = make_term_card(r"\text{Two numerical}", "(x, y) pairs", ORANGE_TERM)
        time = make_term_card(r"\text{Over time}", "month, value", YELLOW)

        grid = VGroup(
            VGroup(cat, one).arrange(RIGHT, buff=1.0),
            VGroup(two, time).arrange(RIGHT, buff=1.0),
        ).arrange(DOWN, buff=0.7)
        grid.move_to(BAND_CHART_CENTER + UP * 0.0)

        self.play(FadeIn(cat,  shift=UP * 0.3, run_time=0.7))
        self.wait(0.3)
        self.play(FadeIn(one,  shift=UP * 0.3, run_time=0.7))
        self.wait(0.3)
        self.play(FadeIn(two,  shift=UP * 0.3, run_time=0.7))
        self.wait(0.3)
        self.play(FadeIn(time, shift=UP * 0.3, run_time=0.7))
        self.wait(1.5)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Match each card to its display (~10 s)
        # ──────────────────────────────────────────────────────────────────
        # Build four "→ display" arrows under the grid.
        arrows = VGroup()
        for card, display, color in [
            (cat,  r"\text{bar / pie}",          BLUE_TERM),
            (one,  r"\text{histogram / dot plot}", TEAL_TERM),
            (two,  r"\text{scatterplot}",         ORANGE_TERM),
            (time, r"\text{line graph}",          YELLOW),
        ]:
            arr = MathTex(r"\rightarrow", color=color).scale(0.9)
            arr.next_to(card, DOWN, buff=0.3)
            lab = MathTex(display, color=color).scale(0.7)
            lab.next_to(arr, RIGHT, buff=0.2)
            lab_bg = BackgroundRectangle(lab, color=BLACK, fill_opacity=0.95, buff=0.1)
            lab_bg.move_to(lab.get_center())
            arrows.add(VGroup(arr, lab, lab_bg))

        for arrow_set in arrows:
            self.play(FadeIn(arrow_set, run_time=0.7))
            self.wait(0.4)

        # Pause to let the four pairings register.
        self.wait(1.5)

        beat2_group = VGroup(grid, arrows)
        self.play(FadeOut(beat2_group, run_time=1.1))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject a clear mismatch: pie for ages (~4 s)
        # ──────────────────────────────────────────────────────────────────
        bad = MathTex(
            r"\text{pie chart for ages?}",
            color=RED_REJECT,
        ).scale(1.0)
        bad.move_to(BAND_CHART_CENTER + UP * 0.5)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.3), Write(bad, run_time=1.2))
        self.wait(0.6)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=0.7))

        why = Text(
            "Ages are numerical, not parts of a whole.",
            font_size=22, color=RED_REJECT,
        )
        why.next_to(bad, DOWN, buff=0.5)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.3), FadeIn(why, run_time=1.0))
        self.wait(1.0)

        beat4_group = VGroup(bad, bad_bg, cross, why, why_bg)
        self.play(FadeOut(beat4_group, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final boxed takeaway (held; final_wait = 20 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{display} = f(\text{data type, question})",
            "Categorical → bar/pie. Numerical → histogram. Time → line.",
            final_wait=20.0,
        )
