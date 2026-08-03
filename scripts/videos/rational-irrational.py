"""
Manim scene for the lesson `rational-irrational`
(topic `l10a-an-surds`).

Surds are irrational roots of non-perfect squares; the animation shows
decimal expansions of sqrt(2) and sqrt(3) to prove they never repeat,
contrasting with terminating decimals like 0.5.

Target duration: ~102.9 s (matches the audio narration length).
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
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Surds are irrational",
            "Roots of non-perfect squares give non-repeating decimals.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — sqrt(2): decimal expansion never repeats (~26 s)
        # ──────────────────────────────────────────────────────────────────
        head = MathTex(r"\sqrt{2}", font_size=32, color=RED_REJECT)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        eq = make_equation_card(
            r"\sqrt{2} \approx 1.41421356\ldots",
            color=RED_REJECT, scale=1.0,
        )
        eq.move_to(BAND_CHART_CENTER + UP * 0.3)

        self.play(FadeIn(eq, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        note = Text("no pattern, never repeats", font_size=22, color=RED_REJECT)
        note.next_to(eq, DOWN, buff=0.3)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(3.0)

        # Compare to terminating decimal 0.5.
        term = make_equation_card(r"\dfrac{1}{2} = 0.5", color=GREEN_OK, scale=1.0)
        term.move_to(BAND_CHART_CENTER + DOWN * 1.5)
        term_lbl = Text("terminates → rational", font_size=20, color=GREEN_OK)
        term_lbl.next_to(term, DOWN, buff=0.25)
        term_lbl_bg = BackgroundRectangle(term_lbl, color=BLACK,
                                          fill_opacity=0.95, buff=0.15)
        term_lbl_bg.move_to(term_lbl.get_center())
        term_grp = VGroup(term, term_lbl, term_lbl_bg)

        self.play(FadeIn(term_grp, shift=UP * 0.2, run_time=1.3))
        self.wait(3.0)

        beat2 = beat_group(head, head_bg, eq, note, note_bg, term_grp)
        self.play(FadeOut(beat2, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — sqrt(3) and pi confirm the pattern (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("More irrationals", font_size=28, color=RED_REJECT)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        sq3 = make_equation_card(
            r"\sqrt{3} \approx 1.7320508\ldots",
            color=RED_REJECT, scale=0.95,
        )
        sq3.move_to(BAND_CHART_CENTER + UP * 0.4)

        pi_card = make_equation_card(
            r"\pi \approx 3.14159265\ldots",
            color=RED_REJECT, scale=0.95,
        )
        pi_card.move_to(BAND_CHART_CENTER + DOWN * 0.6)

        self.play(FadeIn(sq3, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)
        self.play(FadeIn(pi_card, shift=UP * 0.2, run_time=1.4))
        self.wait(3.0)

        note3 = Text("none of these repeat forever", font_size=22, color=RED_REJECT)
        note3.move_to(BAND_CHART_CENTER + DOWN * 1.9)
        note3_bg = BackgroundRectangle(note3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        note3_bg.move_to(note3.get_center())
        self.play(FadeIn(note3_bg, run_time=0.4), FadeIn(note3, run_time=1.0))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, sq3, pi_card, note3, note3_bg)
        self.play(FadeOut(beat3, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: a "clean" decimal like 0.75 IS rational (~15 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Contradiction check", font_size=28, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(1.0)

        ok = make_equation_card(
            r"0.75 = \dfrac{3}{4}",
            color=GREEN_OK, scale=1.1,
        )
        ok.move_to(BAND_CHART_CENTER + UP * 0.2)
        ok_lbl = Text("rational — has fraction form", font_size=22, color=GREEN_OK)
        ok_lbl.next_to(ok, DOWN, buff=0.3)
        ok_lbl_bg = BackgroundRectangle(ok_lbl, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        ok_lbl_bg.move_to(ok_lbl.get_center())
        ok_grp = VGroup(ok, ok_lbl, ok_lbl_bg)

        self.play(FadeIn(ok_grp, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        bad = make_equation_card(
            r"\sqrt{2} \neq \dfrac{a}{b}",
            color=RED_REJECT, scale=1.1,
        )
        bad.move_to(BAND_CHART_CENTER + DOWN * 1.4)
        bad_lbl = Text("irrational — no fraction form", font_size=22, color=RED_REJECT)
        bad_lbl.next_to(bad, DOWN, buff=0.3)
        bad_lbl_bg = BackgroundRectangle(bad_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        bad_lbl_bg.move_to(bad_lbl.get_center())
        bad_grp = VGroup(bad, bad_lbl, bad_lbl_bg)

        self.play(FadeIn(bad_grp, shift=UP * 0.2, run_time=1.4))
        self.wait(3.0)

        beat4 = beat_group(head4, head4_bg, ok_grp, bad_grp)
        self.play(FadeOut(beat4, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 102.9 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Surd} \;=\; \sqrt{n},\ n \text{ not a perfect square}",
            "Non-perfect-square roots give irrational, non-repeating decimals.",
            final_wait=47.0,
        )