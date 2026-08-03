"""
Manim scene for the lesson `multiplication-addition`
(topic `l10a-ap-counting-principles`).

The two fundamental probability rules: P(A and B) = P(A) * P(B) for
independent events and P(A or B) = P(A) + P(B) for mutually exclusive
events. The animation shows concrete dice/coin examples.

Target duration: ~91.5 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class MultiplicationAdditionScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Probability rules: and / or",
            "Multiply for independent AND. Add for mutually-exclusive OR.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: coin then die — independent AND (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Independent events", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        # Two simple fractions side-by-side.
        c1 = make_equation_card(r"P(H) = \dfrac{1}{2}",
                                color=BLUE_TERM, scale=0.95)
        c1.move_to(BAND_CHART_CENTER + UP * 0.5 + LEFT * 2.6)
        c2 = make_equation_card(r"P(6) = \dfrac{1}{6}",
                                color=TEAL_TERM, scale=0.95)
        c2.move_to(BAND_CHART_CENTER + UP * 0.5 + RIGHT * 2.6)

        self.play(FadeIn(c1, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(c2, shift=UP * 0.2, run_time=1.0))
        self.wait(1.5)

        mult = make_equation_card(
            r"P(H \cap 6) = \dfrac{1}{2} \cdot \dfrac{1}{6} = \dfrac{1}{12}",
            color=GREEN_OK, scale=0.95,
        )
        mult.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        self.play(FadeIn(mult, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        note = Text("P(A and B) = P(A) · P(B)",
                    font_size=22, color=GREEN_OK)
        note.next_to(mult, DOWN, buff=0.3)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.5)

        beat2 = beat_group(head, head_bg, c1, c2, mult, note, note_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise to the AND rule (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Multiplication rule", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        gen = make_equation_card(
            r"P(A \cap B) = P(A)\, P(B)",
            color=GREEN_OK, scale=1.3,
        )
        gen.move_to(BAND_CHART_CENTER + UP * 0.2)
        self.play(FadeIn(gen, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        note3 = Text("works only when A and B are independent",
                     font_size=20, color=WHITE)
        note3.next_to(gen, DOWN, buff=0.4)
        note3_bg = BackgroundRectangle(note3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        note3_bg.move_to(note3.get_center())
        self.play(FadeIn(note3_bg, run_time=0.4), FadeIn(note3, run_time=1.0))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, gen, note3, note3_bg)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Mutually exclusive OR rule (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Mutually exclusive", font_size=26, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(1.0)

        # Concrete: P(king or queen) = 4/52 + 4/52.
        k = make_equation_card(
            r"P(\text{king}) = \dfrac{4}{52}, \quad P(\text{queen}) = \dfrac{4}{52}",
            color=ORANGE_TERM, scale=0.85,
        )
        k.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(k, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        add = make_equation_card(
            r"P(\text{K or Q}) = \dfrac{8}{52}",
            color=GREEN_OK, scale=1.1,
        )
        add.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        self.play(FadeIn(add, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        note4 = Text("P(A or B) = P(A) + P(B)", font_size=22, color=GREEN_OK)
        note4.next_to(add, DOWN, buff=0.3)
        note4_bg = BackgroundRectangle(note4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        note4_bg.move_to(note4.get_center())
        self.play(FadeIn(note4_bg, run_time=0.4), FadeIn(note4, run_time=1.0))
        self.wait(2.5)

        beat4 = beat_group(head4, head4_bg, k, add, note4, note4_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 91.5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"P(A \cap B) = P(A) P(B), \quad P(A \cup B) = P(A) + P(B)",
            "Multiply for AND on independent events; add for OR on mutually exclusive ones.",
            final_wait=41.0,
        )