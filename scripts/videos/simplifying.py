"""
Manim scene for the lesson `simplifying`
(topic `l9-a-simplifying-expanding-factorising`).

Like terms share the same variable part, so their coefficients can be
added or subtracted. The animation walks through
$3x + 2y - x + 5y = 2x + 7y$, then generalises the rule and rejects
combining unlike terms (e.g. $x + y$).

Render target: ~71.75 s, matched to the audio narration length.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class SimplifyingScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (visible for entire animation) + intro (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Simplifying algebraic expressions",
            "Collect like terms — leave unlike ones alone.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: 3x + 2y - x + 5y (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Build the four-term expression as a row of term cards.
        t1 = make_term_card("3x",  "x-term", BLUE_TERM)
        t2 = make_term_card("+2y", "y-term", TEAL_TERM)
        t3 = make_term_card("-x",  "x-term", BLUE_TERM)
        t4 = make_term_card("+5y", "y-term", TEAL_TERM)
        plus_signs = VGroup(*[
            MathTex("+", color=WHITE).scale(1.2)
            for _ in range(3)
        ])
        row = VGroup(t1, plus_signs[0], t2, plus_signs[1], t3, plus_signs[2], t4)
        row.arrange(RIGHT, buff=0.25)
        row.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in row:
            m.set_z_index(2)

        self.play(FadeIn(t1, shift=UP * 0.2, run_time=1.0), FadeIn(plus_signs[0], run_time=0.4))
        self.wait(0.6)
        self.play(FadeIn(t2, shift=UP * 0.2, run_time=1.0), FadeIn(plus_signs[1], run_time=0.4))
        self.wait(0.6)
        self.play(FadeIn(t3, shift=UP * 0.2, run_time=1.0), FadeIn(plus_signs[2], run_time=0.4))
        self.wait(0.6)
        self.play(FadeIn(t4, shift=UP * 0.2, run_time=1.0))
        self.wait(2.5)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Group like terms: x's together, y's together (~12 s)
        # ──────────────────────────────────────────────────────────────────
        # Highlight x group (blue) and y group (teal) in turn.
        self.play(Indicate(VGroup(t1, t3), color=BLUE_TERM, scale_factor=1.08), run_time=1.6)
        self.wait(0.5)
        self.play(Indicate(VGroup(t2, t4), color=TEAL_TERM, scale_factor=1.08), run_time=1.6)
        self.wait(1.5)

        # Fade out the row + labels before Beat 4 so the y-term labels
        # don't overlap the upcoming "x + y" reject example.
        self.play(FadeOut(row, run_time=0.8))
        self.wait(0.6)

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject combining unlike terms (~12 s)
        # ──────────────────────────────────────────────────────────────────
        # Show what we MUST NOT do: combining x + y.
        bad = MathTex(r"x + y", color=RED_REJECT).scale(1.0)
        bad.move_to(BAND_CHART_CENTER + DOWN * 0.2)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.5), Write(bad, run_time=1.2))
        self.wait(1.0)

        bad_note = Text(
            "Unlike variable parts  —  cannot combine.",
            font_size=20, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.4)
        bad_note_bg = BackgroundRectangle(bad_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        bad_note_bg.move_to(bad_note.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=0.8))
        self.play(FadeIn(bad_note_bg, run_time=0.4), FadeIn(bad_note, run_time=1.0))
        self.wait(2.0)

        self.play(
            FadeOut(bad, run_time=0.8),
            FadeOut(bad_bg, run_time=0.8),
            FadeOut(cross, run_time=0.8),
            FadeOut(VGroup(bad_note, bad_note_bg), run_time=0.8),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final simplified expression and takeaway (~remainder)
        # ──────────────────────────────────────────────────────────────────
        # Combine: (3x - x) = 2x;  (2y + 5y) = 7y.
        x_part = make_term_card("2x", "3x - x = 2x", BLUE_TERM)
        y_part = make_term_card("+7y", "2y + 5y = 7y", TEAL_TERM)
        plus_final = MathTex("+", color=WHITE).scale(1.5)
        final_row = VGroup(x_part, plus_final, y_part).arrange(RIGHT, buff=0.4)
        final_row.move_to(BAND_CHART_CENTER + UP * 0.6)
        for m in final_row:
            m.set_z_index(2)

        self.play(FadeOut(row, run_time=1.0))
        self.wait(0.4)
        self.play(
            FadeIn(x_part, shift=UP * 0.2, run_time=1.2),
            FadeIn(plus_final, run_time=0.6),
            FadeIn(y_part, shift=UP * 0.2, run_time=1.2),
        )
        self.wait(2.0)

        # Fade out the simplified expression before the final definition
        # so it doesn't overlap the "Like terms" recap.
        self.play(FadeOut(final_row, run_time=0.8))
        self.wait(0.6)

        # Final boxed definition (sized to audio final_wait=26 s).
        animate_final_definition(
            self,
            r"\text{Like terms: same variable part}",
            "Add or subtract the coefficients; leave unlike terms alone.",
            final_wait=26.0,
        )