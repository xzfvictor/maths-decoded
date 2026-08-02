"""
Manim scene for the lesson `primary-vs-secondary`
(topic `l8-st-sampling-techniques`).

Primary data are collected by you, for this question; secondary data
are collected by someone else and reused. Primary fits the question
but costs time; secondary is cheap but may not match exactly.

Render target: ~70 s, matched to the audio narration length. The
title stays at the top of the frame as a constant header.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class PrimaryVsSecondaryScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (CONSTANT header)
        # ──────────────────────────────────────────────────────────────────
        title_group = animate_intro(
            self,
            "Primary vs. secondary data",
            "Who collected it — you, or someone else?",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Primary data: you collect, you spend (~15 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None  # VGroup accumulator for beat 2

        primary_card = make_term_card(r"\text{Primary}", "you collect it", GREEN_OK)
        primary_card.move_to(BAND_CHART_CENTER + UP * 1.2)
        self.play(FadeIn(primary_card, shift=UP * 0.3, run_time=1.4))
        self.wait(1.5)
        beat_2 = beat_group(primary_card)

        # Fade the parent Primary card before showing the pros/cons so
        # the "you collect it" sublabel does not sit on top of them.
        self.play(FadeOut(beat_2, run_time=0.8))
        beat_2 = None

        # Pros / cons ladder
        pro = MathTex(
            r"\text{Fits the question exactly}",
            color=GREEN_OK,
        ).scale(0.95)
        pro_bg = BackgroundRectangle(pro, color=BLACK, fill_opacity=1, buff=0.25)
        pro_bg.move_to(pro.get_center())
        pro.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(
            FadeIn(pro_bg, run_time=0.5),
            Write(pro, run_time=1.4),
        )
        self.wait(2.0)

        # Fade the pro before showing the con so they don't overlap.
        beat_2 = beat_group(pro, pro_bg)
        self.play(FadeOut(beat_2, run_time=0.8))
        beat_2 = None

        con = MathTex(
            r"\text{Costly in time + money}",
            color=RED_REJECT,
        ).scale(0.95)
        con_bg = BackgroundRectangle(con, color=BLACK, fill_opacity=1, buff=0.25)
        con_bg.move_to(con.get_center())
        con.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(
            FadeIn(con_bg, run_time=0.5),
            Write(con, run_time=1.4),
        )
        self.wait(3.0)
        beat_2 = beat_group(con, con_bg)

        # End of beat 2 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Secondary data: someone else already did it (~15 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None  # VGroup accumulator for beat 3

        secondary_card = make_term_card(r"\text{Secondary}", "someone else", BLUE_TERM)
        secondary_card.move_to(BAND_CHART_CENTER + UP * 1.2)
        self.play(FadeIn(secondary_card, shift=UP * 0.3, run_time=1.4))
        self.wait(1.5)
        beat_3 = beat_group(secondary_card)

        # Fade the parent Secondary card before showing the pros/cons so
        # the "someone else" sublabel does not sit on top of them.
        self.play(FadeOut(beat_3, run_time=0.8))
        beat_3 = None

        # Pros / cons ladder
        s_pro = MathTex(
            r"\text{Cheap and quick to access}",
            color=GREEN_OK,
        ).scale(0.95)
        s_pro_bg = BackgroundRectangle(s_pro, color=BLACK, fill_opacity=1, buff=0.25)
        s_pro_bg.move_to(s_pro.get_center())
        s_pro.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(
            FadeIn(s_pro_bg, run_time=0.5),
            Write(s_pro, run_time=1.4),
        )
        self.wait(2.0)

        # Fade the pro before showing the con so they don't overlap.
        beat_3 = beat_group(s_pro, s_pro_bg)
        self.play(FadeOut(beat_3, run_time=0.8))
        beat_3 = None

        s_con = MathTex(
            r"\text{May not match the question}",
            color=RED_REJECT,
        ).scale(0.95)
        s_con_bg = BackgroundRectangle(s_con, color=BLACK, fill_opacity=1, buff=0.25)
        s_con_bg.move_to(s_con.get_center())
        s_con.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(
            FadeIn(s_con_bg, run_time=0.5),
            Write(s_con, run_time=1.4),
        )
        self.wait(3.0)
        beat_3 = beat_group(s_con, s_con_bg)

        # End of beat 3 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reporting checklist + concrete example (~12 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None  # VGroup accumulator for beat 4

        report = Text(
            "Always report: source · n · method · stats · display · comment.",
            font_size=22, color=WHITE,
        )
        report_bg = BackgroundRectangle(report, color=BLACK, fill_opacity=1, buff=0.25)
        report_bg.move_to(report.get_center())
        report.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(
            FadeIn(report_bg, run_time=0.5),
            Write(report, run_time=1.6),
        )
        self.wait(3.0)

        # Fade the checklist before showing the concrete example.
        beat_4 = beat_group(report, report_bg)
        self.play(FadeOut(beat_4, run_time=0.8))
        beat_4 = None

        example = Text(
            "ABS income data → a class reuses it.  That's SECONDARY.",
            font_size=22, color=GREEN_OK,
        )
        example_bg = BackgroundRectangle(example, color=BLACK, fill_opacity=0.95, buff=0.2)
        example_bg.move_to(example.get_center())
        example.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(
            FadeIn(example_bg, run_time=0.5),
            FadeIn(example, run_time=1.4),
        )
        self.wait(4.0)
        beat_4 = beat_group(example, example_bg)

        # End of beat 4 — clean FadeOut of the whole beat.
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Primary} \;\;/\;\; \text{Secondary}",
            "Primary fits perfectly. Secondary is cheap but may not match.",
            final_wait=25.0,
        )