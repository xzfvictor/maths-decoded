"""
Manim scene for the lesson `surd-operations`
(topic `l10a-an-surds`).

Operations on surds: simplify, add like radicals, multiply, and
rationalise the denominator. The animation walks through each
operation on a concrete surd before stating the general rule.

Target duration: ~99.8 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class SurdOperationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Operations with surds",
            "Simplify, add, multiply, and rationalise the denominator.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Simplify sqrt(12) = 2*sqrt(3) (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Simplify", font_size=28, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        before = make_equation_card(
            r"\sqrt{12} = \sqrt{4 \cdot 3}",
            color=BLUE_TERM, scale=1.0,
        )
        before.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(before, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        after = make_equation_card(
            r"= \sqrt{4}\,\sqrt{3} = 2\sqrt{3}",
            color=GREEN_OK, scale=1.0,
        )
        after.move_to(BAND_CHART_CENTER + DOWN * 0.9)
        self.play(FadeIn(after, shift=UP * 0.2, run_time=1.4))
        self.wait(2.5)

        note = Text("pull out the perfect-square factor", font_size=20, color=WHITE)
        note.next_to(after, DOWN, buff=0.3)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, before, after, note, note_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Add like radicals: 3*sqrt(2) + 5*sqrt(2) (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Add like radicals", font_size=28, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        eq3 = make_equation_card(
            r"3\sqrt{2} + 5\sqrt{2} = (3+5)\sqrt{2}",
            color=TEAL_TERM, scale=0.95,
        )
        eq3.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(eq3, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        eq3b = make_equation_card(
            r"= 8\sqrt{2}",
            color=GREEN_OK, scale=1.2,
        )
        eq3b.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        self.play(FadeIn(eq3b, shift=UP * 0.2, run_time=1.4))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, eq3, eq3b)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Multiply and rationalise: sqrt(2)*sqrt(8); 1/sqrt(2) (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Multiply & rationalise", font_size=28, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(1.0)

        # Multiply
        m = make_equation_card(
            r"\sqrt{2} \cdot \sqrt{8} = \sqrt{16} = 4",
            color=ORANGE_TERM, scale=0.95,
        )
        m.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(m, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        # Rationalise: 1/sqrt(2) = sqrt(2)/2.
        r = make_equation_card(
            r"\dfrac{1}{\sqrt{2}} = \dfrac{\sqrt{2}}{2}",
            color=ORANGE_TERM, scale=0.95,
        )
        r.move_to(BAND_CHART_CENTER + DOWN * 0.9)
        self.play(FadeIn(r, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        note4 = Text("multiply top & bottom by sqrt(2)",
                     font_size=20, color=WHITE)
        note4.next_to(r, DOWN, buff=0.3)
        note4_bg = BackgroundRectangle(note4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        note4_bg.move_to(note4.get_center())
        self.play(FadeIn(note4_bg, run_time=0.4), FadeIn(note4, run_time=1.0))
        self.wait(2.5)

        beat4 = beat_group(head4, head4_bg, m, r, note4, note4_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 99.8 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a\sqrt{n} + b\sqrt{n} = (a+b)\sqrt{n}",
            "Like radicals combine; rationalise clears sqrt denominators.",
            final_wait=45.0,
        )