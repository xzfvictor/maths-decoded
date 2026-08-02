"""
Manim scene for the lesson `reading-survey`
(topic `l9-st-survey-reports`).

When you read a survey report, hunt for the who/what/when/where/how-many
and ask how the data was actually obtained. Watch for bias.

Target duration: ~87 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ReadingSurveyScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Reading a survey report",
            "Hunt the who, what, when, where, and how-many first.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Find the basics (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Five small cards arranged in a row: population / sample / size /
        # method / variable.
        pop = make_term_card("\\text{Population}", "the claim is about ...", BLUE_TERM)
        sam = make_term_card("\\text{Sample}", "actually surveyed", TEAL_TERM)
        siz = make_term_card("n", "sample size", ORANGE_TERM)
        met = make_term_card("\\text{Method}", "random? voluntary?", PURPLE_ACCENT)
        var = make_term_card("\\text{Variable}", "what was measured", GREEN_OK)
        row = VGroup(pop, sam, siz, met, var).arrange(RIGHT, buff=0.35)
        # shrink the row so all 5 fit on screen width-wise
        row.scale(0.78)
        row.move_to(BAND_CHART_CENTER + UP * 0.5)
        for c in row:
            c.set_z_index(2)

        self.play(FadeIn(pop, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(sam, shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(siz, shift=UP * 0.2, run_time=0.8))
        self.play(FadeIn(met, shift=UP * 0.2, run_time=0.8))
        self.play(FadeIn(var, shift=UP * 0.2, run_time=0.8))
        self.wait(3.0)

        big_lbl = Text(
            "Method matters more than the headline number.",
            font_size=22,
            color=YELLOW,
        ).next_to(row, DOWN, buff=0.5)
        big_bg = BackgroundRectangle(big_lbl, color=BLACK, fill_opacity=0.95, buff=0.18)
        big_bg.move_to(big_lbl.get_center())
        self.play(FadeIn(big_bg, run_time=0.5), FadeIn(big_lbl, run_time=1.2))
        self.wait(7.0)
        self.play(
            FadeOut(row, run_time=1.0),
            FadeOut(VGroup(big_lbl, big_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Random vs voluntary / convenience (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Contrast two examples: a phone poll vs an online poll.
        good = make_term_card(
            "\\text{Phone poll (random)}",
            "every adult has a chance",
            GREEN_OK,
        )
        bad = make_term_card(
            "\\text{Online poll}",
            "self-selected — biased",
            RED_REJECT,
        )
        pair = VGroup(good, bad).arrange(RIGHT, buff=0.8)
        pair.move_to(BAND_CHART_CENTER + UP * 0.5)
        for c in pair:
            c.set_z_index(2)

        self.play(FadeIn(good, shift=UP * 0.2, run_time=1.2))
        self.play(FadeIn(bad, shift=UP * 0.2, run_time=1.2))
        self.wait(2.5)

        note = Text(
            "Self-selected polls over-represent motivated respondents.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(pair, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.5), FadeIn(note, run_time=1.2))
        self.wait(7.0)
        self.play(
            FadeOut(pair, run_time=1.0),
            FadeOut(VGroup(note, note_bg), run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Red flags (~18 s)
        # ──────────────────────────────────────────────────────────────────
        # List of red flags.
        flag1 = Text("- Tiny sample claiming precise national results", font_size=20, color=RED_REJECT)
        flag2 = Text("- Self-selected online polls", font_size=20, color=RED_REJECT)
        flag3 = Text("- Loaded or leading questions", font_size=20, color=RED_REJECT)
        flag4 = Text("- No description of how the sample was obtained", font_size=20, color=RED_REJECT)
        flags = VGroup(flag1, flag2, flag3, flag4).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        flags.move_to(BAND_CHART_CENTER + UP * 0.3)

        self.play(FadeIn(flag1, run_time=0.8))
        self.play(FadeIn(flag2, run_time=0.8))
        self.play(FadeIn(flag3, run_time=0.8))
        self.play(FadeIn(flag4, run_time=0.8))
        self.wait(2.5)

        # Background plate behind the flags list.
        plate = BackgroundRectangle(flags, color=BLACK, fill_opacity=0.85, buff=0.25)
        plate.move_to(flags.get_center())
        self.play(FadeIn(plate, run_time=0.5))
        self.wait(2.0)
        self.play(FadeOut(VGroup(flags, plate), run_time=1.5))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (total ≈ 87 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Check the method before the numbers}",
            "Population, sample, size, method, variable — read carefully.",
            final_wait=32.0,
        )
