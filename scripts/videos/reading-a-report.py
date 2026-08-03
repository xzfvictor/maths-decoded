"""
Manim scene for the lesson `reading-a-report`
(topic `l10a-ap-investigating-reports`).

Reading a statistical report critically: identify the sample, the
method, the conclusion, and any limitations. The animation walks
through a fictitious opinion-poll example.

Target duration: ~71.2 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class ReadingAReportScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Reading a report",
            "Sample, method, conclusion, limitations — in that order.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Sample: who was asked? (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Step 1: Who was surveyed?", font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        s_card = make_equation_card(
            r"\text{Sample: 500 city residents, ages 18–35}",
            color=BLUE_TERM, scale=0.85,
        )
        s_card.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(s_card, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        warn = Text("is it representative?", font_size=20, color=ORANGE_TERM)
        warn.next_to(s_card, DOWN, buff=0.4)
        warn_bg = BackgroundRectangle(warn, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        warn_bg.move_to(warn.get_center())
        self.play(FadeIn(warn_bg, run_time=0.4), FadeIn(warn, run_time=1.0))
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, s_card, warn, warn_bg)
        self.play(FadeOut(beat2, run_time=0.9))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Method and conclusion (~16 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Step 2 & 3: Method and conclusion",
                     font_size=24, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        m_card = make_equation_card(
            r"\text{Online questionnaire (10 questions)}",
            color=TEAL_TERM, scale=0.9,
        )
        m_card.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(m_card, shift=UP * 0.2, run_time=1.2))
        self.wait(1.2)

        c_card = make_equation_card(
            r"\text{62\% prefer Brand A over Brand B}",
            color=GREEN_OK, scale=0.9,
        )
        c_card.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        self.play(FadeIn(c_card, shift=UP * 0.2, run_time=1.2))
        self.wait(2.0)

        note3 = Text("Does the conclusion match what was measured?",
                     font_size=20, color=WHITE)
        note3.next_to(c_card, DOWN, buff=0.4)
        note3_bg = BackgroundRectangle(note3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        note3_bg.move_to(note3.get_center())
        self.play(FadeIn(note3_bg, run_time=0.4), FadeIn(note3, run_time=1.0))
        self.wait(2.0)

        beat3 = beat_group(head3, head3_bg, m_card, c_card, note3, note3_bg)
        self.play(FadeOut(beat3, run_time=0.9))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Limitations: sample bias, wording, response rate (~16 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Step 4: Limitations",
                     font_size=24, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(1.0)

        lims = VGroup()
        for i, txt in enumerate([
            r"\text{Online-only excludes the elderly}",
            r"\text{Only 12\% response rate}",
            r"\text{Question wording biased toward A}",
        ]):
            row = Text(txt, font_size=20, color=RED_REJECT)
            row.move_to(BAND_CHART_CENTER + UP * 0.6 + DOWN * i * 0.7)
            row_bg = BackgroundRectangle(row, color=BLACK,
                                         fill_opacity=0.9, buff=0.15)
            row_bg.move_to(row.get_center())
            lims.add(VGroup(row, row_bg))

        self.play(
            LaggedStart(*[FadeIn(g, shift=UP * 0.2, run_time=0.8) for g in lims],
                        lag_ratio=0.3),
        )
        self.wait(2.5)

        beat4 = beat_group(head4, head4_bg, lims)
        self.play(FadeOut(beat4, run_time=0.9))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 71.2 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Sample} \;\rightarrow\; \text{Method} \;\rightarrow\;"
            r" \text{Conclusion} \;\rightarrow\; \text{Limitations}",
            "Always read a report in this four-step order.",
            final_wait=30.0,
        )