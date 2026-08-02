"""
Manim scene for the lesson `what-is-polynomial`
(topic `l10a-aa-polynomials`).

A polynomial in x is a sum of terms a_n x^n where n is a non-negative
integer (n = 0, 1, 2, 3, ...). The animation makes that visible by
building a concrete example, generalising to the rule, and rejecting
the most striking counter-example (x^-1 = 1/x).

Render target: ~95-100 s, matched to the audio narration length so the
two streams align cleanly when muxed with ffmpeg. Beats are timed with
explicit self.wait(...) calls; total budget is the sum of beats.
"""

from manim import *


# ─── Vertical budget constants (LAYOUT PLAN) ────────────────────────────────
# Manim's default frame is y ∈ [-4, 4]. Keep the title's TOP edge well clear
# of y = 4 so there's visible breathing room above it.
BAND_TITLE         = UP * 3.1
BAND_SUBTITLE      = UP * 2.5
BAND_CHART_CENTER  = ORIGIN
BAND_BOTTOM        = DOWN * 3.3


# Brand-friendly palette: blue for the accepted example, red for the rejection.
BLUE_TERM  = BLUE_C
TEAL_TERM  = TEAL_C
ORANGE_TERM = ORANGE
RED_REJECT = RED_C
GREEN_OK   = GREEN_C


def _term_card(term_tex: str, exponent_label: str, color) -> VGroup:
    """A coloured term card with the term on top and the exponent below."""
    term = MathTex(term_tex, color=color).scale(1.1)
    expt = MathTex(exponent_label, color=color).scale(0.7)
    box  = SurroundingRectangle(term, color=color, buff=0.18, stroke_width=2)
    bg   = BackgroundRectangle(VGroup(term, box), color=BLACK, fill_opacity=0.85, buff=0.18)
    card = VGroup(bg, box, term)
    expt.next_to(card, DOWN, buff=0.25)
    return VGroup(card, expt)


