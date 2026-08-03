"""
Manim scene for the lesson `range-iqr`
(topic `l10a-ast-measures-of-spread`).

Three ways to summarise spread: range (max-min, simple but blown out
by outliers), IQR (middle 50%, robust when outliers are lurking),
five-number summary (min, Q1, median, Q3, max). Selection guide and
the 1.5×IQR outlier rule of thumb.

Target duration: ~90 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class RangeIqrScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Range, IQR, and the five-number summary",
            "Range is fast, IQR is robust — pick by the shape of the data.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Range = max - min (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Range", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.05)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        rng = make_equation_card(
            r"\text{Range} \;=\; \max \;-\; \min",
            color=GREEN_OK, scale=1.0,
        )
        rng.move_to(BAND_CHART_CENTER + UP * 0.25)
        beat_2 = beat_group(beat_2, rng)
        self.play(FadeIn(rng, run_time=1.4))
        self.wait(2.0)

        sub = Text("Quick — but a single outlier blows it out.",
                   font_size=22, color=ORANGE_TERM)
        sub.move_to(BAND_CHART_CENTER + DOWN * 0.65)
        sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.95, buff=0.15)
        sub_bg.move_to(sub.get_center())
        beat_2 = beat_group(beat_2, sub, sub_bg)
        self.play(FadeIn(sub_bg, run_time=0.4), FadeIn(sub, run_time=1.2))
        self.wait(8.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — IQR = Q3 - Q1, the middle 50 % (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head3 = Text("Interquartile range (IQR)",
                     font_size=24, color=BLUE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.1)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        beat_3 = beat_group(beat_3, head3, head3_bg)
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        # Q1 and Q3 cards.
        q1 = make_term_card(r"Q_{1}", "lower quartile", BLUE_TERM)
        q3 = make_term_card(r"Q_{3}", "upper quartile", TEAL_TERM)
        qrow = VGroup(q1, q3).arrange(RIGHT, buff=1.0)
        qrow.move_to(BAND_CHART_CENTER + UP * 0.25)
        for m in qrow:
            m.set_z_index(2)
        beat_3 = beat_group(beat_3, q1, q3)
        self.play(FadeIn(q1, shift=UP * 0.2, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(q3, shift=UP * 0.2, run_time=1.0))
        self.wait(1.5)

        iqr = make_equation_card(
            r"\text{IQR} \;=\; Q_{3} \;-\; Q_{1}",
            color=GREEN_OK, scale=1.0,
        )
        iqr.move_to(BAND_CHART_CENTER + DOWN * 0.55)
        beat_3 = beat_group(beat_3, iqr)
        self.play(FadeIn(iqr, run_time=1.4))
        self.wait(2.0)

        why = Text("Chops the tails — outliers can't reach Q1 or Q3.",
                   font_size=22, color=GREEN_OK)
        why.move_to(BAND_CHART_CENTER + DOWN * 1.15)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.15)
        why_bg.move_to(why.get_center())
        beat_3 = beat_group(beat_3, why, why_bg)
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.2))
        self.wait(6.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Five-number summary (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        head4 = Text("Five-number summary",
                     font_size=24, color=BLUE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.05)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        beat_4 = beat_group(beat_4, head4, head4_bg)
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        summ = MathTex(
            r"\min,\; Q_{1},\; \text{median},\; Q_{3},\; \max",
            color=ORANGE_TERM,
        ).scale(1.0)
        summ.move_to(BAND_CHART_CENTER + UP * 0.25)
        summ_bg = BackgroundRectangle(summ, color=BLACK, fill_opacity=1, buff=0.22)
        summ_bg.move_to(summ.get_center())
        beat_4 = beat_group(beat_4, summ, summ_bg)
        self.play(FadeIn(summ_bg, run_time=0.4), Write(summ, run_time=2.0))
        self.wait(2.0)

        note = Text("These five values drive the boxplot.",
                    font_size=22, color=GREEN_OK)
        note.next_to(summ, DOWN, buff=0.45)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        beat_4 = beat_group(beat_4, note, note_bg)
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.2))
        self.wait(7.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Selection guide and 1.5 IQR rule (~15 s)
        # ──────────────────────────────────────────────────────────────────
        beat_5 = beat_group()

        guide = Text("Range → quick snapshot    IQR → outliers likely    SD → symmetric data",
                     font_size=20, color=BLUE_TERM)
        guide.move_to(BAND_CHART_CENTER + UP * 0.65)
        guide_bg = BackgroundRectangle(guide, color=BLACK, fill_opacity=0.95, buff=0.13)
        guide_bg.move_to(guide.get_center())
        beat_5 = beat_group(beat_5, guide, guide_bg)
        self.play(FadeIn(guide_bg, run_time=0.4), FadeIn(guide, run_time=1.6))
        self.wait(2.0)

        rule = make_equation_card(
            r"\text{Outlier if } x < Q_{1} - 1.5\,\text{IQR}\;\; \text{or}\;\; x > Q_{3} + 1.5\,\text{IQR}",
            color=ORANGE_TERM, scale=0.65,
        )
        rule.move_to(BAND_CHART_CENTER + DOWN * 0.65)
        beat_5 = beat_group(beat_5, rule)
        self.play(FadeIn(rule, run_time=1.4))
        self.wait(7.0)
        self.play(FadeOut(beat_5, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (~38 s, total ≈ 90 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Range}=\max-\min,\;\; \text{IQR}=Q_{3}-Q_{1},\;\; \tfrac{1}{n(\text{boxplot})}=\text{five numbers}",
            "Pick by data shape: range quick, IQR robust, SD symmetric.",
            final_wait=38.0,
        )
