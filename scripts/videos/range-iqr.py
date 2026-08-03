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
            "Range and IQR: measuring spread",
            "Range is fast, IQR is robust. Pick by the shape of the data.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Range = max - min (~24 s)
        # ──────────────────────────────────────────────────────────────────
        data = [2, 5, 6, 7, 7, 8, 8, 9, 10, 22]
        data_row = VGroup(*[MathTex(str(d), color=BLUE_TERM).scale(1.0) for d in data])
        data_row.arrange(RIGHT, buff=0.35)
        data_row.move_to(BAND_CHART_CENTER + UP * 1.0)
        self.play(*[FadeIn(m, run_time=0.35) for m in data_row], run_time=2.0)
        self.wait(2.0)

        # The 22 highlighted as the outlier.
        last = data_row[-1]
        last.set_color(RED_REJECT)
        last_lbl = Text("outlier", font_size=18, color=RED_REJECT)
        last_lbl.next_to(last, UP, buff=0.2)
        last_lbl_bg = BackgroundRectangle(last_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        last_lbl_bg.move_to(last_lbl.get_center())
        self.play(FadeIn(last_lbl_bg, run_time=0.3), FadeIn(last_lbl, run_time=0.8))
        self.wait(2.0)

        # Range formula.
        rng = make_equation_card(
            r"\text{Range} \;=\; \max - \min \;=\; 22 - 2 \;=\; 20",
            color=ORANGE_TERM,
            scale=0.95,
        )
        rng.next_to(data_row, DOWN, buff=0.7)
        self.play(FadeIn(rng, run_time=1.4))
        self.wait(2.0)

        quick = Text("Quick — but distorted by the 22.", font_size=22, color=ORANGE_TERM)
        quick.next_to(rng, DOWN, buff=0.5)
        quick_bg = BackgroundRectangle(quick, color=BLACK, fill_opacity=0.95, buff=0.15)
        quick_bg.move_to(quick.get_center())
        self.play(FadeIn(quick_bg, run_time=0.4), FadeIn(quick, run_time=1.2))
        self.wait(7.0)

        beat1 = beat_group(data_row, last_lbl, last_lbl_bg, rng, quick, quick_bg)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — IQR = Q3 - Q1 (~32 s)
        # ──────────────────────────────────────────────────────────────────
        # Step 1: sort, then find quartiles.
        step1 = Text(
            "1. Order the data; split the middle 50% off the ends.",
            font_size=22,
            color=BLUE_TERM,
        ).move_to(BAND_CHART_CENTER + UP * 1.35)
        step1_bg = BackgroundRectangle(step1, color=BLACK, fill_opacity=0.95, buff=0.15)
        step1_bg.move_to(step1.get_center())
        self.play(FadeIn(step1_bg, run_time=0.4), FadeIn(step1, run_time=1.2))
        self.wait(2.5)

        # Q1 and Q3 cards.
        q1 = make_term_card("Q_1 = 6", "lower quartile", BLUE_TERM)
        q3 = make_term_card("Q_3 = 9", "upper quartile", TEAL_TERM)
        qrow = VGroup(q1, q3).arrange(RIGHT, buff=1.0)
        qrow.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in qrow:
            m.set_z_index(2)
        self.play(FadeIn(q1, shift=UP * 0.2, run_time=1.0))
        self.wait(1.0)
        self.play(FadeIn(q3, shift=UP * 0.2, run_time=1.0))
        self.wait(2.5)

        # IQR formula.
        iqr = make_equation_card(
            r"\text{IQR} \;=\; Q_3 - Q_1 \;=\; 9 - 6 \;=\; 3",
            color=GREEN_OK,
            scale=0.95,
        )
        iqr.move_to(BAND_CHART_CENTER + DOWN * 0.55)
        self.play(FadeIn(iqr, run_time=1.4))
        self.wait(2.0)

        # Why IQR is robust.
        why = Text(
            "IQR ignores the 22 — it only sees the middle 50%.",
            font_size=22,
            color=GREEN_OK,
        ).move_to(BAND_CHART_CENTER + DOWN * 1.25)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.15)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.2))
        self.wait(11.0)

        beat2 = beat_group(step1, step1_bg, q1, q3, iqr, why, why_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — The 1.5 x IQR rule of thumb (~18 s)
        # ──────────────────────────────────────────────────────────────────
        rule = make_equation_card(
            r"\text{Outlier} :\; x < Q_1 - 1.5 \cdot \text{IQR} \;\;\text{or}\;\; x > Q_3 + 1.5 \cdot \text{IQR}",
            color=ORANGE_TERM,
            scale=0.7,
        )
        rule.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(rule, run_time=1.4))
        self.wait(2.0)

        tag = Text(
            "22 > 9 + 1.5 * 3 = 13.5, so 22 is flagged.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(rule, DOWN, buff=0.5)
        tag_bg = BackgroundRectangle(tag, color=BLACK, fill_opacity=0.95, buff=0.15)
        tag_bg.move_to(tag.get_center())
        self.play(FadeIn(tag_bg, run_time=0.4), FadeIn(tag, run_time=1.2))
        self.wait(7.0)

        beat3 = beat_group(rule, tag, tag_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~40 s, total ≈ 90 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Range} = \max - \min,\;\; \text{IQR} = Q_3 - Q_1",
            "Range is fast; IQR is robust when outliers might be lurking.",
            final_wait=40.0,
        )
