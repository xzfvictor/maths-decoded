"""
Manim scene for the lesson `factorial-permutations`
(topic `l10a-ap-counting-principles`).

The factorial n! = n*(n-1)*...*1 counts the permutations of n distinct
objects. The animation shows the expanding product and ties it to a
concrete arrangement count.

Target duration: ~102.4 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class FactorialPermutationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Factorials and permutations",
            "n! counts the arrangements of n distinct objects.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Build n! = n * (n-1) * ... * 1 with n=4 concrete (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Orderings of n objects", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        # Show 4! product step-by-step.
        prod_card = make_equation_card(
            r"4! \;=\; 4 \cdot 3 \cdot 2 \cdot 1",
            color=BLUE_TERM, scale=1.1,
        )
        prod_card.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(prod_card, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        ans_card = make_equation_card(
            r"= 24",
            color=GREEN_OK, scale=1.5,
        )
        ans_card.move_to(BAND_CHART_CENTER + DOWN * 0.9)
        self.play(FadeIn(ans_card, shift=UP * 0.3, run_time=1.4))
        self.wait(2.5)

        note = Text("24 arrangements of 4 distinct objects",
                    font_size=20, color=WHITE)
        note.next_to(ans_card, DOWN, buff=0.3)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.5)

        beat2 = beat_group(head, head_bg, prod_card, ans_card, note, note_bg)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise to n! (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("General pattern", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        gen = make_equation_card(
            r"n! \;=\; n \cdot (n-1) \cdot (n-2) \cdots 2 \cdot 1",
            color=GREEN_OK, scale=1.0,
        )
        gen.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(gen, shift=UP * 0.2, run_time=1.8))
        self.wait(3.0)

        note3 = Text("n \geq 1, and 0! = 1 by convention",
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
        # Beat 4 — Contrast: n=6 gives 720 — picks up fast (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Bigger n explodes", font_size=26, color=ORANGE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(1.0)

        table = VGroup()
        rows = [
            (r"3! = 6", BLUE_TERM),
            (r"4! = 24", BLUE_TERM),
            (r"5! = 120", ORANGE_TERM),
            (r"6! = 720", RED_REJECT),
        ]
        for i, (txt, color) in enumerate(rows):
            row = make_equation_card(txt, color=color, scale=0.9)
            row.move_to(BAND_CHART_CENTER + UP * 0.6 + DOWN * i * 0.85)
            table.add(row)

        self.play(
            LaggedStart(*[FadeIn(r, shift=UP * 0.2, run_time=0.7) for r in table],
                        lag_ratio=0.25),
        )
        self.wait(2.5)

        warn = Text("growth is faster than exponential", font_size=20, color=RED_REJECT)
        warn.move_to(BAND_CHART_CENTER + DOWN * 2.4)
        warn_bg = BackgroundRectangle(warn, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        warn_bg.move_to(warn.get_center())
        self.play(FadeIn(warn_bg, run_time=0.4), FadeIn(warn, run_time=1.0))
        self.wait(2.5)

        beat4 = beat_group(head4, head4_bg, table, warn, warn_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 102.4 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Number of orderings of } n \text{ objects} = n!",
            "Multiply n by every positive integer below it.",
            final_wait=46.0,
        )