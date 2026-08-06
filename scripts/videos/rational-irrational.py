"""
Manim scene for the lesson `rational-irrational`
(topic `l9-n-real-numbers`).

Every real number is either rational (can be written as a fraction
of two integers) or irrational (cannot). The scene shows the
decimal expansion of sqrt(2) and pi, then contrasts it with
terminating decimals like 0.5, and gives the perfect-square
shortcut.

Render target: ~43 s audio + 20 s final wait.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class RationalIrrationalScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Rational vs irrational numbers",
            "Rational = fraction of two integers. Irrational = anything else.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: sqrt(2) decimal never repeats
        # ──────────────────────────────────────────────────────────────────
        head = MathTex(r"\sqrt{2}", color=RED_REJECT).scale(1.4)
        head.move_to(BAND_CHART_CENTER + UP * 1.0)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=1, buff=0.25)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), Write(head, run_time=1.0))
        self.wait(0.6)

        eq = MathTex(
            r"\sqrt{2} \approx 1.41421356\ldots",
            color=RED_REJECT,
        ).scale(1.0)
        eq.move_to(BAND_CHART_CENTER + UP * 0.0)
        eq_bg = BackgroundRectangle(eq, color=BLACK, fill_opacity=1, buff=0.2)
        eq_bg.move_to(eq.get_center())
        self.play(FadeIn(eq_bg, run_time=0.4), Write(eq, run_time=1.3))
        self.wait(0.6)

        note = Text("no pattern, never repeats",
                    font_size=22, color=RED_REJECT)
        note.next_to(eq, DOWN, buff=0.35)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.3), FadeIn(note, run_time=0.8))
        self.wait(0.6)

        # Fade out the "no pattern" note before showing the terminating
        # decimal comparison, so the two blocks don't overlap.
        self.play(
            FadeOut(note, run_time=0.5),
            FadeOut(note_bg, run_time=0.5),
        )
        self.wait(0.6)

        # Compare to terminating decimal 0.75.
        term = MathTex(r"0.75 = \dfrac{3}{4}", color=GREEN_OK).scale(1.0)
        term.move_to(BAND_CHART_CENTER + DOWN * 0.7)
        term_bg = BackgroundRectangle(term, color=BLACK, fill_opacity=1, buff=0.2)
        term_bg.move_to(term.get_center())

        term_lbl = Text("terminates → rational",
                        font_size=20, color=GREEN_OK)
        term_lbl.next_to(term, DOWN, buff=0.25)
        term_lbl_bg = BackgroundRectangle(term_lbl, color=BLACK,
                                          fill_opacity=0.95, buff=0.13)
        term_lbl_bg.move_to(term_lbl.get_center())

        self.play(FadeIn(term_bg, run_time=0.3), Write(term, run_time=1.0))
        self.wait(0.3)
        self.play(FadeIn(term_lbl_bg, run_time=0.3), FadeIn(term_lbl, run_time=0.6))
        self.wait(0.5)

        beat2 = beat_group(
            head, head_bg, eq, eq_bg,
            term, term_bg, term_lbl, term_lbl_bg,
        )
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: more irrationals (sqrt(3), pi)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("More irrationals", font_size=24, color=RED_REJECT)
        head3.move_to(BAND_CHART_CENTER + UP * 1.1)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.13)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.3), FadeIn(head3, run_time=0.7))
        self.wait(0.4)

        sq3 = MathTex(
            r"\sqrt{3} \approx 1.7320508\ldots",
            color=RED_REJECT,
        ).scale(0.9)
        sq3.move_to(BAND_CHART_CENTER + UP * 0.15)
        sq3_bg = BackgroundRectangle(sq3, color=BLACK, fill_opacity=1, buff=0.18)
        sq3_bg.move_to(sq3.get_center())

        pi_card = MathTex(
            r"\pi \approx 3.14159265\ldots",
            color=RED_REJECT,
        ).scale(0.9)
        pi_card.move_to(BAND_CHART_CENTER + DOWN * 0.55)
        pi_bg = BackgroundRectangle(pi_card, color=BLACK, fill_opacity=1, buff=0.18)
        pi_bg.move_to(pi_card.get_center())

        self.play(FadeIn(sq3_bg, run_time=0.3), Write(sq3, run_time=1.0))
        self.wait(0.3)
        self.play(FadeIn(pi_bg, run_time=0.3), Write(pi_card, run_time=1.0))
        self.wait(0.4)

        note3 = Text("none of these repeat forever",
                     font_size=20, color=RED_REJECT)
        note3.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        note3_bg = BackgroundRectangle(note3, color=BLACK,
                                       fill_opacity=0.95, buff=0.13)
        note3_bg.move_to(note3.get_center())
        self.play(FadeIn(note3_bg, run_time=0.3), FadeIn(note3, run_time=0.7))
        self.wait(0.6)

        beat3 = beat_group(
            head3, head3_bg, sq3, sq3_bg, pi_card, pi_bg, note3, note3_bg,
        )
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Quick test: square roots of perfect squares
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Quick test", font_size=24, color=BLUE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.1)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.13)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.3), FadeIn(head4, run_time=0.7))
        self.wait(0.4)

        ok = MathTex(
            r"\sqrt{4}=2,\ \sqrt{9}=3,\ \sqrt{16}=4 \;\Rightarrow\; \text{rational}",
            color=GREEN_OK,
        ).scale(0.8)
        ok.move_to(BAND_CHART_CENTER + UP * 0.2)
        ok_bg = BackgroundRectangle(ok, color=BLACK, fill_opacity=1, buff=0.2)
        ok_bg.move_to(ok.get_center())
        self.play(FadeIn(ok_bg, run_time=0.3), Write(ok, run_time=1.2))
        self.wait(0.4)

        bad = MathTex(
            r"\sqrt{2},\ \sqrt{3},\ \sqrt{5},\ \sqrt{7} \;\Rightarrow\; \text{irrational}",
            color=RED_REJECT,
        ).scale(0.8)
        bad.move_to(BAND_CHART_CENTER + DOWN * 0.5)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.3), Write(bad, run_time=1.2))
        self.wait(0.6)

        beat4 = beat_group(head4, head4_bg, ok, ok_bg, bad, bad_bg)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        
        animate_final_definition(
            self,
            r"\text{Rational} = \dfrac{a}{b},\ \text{irrational} = \text{otherwise}",
            "Irrationals have decimals that go on forever without repeating.",
            final_wait=126.8,
        )
