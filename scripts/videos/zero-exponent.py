"""
Manim scene for the lesson `zero-exponent`
(topic `l8-n-exponent-laws-integers`).

Why a^0 = 1 (for a ≠ 0): the quotient a^n / a^n equals 1, but the
quotient law gives a^(n - n) = a^0. 0^n = 0 for positive n, but 0^0
is undefined.

Target duration: ~93 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class ZeroExponentScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "The zero exponent",
            "Anything (except 0) to the power 0 is 1",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Why a^0 = 1: start from a^n / a^n (~16 s)
        # ──────────────────────────────────────────────────────────────────

        # Top line: a^n / a^n = 1 (a number divided by itself).
        # Position lowered to BAND_CHART_CENTER + UP*0.5 so the numerator
        # of the fraction has breathing room below the subtitle (~y=2.4)
        # and stays inside the safe area y ∈ [-1.5, 1.8].
        # Each line is its own beat_group so we fade it out BEFORE the
        # next equation fades in, instead of accumulating three equations
        # on screen at once.
        line1 = MathTex(
            r"\dfrac{a^{n}}{a^{n}} \;=\; 1",
            color=BLUE_TERM,
        ).scale(1.1)
        line1.move_to(BAND_CHART_CENTER + UP * 0.5)
        line1_bg = BackgroundRectangle(line1, color=BLACK,
                                       fill_opacity=1, buff=0.25)
        line1_bg.move_to(line1.get_center())
        beat_2a = beat_group(line1_bg, line1)

        self.play(
            FadeIn(line1_bg, run_time=0.4),
            Write(line1, run_time=1.6),
        )
        self.wait(3.0)

        # Fade line1 out before showing line2 so we never have two
        # equations overlapping on screen.
        self.play(FadeOut(beat_2a, run_time=0.6))

        # Middle line: quotient law → a^(n-n) = a^0.
        line2 = MathTex(
            r"\dfrac{a^{n}}{a^{n}} \;=\; a^{\,n - n} \;=\; a^{0}",
            color=TEAL_TERM,
        ).scale(1.05)
        line2.move_to(BAND_CHART_CENTER + UP * 0.5)
        line2_bg = BackgroundRectangle(line2, color=BLACK,
                                       fill_opacity=1, buff=0.25)
        line2_bg.move_to(line2.get_center())
        beat_2b = beat_group(line2_bg, line2)

        self.play(
            FadeIn(line2_bg, run_time=0.4),
            Write(line2, run_time=1.6),
        )
        self.wait(4.0)

        # Fade line2 out before showing line3.
        self.play(FadeOut(beat_2b, run_time=0.6))

        # Conclusion: both equal the same thing, so a^0 = 1.
        line3 = MathTex(
            r"\therefore \; a^{0} \;=\; 1 \quad (\text{for } a \neq 0)",
            color=GREEN_OK,
        ).scale(1.1)
        line3.move_to(BAND_CHART_CENTER + UP * 0.5)
        line3_bg = BackgroundRectangle(line3, color=BLACK,
                                       fill_opacity=1, buff=0.25)
        line3_bg.move_to(line3.get_center())
        beat_2c = beat_group(line3_bg, line3)

        self.play(
            FadeIn(line3_bg, run_time=0.4),
            Write(line3, run_time=1.6),
        )
        self.wait(3.0)

        self.play(FadeOut(beat_2c, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Apply it: 7^0, (-3)^0, 100^0 are all 1 (~14 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head = Text("So any non-zero base to the power 0 is 1:",
                    font_size=22, color=WHITE)
        # Header sits at UP*0.9 — well below the subtitle (~y=2.4) so
        # the equations beneath it stay inside y ∈ [-1.5, 1.8].
        head.move_to(BAND_CHART_CENTER + UP * 0.9)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_3 = beat_group(beat_3, head_bg, head)

        eq1 = make_equation_card(r"7^{0} = 1", color=GREEN_OK, scale=1.0)
        eq2 = make_equation_card(r"(-3)^{0} = 1", color=GREEN_OK, scale=1.0)
        eq3 = make_equation_card(r"100^{0} = 1", color=GREEN_OK, scale=1.0)
        equations = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.4).scale(0.85)
        equations.next_to(head, DOWN, buff=0.35)
        beat_3 = beat_group(beat_3, equations)

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
        )
        self.wait(1.5)
        self.play(FadeIn(eq1, shift=UP * 0.2, run_time=1.0))
        self.wait(1.5)
        self.play(FadeIn(eq2, shift=UP * 0.2, run_time=1.0))
        self.wait(1.5)
        self.play(FadeIn(eq3, shift=UP * 0.2, run_time=1.0))
        self.wait(3.5)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject 0^0; clarify 0^n = 0 for positive n (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        bad = MathTex(r"0^{0}", color=RED_REJECT).scale(1.6)
        bad.move_to(BAND_CHART_CENTER + UP * 1.0)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.3)
        bad_bg.move_to(bad.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        beat_4 = beat_group(beat_4, bad_bg, bad, cross)

        self.play(
            FadeIn(bad_bg, run_time=0.4),
            Write(bad, run_time=1.4),
        )
        self.play(Create(cross, run_time=1.0))
        self.wait(2.0)

        undef = Text("undefined", font_size=26, color=RED_REJECT)
        undef.next_to(VGroup(bad, cross), DOWN, buff=0.5)
        undef_bg = BackgroundRectangle(undef, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        undef_bg.move_to(undef.get_center())
        beat_4 = beat_group(beat_4, undef_bg, undef)
        self.play(
            FadeIn(undef_bg, run_time=0.4),
            FadeIn(undef, run_time=0.9),
        )
        self.wait(3.5)

        # Fade out the 0^0 stack.
        self.play(
            FadeOut(VGroup(bad, bad_bg, cross, undef, undef_bg),
                    run_time=1.2),
        )

        # 0^n = 0 for positive n: clear boxed affirmation.
        ok = make_equation_card(
            r"0^{5} \;=\; 0 \times 0 \times 0 \times 0 \times 0 \;=\; 0",
            color=GREEN_OK, scale=1.0,
        )
        ok.move_to(BAND_CHART_CENTER + UP * 0.4)
        beat_4 = beat_group(beat_4, ok)

        self.play(FadeIn(ok, shift=UP * 0.2, run_time=1.4))
        self.wait(3.0)

        # Sub note: any positive power of 0 is 0.
        note = Text(
            "0 raised to any positive power is 0.",
            font_size=22, color=GREEN_OK,
        )
        note.next_to(ok, DOWN, buff=0.45)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        beat_4 = beat_group(beat_4, note_bg, note)
        self.play(
            FadeIn(note_bg, run_time=0.4),
            FadeIn(note, run_time=1.0),
        )
        self.wait(3.0)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (total ≈ 93 s; final_wait = 35 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"a^{0} \;=\; 1 \quad \text{for any } a \neq 0",
            "0 raised to a positive power is 0; 0^0 is undefined.",
            final_wait=35.0,
        )