class WhatIsPolynomial(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = Text("What is a polynomial?", font_size=40).move_to(BAND_TITLE)
        title_bg = BackgroundRectangle(title, color=BLACK, fill_opacity=1, buff=0.2)
        title_bg.move_to(title.get_center())
        # Place subtitle relative to title so spacing is automatic.
        sub = Text(
            "Sum of terms with whole-number powers of x",
            font_size=24,
        ).next_to(title, DOWN, buff=0.35)

        self.play(FadeIn(title_bg, run_time=0.5), Write(title, run_time=1.5))
        self.play(FadeIn(sub, shift=UP * 0.2, run_time=1.0))
        self.wait(2.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Build the example 5x³ - 2x + 7 with exponent labels (~28 s)
        # ──────────────────────────────────────────────────────────────────
        # Centre the row of three cards on the chart band.
        card1 = _term_card("5x^{3}",   "n = 3", BLUE_TERM)
        card2 = _term_card("-2x^{1}",  "n = 1", TEAL_TERM)
        card3 = _term_card("+7x^{0}",  "n = 0", ORANGE_TERM)
        row = VGroup(card1, card2, card3).arrange(RIGHT, buff=0.9)
        row.move_to(BAND_CHART_CENTER + UP * 0.2)

        self.play(FadeIn(card1, shift=UP * 0.3, run_time=1.2))
        self.wait(2.0)
        self.play(FadeIn(card2, shift=UP * 0.3, run_time=1.2))
        self.wait(2.0)
        self.play(FadeIn(card3, shift=UP * 0.3, run_time=1.2))
        self.wait(2.5)

        # Spell out the "constant = 7x^0" note to anchor the n=0 case.
        note = Text(
            "A constant is just a power with n = 0.",
            font_size=22,
        ).next_to(row, DOWN, buff=0.7)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.9, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.6), FadeIn(note, run_time=1.2))
        self.wait(3.0)

        # Indicate each exponent in turn to drive home the pattern.
        self.play(Indicate(card1[1], color=BLUE_TERM, scale_factor=1.2), run_time=1.5)
        self.wait(0.5)
        self.play(Indicate(card2[1], color=TEAL_TERM, scale_factor=1.2), run_time=1.5)
        self.wait(0.5)
        self.play(Indicate(card3[1], color=ORANGE_TERM, scale_factor=1.2), run_time=1.5)
        self.wait(2.5)

        # Hint at the pattern: every exponent is a whole number.
        whole_note = Text(
            "Every exponent is a whole number (0, 1, 2, 3, ...)",
            font_size=22,
            color=GREEN_OK,
        ).next_to(note, DOWN, buff=0.5)
        whole_bg = BackgroundRectangle(whole_note, color=BLACK, fill_opacity=0.95, buff=0.18)
        whole_bg.move_to(whole_note.get_center())
        self.play(FadeIn(whole_bg, run_time=0.6), FadeIn(whole_note, run_time=1.2))
        self.wait(4.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise to the rule a_n x^n (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat2_group = VGroup(card1, card2, card3, note, note_bg, whole_note, whole_bg)
        self.play(FadeOut(beat2_group, run_time=1.6))

        # The general sum-of-terms formula.
        general = MathTex(
            r"a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0",
        ).scale(1.05)
        general.move_to(BAND_CHART_CENTER + UP * 0.4)

        # Opaque background so the formula reads even when labels overlap.
        gen_bg = BackgroundRectangle(general, color=BLACK, fill_opacity=1, buff=0.25)
        gen_bg.move_to(general.get_center())

        self.play(FadeIn(gen_bg, run_time=0.6), Write(general, run_time=2.0))
        self.wait(3.0)

        # Highlight the exponent constraint.
        n_rule = MathTex(r"n \in \{0, 1, 2, 3, \ldots\}", color=GREEN_OK).scale(1.0)
        n_rule.next_to(general, DOWN, buff=0.6)
        n_rule_bg = BackgroundRectangle(n_rule, color=BLACK, fill_opacity=0.95, buff=0.2)
        n_rule_bg.move_to(n_rule.get_center())
        self.play(FadeIn(n_rule_bg, run_time=0.6), FadeIn(n_rule, run_time=1.2))
        self.wait(2.5)

        # Label
        allowed_lbl = Text("allowed", font_size=22, color=GREEN_OK)
        allowed_lbl.next_to(n_rule, DOWN, buff=0.4)
        allowed_bg  = BackgroundRectangle(allowed_lbl, color=BLACK, fill_opacity=0.95, buff=0.15)
        allowed_bg.move_to(allowed_lbl.get_center())
        self.play(FadeIn(allowed_bg, run_time=0.5), FadeIn(allowed_lbl, run_time=1.0))
        self.wait(8.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject the most striking counter-example: x^-1 (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat3_group = VGroup(general, gen_bg, n_rule, n_rule_bg, allowed_lbl, allowed_bg)
        self.play(FadeOut(beat3_group, run_time=1.5))

        reject = MathTex(r"x^{-1}", color=RED_REJECT).scale(1.4)
        reject.move_to(BAND_CHART_CENTER + UP * 0.5)
        reject_bg = BackgroundRectangle(reject, color=BLACK, fill_opacity=1, buff=0.25)
        reject_bg.move_to(reject.get_center())

        self.play(FadeIn(reject_bg, run_time=0.5), Write(reject, run_time=1.5))
        self.wait(1.5)

        # Reveal that x^-1 = 1/x — a reciprocal, not a polynomial term.
        recip = MathTex(
            r"x^{-1} \;=\; \dfrac{1}{x}",
            color=RED_REJECT,
        ).scale(1.1)
        recip.move_to(BAND_CHART_CENTER + DOWN * 0.2)
        recip_bg = BackgroundRectangle(recip, color=BLACK, fill_opacity=1, buff=0.25)
        recip_bg.move_to(recip.get_center())

        self.play(
            FadeOut(reject_bg, run_time=0.4),
            FadeOut(reject, run_time=0.4),
            FadeIn(recip_bg, run_time=0.5),
            Write(recip, run_time=1.6),
        )
        self.wait(2.5)

        # Cross it out and label.
        cross = Cross(recip, color=RED_REJECT, stroke_width=6)
        not_lbl = Text("not allowed", font_size=24, color=RED_REJECT)
        not_lbl.next_to(recip, DOWN, buff=0.6)
        not_bg = BackgroundRectangle(not_lbl, color=BLACK, fill_opacity=0.95, buff=0.18)
        not_bg.move_to(not_lbl.get_center())
        self.play(Create(cross, run_time=1.0))
        self.play(FadeIn(not_bg, run_time=0.5), FadeIn(not_lbl, run_time=1.0))
        self.wait(7.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final boxed takeaway at BAND_BOTTOM (~22 s, held)
        # ──────────────────────────────────────────────────────────────────
        beat4_group = VGroup(recip, recip_bg, cross, not_lbl, not_bg)
        self.play(FadeOut(beat4_group, run_time=1.5))

        final = MathTex(
            r"\text{Polynomial} \;=\; \sum_{n=0}^{N} a_n\, x^n",
        ).scale(1.05)
        # Place the equation's center well above BAND_BOTTOM so the
        # SurroundingRectangle + sub2 label have ≥0.6 unit margin from the
        # bottom edge of the [-4, 4] frame.
        final.move_to(BAND_BOTTOM + UP * 1.7)
        final_bg = BackgroundRectangle(final, color=BLACK, fill_opacity=1, buff=0.28)
        final_bg.move_to(final.get_center())
        final_box = SurroundingRectangle(final, color=GREEN_OK, buff=0.3, stroke_width=3)

        self.play(FadeIn(final_bg, run_time=0.6), Write(final, run_time=2.0))
        self.play(Create(final_box, run_time=1.0))
        self.play(Indicate(final, color=GREEN_OK, scale_factor=1.05), run_time=1.5)

        # Subtitle below the boxed equation.
        sub2 = Text(
            "Each exponent n is a non-negative integer.",
            font_size=22,
            color=GREEN_OK,
        )
        sub2.next_to(final_box, DOWN, buff=0.3)
        sub2_bg = BackgroundRectangle(sub2, color=BLACK, fill_opacity=0.95, buff=0.18)
        sub2_bg.move_to(sub2.get_center())
        self.play(FadeIn(sub2_bg, run_time=0.5), FadeIn(sub2, run_time=1.2))
        # Final hold tuned to match the audio narration length (~99 s total).
        self.wait(23.0)