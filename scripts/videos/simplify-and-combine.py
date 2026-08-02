"""
Manim scene for the lesson `simplify-and-combine`
(topic `l8-a-linear-expressions`).

Like terms have the same variable part; you can add or subtract them.
Different variables (or different powers) cannot be combined.

Target duration: ~94 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SimplifyAndCombineScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Simplify by combining like terms",
            "Same variable part ⇒ add or subtract. Different ⇒ leave alone.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Like terms CAN be combined (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Three x-terms that should combine: 3x + 5x = 8x.
        card1 = make_term_card("3x", "variable part: x", BLUE_TERM)
        card2 = make_term_card("+5x", "variable part: x", BLUE_TERM)
        plus = MathTex("+", color=WHITE).scale(1.5)
        cards = VGroup(card1, plus, card2).arrange(RIGHT, buff=0.4)
        cards.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in cards:
            m.set_z_index(2)

        self.play(
            FadeIn(card1, shift=UP * 0.2, run_time=1.0),
            FadeIn(plus, run_time=0.6),
            FadeIn(card2, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(2.0)

        # Combine into 8x.
        combined = make_term_card("8x", "3x + 5x = 8x", GREEN_OK)
        combined.move_to(BAND_CHART_CENTER + UP * 0.5)
        combined.set_z_index(2)
        self.play(FadeOut(VGroup(card1, plus, card2), run_time=1.2))
        self.play(FadeIn(combined, shift=UP * 0.2, run_time=1.4))
        self.wait(3.0)

        # Highlight that both inputs had the same variable part.
        hl = SurroundingRectangle(combined[0], color=GREEN_OK, buff=0.25, stroke_width=3)
        hl.set_z_index(3)
        self.play(Create(hl, run_time=1.0))
        self.wait(3.0)
        self.play(FadeOut(VGroup(combined, hl), run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Different variables CANNOT be combined (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Show 3x + 2y — different variable parts.
        x_card = make_term_card("3x", "variable part: x", BLUE_TERM)
        y_card = make_term_card("+2y", "variable part: y", TEAL_TERM)
        diff_pair = VGroup(
            x_card, MathTex("+", color=WHITE).scale(1.5), y_card
        ).arrange(RIGHT, buff=0.4)
        diff_pair.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in diff_pair:
            m.set_z_index(2)

        self.play(
            FadeIn(x_card, shift=UP * 0.2, run_time=1.0),
            FadeIn(y_card, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(2.5)

        # Cross through to show "cannot combine".
        cross = Cross(diff_pair, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=1.2))
        self.wait(2.5)

        # Explain in words below.
        note = Text(
            "Different variable parts → leave them as they are.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(diff_pair, DOWN, buff=0.6)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.5), FadeIn(note, run_time=1.2))
        self.wait(4.0)
        self.play(
            FadeOut(diff_pair, run_time=1.0),
            FadeOut(cross, run_time=1.0),
            FadeOut(VGroup(note, note_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Different powers also cannot be combined (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Show 3x vs 3x^2 — same variable x but different powers.
        x1 = make_term_card("3x", "power: 1", BLUE_TERM)
        x2 = make_term_card("+3x^{2}", "power: 2", ORANGE_TERM)
        diff_pwr = VGroup(
            x1, MathTex("+", color=WHITE).scale(1.5), x2
        ).arrange(RIGHT, buff=0.4)
        diff_pwr.move_to(BAND_CHART_CENTER + UP * 0.5)
        for m in diff_pwr:
            m.set_z_index(2)

        self.play(
            FadeIn(x1, shift=UP * 0.2, run_time=1.0),
            FadeIn(x2, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(3.0)

        # Cross through, with explicit "power" annotation.
        cross2 = Cross(diff_pwr, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross2, run_time=1.2))
        self.wait(2.5)

        note2 = Text(
            "Same variable, but different powers → not like terms.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(diff_pwr, DOWN, buff=0.6)
        note2_bg = BackgroundRectangle(note2, color=BLACK, fill_opacity=0.95, buff=0.18)
        note2_bg.move_to(note2.get_center())
        self.play(FadeIn(note2_bg, run_time=0.5), FadeIn(note2, run_time=1.2))
        self.wait(4.5)
        self.play(
            FadeOut(diff_pwr, run_time=1.0),
            FadeOut(cross2, run_time=1.0),
            FadeOut(VGroup(note2, note2_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~23 s, total ≈ 94 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Like terms} \;=\; \text{same variable part}",
            "Add or subtract when the variable part matches exactly.",
            final_wait=45.0,
        )