"""
Manim scene for the lesson `shape-terms`
(topic `l9-st-comparing-data-sets`).

Distribution shapes: symmetric, right-skewed, left-skewed,
bimodal, uniform. For each shape we draw a tiny dot-plot
silhouette and pin the mean-vs-median rule.

Target duration: ~78.44 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


def _silhouette(values, color, height=0.9, dx=0.18, baseline_y=0.0):
    """Return a tiny VGroup of squares whose heights form a distribution
    silhouette. values is a list of positive integers per column."""
    bars = VGroup()
    n = len(values)
    for i, v in enumerate(values):
        h = max(0.05, v) * height / max(values)
        b = Rectangle(
            width=dx * 0.85, height=h,
            fill_color=color, fill_opacity=0.9,
            stroke_color=color, stroke_width=1.5,
        )
        b.move_to([
            (i - (n - 1) / 2) * dx,
            baseline_y + h / 2,
            0,
        ])
        bars.add(b)
    return bars


class ShapeTermsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Shape: symmetric, skewed, bimodal",
            "Centre, spread, shape — and what shape says about mean vs median.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Symmetric: mean ≈ median (~14 s)
        # ──────────────────────────────────────────────────────────────────
        sym_card = make_term_card(
            r"\text{Symmetric}", r"\text{mean} \approx \text{median}", BLUE_TERM,
        )
        sym_card.move_to(BAND_CHART_CENTER + UP * 1.4)
        self.play(FadeIn(sym_card, shift=UP * 0.3, run_time=1.2))
        self.wait(1.2)

        sym_shape = _silhouette([1, 2, 4, 6, 4, 2, 1], BLUE_TERM,
                                 baseline_y=-0.6)
        sym_shape.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        self.play(FadeIn(sym_shape, run_time=1.2))
        self.wait(3.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Skewed left vs right (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat2_group = VGroup(sym_card, sym_shape)
        self.play(FadeOut(beat2_group, run_time=1.2))

        # Right-skewed: long tail to the right; mean > median.
        right_card = make_term_card(
            r"\text{Right-skewed}", r"\text{mean} > \text{median}", ORANGE_TERM,
        )
        right_card.move_to(BAND_CHART_CENTER + UP * 1.5 + LEFT * 3.2)
        right_shape = _silhouette([4, 3, 2, 2, 1, 1], ORANGE_TERM,
                                   baseline_y=-0.6, dx=0.22)
        right_shape.move_to(BAND_CHART_CENTER + DOWN * 0.4 + LEFT * 3.2)

        left_card = make_term_card(
            r"\text{Left-skewed}", r"\text{mean} < \text{median}", TEAL_TERM,
        )
        left_card.move_to(BAND_CHART_CENTER + UP * 1.5 + RIGHT * 3.2)
        left_shape = _silhouette([1, 1, 2, 2, 3, 4], TEAL_TERM,
                                  baseline_y=-0.6, dx=0.22)
        left_shape.move_to(BAND_CHART_CENTER + DOWN * 0.4 + RIGHT * 3.2)

        self.play(
            FadeIn(right_card, shift=UP * 0.3, run_time=1.2),
            FadeIn(left_card,  shift=UP * 0.3, run_time=1.2),
        )
        self.wait(1.0)
        self.play(
            FadeIn(right_shape, run_time=1.2),
            FadeIn(left_shape,  run_time=1.2),
        )
        self.wait(3.5)

        beat3_group = VGroup(
            right_card, left_card, right_shape, left_shape,
        )
        self.play(FadeOut(beat3_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Bimodal & uniform (~12 s)
        # ──────────────────────────────────────────────────────────────────
        bi_card = make_term_card(
            r"\text{Bimodal}", r"\text{two peaks}", GREEN_OK,
        )
        bi_card.move_to(BAND_CHART_CENTER + UP * 1.5 + LEFT * 3.2)
        bi_shape = _silhouette([1, 4, 2, 1, 4, 1], GREEN_OK,
                               baseline_y=-0.6, dx=0.22)
        bi_shape.move_to(BAND_CHART_CENTER + DOWN * 0.4 + LEFT * 3.2)

        uni_card = make_term_card(
            r"\text{Uniform}", r"\text{flat shape}", YELLOW,
        )
        uni_card.move_to(BAND_CHART_CENTER + UP * 1.5 + RIGHT * 3.2)
        uni_shape = _silhouette([2, 2, 2, 2, 2, 2], YELLOW,
                                baseline_y=-0.6, dx=0.22)
        uni_shape.move_to(BAND_CHART_CENTER + DOWN * 0.4 + RIGHT * 3.2)

        self.play(
            FadeIn(bi_card, shift=UP * 0.3, run_time=1.0),
            FadeIn(uni_card, shift=UP * 0.3, run_time=1.0),
        )
        self.wait(0.7)
        self.play(
            FadeIn(bi_shape, run_time=1.0),
            FadeIn(uni_shape, run_time=1.0),
        )
        self.wait(2.0)

        beat4_group = VGroup(
            bi_card, uni_card, bi_shape, uni_shape,
        )
        self.play(FadeOut(beat4_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4b — Reject: "more data is always better" off-topic —
        # instead show the rule that "shape tells you about mean vs median".
        # We re-use the rule text and mark a right-skewed silhouette
        # crossing it out where people mistakenly swap the inequality.
        # ──────────────────────────────────────────────────────────────────
        # Show the rule: skew direction predicts the mean-median relation.
        rule = MathTex(
            r"\text{tail direction} \;\Rightarrow\; \text{mean vs median}",
            color=GREEN_OK,
        ).scale(1.0)
        rule.move_to(BAND_CHART_CENTER + UP * 0.7)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.25)
        rule_bg.move_to(rule.get_center())
        self.play(FadeIn(rule_bg, run_time=0.4), Write(rule, run_time=1.6))
        self.wait(2.0)

        # Sub-line: the rejected misclaim.
        bad = MathTex(
            r"\text{``skewed always means mean = median''}",
            color=RED_REJECT,
        ).scale(0.85)
        bad.next_to(rule, DOWN, buff=0.55)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=0.95, buff=0.2)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.2))
        self.wait(1.0)
        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.8))
        self.wait(2.0)

        beat4b_group = VGroup(rule, rule_bg, bad, bad_bg, cross)
        self.play(FadeOut(beat4b_group, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final boxed takeaway (held; total ≈ 78 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Shape} \;\Rightarrow\; \text{mean vs median}",
            "Right tail → mean > median. Symmetric → mean ≈ median.",
            final_wait=29.0,
        )
