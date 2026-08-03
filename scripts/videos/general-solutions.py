"""
Manim scene for the lesson `general-solutions`
(topic `l10a-asp-trig-equations`).

For sin(x) = sin(α), the general solutions are
x = α + 2πk  OR  x = π − α + 2πk  for integer k. The animation draws
the unit circle to show why both families are needed.

Target duration: ~88.2 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class GeneralSolutionsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "General solutions of sin x = sin α",
            "Two families: x = α + 2πk and x = π − α + 2πk.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Unit circle with sin x = sin α marked (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Two points on the unit circle", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        centre = BAND_CHART_CENTER + DOWN * 0.4
        circle = Circle(radius=1.5, color=WHITE).move_to(centre)
        # Reference axes through circle.
        x_axis = Line(centre + LEFT * 1.8, centre + RIGHT * 1.8,
                      color=WHITE, stroke_width=2)
        y_axis = Line(centre + DOWN * 1.8, centre + UP * 1.8,
                      color=WHITE, stroke_width=2)

        # α point in Q1.
        alpha = np.deg2rad(40)
        p_alpha = centre + 1.5 * np.array([np.cos(alpha), np.sin(alpha), 0])
        # Mirror point in Q2: π - α.
        mirror = np.deg2rad(180) - alpha
        p_mirror = centre + 1.5 * np.array([np.cos(mirror), np.sin(mirror), 0])

        dot_a = Dot(p_alpha, color=BLUE_TERM)
        dot_b = Dot(p_mirror, color=TEAL_TERM)
        a_lbl = MathTex(r"\alpha", color=BLUE_TERM).scale(0.9).next_to(
            dot_a, UR, buff=0.1)
        b_lbl = MathTex(r"\pi - \alpha", color=TEAL_TERM).scale(0.9).next_to(
            dot_b, UL, buff=0.1)

        # Horizontal dashed line through both points (same sin).
        sin_line = DashedLine(
            np.array([centre[0] - 1.8, p_alpha[1], 0]),
            np.array([centre[0] + 1.8, p_alpha[1], 0]),
            color=ORANGE_TERM, stroke_width=2,
        )
        sin_lbl = MathTex(r"\sin x = \sin\alpha",
                          color=ORANGE_TERM).scale(0.7)
        sin_lbl.move_to(BAND_CHART_CENTER + UP * 1.3 + RIGHT * 3.0)
        sin_lbl_bg = BackgroundRectangle(sin_lbl, color=BLACK,
                                         fill_opacity=0.9, buff=0.15)
        sin_lbl_bg.move_to(sin_lbl.get_center())

        self.play(Create(circle), Create(x_axis), Create(y_axis), run_time=1.5)
        self.play(FadeIn(dot_a), FadeIn(dot_b),
                  FadeIn(a_lbl), FadeIn(b_lbl), run_time=0.8)
        self.play(Create(sin_line, run_time=1.0),
                  FadeIn(sin_lbl_bg), FadeIn(sin_lbl), run_time=0.8)
        self.wait(2.5)

        beat2 = beat_group(head, head_bg, circle, x_axis, y_axis,
                           dot_a, dot_b, a_lbl, b_lbl,
                           sin_line, sin_lbl, sin_lbl_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — General-solution families (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("General solutions", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        eq1 = make_equation_card(
            r"x = \alpha + 2\pi k",
            color=BLUE_TERM, scale=1.1,
        )
        eq1.move_to(BAND_CHART_CENTER + UP * 0.4 + LEFT * 2.0)
        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        eq2 = make_equation_card(
            r"x = \pi - \alpha + 2\pi k",
            color=TEAL_TERM, scale=1.1,
        )
        eq2.move_to(BAND_CHART_CENTER + UP * 0.4 + RIGHT * 2.0)
        self.play(FadeIn(eq2, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        or_label = MathTex(r"\text{or}", color=WHITE).scale(1.0)
        or_label.move_to(BAND_CHART_CENTER + UP * 0.4)
        or_label_bg = BackgroundRectangle(or_label, color=BLACK,
                                          fill_opacity=0.95, buff=0.2)
        or_label_bg.move_to(or_label.get_center())
        self.play(FadeIn(or_label_bg), FadeIn(or_label), run_time=0.6)
        self.wait(1.5)

        k_note = MathTex(r"k \in \mathbb{Z}", font_size=20, color=WHITE)
        k_note.move_to(BAND_CHART_CENTER + DOWN * 0.9)
        k_note_bg = BackgroundRectangle(k_note, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        k_note_bg.move_to(k_note.get_center())
        self.play(FadeIn(k_note_bg, run_time=0.4), FadeIn(k_note, run_time=1.0))
        self.wait(2.0)

        beat3 = beat_group(head3, head3_bg, eq1, eq2,
                           or_label, or_label_bg, k_note, k_note_bg)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Concrete: sin x = 1/2 (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Example: sin x = ½", font_size=26, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        # alpha = π/6, so solutions are π/6 and 5π/6 (mod 2π).
        ans1 = make_equation_card(
            r"x = \dfrac{\pi}{6} + 2\pi k",
            color=BLUE_TERM, scale=1.0,
        )
        ans1.move_to(BAND_CHART_CENTER + UP * 0.3 + LEFT * 2.3)
        self.play(FadeIn(ans1, shift=UP * 0.2, run_time=1.4))

        ans2 = make_equation_card(
            r"x = \dfrac{5\pi}{6} + 2\pi k",
            color=TEAL_TERM, scale=1.0,
        )
        ans2.move_to(BAND_CHART_CENTER + UP * 0.3 + RIGHT * 2.3)
        self.play(FadeIn(ans2, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        note = Text("Two solutions per 2π period — both families needed.",
                    font_size=20, color=WHITE)
        note.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.0)

        beat4 = beat_group(head4, head4_bg, ans1, ans2, note, note_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 88.2 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"x = \alpha + 2\pi k \;\;\text{or}\;\; x = \pi - \alpha + 2\pi k",
            "Mirror angle in Q1 ↔ Q2 gives the second family.",
            final_wait=39.0,
        )